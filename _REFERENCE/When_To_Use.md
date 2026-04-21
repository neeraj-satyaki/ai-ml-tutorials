# When to Use Which Algorithm — Scenario Rules

For each algorithm: **signals to reach for it**, **signals to avoid**, **typical scenario**.

---

## ML — Supervised

### Linear Regression
- **Use when:** continuous target; relationship ~linear; interpretability matters.
- **Avoid when:** nonlinear, heteroskedastic, heavy outliers (use Huber/quantile reg).
- **Scenarios:** price prediction with few features, dose-response, econometrics baseline.

### Logistic Regression
- **Use when:** binary/multiclass, linear decision boundary OK, need calibrated probabilities.
- **Avoid:** nonlinear boundary, very high-dim sparse text (unless L1-regularized).
- **Scenarios:** spam/not-spam, churn, click-through baseline, medical risk scores.

### Decision Tree
- **Use when:** mixed data types, need human-readable rules, no scaling wanted.
- **Avoid:** noisy data (overfits), very smooth continuous relationships.
- **Scenarios:** credit decisioning explanation, simple rule extraction, prototype.

### Random Forest
- **Use when:** tabular data, medium feature count, want strong OOB baseline.
- **Avoid:** huge sparse text, extreme low-latency needs, billions of rows.
- **Scenarios:** default tabular classifier/regressor; feature importance quick scan.

### Gradient Boosting / XGBoost / LightGBM / CatBoost
- **Use when:** tabular SOTA needed; heterogeneous features; missing values; interactions matter.
- **Avoid:** unstructured (images, text) — use NN; very few samples.
- **Scenarios:** Kaggle tabular, fraud detection, CTR, pricing — still beats NNs on small tabular.

### SVM
- **Use when:** small/medium data, clear margin, high-dim (text).
- **Avoid:** >50k samples (slow), need probabilities natively.
- **Scenarios:** text classification (TF-IDF + linear SVM), bio-informatics.

### KNN
- **Use when:** low-dim, smooth decision boundary, interpretable baselines, local recommendations.
- **Avoid:** high-dim (curse of dimensionality), huge datasets (slow query).
- **Scenarios:** recommendation seed, anomaly via distance, quick baseline.

### Naive Bayes
- **Use when:** text (bag-of-words), many features, little data, need fast baseline.
- **Avoid:** strong feature dependencies, continuous non-Gaussian.
- **Scenarios:** spam filtering, sentiment baseline, document classification.

---

## ML — Unsupervised

### KMeans
- **Use when:** spherical clusters, known/target k, large data.
- **Avoid:** non-convex clusters, varying density, categorical data.
- **Scenarios:** customer segmentation, vector quantization, initialization for other algos.

### DBSCAN / HDBSCAN
- **Use when:** arbitrary-shape clusters, noise present, unknown k.
- **Avoid:** very high-dim, hugely varying density (try HDBSCAN).
- **Scenarios:** spatial clustering (GIS), anomaly grouping, density-aware segmentation.

### Hierarchical Clustering
- **Use when:** small data, need dendrogram for cut-off decision, taxonomy discovery.
- **Avoid:** large data (O(n²)/O(n³)).
- **Scenarios:** gene expression, document hierarchies, small behavioural segments.

### Gaussian Mixture
- **Use when:** soft cluster assignments needed, clusters roughly elliptical.
- **Avoid:** very non-Gaussian shapes.
- **Scenarios:** background modelling, speaker clustering, density estimation.

### PCA
- **Use when:** need linear dim-reduction, visualization, noise reduction, preprocessing.
- **Avoid:** nonlinear structure (use UMAP/tSNE), sparse data (use TruncatedSVD).

### t-SNE / UMAP
- **Use when:** 2D visualization of high-dim data.
- **Avoid:** interpret global distances (local structure only); using result as downstream features (usually not stable).

### Isolation Forest / LOF / One-Class SVM
- **Use when:** anomaly / outlier detection, unlabeled or imbalanced.
- **Scenarios:** fraud, defect detection, equipment failure.

---

