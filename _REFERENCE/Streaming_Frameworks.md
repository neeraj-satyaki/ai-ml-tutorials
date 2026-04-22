# Video / Media Streaming Frameworks for AI Pipelines

Comparison of the common pipeline engines used to move media from sensor → decode → preprocess → inference → post → sink.

Each has a different scope, hardware affinity, and abstraction level. Pick based on target hardware, throughput, deployment, and team skill.

---

## 1. GStreamer
The foundation. Open-source, LGPL. Element-based graph (source → filters → sinks).

- **Scope:** general multimedia framework. Audio + video + metadata.
- **Strengths:** battle-tested (desktop, embedded, automotive), mature codec support, huge plugin library, runs on Linux/macOS/Windows/Android.
- **Weaknesses:** C API, steep learning curve, debugging pipelines painful.
- **Use when:** you need codec coverage + flexibility and can invest in the API.
- **Hardware:** CPU, Intel VAAPI, NVIDIA NVDEC (via `nvh264dec`), V4L2, RPi MMAL, Apple VideoToolbox.
- **Language:** C, bindings for Python (`pygobject`), Rust, Go, Node.

```bash
# decode RTSP, resize, display
gst-launch-1.0 rtspsrc location=rtsp://... ! decodebin ! videoscale ! autovideosink
```

---

## 2. NVIDIA DeepStream
GStreamer + NVIDIA plugins for AI video analytics. Proprietary SDK, free-to-use.

- **Built on:** GStreamer.
- **Scope:** multi-stream real-time inference on NVIDIA GPUs / Jetson / DGX.
- **Key plugins:** `nvstreammux`, `nvinfer`, `nvtracker` (NvDCF / IOU / DeepSORT), `nvmultiurisrcbin`, `nvdewarper`, `nvdsanalytics`, `nvmsgbroker` (Kafka/MQTT/Redis sink).
- **Strengths:** 100+ streams / GPU at real time, TensorRT built-in, Python + C++ APIs, DeepStream 7+ supports **Rivermax** ingest.
- **Weaknesses:** NVIDIA-only, opaque plugin internals, versions bump fast.
- **Use when:** high-throughput GPU video analytics at edge (Jetson) or server (T4/A100/L40).

```
rtsp → nvstreammux → nvinfer (YOLO TRT) → nvtracker → nvdsanalytics → Kafka
```

---

## 3. Intel DL Streamer (`dlstreamer`)
GStreamer plugins optimized for Intel CPUs + iGPU + NPUs. Open-source, Apache-2.

- **Built on:** GStreamer + OpenVINO.
- **Key plugins:** `gvadetect`, `gvaclassify`, `gvainference`, `gvatrack`, `gvapython`, `gvametaconvert`, `gvametapublish`.
- **Strengths:** runs on any Intel box, metadata JSON flows natively, Kafka/MQTT publishers, Kubernetes-friendly.
- **Weaknesses:** tied to OpenVINO model format, smaller ecosystem than DeepStream.
- **Use when:** target is Intel (Core / Xeon / Arc / Gaudi / Movidius).
- **Part of:** OpenVINO toolkit / Edge Insights for Industrial (EII).

```
rtsp → decodebin ! videoconvert ! gvadetect model=yolov8.xml ! gvatrack ! gvametapublish ! kafka
```

---

## 4. NNStreamer
Samsung + LG open-source (LG Electronics, Linux Foundation). Tensor-aware GStreamer plugins.

- **Built on:** GStreamer.
- **Scope:** on-device ML pipelines on phones, TVs, appliances, edge IoT. Consumer-electronics heritage.
- **Key plugins:** `tensor_filter` (TFLite, ONNX, NCNN, Pytorch, NNFW, SNPE, OpenVINO), `tensor_converter`, `tensor_transform`, `tensor_sink`.
- **Strengths:** runtime-agnostic, minimal footprint, Android support, signed hot-swap of models.
- **Weaknesses:** less inference tuning than DeepStream / DL Streamer.
- **Use when:** mobile / CE devices, multi-runtime portability, Tizen/Android Edge.

---

## 5. VideoPipe
Open-source C++ pipeline framework (Apache-2). Lightweight, GStreamer-free.

- **Scope:** build video analytics pipelines without GStreamer's learning curve.
- **Architecture:** node graph — `VP_RTSP_SRC_NODE → VP_INFER_NODE → VP_TRACK_NODE → VP_OSD_NODE → VP_ENC_RTSP_SINK_NODE`.
- **Backends:** OpenCV DNN, ONNX Runtime, TensorRT, Paddle Inference, Triton.
- **Strengths:** small codebase, easy to read/extend, no GStreamer ABI chasing.
- **Weaknesses:** smaller community, fewer codec paths than GStreamer.
- **Use when:** you want a readable pipeline in pure C++ with Python bindings.
- **Repo:** github.com/sherlockchou86/VideoPipe.

