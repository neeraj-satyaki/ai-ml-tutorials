# ONNX — Open Neural Network Exchange + Accessories

ONNX = framework-agnostic model format + runtime ecosystem. "Train anywhere, deploy anywhere."

## 1. What ONNX is

- Open spec (.onnx protobuf) for computation graph + weights.
- Originated at Facebook + Microsoft (2017); now LF AI & Data project.
- Operators versioned by **opset** (current ≥ 21).
- Supports static + dynamic shapes, control flow (If / Loop / Scan).
- **ONNX-ML** extension for classical ML (sklearn, XGBoost, LightGBM).

## 2. Why use it

- Decouple training framework from inference target.
- **One runtime, many backends**: CUDA, TensorRT, CoreML, DirectML, OpenVINO, ROCm, CPU, WebGPU, mobile.
- Better perf than framework native in many cases (graph-level optim, operator fusion).
- Stable format for model zoo distribution + versioning.

## 3. Export paths

| From | Tool |
|------|------|
| PyTorch | `torch.onnx.export` (legacy) **or** `torch.onnx.dynamo_export` (modern TorchDynamo-based) |
| TensorFlow | `tf2onnx` |
| Keras | `tf2onnx` via SavedModel |
| scikit-learn | `skl2onnx` |
| XGBoost | `onnxmltools` |
| LightGBM | `onnxmltools` |
| CatBoost | built-in `model.save_model(..., format="onnx")` |
| CoreML | `coremltools` (bidirectional) |
| MATLAB | `exportONNXNetwork` |
| JAX | `jax2tf` → `tf2onnx` |
| HuggingFace | `optimum.exporters.onnx` (one-liner) |

## 4. ONNX Runtime (ORT) execution providers

Single API, pluggable backends:

- **CPUExecutionProvider** (default).
- **CUDAExecutionProvider** (NVIDIA).
- **TensorRTExecutionProvider** — FP16/INT8, fuses.
- **DmlExecutionProvider** (DirectML, Windows GPU/NPU).
- **CoreMLExecutionProvider** (Apple).
- **ROCMExecutionProvider** (AMD).
- **OpenVINOExecutionProvider** (Intel CPU/iGPU/NPU).
- **QNNExecutionProvider** (Qualcomm NPU).
- **XNNPACKExecutionProvider** (mobile CPU).
- **NNAPIExecutionProvider** (Android).
- **JsExecutionProvider / WebGPUExecutionProvider** (browser).

Set with a list; ORT picks first available per op.

## 5. Tooling (accessories)

| Tool | Purpose |
|------|---------|
| **Netron** | Graph visualizer (desktop + web). First stop for any .onnx. |
| **onnx-simplifier (onnxsim)** | Folds constants, removes dead nodes, simplifies shapes. |
| **onnxoptimizer** | Legacy optimization passes. |
| **onnxruntime-tools** | Quantization + optimization utilities. |
| **onnxruntime-genai** | LLM-specific ONNX runtime with KV cache + tokenizer. |
| **onnx-web** | Stable Diffusion pipeline in onnxruntime-web. |
| **onnx2pytorch** / **onnx2keras** / **onnx-tensorflow** | Import ONNX back to frameworks. |
| **onnx-mlir** | MLIR-based ONNX compiler. |
| **onnxscript** | Pythonic DSL to write ONNX functions + exporter replacement. |
| **onnxconverter-common** | Shared converter utilities. |
| **tract** | Rust-native ONNX inference — small, fast, no-deps. |
| **BurnZoo** / **wonnx** | WebGPU + Rust ONNX runtimes. |
| **ONNX Model Zoo** | Reference model collection. |

## 6. Model optimization within ONNX

### Graph optimization (always on)
Constant folding, common subexpression elimination, op fusion (Conv+BN+ReLU), layout conversion, memory-planning.

### Quantization
- **Dynamic** — weights quantized, activations computed at runtime. Easiest.
- **Static** — calibration set → quantize activations. Best perf.
- **QAT (Quantization-Aware Training)** — best quality, requires training.
- Int8 symmetric / asymmetric, per-channel scales.
- FP16 / BF16 conversion via ORT transformers tools.

API:
```python
from onnxruntime.quantization import quantize_dynamic, QuantType
quantize_dynamic("model.onnx", "model.int8.onnx", weight_type=QuantType.QInt8)
```

### Pruning / sparsity
- 2:4 structured sparsity passes via ORT + TensorRT EP.
- Magnitude pruning done pre-export.

