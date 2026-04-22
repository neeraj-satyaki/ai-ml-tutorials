# Plan — Real-time multi-camera video inference pipeline (detection + tracking)

> Low-latency, on-premise video analytics that ingests RTSP from N cameras, runs detection + cross-camera tracking on a GPU edge box, emits events to a message bus, and exposes a WebRTC preview stream.

## Non-goals
- Cloud-only deployment.
- Training new models (uses pretrained YOLO + ReID).
- Audio analysis (separate pipeline).

## Open Questions
- Target FPS per camera vs GPU count — do we time-share 8 cameras on one GPU or dedicate 1:1?
- ReID embedding storage: in-process vs redis vs Milvus?
- Do we need person de-identification at the edge for privacy by default?

## Domain: DL
> **Why:** The vision models (YOLO, ByteTrack, OSNet) come from the CV + streaming knowledge base.

### Concept: Computer Vision — Streaming Inference
> **Why:** Batching, latency budgets, and tracking logic differ materially from image-level inference.

#### Chapter: Detection
> **Why:** Upstream step — errors cascade into tracking.

##### Topic: YOLOv10 (or v9) for real-time detection
> **Why:** End-to-end NMS-free + strong speed/accuracy on commodity GPUs.
> **Refs:** `DL/ComputerVision/ObjectDetection/`, `DL/ComputerVision/Streaming.md`

- **Rule:** Run at 640x640, FP16, INT8 where supported.
  - *Why:* 2-3x throughput gain with <0.5 mAP loss.
  - *Enforce:* CI benchmark + regression gate.
- **Rule:** TensorRT-compiled engines pinned per GPU model.
  - *Why:* JIT compilation on first request kills P99 latency.
  - *Enforce:* Build engines in CI; store in artifact registry; runtime loads by SHA.

#### Chapter: Multi-object Tracking (MOT)
> **Why:** Detection ≠ identity; downstream events need stable IDs.

##### Topic: ByteTrack + OSNet ReID
> **Why:** ByteTrack for single-cam, OSNet features for cross-camera linking.
> **Refs:** `DL/ComputerVision/MultiObjectTracking/`

- **Rule:** IoU + appearance fusion with appearance weight = 0.3 initial.
  - *Why:* Motion dominates when detections are dense; appearance rescues occlusions.
  - *Enforce:* A/B by HOTA on a held-out clip set.
- **Rule:** ReID feature store rolls a 30-second window per camera.
  - *Why:* Bounds memory + keeps matches topical.

### Concept: Latency + Throughput Engineering
> **Why:** "Real-time" is only real if p95 < target.

#### Chapter: Pipeline design
> **Why:** Bad pipeline design ruins even a fast model.

##### Topic: Asynchronous producer-consumer
> **Why:** Decouple decode → preprocess → infer → postprocess → emit.
> **Refs:** `DesignPatterns/Concurrency/ProducerConsumer/`

- **Rule:** Bounded ring-buffer per stage; drop oldest on overflow.
  - *Why:* Back-pressure on ingest; never run out of memory.
  - *Enforce:* Metric `queue.drop_rate` with SLO.
- **Rule:** Batch detections across cameras within a 10 ms window.
  - *Why:* GPU efficiency at the cost of +10 ms latency — tunable.

## Domain: ComputerArchitecture
> **Why:** GPU memory + PCIe are the real bottlenecks for multi-stream inference.

### Concept: Accelerator-aware scheduling
> **Why:** A model that "fits in VRAM" still thrashes under parallel streams.

#### Chapter: GPU resource contention
> **Why:** Avoid the sawtooth latency pattern under load.

##### Topic: MPS / MIG / single-process batching
> **Why:** Three viable strategies with different tradeoffs.
> **Refs:** `ComputerArchitecture/Parallelism/`, `Ops/MLOps/` (GPU scheduling section)

- **Rule:** Prefer a single inference process that batches across streams.
  - *Why:* MPS multi-process has kernel-launch overhead per client.
- **Rule:** If using K8s, pin the process to a single GPU via device plugin.
  - *Why:* Prevents noisy-neighbor VRAM fragmentation.

## Domain: Backend
> **Why:** Events + control plane + serving layer are classic backend work.

### Concept: Streaming APIs
> **Why:** Two consumers: event bus (async) and live preview (sync).

#### Chapter: Event bus
> **Why:** Detections feed downstream analytics, alerts, retention.

##### Topic: Kafka (or Redpanda) with Avro
> **Why:** Schema evolution matters; JSON-only is a maintenance bomb.
> **Refs:** `Backend/MessagingJobs/`, `SystemDesign/Messaging/`

- **Rule:** One topic per event type: `detections.v1`, `tracks.v1`, `alerts.v1`.
  - *Why:* Consumers subscribe to what they need; independent compaction.
  - *Enforce:* Schema registry gates CI.
- **Rule:** Partition by `camera_id`.
  - *Why:* Per-camera ordering preserved downstream without global sequencing.

#### Chapter: Live preview
> **Why:** Operators want a dashboard with overlays.

##### Topic: WebRTC fan-out via Pion (Go) or MediaSoup
> **Why:** Sub-200 ms glass-to-glass, NAT traversal, browser-native.
> **Refs:** `NetworkSecurity/Crypto_Protocols/QUIC_Security/`, `DL/ComputerVision/Streaming.md`

- **Rule:** Encode preview as VP9/H.264 at 720p15, not 4K30.
  - *Why:* Bandwidth + CPU; operators don't need full res for monitoring.

## Domain: Ops
> **Why:** 24/7 edge deployment = observability is the whole game.

### Concept: Edge-box operability
> **Why:** You ship to N sites; debugging by SSH is not scalable.

#### Chapter: Remote ops
> **Why:** Field tech < cloud tech.

##### Topic: Tailscale / Netbird + centralized logs
> **Why:** Secure mesh + log aggregation is the minimum.
> **Refs:** `Ops/GitOps/`, `SystemDesign/Observability/`

- **Rule:** Every box pushes logs + metrics + traces via OpenTelemetry.
  - *Why:* One pane of glass; no SSH required for triage.
  - *Enforce:* Bootstrap config includes telemetry; alert if missing.
- **Rule:** OTA updates via GitOps; site-local rollback tag.
  - *Why:* Cannot afford to brick a remote site.

### Concept: Privacy + Safety
> **Why:** Cameras create compliance exposure the moment they record humans.

#### Chapter: Privacy by default
> **Why:** Legal is cheaper when the design is right from day 1.

##### Topic: On-device anonymization for preview + retention
> **Why:** Blurred faces leaving the box = smaller compliance surface.
> **Refs:** `DL/ComputerVision/DeepfakeDetection_Forensics/` (inverse) + `Cybersecurity/PrivacyEngineering/`

- **Rule:** Preview streams blur faces by default; unblur is an auditable action.
  - *Why:* Separates "monitoring" from "investigation" roles.
- **Rule:** Retention ≤ 30 days unless flagged; flagged clips go to WORM storage.
  - *Why:* Matches typical data-minimization policy.
