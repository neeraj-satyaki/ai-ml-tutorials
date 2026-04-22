# Multi-Camera Tracking (MCT / MTMC / MCMT)

Deeper dive than `Tracking_and_ReID.md` section 5. Goal: one global ID per object across N cameras, regardless of overlap or view.

---

## 1. Problem flavors

| Flavor | Definition |
|--------|------------|
| **Overlapping MCT** | Cameras share FOV. Solve via geometry (homography, triangulation). |
| **Non-overlapping MTMC** | Cameras cover disjoint zones. Objects disappear, reappear elsewhere. Rely on appearance + topology + time. |
| **Hybrid** | Some overlap, some gaps (real city deployments). |
| **Camera-array / light-field** | Many cameras, one scene. Use for 3D reconstruction + tracking. |
| **Moving cameras** | Drones, AV fleets. Need ego-motion compensation + map frame. |

---

## 2. Full pipeline

```
per camera:
  decode → detect → single-camera MOT (ByteTrack / BoT-SORT) → appearance emb (OSNet / CLIP-ReID)
                                      │
                                      ▼
global:
  tracklet buffer per camera
  spatio-temporal feasibility filter (topology + transit time)
  cross-camera association (Hungarian / graph / clustering)
  global-ID assignment + persistence store
  sink (Kafka / DB)
```

---

## 3. Tracklet representation

A tracklet = `(camera_id, local_track_id, frames[], bboxes[], features[], timestamps[], entry_exit_zone)`.
- Features: mean-pool or attention-pool of per-frame ReID embeddings (ℓ2-normalized).
- Entry/exit zone: which edge of the FOV the track appeared at / left from.
- Keep feature bank per tracklet (top-K most-confident frames) for robustness.

---

## 4. Camera topology

### Manual topology graph
Nodes = cameras (or regions). Edges = possible transitions with `(p_transition, µ_transit, σ_transit)`.
Built once from site plan + operator knowledge.

### Learned topology
- Co-occurrence mining from initial noisy tracking.
- Estimate transit distributions per edge.
- Prune unreachable pairs — big recall boost.

### Calibration
- Extrinsic per camera w.r.t. a world map (floor plan / satellite).
- For overlapping: homography to ground plane → BEV fusion.
- For non-overlapping: only topology + distance needed.

---

## 5. Cross-camera association

### Hungarian on cost matrix
Cost = `α · (1 - cos_sim(feat)) + β · Δt_mahalanobis + γ · topology_penalty`.
Run globally (bipartite) or per-edge (camera pair).

### Graph-based clustering
- Nodes = tracklets. Edges = weighted similarity.
- Correlation clustering / label propagation.
- Useful when > 2 cameras interact simultaneously.

### Hierarchical clustering
- Merge tracklets iteratively; stop when below similarity threshold.
- Used by top AI City Challenge entries.

### Transformer / GNN re-ranking
- MGCN, CAL, DualBERT — model tracklet-to-tracklet relations.
- Learn to re-rank Hungarian candidates.

### Online vs offline
- **Online**: decisions made with only past data; mandatory for live ops.
- **Offline** (batch): whole day of video, globally optimize. Forensics / retail analytics.

---

## 6. Dealing with appearance shift across cameras

Same person looks different camera-to-camera: white balance, illumination, angle, compression.

Mitigations:
- **Camera-aware batch norm** (CamStyle, CBN) during ReID training.
- **Domain adaptation** via CycleGAN image translation between cameras.
- **Unsupervised fine-tune** on unlabeled target-camera crops (clustering-based pseudo-labels).
- **Lighting augmentation** (AutoAugment, RandAug) at train time.
- **Part-based features** (MGN, PCB) — less sensitive to overall color cast.

---

## 7. Spatio-temporal constraints

Cheap but powerful filters before any ML:
- Velocity cap: `dist(cam_i, cam_j) / Δt > v_max` → reject.
- Direction consistency: exit-zone of cam_i must plausibly lead to entry-zone of cam_j.
- Unreachable pairs: topology graph has no edge → skip.
- Cool-down: same object can't re-appear in cam_i within τ seconds.
These alone cut association complexity by 10-100x and kill most false matches.

---

## 8. Benchmarks

