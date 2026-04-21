# Machine Learning — Algorithms & Paradigms

Each folder has runnable `example.py`. Click through to see toy implementation.

## Supervised (`Supervised/`)
Learn f: X → Y from labeled examples.
- **LinearRegression** — least squares.
- **LogisticRegression** — sigmoid + CE loss. Linear classifier.
- **DecisionTree** — recursive binary splits.
- **RandomForest** — bagged trees + feature subsampling.
- **SVM** — max-margin hyperplane, kernels for nonlinearity.
- **KNN** — lazy learner; majority vote of neighbors.
- **NaiveBayes** — Bayes + feature independence.
- **GradientBoosting** — sequential trees fitting residuals.
- **XGBoost** — 2nd-order, regularized, fast.

## Unsupervised (`Unsupervised/`)
Structure without labels.
- **KMeans** — Lloyd's algorithm; minimize within-cluster variance.
- **DBSCAN** — density-based; handles arbitrary shapes; noise-aware.
- **HierarchicalClustering** — agglomerative dendrogram.
- **PCA** — linear variance-preserving projection.
- **tSNE** — nonlinear local-neighborhood preserving embedding.
- **GaussianMixture** — EM over mixture of gaussians.
- **IsolationForest** — outlier detection via split depth.

## Semi-Supervised (`SemiSupervised/`)
- **LabelPropagation** — graph-based label diffusion.

## Ensemble (`Ensemble/`)
- **Bagging** — bootstrap aggregation.
- **AdaBoost** — reweight errors, weighted voting.
- **Stacking** — meta-learner over base predictions.

## Advanced Paradigms (`Advanced/`)
### IncrementalLearning
Train on stream; update model with new samples without full retrain. Algorithms: online gradient descent, incremental Naive Bayes, Hoeffding Trees (VFDT), incremental SVM.

### ContinualLearning (= Lifelong Learning)
Sequential tasks without forgetting old ones (fight **catastrophic forgetting**).
Approaches:
- **Regularization-based**: EWC (Elastic Weight Consolidation), SI, MAS.
- **Replay-based**: store past samples (ER, A-GEM) or generate them (GenerativeReplay, DGR).
- **Architecture-based**: Progressive Nets, PackNet, HAT, dynamic expansion.
- **Prompt-based** (for LLMs): L2P, DualPrompt.

### ConceptDrift
Distribution P(X,y) changes over time. Detection + adaptation.
Types:
- **Sudden** — abrupt change (COVID on retail).
- **Gradual** — old and new concepts coexist, old fades.
- **Incremental** — slow migration.
- **Recurring** — seasonality, returning patterns.
- **Blip / outlier** — transient.
Detection: DDM, EDDM, ADWIN, Page-Hinkley, KS test on features.
Adaptation: sliding window retraining, ensembles (Learn++.NSE), dynamic weighting.

### FederatedLearning
Train across devices without centralizing data. Privacy + bandwidth + regulation.
- **FedAvg** — clients do SGD on local data → server averages weights.
- **FedProx** — adds proximal term for heterogeneous clients.
- **FedSGD / FedOpt / FedAdam** — server optimizer variants.
- **Personalized FL** — per-client head or adapters.
- **Secure aggregation** (cryptographic sum) + **Differential Privacy** noise.
- Challenges: non-IID data, stragglers, Byzantine clients (Krum, Median).

### OnlineLearning
Single-pass, regret-minimization framing. Perceptron, Follow-the-Regularized-Leader, Online Gradient Descent, Multi-armed bandits (ε-greedy, UCB, Thompson).

### ActiveLearning
Model queries labels for most-informative samples (uncertainty sampling, query-by-committee, expected model change).

### SelfSupervisedLearning
Labels from the data itself. Pretext tasks (rotation, masked modeling). Foundation of BERT, SimCLR, MAE, DINO.

### ContrastiveLearning
Pull similar pairs together, push dissimilar apart. SimCLR, MoCo, CLIP, InfoNCE loss.

### MetaLearning
"Learn to learn". MAML, Reptile, ProtoNets. Quick adaptation to new tasks.

### FewShotLearning / ZeroShotLearning
Few/zero labeled examples. Uses embeddings + prototypes; foundation models (CLIP, GPT) natively zero-shot.

### DomainAdaptation
Source distribution ≠ target. DANN (adversarial), CORAL (align moments), Self-training.

### CurriculumLearning
Easy → hard sample ordering. Speeds and stabilizes training.

---
## Suggested tour
LinearReg → LogReg → DecisionTree → RF/GBM → PCA → KMeans → SVM → Ensemble → NaiveBayes → Advanced (SSL, Continual, Federated).
