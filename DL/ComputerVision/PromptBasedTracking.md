# Prompt-Based Object Tracking

"Prompt" = any user-supplied cue (click, box, mask, text) that specifies *what* to track, no training per target. Modern successor to Siamese template trackers.

---

## 1. Prompt modalities

| Prompt | Example model | Use case |
|--------|---------------|----------|
| **Point / click** | SAM 2 | user-friendly labeling, VOS |
| **Box** | SAM 2, GroundingDINO + tracker | bbox initialization from UI |
| **Mask** | SAM 2, XMem, Cutie | start from existing segmentation |
| **Text / caption** | GroundingDINO + BoT-SORT, OVTrack, MASA, T-Rex2 | open-vocabulary tracking |
| **Reference image** | DINOv2 + tracker, MASA, CoTracker | "track this exemplar" |
| **Multi-modal** | DAM4SAM, SAM 2.1 + CLIP | combined text + click |

---

## 2. Foundation: SAM 2 (Segment Anything 2)

Meta (2024). Universal promptable segmenter that works on **images and videos**.

- Architecture: hierarchical image encoder + memory attention + mask decoder + prompt encoder.
- Memory module persists across frames → tracking for free.
- Prompts: click(s), box, mask, in any frame, refinable mid-video.
- Zero-shot on unseen classes.

Variants / follow-ups:
- **SAM 2.1** (late 2024) — improved occlusion + memory.
- **SAMURAI** (2024) — motion-aware memory for long video.
- **DAM4SAM** (2024) — distractor-aware memory.
- **EfficientSAM**, **MobileSAM 2** — edge-deployable.
- **Track-Anything** — Gradio wrapper around SAM.
- **SAM-PT** (2023) — point-prompt tracking with SAM1.
- **PerSAM / PerSAM-F** (2023) — personalize SAM with one example.

### Minimal flow
```
1. User clicks on frame 0.
2. SAM2 returns mask + propagates through video via memory attention.
3. User can add correction clicks on any later frame; model refines.
```

---

## 3. Text-prompt tracking (Open-Vocabulary)

Input: natural-language description ("the red truck", "person in yellow jacket"). Tracker grounds + follows.

### Grounding + tracking stacks
- **GroundingDINO** (text → boxes) + **BoT-SORT / ByteTrack** (frame-to-frame). Simplest pipeline.
- **GroundingSAM / Grounded-SAM 2** — GroundingDINO finds box → SAM2 segments + tracks.
- **GLIP / GLIPv2** — phrase grounding backbone.
- **YOLO-World + tracker** — open-vocab detector + MOT.
- **OWL-ViT / OWLv2** — open-vocab det then track.

### End-to-end open-vocab trackers
- **OVTrack** (CVPR 2023) — first open-vocab MOT.
- **MASA** (CVPR 2024) — Matching Anything by Segmenting Anything; universal appearance for open-set tracking.
- **TAM (Track Anything Model)** (2023) — SAM + XMem.
- **T-Rex / T-Rex2** (2024) — visual prompt → detect + track across domains.
- **TAPTR / TAPIR / CoTracker** (2023-24) — track any point given a query point.
- **LocoTrack / BootsTAPIR** (2024) — dense point tracking.

---

## 4. Referring Expression Tracking

Track based on a sentence: "the child chasing the dog".

- **Refer-YouTube-VOS** / **Refer-DAVIS** benchmarks.
- **ReferFormer** (2022), **OnlineRefer** (2023).
- **LISA** (2023) — reasoning segmentation via LLM.
- **VideoLISA**, **VISA** (2024) — video reasoning + tracking via multimodal LLM.

---

## 5. Point-tracking (TAP / TAPIR family)

Track any pixel over long video — "pixel-level tracking".
- **TAP-Vid** benchmark (DeepMind 2022).
- **TAPIR** (2023), **CoTracker v1/v2/v3** (2023-24).
- **OmniMotion** — full-video 3D-aware tracking.
- Uses: dense motion for AR, video effects, feature-point SLAM, object tracking via point anchors.

---

## 6. Typical architectures

```
[Prompt]  →  [Prompt encoder]  →  [Cross-attn with image feats]
                                           │
                                           ▼
                                    [Mask / box head]
                                           │
                                           ▼
                                    [Memory bank] ◄─ past frames
                                           │
                                           ▼
                                     [Next frame]
```

Key design choices:
- **Memory length** — short (SAM2 default) vs long (SAMURAI, DAM4SAM).
- **Memory compression** — full frames (XMem) vs compact tokens.
- **Multi-object prompting** — per-object memory or shared.
- **Re-entry / re-identification** — reinit when object reappears after occlusion (usually weak in SAM2; add ReID).

---

## 7. Choosing a model

| Goal | Pick |
|------|------|
| Label a video once (GUI, click-based) | SAM 2 |
| Track by text in CCTV | GroundingDINO + SAM2 + BoT-SORT |
| Open-vocab MOT | MASA or OVTrack |
| Long video with occlusion | SAMURAI / DAM4SAM |
| Edge device | EfficientSAM or MobileSAM 2 + ByteTrack |
| Dense motion / AR | CoTracker v3 |
| Reasoning prompts ("the one opening the door") | VideoLISA / VISA |
| Personalize to an object from one exemplar | PerSAM-F or MASA with image prompt |

---

## 8. Evaluation

- **VOS**: J&F score (region similarity + contour accuracy). Benchmarks: DAVIS, YouTube-VOS, MOSE, LVOS.
- **Open-vocab MOT**: HOTA / IDF1 on open-set splits (OV-TAO, OV-MOT).
- **Point tracking**: <δ_avg (average position accuracy), OA (occlusion accuracy) on TAP-Vid.
- **Referring VOS**: J&F on Refer-YouTube-VOS.

---

## 9. Practical deployment notes

- SAM2 is heavy. Distill or use EfficientSAM for real-time.
- GroundingDINO boxes are noisy; add temporal smoothing before feeding MOT.
- Cache text embeddings once per session — don't re-encode prompts per frame.
- For UI apps, run the prompt encoder on CPU and the image encoder on GPU async.
- ReID still useful on top of SAM2 for long occlusion — SAM2 memory is short-range.

---

## 10. Open problems (2025)

- Long-term identity with clothing / viewpoint change.
- Efficient SAM2-class models for phones / Jetson.
- Reasoning-heavy prompts ("the person who dropped the bag").
- Consistent multi-object prompting without interference.
- Real-time streaming SAM2 (30 FPS at 1080p).

---

## Papers / repos
- *Segment Anything 2* — Ravi et al. 2024.
- *Grounded-SAM* — IDEA 2023.
- *MASA: Matching Anything by Segmenting Anything* — Li et al. CVPR 2024.
- *OVTrack* — Li et al. CVPR 2023.
- *CoTracker: It is Better to Track Together* — Karaev et al. 2023-24.
- *SAMURAI* — Yang et al. 2024.
- *Track Anything* — Cheng et al. 2023.
