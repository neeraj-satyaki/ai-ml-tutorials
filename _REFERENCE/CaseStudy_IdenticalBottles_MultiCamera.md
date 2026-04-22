# Case Study — Tracking Identical Bottles Across Multiple Cameras

## Problem
Tray full of Fanta bottles enters processing equipment. Exits filled, capped — all bottles look **visually identical** (same label, same fill level, same cap). Multiple cameras watch the line. Goal: maintain per-bottle identity end-to-end.

Post-processing appearance-ReID fails (nothing to distinguish). Must substitute **spatial + temporal + instrumented** identity.

---

## 1. Identity reformulation
`bottle_id ≠ appearance`. Instead:
```
bottle_id = f(tray_id, slot_row, slot_col)
```
Track the tray, not the bottle. Bottles inherit ID from fixed slot geometry.

---

## 2. Physical-world identity anchors (cheapest → most robust)

| Anchor | Cost | Robustness | Notes |
|--------|------|------------|-------|
| Tray pose + slot grid | low | medium | Requires FIFO through equipment |
| Colored marker trays (periodic) | low | low (validation only) | Sanity-check ID continuity |
| Tray barcode / QR / datamatrix | low | medium-high | Camera or laser scanner at in/out |
| RFID tag on tray | medium | high | Reader antennas at in/out of blackbox |
| Inkjet code on cap (bottom side) | low | high | Domino/Videojet inline; readable under camera |
| Laser-etched datamatrix on cap | medium | very high | Inline fiber laser at capping station |
| Bottle-shoulder engraving | higher | highest | Permanent, works even label-less |
| Datamatrix on label (during label apply) | low | high | If label station is in your line |

Pick based on whether the processing equipment **preserves order (FIFO)** or may **reorder internally**.

---

## 3. Equipment-preserves-order (FIFO) path
Cheapest working solution when operationally verified.

### Steps
1. **Validate FIFO** with test runs (dyed bottles in known slots → verify exit order).
2. Measure **transit time distribution** through equipment. Must be tight (low σ).
3. Pre-equipment: assign `tray_id` + per-slot `(row, col)`.
4. At exit: predicted tray = entry tray shifted by transit time.
5. Reconcile: bottle count in = bottle count out per tray. Alarm on mismatch.

### Caveats
- Upstream backup or operator intervention can break FIFO.
- Jam / recovery events break FIFO — must emit "unknown identity" flag and quarantine those trays.

---

## 4. Equipment may reorder — instrumented path
Must add **read-only identity** that survives the blackbox.

### Recommended: per-tray RFID
- Passive UHF tag glued under tray (once).
- RFID reader at entry → write `tray_id` to WMS.
- RFID reader at exit → recover `tray_id`.
- Vision outside the blackbox tracks tray; inside, RFID carries the ID.

### Alternative: per-bottle cap code
- Inline laser/inkjet at capping station writes a short code (timestamp-derived) on cap crown.
- Top-down vision reads code via small high-res camera with ring light.
- Works even if equipment reorders (each bottle self-identifies).

---

## 5. Multi-camera fusion

### Calibration
- Extrinsic calibration of all N cameras to a common **belt-plane** frame (a flat surface = conveyor top).
- Use a checkerboard or ChArUco target laid on belt; compute homographies.
- Output: each camera can project detections to a common (x, y) on belt.

### Temporal sync
- **PTP (IEEE 1588)** hardware time on all NICs / cameras.
- **Conveyor encoder** (incremental or absolute) broadcast to every node. Each frame stamped with `(t_ptp, belt_pos)`.
- Handoff between cameras uses `belt_pos`, not wall-clock — immune to varying processing latency.

### Tracking in belt-BEV (bird's-eye view)
```
frame ─► detector ─► boxes in image coords
                     │
                     ▼
              homography H_i to belt plane
                     │
                     ▼
   unified belt-BEV detection stream (x, y, belt_pos, camera_id)
                     │
                     ▼
        tray tracker (ByteTrack / BoT-SORT on BEV)
                     │
                     ▼
         per-tray slot assignment
                     │
                     ▼
              bottle_id stream
```