### Transformer-specific
- `onnxruntime.transformers.optimizer` — attention fusion, GELU approx, LayerNorm fusion.
- Mixed-precision conversion.
- KV-cache friendly export via `past_key_values`.

## 7. LLM with ONNX (2024-25)

- **onnxruntime-genai** — single lib for Llama / Phi / Qwen / Gemma / Mistral.
- Supports KV cache, continuous batching (lite), tokenization, sampling.
- Quantization down to **INT4 Group** (AWQ-compatible).
- Runs on Windows Copilot+ PCs via DirectML + NPU.
- Phi-3 / Phi-4 models ship with official ONNX builds.
- **MLC-LLM** and **llama.cpp** alternatives but ONNX integrates cleaner in Windows/enterprise.

## 8. Mobile / Edge

- **ONNX Runtime Mobile** — reduced-size build (< 10 MB). Hand-picked operators.
- Export → ORT format (`.ort`) for even smaller binary.
- Android: NNAPI EP.
- iOS: CoreML EP.
- NPUs: QNN (Snapdragon), OpenVINO (Intel VPU/NPU), Ryzen AI (AMD XDNA).

## 9. Web / Browser

- **onnxruntime-web** — WASM backend + optional **WebGPU** backend.
- Good for small models (< 50 MB after quant).
- Used in Transformers.js, ONNX-Web Stable Diffusion, MediaPipe Web.

## 10. Common pitfalls

- Dynamic shapes not handled → export at multiple shape configs or use `dynamic_axes`.
- Custom operators missing → register with ORT custom op API or swap to standard ops.
- Old opset incompatible with runtime — upgrade with `onnx.version_converter`.
- Large models > 2 GB need external weights (protobuf limit).
- Exporter bug paths — `torch.onnx.dynamo_export` + `onnxscript` recommended for modern PyTorch.
- Numerical mismatch vs framework — check with tolerance; precision conversion is the usual culprit.
- TensorRT EP has long JIT warmup; cache engines.

## 11. Deployment patterns

- **Triton Inference Server** with ONNX backend — production default for many shops.
- **ORT Server** minimal gRPC/HTTP.
- Fastapi + onnxruntime Python — simplest.
- Mobile: bundle `.ort` in app; CoreML / NNAPI EP selected based on device.
- Edge: Jetson + TensorRT EP or CPU + XNNPACK.
- Browser: onnxruntime-web + WebGPU.

## 12. Opset / compatibility

- Opset ≥ 15 for transformer models.
- Opset ≥ 21 (2024) for modern ops (GroupNormalization, FlashAttention-ish).
- Check runtime support before choosing opset.

## 13. Relation to this repo

- Fits under `HPC/Inference_Frameworks/` + `Ops/MLOps/` + `_REFERENCE/Model_Compression.md`.
- Primary path for **cross-platform deploy** when TensorRT / CoreML / TFLite alone isn't enough.
- Referenced by `Mobile/OnDeviceAI/ONNX_Runtime_Mobile` and `Frontend/JavaScriptCore` (via onnxruntime-web).
- Bridges PyTorch / TF / sklearn → any target hardware.

## 14. Quick starter

```python
import torch, onnxruntime as ort
import numpy as np

# export
model = torch.jit.load("model.pt").eval()
dummy = torch.randn(1, 3, 224, 224)
torch.onnx.export(
    model, dummy, "model.onnx", opset_version=17,
    dynamic_axes={"input": {0: "batch"}, "output": {0: "batch"}},
    input_names=["input"], output_names=["output"],
)

# simplify
import onnx, onnxsim
simplified, ok = onnxsim.simplify(onnx.load("model.onnx"))
onnx.save(simplified, "model.simp.onnx")

# quantize
from onnxruntime.quantization import quantize_dynamic, QuantType
quantize_dynamic("model.simp.onnx", "model.int8.onnx", weight_type=QuantType.QInt8)

# run
sess = ort.InferenceSession(
    "model.int8.onnx",
    providers=["TensorrtExecutionProvider", "CUDAExecutionProvider", "CPUExecutionProvider"],
)
print(sess.get_providers())   # whichever actually loaded
out = sess.run(None, {"input": np.random.randn(1,3,224,224).astype(np.float32)})
```

## Refs
- onnx.ai (spec + model zoo).
- onnxruntime.ai (ORT docs + EPs).
- github.com/microsoft/onnxruntime-genai.
- github.com/onnx/onnx + github.com/onnx/onnxmltools.
- Netron.app.
- Optimum ONNX exporter docs (Hugging Face).
