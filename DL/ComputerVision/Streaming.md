# Computer Vision — Streaming & Real-Time Inference

Everything specific to video streams vs single-image inference.

## 1. Ingest
- Protocols: **RTSP** (IP cams), **RTMP** (legacy ingest), **WebRTC** (low-latency bi-di), **HLS / DASH** (adaptive playback), **SRT** (contribution).
- Tools: **FFmpeg** (decode/transcode), **GStreamer** (pipelines), **NVIDIA DeepStream** (GPU-native), **MediaMTX** (router).
- Keyframe detection, GOP structure, frame skipping strategies.

## 2. Inference pipelines
- **NVIDIA Rivermax** — kernel-bypass SMPTE 2110 / RoCE ingest, NIC→GPU zero-copy. Sub-µs jitter. See `_REFERENCE/Rivermax.md`.
- **NVIDIA DeepStream** + Triton Inference Server — GPU-accelerated, H.264/265 hw decode.
- **NVIDIA Holoscan** — medical/edge streaming AI.
- **Intel DL Streamer** (GStreamer plugins).
- **OpenVINO** for Intel CPUs/iGPU.
- **TensorRT-LLM** + **TensorRT** for model optimization.

## 3. Online / Streaming Algorithms
- **Online object detection** — YOLO v8/v9/v10 on frames, tuned for FPS budget.
- **Online tracking** — ByteTrack, OC-SORT, DeepSORT, StrongSORT, BoT-SORT.
- **ReID across streams + cameras** — OSNet, TransReID embeddings.
- **Sliding-window inference** — for action/segmentation temporal context.
- **Incremental / warm-start** — reuse prior-frame features to save compute.

## 4. Latency-critical design
- **Batched vs single-frame** — batching improves throughput, hurts tail latency.
- **KV-Cache + streaming VLMs** — for video-LLM captioning in real-time.
- **Frame skipping + motion gating** — skip static frames to save GPU.
- **Async pipelines** — producer/consumer queues (frame capture → pre → model → post → display).

## 5. Edge streaming
- **Jetson Orin Nano / NX / AGX** — on-device inference + streaming.
- **Google Coral** (Edge TPU), **Hailo-8/15**, **Qualcomm QNN**.
- **ONNX Runtime Mobile / TFLite** — on mobile.
- Bandwidth-adaptive: send region-of-interest only, downscale off-hours.

## 6. Specialized topics
- **Event cameras (DVS)** — asynchronous pixel events; low-latency, low-power.
- **Multi-camera fusion** — calibrated rigs, BEV fusion.
- **Low-latency protocols** — **SRT** (secure reliable transport), WebRTC data channels, LL-HLS.
- **ROI streaming** — encode only changed regions.
- **Video analytics pipelines** — loitering, line-crossing, people-counting.
- **Privacy / anonymization streams** — real-time face blur / license-plate blur.
- **Video summarization** — keyframe + caption + query.
- **Streaming VQA + VLM** — live narration with Qwen2-VL, GPT-4o realtime, Gemini Live.

## 7. Evaluation
- **FPS** (target 30/60 depending on use).
- **End-to-end latency** (capture → decision) p50/p95/p99.
- **MOTA / IDF1 / HOTA** — multi-object tracking metrics.
- **mAP / IoU** for detection/seg.
- **Frame drops**, GPU utilization, bandwidth.

## 8. Typical stacks
- **Security / VMS**: Milestone, Genetec + YOLO/RTSP ingest.
- **Retail analytics**: People counting / heat-map + BI dashboard.
- **Traffic / smart city**: Lane detection, vehicle count + ANPR.
- **Sports / broadcast**: Pose + tracking + graphics overlay.
- **Industrial QA**: Conveyor anomaly detection with line-scan cameras.
- **Medical OR**: Holoscan + surgical phase segmentation.