## ML — Semi/Self/Active/Few-shot

### Label Propagation / Self-Training
- **Use when:** lots of unlabeled + few labeled; assume smoothness (similar→same label).
- **Avoid:** noisy graph, label imbalance.

### Self-Supervised (SimCLR, MAE, DINO, CLIP)
- **Use when:** huge unlabeled data, want foundation representations for downstream tasks.

### Contrastive (CLIP, SimCLR)
- **Use when:** need joint embeddings, zero-shot classification, retrieval.

### Active Learning
- **Use when:** labeling is expensive; have oracle; can retrain cheaply.

### Few-shot / Zero-shot (prompting, ProtoNets)
- **Use when:** only 0-10 examples per class; rapid domain adaptation.

---

## ML — Advanced

### Incremental Learning
- **Use when:** data arrives in stream, can't store full history.

### Continual Learning (EWC, Replay, etc.)
- **Use when:** sequence of tasks; must retain old knowledge (avoid catastrophic forgetting).

### Concept Drift Adaptation (ADWIN, Page-Hinkley, windowed retraining)
- **Use when:** distribution changes over time (fraud patterns, user behavior post-event).

### Federated Learning (FedAvg, FedProx)
- **Use when:** data can't leave devices (privacy / regulation); many edge clients.

### Meta-Learning (MAML, Reptile)
- **Use when:** many related small tasks; need rapid adaptation.

### Domain Adaptation (DANN, CORAL)
- **Use when:** labeled source, unlabeled target with different distribution.

### Curriculum Learning
- **Use when:** unstable training on full data; natural easy→hard ordering exists.

---

## DL — Architectures

### MLP
- **Use when:** tabular after feature engineering, low-dim; building block.

### CNN (ResNet / ConvNeXt / EfficientNet)
- **Use when:** images, spectrograms, 1D signals, local pattern detection.
- **Avoid:** variable-length sequences without spatial structure.

### RNN (vanilla)
- **Use when:** short sequences, didactic.
- **Avoid:** long-range deps (vanishing gradient) — use LSTM/Transformer.

### LSTM / GRU
- **Use when:** medium-length sequences, low resources, streaming.
- **Avoid:** very long sequences, parallel training critical → Transformer.

### Transformer (BERT / GPT / T5)
- **Use when:** sequences (text, code, time series, audio, video tokens).
- **Avoid:** truly tiny data (overfits) unless fine-tuning foundation model.

### Autoencoder
- **Use when:** unsupervised feature learning, denoising, compression, anomaly detection.

### VAE
- **Use when:** generative model with latent structure, interpolation, semi-supervised.

### GAN
- **Use when:** sharp image generation, domain translation.
- **Avoid:** need diverse sampling (mode collapse), need likelihood.

### Diffusion
- **Use when:** high-fidelity generation (image/video/audio), conditional generation.
- **Scenarios:** text-to-image, super-resolution, inpainting, video gen.

### Graph NN (GCN, GAT, GraphSAGE)
- **Use when:** data is a graph (social nets, molecules, recommendations with relations).

---

## RL

### Q-Learning / SARSA (tabular)
- **Use when:** small discrete state-action spaces; didactic.

### DQN
- **Use when:** discrete actions, pixel or feature observations, have sim.
- **Scenarios:** Atari, grid games, routing.

### REINFORCE
- **Use when:** didactic; episodic; full return available.

### PPO
- **Use when:** general default for continuous or discrete; robust; default policy method.

### TRPO
- **Use when:** need provable KL bounds; PPO usually suffices in practice.

### A2C / A3C
- **Use when:** parallel CPU cores, moderate problems; PPO often preferred.

### DDPG / TD3 / SAC
- **Use when:** continuous actions (robotics, control).
- **Prefer:** SAC for sample efficiency + stability; TD3 for determinism.

### Model-based RL (DynaQ, Dreamer, MCTS, MuZero)
- **Use when:** samples expensive (robotics, real-world), planning beneficial.

### MCTS
- **Use when:** discrete, perfect info, large branching (Go, chess, puzzle).