---

## 6. Pipeless
Rust-based CV framework with Python stages. Apache-2.

- **Scope:** "serverless CV" — write a few Python functions, Pipeless wires them with a Rust core that handles decode/encode/streams.
- **Stages:** `pre-process → process → post-process → on_stream_start / end`.
- **Strengths:** Python-first DX, streams are hot-reloadable, works with RTSP/WebRTC/files, runs in Docker or bare metal, K8s operator planned.
- **Weaknesses:** newer project, smaller plugin catalog.
- **Use when:** prototyping CV apps fast without writing GStreamer, or wrapping existing Python models.
- **Repo:** github.com/pipeless-ai/pipeless.

---

## 7. MediaStream (W3C)
Browser API, not a server framework. `navigator.mediaDevices.getUserMedia({video, audio})`.

- **Scope:** capture webcam/mic in a browser, feed to `<video>`, `RTCPeerConnection`, or `MediaRecorder`.
- **Related APIs:** MediaStreamTrack, MediaStreamTrackProcessor (`requestVideoFrameCallback`), Web Codecs, WebRTC.
- **Use when:** building browser video apps, WebRTC clients, in-browser ML via `tfjs` / `onnxruntime-web` / WebGPU.
- **Bridges to backend:** WebRTC (to SFU like mediasoup/LiveKit/Janus) → server pipeline (GStreamer/DeepStream).

```js
const stream = await navigator.mediaDevices.getUserMedia({video: true})
videoEl.srcObject = stream
const track = stream.getVideoTracks()[0]
const proc = new MediaStreamTrackProcessor({track})
for await (const frame of proc.readable) { /* infer */ frame.close() }
```

---

## 8. Related / adjacent

- **FFmpeg** — CLI + libs. Unmatched codec support. Good for batch transcoding or feeding frames into Python. Not pipeline-graph-native, but DeepStream/DL Streamer/VideoPipe/Pipeless all lean on it via GStreamer elements or libav directly.
- **NVIDIA Holoscan** — medical/edge AI framework; uses GStreamer + Rivermax + TensorRT under the hood.
- **MediaPipe (Google)** — on-device graph framework (mainly mobile). Hand/pose/face models + custom calculators. Similar graph mental model; own runtime, not GStreamer.
- **GStreamer WebRTC (`webrtcbin`) / LiveKit / mediasoup / Janus / Pion** — SFU/MCU for real-time video transport.
- **Rivermax (NVIDIA)** — kernel-bypass SMPTE 2110 ingest; plugs into DeepStream/Holoscan/GStreamer via rivermaxsrc. See `_REFERENCE/Rivermax.md`.

---

## Choose-one cheatsheet

| Need | Pick |
|------|------|
| Max throughput on NVIDIA GPU | **DeepStream** |
| Intel CPU / NPU target | **DL Streamer** |
| Mobile / CE on-device | **NNStreamer** or **MediaPipe** |
| Readable C++ pipeline, any backend | **VideoPipe** |
| Python-first prototyping, RTSP→model→sink | **Pipeless** |
| General-purpose / any codec / desktop | **GStreamer** directly |
| Browser webcam / WebRTC | **MediaStream API** |
| Uncompressed broadcast (ST 2110) | **Rivermax** (often + DeepStream) |
| Batch transcoding, file I/O | **FFmpeg** |
| Medical / scientific AI | **Holoscan** |

---

## Common anti-patterns

- Hand-rolling OpenCV `VideoCapture` + `while True:` for 16 streams. Works for demos, collapses under load.
- Running TensorRT in Python per-frame without batching. You bought a GPU; use `nvinfer` or Triton batching.
- Mixing 3 frameworks in one binary. Pick one graph engine per deploy.
- Skipping timestamps / PTS propagation — downstream analytics need monotonic time, not wall clock.
- Logging every frame. Sample.

---

## Refs
- gstreamer.freedesktop.org
- developer.nvidia.com/deepstream-sdk
- github.com/open-edge-platform/dlstreamer
- github.com/nnstreamer/nnstreamer
- github.com/sherlockchou86/VideoPipe
- github.com/pipeless-ai/pipeless
- developer.mozilla.org/en-US/docs/Web/API/MediaStream_API
