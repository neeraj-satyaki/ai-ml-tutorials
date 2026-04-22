# Object Tracking & Re-Identification (ReID)

Tracking = maintain identity of objects over time. ReID = match identity across cameras / after long occlusion.

---

## 1. Taxonomy

| Task | Input | Output | Typical setting |
|------|-------|--------|-----------------|
| **SOT** Single-Object Tracking | box in frame 1 | box in all frames | user-initialized, 1 target |
| **MOT** Multi-Object Tracking | detections per frame | tracks with stable IDs | surveillance, autonomy |
| **VOS** Video Object Segmentation | mask in frame 1 | mask per frame | video editing, labeling |
| **VIS** Video Instance Segmentation | — | per-instance masks + IDs | cells, crowds |
| **ReID** | query image | ranked gallery matches | cross-camera, re-entry |
| **MTMC** Multi-Target Multi-Camera | detections from N cams | global IDs | smart city, retail |
| **Pose Tracking** | keypoints per frame | consistent skeletons | sports, mocap |

---

## 2. Single-Object Tracking (SOT) (`SingleObjectTracking/`)

### Classical
- **MOSSE** (2010) — correlation filter in frequency domain. Fast.
- **KCF** (2014) — kernelized correlation filter.
- **CSR-DCF** (2017) — spatial reliability map.

### Siamese (learned similarity) (`SiameseTrackers/`)
- **SiamFC** (2016) — cross-correlate template vs search.
- **SiamRPN / SiamRPN++** (2018-19) — add region proposal net.
- **SiamMask** — joint seg + tracking.
- **Ocean, SiamCAR, SiamBAN** — anchor-free.

### Transformer-based (`TransformerTrackers/`)
- **TransT** (2021) — attention for template-search fusion.
- **STARK** (2021) — spatio-temporal transformer.
- **MixFormer** (2022) — iterative mixed attention.
- **OSTrack** (2022) — one-stream joint backbone + relation.
- **SeqTrack** (2023), **ARTrack** (2023) — autoregressive.
- **SAM 2** (2024) — prompt-based track-anything (video segmentation).

### Benchmarks
OTB, VOT, GOT-10k, LaSOT, TrackingNet, UAV123.

---

## 3. Multi-Object Tracking (MOT) (`MultiObjectTracking/`)

### Tracking-by-detection paradigm
Detector → per-frame boxes → associator links across frames.

### Classic
- **SORT** (2016) — Kalman filter + Hungarian on IoU.
- **DeepSORT** (2017) — SORT + appearance embeddings.
- **IoU Tracker** — IoU-only fallback.

### Modern two-stage
- **ByteTrack** (2022) — associate **all** detections (high + low conf). Big jump in MOTA.
- **OC-SORT** (2022) — Observation-Centric; fixes Kalman drift during occlusions.
- **BoT-SORT** (2022) — ByteTrack + camera motion compensation + ReID.
- **StrongSORT** (2022) — DeepSORT polished with strong backbones.
- **DeepOC-SORT** (2023) — OC-SORT + deep embeddings.
- **Hybrid-SORT** (2024).

### End-to-end (detect + track jointly)
- **CenterTrack** (2020) — predict offsets between frames.
- **FairMOT** (2020) — joint det + ReID head.
- **TransTrack** (2020), **TrackFormer** (2021), **MOTR / MOTRv2** (2022) — transformer decoders carry track queries across frames.
- **MOTRv3 / CO-MOT** (2023-24).
- **MeMOTR**, **MeMOT** — memory-augmented.

### Benchmarks
MOT15/16/17/20 (pedestrians), DanceTrack (similar appearance), SportsMOT, BDD100K (driving), KITTI, TAO (long-tail).

### Metrics
- **MOTA** (accuracy; penalizes FP/FN/ID switches).
- **MOTP** (localization precision).
- **IDF1** (identity-focused F1).
- **HOTA** (current gold standard; balances det + assoc + localization).
- **AssA, DetA** — sub-components of HOTA.
- **IDSW** — ID switch count.

---

## 4. Re-Identification (ReID) (`PersonReIdentification/`, `VehicleReIdentification/`)

### Goal
Given a probe image, rank gallery images by identity similarity. Works across different cameras, times, poses.

### Architectures
- **IDE** (Identity Discriminative Embedding, 2016) — classification backbone + feature.
- **PCB** (Part-based Conv Baseline, 2018) — horizontal stripes.
- **MGN** (Multi-Granularity Network, 2018) — global + part branches.
- **OSNet** (2019) — multi-scale omni-scale features. Lightweight SOTA for edge.
- **BoT / AGW** (2019-20) — batch-hard tricks + non-local.
- **TransReID** (2021) — pure ViT for ReID.
- **CLIP-ReID** (2023) — CLIP init + prompt learning.
- **SOLIDER** (2023) — self-supervised human-centric pretrain.

