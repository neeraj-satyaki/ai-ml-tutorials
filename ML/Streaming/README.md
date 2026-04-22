# Streaming / Online Learning

Data arrives in unbounded streams. Models must: (a) train one-sample-at-a-time OR in mini-batches, (b) bound memory, (c) adapt to concept drift.

Two worlds: **supervised** (labels available) and **unsupervised** (no labels).

---

## Why streaming differs from batch

| Axis | Batch | Streaming |
|------|-------|-----------|
| Data | bounded, static | unbounded, evolving |
| Memory | O(n) fine | O(1) or sliding window |
| Passes | many | one (or few) |
| Distribution | assumed stationary | drifts, shifts, seasonality |
| Evaluation | holdout/CV | prequential (test-then-train) |
| Failure mode | overfit | catastrophic forgetting + stale model |

---

## Supervised Streaming (`Supervised/`)

### Trees (Hoeffding family)
- **Hoeffding Tree / VFDT** (Domingos & Hulten, 2000) — split when Hoeffding bound guarantees chosen split beats runner-up with prob 1-δ. Foundation of streaming decision trees.
- **Hoeffding Adaptive Tree (HAT)** — adds ADWIN at each node to detect local drift and regrow subtrees.
- **Extremely Fast Decision Tree (EFDT/HATT)** — more aggressive splitting.

### Ensembles
- **Adaptive Random Forest (ARF)** — RF with drift detectors per tree; replace drifted trees.
- **SEA Ensemble** — accuracy-weighted classifiers over sliding chunks.
- **Leveraging Bagging** — Poisson(λ=6) weighting for diversity.
- **Oza Bagging / Online Boosting**.
- **Dynamic Weighted Majority (DWM)** — add/remove experts based on error.
- **OzaBaggingASHT** — adaptive-size Hoeffding Trees.

### Linear / kernel
- **SGD Classifier / Regressor** (online) — sklearn `partial_fit`.
- **Passive-Aggressive (PA-I, PA-II)** — hinge-loss online with aggressive updates on mistakes.
- **Online Logistic Regression** — SGD + log loss.

### Neighbors / probabilistic
- **k-NN Sliding Window** — keep last W samples.
- **SAMkNN** — Self-Adjusting Memory: short + long-term memories.
- **Incremental Naive Bayes** — update class + feature stats per sample.

### Gradient boosting (streaming)
- **Online Gradient Boosting** (Beygelzimer 2015).
- **XGBoost / LightGBM**: not native, but support incremental training via `init_model` + small batches.

---

## Unsupervised Streaming (`Unsupervised/`)

### Clustering
- **CluStream** (Aggarwal 2003) — online micro-clusters + offline macro-cluster (k-means) on snapshots.
- **DenStream** — density-based; potential / outlier / core micro-clusters. Works like streaming DBSCAN.
- **StreamKM++** — coreset construction for k-means on streams.
- **BIRCH (online)** — CF-tree; incremental hierarchical clustering.
- **Streaming Mini-batch k-means** — sklearn `MiniBatchKMeans.partial_fit`.
- **Incremental DBSCAN** — update clusters on insert/delete.

### Dimensionality reduction
- **Incremental PCA (IPCA)** — sklearn `IncrementalPCA.partial_fit`.
- **Incremental / truncated SVD** — Brand 2002 algorithm.
- **Oja's rule** — online principal component via stochastic gradient.
- **Online Matrix Factorization** — for recommender streams.

### Anomaly detection
- **Half-Space Trees (HS-Trees)** — Tan 2011, streaming isolation forest alternative.
- **RRCF (Robust Random Cut Forest)** — Guha 2016, AWS KinesisAnalytics uses it.
- **Online Isolation Forest** — incremental tree updates.
- **LODA (online)** — random projections + histograms.
- **Streaming Autoencoder** — reconstruction error per sample; EMA-threshold.

---

## Concept Drift Detection (`DriftDetection/`)

Signal a drift event so downstream can retrain / reset / swap model.

