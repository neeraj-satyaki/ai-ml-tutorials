# Training Optimization

Everything you change between "model builds" and "model converges fast to a good minimum".

## 1. Optimizers

| Optimizer | When to use | Notes |
|-----------|-------------|-------|
| **SGD + momentum (0.9)** | vision classification, GANs | best generalization often; needs tuned LR + schedule |
| **AdamW** | almost everything else | default; decouples weight decay properly |
| **Adam** | legacy; prefer AdamW | weight decay is buggy |
| **Adafactor** | very large models, memory-limited | used in T5 / PaLM |
| **Lion** | LLM pretrain | 10-15% less memory than Adam; slightly better in some runs |
| **Sophia** | LLM pretrain | second-order; ~2x faster to same loss |
| **Shampoo / SOAP / Muon** | large-scale (2024) | second-order; SOTA in Llama-scale trials |
| **RMSProp** | legacy RNN | mostly replaced by Adam |
| **LAMB** | huge batch sizes | BERT's friend |
| **LARS** | ResNet with batch > 8k | layer-wise adaptive |
| **Nesterov** | better than plain momentum; cheap |

## 2. Learning rate schedules

- **Constant** — only for short debug runs.
- **Step decay** — drop by 10x at 1/3 and 2/3 (classic ResNet recipe).
- **Cosine decay** — smooth to near-zero; modern default.
- **Linear warmup + cosine / linear decay** — mandatory for transformers, large batches.
- **Polynomial (power=1 or 2)** — T5 style.
- **Inverse sqrt** — original Transformer paper.
- **OneCycleLR** (Smith) — warmup → max → long decay; fast training.
- **Cyclic LR / SGDR** (warm restarts) — periodic; good for escape plateaus.
- **Piecewise** — custom milestones.

### Warmup
- Essential for large batch, transformers, low precision.
- 1-10% of total steps typical; 10-500 steps for fine-tunes.
- Linear warmup from 0 → peak LR.

### LR finder
Smith's log-sweep: LR from 1e-7 → 10 over a few hundred steps; plot loss; pick LR one decade below divergence.

## 3. Batch size

- **Larger batch** = faster wall-clock (if hardware allows) + more stable grads.
- **Linear scaling rule (SGD)**: double batch → double LR (with warmup).
- **Sqrt scaling (Adam-family)**: double batch → × √2 LR.
- Gradient accumulation to simulate big batch on small GPU.
- **Gradient checkpointing** if memory-bound — trade compute for memory.

### Mega-batch caveats
- Generalization can drop past a critical batch size (Keskar 2017).
- LAMB / LARS let you push past that.
- DeepMind's "scaling laws for optimal batch size" = ~B* ∝ √loss-scale.

## 4. Regularization

- **Weight decay** (L2 in SGD, decoupled in AdamW) — 1e-4 vision, 0.01-0.1 transformers.
- **Dropout** — 0.1-0.3 dense layers; 0 in conv where BN is present.
- **DropPath / Stochastic Depth** — transformers + deep CNNs.
- **Label smoothing** (0.1) — always helps classification calibration.
- **Mixup** (α=0.2-0.4), **CutMix** (prob 0.5) — strong for vision.
- **RandAugment / AutoAugment / TrivialAugment** — image aug.
- **EMA (Exponential Moving Average) of weights** — stabilizer, used in diffusion, EfficientNet, GANs.

## 5. Normalization

- **BatchNorm** — CNN default; fails on small batches, RNNs.
- **LayerNorm** — transformers, RNNs.
- **RMSNorm** — drop-in LN, cheaper; Llama default.
- **GroupNorm** — small-batch CNNs (detection, segmentation).
- **InstanceNorm** — style transfer.
- **Weight Normalization / Spectral Norm** — GANs.
- **pre-LN vs post-LN** — pre-LN easier to train, slightly worse generalization.

## 6. Numerical stability

