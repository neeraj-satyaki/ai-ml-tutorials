# Model Compression

Make large models small / fast / cheap without losing (too much) quality.

## 1. Why

- Inference cost = dominant AI spend.
- Latency budgets (real-time, mobile, edge).
- Memory limits (phone, Jetson, RAM/VRAM ceilings).
- Multi-tenant serving → more QPS per GPU.

## 2. Levers (compose them)

| Lever | What | Typical gain |
|-------|------|-------------|
| **Quantization** | lower-precision weights/activations | 2-8x memory + speed |
| **Pruning** | drop weights/heads/channels | 1.5-4x with care |
| **Distillation** | teach a small student | 2-10x with small quality drop |
| **Architecture search / compact design** | smaller model from start | 3-100x for task-fit |
| **Weight sharing / factorization** | low-rank, tied | 1.5-3x |
| **Early exit / mixture-of-depths** | skip layers per token | 1.5-3x |
| **Speculative decoding** | draft + verify | 2-5x inference only |
| **KV-cache compression** | fewer tokens of state | big for long context |

## 3. Quantization

### Levels
- **FP16 / BF16** — half precision, nearly free, default for DL training.
- **FP8** (E4M3, E5M2) — H100/B100 native, 2x over FP16, good for training + inference.
- **INT8** — mainstream for serving; SmoothQuant, ZeroQuant.
- **INT4 / NF4** — aggressive; GPTQ, AWQ, **QLoRA** uses it for fine-tune.
- **INT3 / INT2 / 1.58-bit (BitNet)** — research / frontier 2024-25.
- **FP4 (microscaling, MX)** — Blackwell native.

### Methods
- **PTQ** (Post-Training) — calibration set → quantize. Cheap. GPTQ, AWQ, SmoothQuant.
- **QAT** (Quantization-Aware Training) — fake quant in training loop. Best quality.
- **Mixed precision** — sensitive layers stay high, rest low.
- **Weight-only** vs **weight+activation**. Weight-only easier; activations have outliers.
- **Group / channel / tensor scale** — trade speed for quality.

### Frameworks
- `bitsandbytes` (4/8-bit HF), **AutoGPTQ**, **AutoAWQ**, **llm-awq**, **optimum-quanto**, TensorRT-LLM INT8/FP8, **llama.cpp** GGUF (Q4_K_M is de-facto portable quant), MLX quantize.

## 4. Pruning

### Structured (hardware-friendly)
- Remove heads, channels, layers, experts. Runs faster on real hardware.
- **N:M sparsity** (e.g., 2:4 on Ampere+) — 2x speed on tensor cores.
- Head pruning in transformers (many heads redundant).

### Unstructured
- Individual weights set to 0. High compression rate but needs sparse kernels.
- **Magnitude pruning**, **SparseGPT**, **Wanda** (2023) — LLM-scale one-shot pruning.

### Pruning + retrain
Iterative: prune → fine-tune → prune again (Lottery Ticket, IMP).

## 5. Distillation

Train **student** to match **teacher** output.
- **Soft labels** (logits + temperature) — classic Hinton.
- **Feature distillation** — match intermediate activations.
- **Response / preference** distillation (for LLMs) — student imitates teacher on curated prompts.
- **Self-distillation** — same model, different layers.
- Modern LLM distillation: MiniLM, DistilBERT, DistilGPT, phi-family, Zephyr, Llama-3.3-70B-instruct → small students.
- **On-policy distillation** — student generates, teacher grades (RLHF-like).
- **Instruction distillation** — Alpaca-style from GPT-4 outputs.

## 6. Architecture-level

- **MoE** sparse — big params, few active. Mixtral, DeepSeek-V3.
- **Shared expert + routed experts** (DeepSeek).
- **Grouped-query attention (GQA)** — fewer KV heads than query. Llama-2/3 default.
- **Multi-query attention (MQA)** — one KV head.
- **Mamba / SSM** hybrid — linear-time, smaller KV state.
- **Small-LM families**: Phi-3 / Phi-4, Gemma 2/3, Llama 3.x 1B/3B, Qwen 2.5 0.5/1.5B.
- **TinyML** on MCU: TFLM, CMSIS-NN, µTVM.

## 7. Inference-only tricks

### Speculative decoding
Small draft proposes N tokens, big verifies. 2-5x on latency.
- **EAGLE / EAGLE-2 / EAGLE-3**, **Medusa**, **Lookahead**, draft+verify in vLLM/TensorRT-LLM natively.

### KV-cache optimization
- **PagedAttention** (vLLM) — page-based KV → higher concurrency.
- **KV quantization** (INT8/INT4 KV).
- **Sliding window attention** (Mistral).
- **StreamingLLM**, **SnapKV**, **H2O** — keep only important tokens.
- **Grouped KV** / shared KV across layers.

### Continuous batching
Dynamic batch — new requests joined mid-flight. Default in vLLM, TGI, SGLang.

### Prompt caching
Reuse shared prefix across requests. Huge for system prompts + RAG context.

### Early exit / mixture-of-depths
Per-token: skip layers if confident.
- **MoD** (Mixture-of-Depths, 2024).

## 8. Compression for specific modalities

- **Vision**: MobileViT, EfficientFormer, TinyViT. Distilled ResNets, MobileNets.
- **Audio**: Distil-Whisper, faster-whisper, Mimi codec (compress audio tokens).
- **Diffusion**: **LCM** (Latent Consistency Models), **SDXL-Turbo** (adversarial diffusion), TAESD decoder, step-distillation.

## 9. Workflow for an existing model

```
1. Measure baseline: quality + latency + cost.
2. Apply: BF16/FP16 (if not already).
3. Apply: INT8 PTQ → measure; if quality holds, ship.
4. Apply: INT4 AWQ/GPTQ → measure; expect 1-3% drop.
5. Apply: speculative decoding + KV cache → latency wins.
6. If need more: distillation from current model to smaller backbone.
7. QAT only if PTQ insufficient.
```

## 10. Quality loss budget

- Typical acceptable drops:
  - Benchmark suite: < 1% abs for classification; < 0.5 BLEU for translation.
  - LLM downstream task: < 2% on golden eval set.
- Always test on **your** eval set, not just MMLU.

## 11. Hardware interactions

- Tensor cores: prefer multiples of 8 in FP16, 16 in INT8, 32 in INT4.
- Sparsity: 2:4 on Ampere+; 4:8 on Hopper.
- MX formats on Blackwell.
- Mobile NPUs: INT8 symmetric usually; per-channel scales.

## 12. Pitfalls

- Quantizing without calibration → bad outputs.
- Mixing INT8 weights + FP32 activations → negates speedup on some hardware.
- Overfitting pruning to calibration set → test on held-out.
- Distillation with bad teacher data → student inherits flaws.
- Ignoring operator coverage → quantized model falls back to FP32 kernels.

## Refs
- *A Survey of Model Compression* — Cheng et al. (updated).
- *LLM.int8(), GPTQ, AWQ, QLoRA* papers.
- vLLM, TensorRT-LLM, SGLang, llama.cpp docs.
- Unsloth + Hugging Face PEFT docs.
- NVIDIA Hopper/Blackwell whitepapers.
