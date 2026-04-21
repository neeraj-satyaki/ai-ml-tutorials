# Tutorials — AI / ML / DL / RL / CS / Math / Data Science / System Design

Personal learning index. Each top-level folder has its own `README.md` with detailed topics; leaf algorithm folders have runnable `example.py`.

## Layout

```
Tutorials/
├── ML/                       # Classical machine learning
│   ├── Supervised/           # LinearReg, LogReg, Tree, RF, SVM, KNN, NB, GB, XGBoost
│   ├── Unsupervised/         # KMeans, DBSCAN, Hier, PCA, tSNE, GMM, IsolationForest
│   ├── SemiSupervised/       # LabelPropagation
│   ├── Ensemble/             # Bagging, AdaBoost, Stacking
│   └── Advanced/             # Incremental, Continual, Concept-drift, Federated,
│                             # Online, Active, SSL, Contrastive, Meta, FewShot, etc.
│
├── DL/                       # Deep learning
│   ├── FeedForward/MLP
│   ├── CNN/                  # LeNet, ResNet
│   ├── RNN/                  # Vanilla, LSTM, GRU
│   ├── Transformer/          # BERT, GPT
│   ├── Autoencoder/          # VanillaAE, VAE
│   ├── GAN/DCGAN
│   ├── GraphNN/GCN
│   ├── Diffusion/DDPM
│   └── ComputerVision/       # 19 CV tasks (det, seg, pose, depth, gen, etc.)
│
├── RL/                       # Reinforcement learning
│   ├── ValueBased/           # Q-Learn, SARSA, DQN
│   ├── PolicyBased/          # REINFORCE, PPO, TRPO
│   ├── ActorCritic/          # A2C, A3C, DDPG, SAC, TD3
│   ├── ModelBased/           # DynaQ, MCTS
│   └── MultiAgent/MADDPG
│
├── AI/                       # AI topics (classical + frontier + agentic + AGI)
│   ├── Basics/               # Agents, Search, Logic, KR, Planning, ExpertSys...
│   ├── Frontier2024_2026/    # Mamba, MoE, FlashAttn, DPO, GRPO, RAG,
│   │                         # Constitutional AI, Diffusion-Trans, KAN,
│   │                         # o1/test-time compute, JEPA, Sora, ...
│   ├── Agentic/              # ReAct, Reflexion, ToT, MCP, tool use,
│   │                         # multi-agent, computer-use, code agents, evals
│   └── AGI/                  # Scaling laws, emergence, alignment, mech-interp,
│                             # red-team, safety evals, superalignment...
│
├── CS/                       # Computer Science — basics to PhD
│   ├── Basics/               # Types, control flow, OOP, FP
│   ├── DataStructures/       # Arrays → LSM-Trees → Succinct
│   ├── Algorithms/           # Sort, Search, Graph, Paradigms, String, Geom, Numerical
│   ├── Complexity/           # Basics, Classes, Theorems, Hardness, Advanced
│   ├── Computability/        # TMs, Halting, Rice, Gödel, Kolmogorov
│   ├── FormalLanguages/      # Regex → CFG → Chomsky → Parsing → Semantics
│   ├── Systems/              # Arch, OS, Net, DB, Compilers, Types, GC
│   ├── Parallel_Distributed/ # Consensus, CAP, Byzantine, DHT, clocks
│   ├── Crypto_Security/      # Symmetric, ZKP, FHE, PQ, DP, TEE
│   ├── Quantum/              # Shor, Grover, QFT, error correction
│   └── PhD_Research_Frontier/# ω<2.4, IP=PSPACE, barriers, GCT, PCP, SOS
│
├── Math/                     # Mathematics for ML/DL/RL
│   ├── LinearAlgebra/        # Vectors, Matrices, Eigen, SVD, MatrixCalculus
│   ├── Calculus/             # Limits → Jacobian/Hessian
│   ├── Probability/
│   ├── Statistics/
│   ├── Optimization/
│   ├── InformationTheory/
│   ├── Discrete/
│   ├── NumericalMethods/
│   └── Geometry/
│
├── DataScience/              # End-to-end data work
│   ├── Pipeline/             # Frame → Collect → Clean → EDA → FE → Model → Deploy
│   ├── Analytics/            # Descriptive, Diagnostic, Predictive, Prescriptive,
│   │                         # Time-Series, A/B, Causal, Cohort, Funnel
│   ├── Tools/                # SQL, Pandas, Spark, dbt, Airflow, BI
│   ├── Storytelling/         # Audience, Narrative, Charts, Color, Dashboards, Ethics
│   └── EDA_Coefficients.md   # Every coefficient + when/scenario
│
├── Ops/                      # All *-Ops disciplines
│   ├── DevOps/, DevSecOps/, GitOps/, PlatformOps/
│   ├── DataOps/, MLOps/, ModelOps/, LLMOps/
│   ├── AIOps/, CVOps/, QAOps/
│   └── FinOps/, SecOps/      # full README with scope, tools, metrics
│
├── SystemDesign/             # Full system design curriculum
│   ├── Fundamentals/
│   ├── Networking/, Storage/, Databases/
│   ├── Caching/, Messaging/
│   ├── Patterns/, ReliabilityDR/, Security/
│   ├── Observability/, Scaling/, DevOps_Infra/
│   ├── CaseStudies/          # 30+ real-world designs
│   └── MLSystems/            # Feature stores → LLM serving
│
└── _REFERENCE/               # Cross-cutting references
    ├── Activations_5Ws.md          # Sigmoid → SwiGLU — 5Ws each
    ├── NeuralNet_Derivations.md    # One-iteration math per arch
    ├── Pseudocode_and_Flowcharts.md# All algos: pseudocode + mermaid flows
    ├── When_To_Use.md              # Scenario rules for every algorithm
    └── sample_linear_regression.drawio # draw.io XML template
```