- **Mixed precision** — FP16/BF16 with FP32 master weights.
- **BF16** preferred over FP16 (wider exp, no loss scaling needed).
- **FP8** on H100/B100 via TransformerEngine.
- **Gradient clipping** — norm ≤ 1.0 (transformers), 5.0 (RNN). By global norm.
- **Loss scaling** (FP16 only) to avoid underflow.
- **LogSumExp trick** for stable softmax / CE.
- **NaN hunting** — `torch.autograd.set_detect_anomaly(True)` (debug only, slow).

## 7. Initialization

- **Xavier/Glorot** — tanh.
- **He (Kaiming)** — ReLU; default PyTorch.
- **Truncated normal (σ=0.02)** — transformers.
- **Orthogonal** — RNN hidden-to-hidden.
- **Scaled init for deep residual** — multiply residual branch by 1/√(2L).

## 8. Convergence diagnostics

- **Train vs val loss gap** widening → overfit → more reg / data / smaller model.
- **Both flat high** → underfit → bigger model / more epochs / better features.
- **Loss spike** → LR too high or bad batch. Lower LR or clip harder.
- **Plateau** → LR too low or bad init.
- **NaN** → explode — clip, lower LR, check data.
- **Accuracy plateau but loss still decreasing** → overconfident on wrong answers; label smoothing helps.

## 9. Reproducibility

- Fix seeds: `random`, `numpy`, `torch`, `torch.cuda`.
- `torch.backends.cudnn.deterministic = True` (costly, sometimes).
- Pin package versions (`pip freeze`, `lockfiles`).
- Fixed data ordering (shuffle seed).
- Log all HPs + code hash.
- **Full determinism is rarely achievable** on GPU; aim for seed-stability across runs.

## 10. Training-time optimizations

- **torch.compile** — 1.2-2x on eligible PyTorch code.
- **FlashAttention 2/3** — faster transformer attention, lower memory.
- **Fused optimizers** (APEX `FusedAdam`, `torch.optim.AdamW(fused=True)`).
- **Activation checkpointing** — save memory, recompute forward in backward.
- **CPU offloading** (ZeRO-offload, DeepSpeed) — for very large models.
- **Gradient accumulation** — effective batch without memory.
- **bf16 + tf32** matmuls.

## 11. Fine-tuning specifics

- Start with 10x smaller LR than pretrain.
- Warmup shorter (3% of steps).
- Fewer epochs (1-5).
- Freeze early layers for small data; unfreeze gradually.
- LoRA / QLoRA instead of full fine-tune when feasible.
- Layer-wise LR decay (lower layers get smaller LR).

## 12. Distributed tricks

- **All-reduce** overlap with compute — `bucket_cap_mb`, gradient compression.
- **Gradient accumulation** reduces comm frequency.
- **Torch DDP** gradient bucketing.
- **ZeRO-3 / FSDP** for > 10B models.
- **Pipeline parallel** when model won't fit on one GPU.
- **Tensor parallel** for very wide matmuls.
- **Context parallel** (ring attention) for very long sequences.

## 13. Checklist before long run

```
[ ] Overfit a single batch (loss → 0).
[ ] Compute / memory profile on one node first.
[ ] Dry-run 100 steps; check loss curve shape.
[ ] Log lr, loss, grad_norm, param_norm every step.
[ ] Save checkpoints + ensure resume works.
[ ] Eval set reserved, unseen in training.
[ ] Alert thresholds (NaN, divergence, lag).
[ ] Reproducibility (seed, versions, data hash) logged.
```

## Books / refs
- *Deep Learning* — Goodfellow, Bengio, Courville.
- *Bag of Tricks for Image Classification* — He et al.
- *Scaling Laws for Neural Language Models* — Kaplan.
- *Chinchilla* — Hoffmann et al.
- Andrej Karpathy's training tips gist.
- *Efficient Deep Learning* — Menghani survey.
