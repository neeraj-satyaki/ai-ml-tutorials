# High-Performance Computing + Distributed Training

Scale DL/scientific workloads across GPUs, nodes, clusters.

## Parallelism strategies (`Parallelism/`)
- **Data Parallel (DP / DDP)** — replicate model, split batch.
- **FSDP / ZeRO** (1/2/3) — shard optimizer state → grads → params.
- **Tensor Parallel** (Megatron) — shard within a matmul.
- **Pipeline Parallel** (GPipe, PipeDream, Interleaved 1F1B).
- **Sequence Parallel** — shard along sequence dim (long context).
- **Expert Parallel (MoE)** — route tokens to experts on different GPUs.
- **Context / Ring Attention** — shard KV across devices for 1M+ context.
- **3D Parallel** — combine DP + TP + PP.

## Communication (`Communication/`)
- **NCCL**, NVSHMEM (NVIDIA).
- **MPI** (OpenMPI, Intel MPI). UCX unified transport.
- **RDMA** over InfiniBand + RoCE, **GPUDirect RDMA**, **GPUDirect Storage**.
- Collectives: all-reduce (ring + 2D + tree), all-gather, reduce-scatter, all-to-all.

## Accelerators (`Accelerators/`)
- **NVIDIA CUDA** — streams, graphs, CUTLASS, cuDNN/cuBLAS, Triton-lang.
- **AMD ROCm / HIP** — MI300X in production 2024+.
- **Intel oneAPI / SYCL**.
- **Google TPU** — JAX + XLA; v5e, v5p, Trillium (v6).
- **Apple MLX**.
- **Cerebras**, **Groq LPU**, **Graphcore IPU**, **AWS Trainium/Inferentia**, **Tenstorrent**.

## Training frameworks (`Training_Frameworks/`)
- **DeepSpeed**, **FSDP (PyTorch)**, **Megatron-LM**, **Colossal-AI**, **Mosaic Composer**, **NeMo + NeMo-Megatron**, **TorchTitan**, **MaxText (JAX)**, **Nanotron (HF)**, **Axolotl**, **Unsloth** (2x LoRA), **Llama-Factory**.

## Inference frameworks (`Inference_Frameworks/`)
- **vLLM** (PagedAttention, continuous batching), **SGLang**, **TGI**, **TensorRT-LLM**, **LMDeploy**, **DeepSpeed-Inference**, **FasterTransformer** (legacy), **Triton Inference Server**, **Ollama / llama.cpp / MLX-lm**.

## Clusters + scheduling (`Clusters_Scheduling/`)
- **Slurm** (academic + many industry), **Kubeflow TrainingOperator**, **Ray**, **Volcano**, NeMo Launcher, **Kueue**, **JobSet API**, elasticity + instance flex, fault tolerance (checkpoint/restart, elastic training).

## Profiling (`Profiling/`)
- Nsight Systems, Nsight Compute, NVIDIA DCGM, PyTorch Profiler, `torch.compile` Inductor trace, NCCL debug, MPI trace.
- Flame graphs for CPU-side pipeline bottlenecks.

## Useful rules
- Start with **DDP + mixed precision**; add sharding only when param × 4 bytes > GPU memory.
- FSDP beats ZeRO-3 for PyTorch-native code; DeepSpeed still best for MoE.
- Tensor parallel degree = 2, 4, 8. Pipeline + tensor together = 3D parallel (GPT-3 / Llama 70B style).
- Always profile — comm usually eats > 30% at scale.

## Books + refs
- *Programming Massively Parallel Processors* — Kirk & Hwu.
- *High Performance Python* — Gorelick & Ozsvald.
- *Distributed Machine Learning Patterns* — Tang.
- NVIDIA / DeepSpeed / MosaicML tech blogs.
- PyTorch FSDP + TorchTitan docs.