## How to use

| I want to... | Go to... |
|--------------|----------|
| See a working example of an algorithm | `<area>/<family>/<algo>/example.py` |
| Understand *when* to use an algorithm | `_REFERENCE/When_To_Use.md` |
| See pseudocode + flowchart | `_REFERENCE/Pseudocode_and_Flowcharts.md` |
| Understand activation functions | `_REFERENCE/Activations_5Ws.md` |
| See one-iteration math for a NN type | `_REFERENCE/NeuralNet_Derivations.md` |
| Know what coefficient to use in EDA | `DataScience/EDA_Coefficients.md` |
| Study math prereqs | `Math/README.md` |
| Study the CS theory stack | `CS/README.md` |
| Design a system | `SystemDesign/README.md` |
| Learn latest AI (2024-26) | `AI/README.md` (Frontier section) |
| Build an agent | `AI/Agentic/` + `AI/README.md` |

## Running examples

Most scripts use `sklearn`, `numpy`, `torch`. Install:
```bash
pip install numpy scipy scikit-learn torch matplotlib pandas
pip install xgboost transformers        # for specific examples
```
Then run any:
```bash
python ML/Supervised/RandomForest/example.py
python DL/FeedForward/MLP/example.py
python RL/ValueBased/QLearning/example.py
```

## Conventions
- One `example.py` per algorithm leaf — minimal runnable toy.
- Architectures with heavy training needs show just the model + one forward/gradient step with a note about full train loop.
- Consolidated READMEs per section explain the *map* of topics.
- `_REFERENCE/` has cross-cutting reference docs.

## Flowcharts
- Mermaid renders natively on GitHub (`.md`).
- For draw.io: File → Import from → Mermaid, OR open `sample_linear_regression.drawio` for full XML template.

## Open follow-ups (not yet in repo)
These would be useful next passes — not done to avoid scope explosion:
- Per-leaf `pseudocode.md` + `when_to_use.md` + `.drawio` flowchart files (currently consolidated in `_REFERENCE/`).
- Per-leaf expansion of CV tasks with runnable examples (currently in `Architectures.md`).
- Full draw.io diagrams for each algorithm (sample provided; rest are in Mermaid).