### Multi-Agent (MADDPG, QMIX)
- **Use when:** multiple interacting agents, cooperation/competition.

### Offline RL (CQL, IQL)
- **Use when:** fixed dataset only, no sim, can't explore.

### RLHF / DPO / GRPO
- **Use when:** aligning LLMs with preferences / reasoning.

---

## AI Frontier Topics

### Mamba / SSMs
- **Use when:** very long sequences, linear-time needed, hardware constraints.

### MoE
- **Use when:** need scale at inference-time FLOPs budget; have many experts of data.

### FlashAttention
- **Use when:** transformer training/inference — almost always. Drop-in.

### RAG
- **Use when:** factual QA, domain knowledge outside model, frequently-updated data.
- **Avoid:** reasoning-only tasks, creative generation without sources.

### RLHF vs DPO vs GRPO
- **RLHF** — traditional, needs reward model + PPO.
- **DPO** — simpler, stable, no reward model; default for pref data.
- **GRPO** — reasoning/math, no critic needed; DeepSeek-R1 style.

### LoRA / QLoRA
- **Use when:** fine-tune big models on limited GPU; adapter families; multi-task.

### Flow Matching
- **Use when:** new generative project; simpler than diffusion; strong samples.

### JEPA
- **Use when:** self-supervised representation learning without pixel reconstruction.

### Test-Time Compute (o1-style)
- **Use when:** hard reasoning (math, code, science); long CoT rollouts acceptable latency.

### Speculative Decoding
- **Use when:** lowering inference latency for LLMs.

---

## Agentic

### ReAct
- **Use when:** agent needs interleaved reason + tool use.

### Reflexion
- **Use when:** multi-attempt tasks with feedback; let agent learn from its failures.

### Tree-of-Thoughts / Graph-of-Thoughts
- **Use when:** hard search/planning where single CoT fails; willing to spend more compute.

### Tool Use / Function Calling
- **Use when:** agent needs web, DB, calculator, APIs.

### MCP
- **Use when:** standardizing tool/resource integrations across apps + models.

### Multi-Agent (AutoGen, CrewAI, LangGraph)
- **Use when:** complex workflows benefit from specialists; enough tolerance for complexity.

### Computer-Use agents
- **Use when:** GUI automation where API isn't available.

### Code agents (Claude Code, Cursor, Devin)
- **Use when:** software engineering tasks — planning, edits, test runs.

---

## AGI-adjacent

### Scaling / Foundation models
- **Use when:** have budget + data; want broad capabilities.

### Mechanistic interpretability
- **Use when:** debugging model internals; safety research.

### RLHF / Constitutional AI / Red teaming
- **Use when:** productionizing LLMs — alignment + safety.

---

## Quick "what to try first" tree
```
Problem type?
├─ Tabular supervised          → GBM (XGBoost/LightGBM/CatBoost)
├─ Tabular unsupervised        → KMeans / DBSCAN, PCA
├─ Text classification (small) → Linear SVM / LogReg on TF-IDF
├─ Text classification (large) → Fine-tune BERT / LLM
├─ Text generation / QA        → RAG + LLM, or fine-tuned LLM
├─ Image classification        → ViT / ConvNeXt (or DINOv2 features + linear)
├─ Object detection            → YOLOv8-v10 or RT-DETR
├─ Segmentation                → SAM (prompt) / nnU-Net (medical) / Mask2Former
├─ Pose                        → RTMPose / ViTPose
├─ Depth                       → Depth Anything v2
├─ Video understanding         → VideoMAE v2 / V-JEPA
├─ Time series forecast        → GBM + lag feats; Prophet/NBEATS/PatchTST if needed
├─ Anomaly detection           → Isolation Forest / autoencoder / PatchCore (vision)
├─ Control / robotics          → PPO, SAC, or World Models
├─ Game AI (discrete)          → MCTS / MuZero / AlphaZero
├─ LLM alignment               → DPO (pref), GRPO (reasoning), RLHF (classical)
└─ Agentic workflow            → ReAct + tool use; add memory; multi-agent only if needed
```