Motion model for tracker is trivial: x moves with belt velocity (known from encoder), y near zero.

---

## 6. Detector choices

- **Tray detection**: YOLOv8/v10 or RT-DETR fine-tuned on top-down tray images. Mask head helps slot grid accuracy.
- **Bottle detection**: optional; if slot grid is reliable, skip per-bottle detection outside of fill-check QA.
- **Cap-code reading**: specialized OCR (TrOCR or dedicated barcode decoder like libdmtx / ZBar for datamatrix).
- **Tray corner / fiducial**: AprilTag or ChArUco printed on tray aids pose when bottles occlude.

---

## 7. Software stack (reference)

### Ingest
- **NVIDIA Rivermax** for SMPTE 2110 or low-latency RTP if cameras are broadcast-grade.
- **GigE Vision / USB3 Vision** cameras → **Aravis** or vendor SDK → **GStreamer**.
- **NVIDIA DeepStream** for multi-stream GPU-native pipeline.

### Inference
- TensorRT INT8 YOLO for detection.
- BoT-SORT with BEV positions (appearance weight = 0 for bottles, = 0.3 for tray).

### Data plane
- Kafka topic `trays.events` (tray enter/exit, slot assignments).
- Kafka topic `bottles.events` (per-bottle state at each camera).
- Redis for active-tray state (TTL-bound; cleared on exit).

### Control / HMI
- Node-RED or internal dashboard shows live tray→slot→bottle state.
- Manual override UI for jams (operator marks tray as "unknown — quarantine").

---

## 8. Validation & QA

| Test | What it catches |
|------|-----------------|
| Dye batch | FIFO assumption, order preservation |
| Missing-bottle slot | Slot-grid assignment accuracy |
| Double-tray overlap in camera | Tracker under crowding |
| High-speed run | Motion blur, detector recall |
| Occluded tray corner | Pose estimation without fiducials |
| Reader failure simulation | Degraded mode behavior |
| Power blip | State recovery / Kafka replay |

---

## 9. Degraded modes
Design for them upfront.

- **Tag read miss** → mark tray "identity uncertain"; downstream can still count but not trace.
- **Detector gap** → predict from belt velocity; if > T seconds, escalate.
- **Camera offline** → tracker continues on neighbor cameras if overlap exists; belt-pos fills gap.
- **Equipment jam** → stop tracking ID assignment; flush state; resume on confirmed restart.

---

## 10. Repo mapping

| This case touches | Location |
|-------------------|----------|
| Tracking + ReID | `DL/ComputerVision/Tracking_and_ReID.md` |
| Pipeline engines | `_REFERENCE/Streaming_Frameworks.md` |
| Low-latency ingest | `_REFERENCE/Rivermax.md` |
| Multi-camera fusion | `DL/ComputerVision/CrossCameraTracking_MTMC/` |
| Embedded / PLC bridge | `ElectronicsCommunication_Embedded/EmbeddedBuses_Protocols/` (Modbus/OPC-UA to PLC encoder) |
| OT/ICS security boundary | `Cybersecurity/OT_ICS_SCADA/` |
| Concept drift on fill level | `ML/Streaming/DriftDetection/` |

---

## 11. TL;DR decision tree

```
Is processing equipment strictly FIFO?
├─ yes → tray pose + slot grid + encoder-tagged BEV tracking. Done.
└─ no  → need hard identity anchor.
         ├─ tray-level granularity OK?   → RFID per tray.
         └─ bottle-level required?       → inline cap code (laser or inkjet).
```

## 12. Cost-ranked solution order
1. FIFO + tray pose + slot grid + encoder sync. **Try first.**
2. Add colored-marker validation runs.
3. Add per-tray RFID.
4. Add per-bottle cap code if tracing per bottle is mandated (QA / regulatory).