| Dataset | Scenario | Cams | Notes |
|---------|----------|------|-------|
| **DukeMTMC** (retired) | campus | 8 | seminal; withdrawn for privacy |
| **MOTChallenge MCMT (MOT20-MCMT)** | crowded | up to 4 | pedestrians |
| **WILDTRACK** | overlapping plaza | 7 | ground-plane fusion |
| **PETS2009 S2** | surveillance | multiple | classic |
| **EPFL-RLC / Terrace / Laboratory** | indoor | 3-4 | overlapping |
| **CAMPUS / CityFlow** | outdoor vehicles | multi-site | AI City |
| **AI City Challenge** (yearly) | city-scale vehicles + pedestrians | 10-40 | de-facto leaderboard |
| **SportsMCMT / SoccerNet** | sports | 4-8 | team/role clutter |
| **DanceTrack / SportsMOT** | single-cam but similar-appearance | 1 | stresses ReID |

---

## 9. Metrics

- **IDF1 (global)**: identity-focused F1 computed with one global ID per object across all cams. Primary metric.
- **IDP / IDR**: precision / recall of identity mapping.
- **MOTA-MC, MOTP-MC**: multi-camera extensions.
- **HOTA-MC**: current gold standard (association + detection + localization, joint).
- **MCTA** (Multi-Camera Tracking Accuracy): older.
- **Rank-1 @ handover** across specific camera pair.

---

## 10. Notable systems

- **AI City Challenge 2021-2024 winners** (Baidu, NCKU, NVIDIA) — hierarchical clustering + learned topology + TransReID.
- **MTMCT-ELECTRICITY** — single-stage joint detection + ReID + topology.
- **Deep-EIoU / DeepEIoU-Track** — vehicle-focused.
- **ReST** — re-identification via spatio-temporal transformer.
- **Deep-Person** — person reID baseline still used.
- **FastReID** — widely used toolbox (JDAI).
- **BoxMOT / mmdet + Trackers** (OSS) — ByteTrack/BoT-SORT with ReID, easy drop-in.
- **FastMOT** — production-grade real-time MOT; extensible to MTMC with external topology.

---

## 11. OSS tool stack (2025)

- **BoxMOT** (`github.com/mikel-brostrom/boxmot`) — MOT + ReID wrappers; best starting point.
- **MMTracking** (OpenMMLab) — research-style; many SOTA trackers.
- **FastReID** — state-of-the-art ReID backbones, easy to finetune.
- **DeepStream Multi-Camera App** — production NVIDIA reference, Kafka sink.
- **NVIDIA Metropolis / Isaac** — higher-level city / robot platforms.
- **OpenCV** homography + Kalman for overlapping quick-start.
- **FAISS / Milvus / Qdrant** — vector DB for gallery search across cameras.

---

## 12. Production notes

- Run per-camera MOT on edge (Jetson / Xeon); ship **tracklets + features** to central node, not frames.
- Feature vectors are ~1-4 KB each; cheap to ship.
- Global associator should be stateful service (Redis / in-memory map) with TTL eviction.
- Design for N+1 camera scale-out: new camera = new input + topology edges, no rearchitecture.
- Log every global-ID assignment + merge for forensics.

---

## 13. Relation to the identical-bottles case study

`_REFERENCE/CaseStudy_IdenticalBottles_MultiCamera.md` is a **degenerate MTMC** — appearance embedding carries zero signal because every object is visually identical. Solution: replace appearance with:
- Physical anchor (RFID / cap code) = identity feature.
- Conveyor encoder = exact transit time across cameras.
- Tray pose + slot grid = spatial identity feature.

Same pipeline, appearance channel swapped for instrumentation channel.

---

## 14. Common pitfalls

- Ignoring topology → combinatorial explosion of false matches.
- Using per-camera ReID models → domain shift destroys similarity.
- No cool-down → same person matched to themselves in rapid flicker.
- Treating every frame as independent → tracklet features are way more robust than per-frame.
- Relying on wall-clock time across cameras without PTP → µs drift kills overlapping fusion.

---

## 15. Reading list

- *AI City Challenge* yearly workshop papers — CVPRW.
- *Multi-Target Multi-Camera Tracking: A Survey* — Iguernaissi et al. 2019.
- *TransReID* — He et al. 2021.
- *Camera-aware Proxies for Unsupervised Person ReID* — Wang et al. 2021.
- *Real-Time City-Scale Multi-Camera Vehicle Tracking* (NVIDIA) — 2022.
- *WILDTRACK* — Chavdarova et al. 2018.