| Detector | Mechanism | When to use |
|----------|-----------|-------------|
| **ADWIN** | adaptive sliding window; cuts when two sub-windows differ | general purpose, gold standard |
| **DDM** (Drift Detection Method) | tracks error rate + stddev | supervised only |
| **EDDM** | distance between classification errors | gradual drift |
| **Page-Hinkley** | CUSUM-like on mean | abrupt drift on metrics |
| **KSWIN** | Kolmogorov-Smirnov on windows | distributional |
| **HDDM-A / HDDM-W** | Hoeffding bounds on error | theoretically tight |
| **STEPD** | recent vs overall accuracy | balanced |
| **ECDD** | EWMA control charts | quality-control style |
| **ChangeFinder** | AR model residual | time series |

### Rules for picking
- Abrupt shift → Page-Hinkley / ADWIN.
- Gradual → EDDM / KSWIN.
- Seasonal → windowed + retrain-on-cycle, no detector needed.
- Drift type unknown → ADWIN by default.

---

## Frameworks & Platforms (`Frameworks_Platforms/`)

### Python
- **River** (merger of Creme + scikit-multiflow) — THE online-ML library in 2024+. `partial_fit` everywhere, drift detectors built-in.
- **scikit-multiflow** — older; superseded by River.
- **sklearn** — `partial_fit` on `SGDClassifier`, `PassiveAggressive`, `MiniBatchKMeans`, `IncrementalPCA`, `GaussianNB`.

### JVM
- **MOA** (Massive Online Analysis) — Java reference platform; ARF, Hoeffding trees, drift detectors all here first.
- **SAMOA** — distributed MOA on Storm/Flink.

### Big-data / streaming engines
- **Flink ML** — native online training.
- **Spark Structured Streaming** — micro-batch; streaming k-means, streaming LR.
- **Kafka Streams** + custom UDFs.
- **Bytewax** (Python-native, Rust core) — stream topologies.
- **Apache Beam** — portable across runners.

### Online inference stores
- **Redis / RedisAI** — feature store + low-latency model serving.
- **Vowpal Wabbit** — insanely fast online learner (contextual bandits, LR, FTRL).

---

## Evaluation (`EvaluationProtocols/`)

Batch metrics break on streams. Use:

- **Prequential (interleaved test-then-train)**: for each x_t — predict, score, then train. Like real life.
- **Holdout on sliding window** — reserve last k samples.
- **Windowed accuracy** (fading factor α) — EMA of correct predictions.
- **Kappa-Temporal** — corrects for majority-class baseline that changes.
- **Streaming AUC / ROC** — online variants (Brzezinski & Stefanowski).
- **Cumulative MAE / RMSE** for regression.
- **ARI / NMI over windows** for streaming clustering.

---

## Typical stacks

### Supervised fraud detection
`Kafka → Flink → HoeffdingAdaptiveTree (River) → ADWIN drift → RedisAI for serving → Grafana drift alerts`

### Unsupervised anomaly on metrics
`Prometheus scrape → RRCF online → threshold → PagerDuty`

### Online recommendation
`Click stream → Vowpal Wabbit contextual bandit → Redis feature store`

### Streaming sensor clustering
`MQTT → Bytewax → DenStream → dashboard + alert on outliers`

---

## Pitfalls

1. **Shuffled != streaming.** True streams have time-order + drift. Shuffled batch = easy mode.
2. **Label latency.** Real systems label hours/days later. Build for delayed feedback.
3. **Catastrophic forgetting.** Too-fast adaptation overwrites useful structure. Use ensemble with slow + fast learners.
4. **Evaluation leak.** Test-then-train discipline; don't peek.
5. **Memory unbounded.** Every data structure needs a bounded mode (reservoir, exp decay, windowed).
6. **No A/B.** Can't A/B a streaming model trivially; use shadow deploys + delayed reward metrics.

---

## Books / papers
- *Machine Learning for Data Streams* — Bifet, Gavaldà, Holmes, Pfahringer (the book).
- *Mining Data Streams* — chapter in Rajaraman & Ullman's MMDS.
- *Learning under Concept Drift: A Review* — Lu et al. (2018).
- River docs: `riverml.xyz`.
