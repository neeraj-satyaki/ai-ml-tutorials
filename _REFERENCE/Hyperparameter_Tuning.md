# Hyperparameter Tuning

Model has **parameters** (learned) + **hyperparameters** (set before training). HP choice often matters more than algorithm choice. This doc covers search spaces, algorithms, tooling, and domain-specific defaults.

## 1. What counts as a hyperparameter

| Class | Examples |
|-------|----------|
| **Optimization** | lr, momentum, β1/β2 (Adam), weight decay, grad clip, batch size |
| **Architecture** | #layers, width, heads, kernel size, depth, dropout rate, activation |
| **Regularization** | L1/L2, dropout, label smoothing, mixup α, cutmix prob |
| **Schedule** | warmup steps, decay type (cosine/linear/poly), total steps |
| **Data** | aug strength, oversample ratio, noise level, sequence length |
| **Loss** | margin, temperature, focal γ, class weights |
| **Ensembling** | #trees, depth, learning rate (GBM), bagging fraction |
| **Task-specific** | NMS IoU threshold, top-k, SAM mask threshold, RAG top-k, LLM temp |

## 2. Search algorithms

### Grid search
All combinations on a grid. Works for ≤ 3 HPs with cheap eval. Scales terribly.

### Random search
Sample HP combos uniformly. **Beats grid** when only a few HPs matter (Bergstra & Bengio 2012). Default starting point.

### Bayesian Optimization (BO)
Fit surrogate model (GP / TPE / RF) on observed (HP, metric), pick next HP via acquisition function (EI, UCB, PI).
- **Gaussian Process** — small dims, continuous.
- **TPE** (Tree-structured Parzen Estimator) — mixed/conditional spaces. Used in Hyperopt, Optuna.
- **SMAC** — RF-based, handles categoricals.

### Evolutionary / Genetic
Mutation + crossover over HP populations. CMA-ES, NSGA-II. Good for non-differentiable, multi-objective.

### Hyperband / BOHB / ASHA
Early stopping + multi-fidelity. Run many short trials, kill weak ones, promote strong ones.
- **Hyperband** — random + successive halving.
- **BOHB** — Hyperband + TPE.
- **ASHA** — Async Successive Halving; best for GPU clusters.
- **PBT** (Population Based Training) — evolve HPs *during* training; exploit+explore on warm weights.

### Gradient-based HP
- **HyperGradient** — grad of metric w.r.t. HPs via implicit diff.
- **MAML-style** — rare in production.

### Bandit-based
Explore/exploit HP combos as arms. UCB, Thompson. Used in prod A/B model selection.

## 3. Search space design

- **Log-uniform** for lr, weight_decay, dropout — never linear.
- **Uniform** for layer width if in a small range.
- **Categorical** for optimizer choice, activation, scheduler type.
- **Conditional** — "use dropout only if `has_dropout=True`". Optuna / Hyperopt handle this.
- **Ordinal** — tree depth, # layers.

### Starting ranges (sane defaults)

| HP | Typical range |
|----|---------------|
| lr (Adam/W) | 1e-5 to 1e-3 (log) |
| lr (SGD) | 1e-3 to 1e-1 (log) |
| weight_decay | 0 to 1e-2 (log) |
| dropout | 0 to 0.5 (linear) |
| batch_size | 16, 32, 64, 128, 256, ... |
| warmup_steps | 0 to 10% of total |
| label_smoothing | 0 to 0.1 |
| gradient_clip | 0.5 to 5.0 |
| tree depth (GBM) | 3 to 10 |
| n_estimators | 100 to 2000 |
| #heads (transformer) | power of 2 matching d_model |

## 4. Budget + protocol

- **Fixed budget**: N trials total. Allocate 20% to warm-up random, 80% to BO/Hyperband.
- **Fidelity**: train on small subset / few epochs first; promote best.
- **Nested CV** if data is small (otherwise leak).
- **Seed multiple runs** at final HP — HP variance ≠ seed variance.
- **Log everything** — HPs, metrics, wall time, GPU hours, artifact paths.

## 5. Tooling

| Tool | Strength |
|------|----------|
| **Optuna** | TPE/CMA-ES/NSGA-II, pruners, easy Python, great for Python ML |
| **Ray Tune** | distributed, ASHA, PBT, framework-agnostic, best for clusters |
| **Hyperopt** | classic TPE; still usable |
| **Ax / BoTorch** | Meta's BO; Gaussian processes, multi-objective |
| **Weights & Biases Sweeps** | simple, integrated tracking |
| **SMAC3** | configuration optimization; academic / AutoML heritage |
| **Keras Tuner** | Keras-integrated |
| **Scikit-Optimize** | sklearn-style BO |
| **FLAML** | efficient BO + blendsearch, good for AutoML |
| **Optuna Dashboard / W&B / MLflow** | visualize results |