### Losses
- **Softmax** (identity classification).
- **Triplet loss** with batch-hard sampling: pull positive, push negative.
- **Center loss**, **Circle loss**, **Arcface** (also used in face recog).
- **Contrastive** — multi-view / multi-camera.
- Combined: ID + triplet (standard recipe).

### Data tricks
- Random erasing, random cropping, flipping.
- Camera-style augmentation (CycleGAN between cams).
- Label smoothing (+0.1).

### Benchmarks
Market-1501, DukeMTMC-reID, MSMT17, CUHK03, LTCC (long-term, clothing change), PRCC, VeRi-776 (vehicle), VehicleID.

### Metrics
- **Rank-1 / Rank-5 / Rank-10** accuracy.
- **mAP**.
- **CMC** curve.

### Specialized
- **Occluded ReID** (OCC-Duke, OCC-Reid): OccRef models.
- **Cross-modality ReID** (RGB ↔ thermal, RGB ↔ sketch).
- **Long-term ReID** (clothing change): LTCC, Cloth-Changing baselines.
- **Text-to-image person retrieval**: CUHK-PEDES, **IRRA** (2023).

---

## 5. Cross-camera / MTMC Tracking (`CrossCameraTracking_MTMC/`)

Connect tracks from multiple cameras into one global identity per person/vehicle.

### Pipeline
1. Per-camera MOT (e.g., ByteTrack).
2. Extract per-track appearance (OSNet, CLIP-ReID).
3. Spatio-temporal filter: unreachable transitions are pruned (camera topology, speed limits).
4. Appearance-based clustering / Hungarian across cameras.

### Notable systems
- **AI City Challenge** winners (NVIDIA) — for city-scale.
- **Deep-EIoU** — vehicle MTMC.

### Metrics
IDF1, IDP, IDR at the **global** ID level (CityFlow-ReID, AICity).

---

## 6. Video Object Segmentation (VOS) (`VideoObjectSegmentation_VOS/`)

Track a mask, not a box.
- **STM** (Space-Time Memory Networks, 2019).
- **XMem** (2022) — memory-efficient.
- **Cutie** (2023).
- **SAM 2** (2024) — universal prompt-based video segmentation.

Benchmarks: DAVIS, YouTube-VOS, MOSE, LVOS.

---

## 7. Online / Realtime Tracking (`OnlineTracking_Realtime/`)

### Design constraints
- Causal (no future frames).
- Latency budget per frame (e.g., ≤ 33 ms for 30 FPS).

### Engineering tricks
- Asynchronous detection + tracking threads.
- Track on every frame, detect every K frames (K=2-4).
- Skip ReID compute unless new track OR occlusion resolved.
- Pre-compute ReID features in batches on GPU.
- Keep embedding store bounded (30-60 sec sliding).

### Stacks
- **NVIDIA DeepStream** + **NvDCF** or **NvDeepSORT** tracker.
- **Ultralytics** YOLO + built-in BoT-SORT / ByteTrack.
- **FFmpeg** → per-frame numpy → tracker → Kafka events.

---

## 8. Appearance Embeddings (`AppearanceEmbeddings/`)

Cross-cut concept used by DeepSORT/ByteTrack/ReID alike.
- CNN backbone (OSNet / ResNet-50-ibn).
- ViT (TransReID, CLIP vision).
- Trained with **identity + triplet**.
- Output ℓ2-normalized vector (typically 256-2048d).
- Similarity = cosine; ANN index for gallery search (FAISS, HNSW).

---

## 9. Common pitfalls

- **ID switches under occlusion** — fix: appearance + longer Kalman horizon (OC-SORT).
- **Camera motion → Kalman drift** — fix: camera motion compensation (BoT-SORT).
- **Similar appearance (crowds, teams)** — fix: DanceTrack-style appearance-robust methods.
- **Domain shift across cameras** — fix: per-camera batch norm, camera-adversarial training.
- **Clothing change** — fix: face / biometrics / gait fallback; LTCC models.
- **ReID feature drift over long sessions** — fix: EMA update, feature bank replacement.

---

## 10. Recommended stack (2025)

**Real-time surveillance (edge GPU):**
- Detector: YOLOv10 INT8 TensorRT.
- Tracker: BoT-SORT with OSNet-x1.0 ReID head.
- Cross-camera: OSNet features + FAISS HNSW index.
- Sink: Kafka → analytics.

**Research / offline:**
- Detector: Co-DETR / RT-DETR.
- Tracker: MOTRv3 end-to-end or ByteTrack + CLIP-ReID.
- Benchmarks on HOTA / IDF1.

---

## Books / papers to start
- *Simple Online and Realtime Tracking* (SORT) — Bewley 2016.
- *ByteTrack: Multi-Object Tracking by Associating Every Detection Box* — Zhang 2022.
- *Observation-Centric SORT* — Cao 2022.
- *TransReID* — He 2021.
- *OSNet: Omni-Scale Feature Learning for Person ReID* — Zhou 2019.
- *HOTA metric paper* — Luiten 2021.