## 6. Domain-specific guidance

### Tabular (XGBoost / LightGBM / CatBoost)
Most impactful: `learning_rate`, `n_estimators`, `max_depth`, `min_child_weight / min_samples_leaf`, `subsample`, `colsample_bytree`, `reg_alpha`, `reg_lambda`.
- Start with LR=0.05, depth=6, 1000 rounds + early stopping.
- Tune depth & min_child_weight first, then colsample/subsample, then regularization, then lower LR with more rounds.

### Classical ML
- SVM RBF: `C` and `gamma` on log grid.
- kNN: `k`, distance metric, weight scheme.
- Logistic Reg: `C` (inverse regularization), solver.
- Random Forest: `n_estimators`, `max_depth`, `max_features`.

### Deep Learning (vision / speech / general)
- **Learning rate finder** (Smith 2015) — sweep lr over log range, plot loss; pick 1 decade below minimum.
- **Batch size**: largest that fits, with linear LR scaling (SGD) or sqrt (Adam). Warmup required.
- **Optimizer**: AdamW default. SGD + momentum for vision classification. Lion / Sophia for LLMs (sometimes better).
- **Schedule**: cosine with warmup = hard-to-beat default.
- **Regularization**: label smoothing 0.1, dropout 0.1, weight decay 0.01-0.1 for transformers.
- **Mixed precision**: always BF16 on Ampere+.

### CV detection / segmentation
Tune: NMS IoU threshold, confidence threshold, anchor sizes (if anchor-based), input resolution, aug strength (RandAug magnitude, mosaic prob).

### LLM fine-tuning (SFT / DPO / LoRA)
- LoRA rank (r): 8 → 32 → 64. Higher for knowledge, lower for style.
- LoRA alpha: usually 2×r or = r.
- LoRA dropout: 0 to 0.1.
- LR: 1e-5 to 2e-4 (rank-dependent).
- Warmup: 3-10% of total steps.
- Epochs: 1-3 typical; more = overfit.
- DPO β: 0.01-0.5; lower = closer to ref policy.
- Batch size: 32-128 effective; use grad accumulation.

### RAG
Not gradient HPs but still tunable:
- Chunk size (256-1024 tokens), overlap (10-20%).
- Top-k retrieved (3-10).
- Rerank cutoff, hybrid BM25+dense weight.
- Embedding model choice.
- Prompt template variants.

## 7. Multi-objective tuning

Accuracy alone ≠ deploy-ready.
- Pareto front over (acc, latency, memory, cost).
- Tools: Optuna `NSGAIISampler`, Ax multi-objective, Ray Tune multi-objective.
- Always add latency + memory constraints as a metric.

## 8. AutoML

End-to-end pipelines that include HP tuning.
- **AutoGluon** — tabular SOTA at "push-button".
- **H2O AutoML**, **TPOT**, **Auto-sklearn**, **FLAML**.
- Cloud: SageMaker Autopilot, Vertex AI AutoML.
- Use for baselines; hand-tuned + domain features still win on hard problems.

## 9. Pitfalls

1. **Tuning on test set** → looks great, fails in prod.
2. **One seed** → HP quality conflated with luck.
3. **Leaky CV** (time-series with random splits, groups broken).
4. **Tuning too many HPs with small budget** → noise wins.
5. **Ignoring interaction** — HPs interact; one-at-a-time fails.
6. **Not logging early stopping** — reproducibility dies.
7. **Different fidelity at train vs final** — best HP at 10 epochs ≠ best at 100.

## 10. Default recipe (when in doubt)

```
1. Define 1 metric + its constraints.
2. Random-search 30 trials over log-scaled HPs.
3. Pick best region → Optuna TPE for 100 more trials with pruning.
4. Take top-3 HPs → 5 seeds each → choose by mean-sigma.
5. Retrain final model on full data with chosen HPs.
6. Lock + version.
```

## Books / refs
- *Practical Bayesian Optimization of Machine Learning Algorithms* — Snoek et al.
- *Random Search for HP Optimization* — Bergstra & Bengio.
- *Hyperband* — Li et al. 2018.
- *Population Based Training* — Jaderberg et al.
- Optuna docs + Ray Tune docs.
- Leslie Smith's LR finder papers.
