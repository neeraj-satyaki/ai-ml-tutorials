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
├── DesignPatterns/           # GoF + architectural + concurrency + cloud-native + anti-patterns
├── DBMS/                     # Deep DB: theory, storage, query, txns, recovery, distributed
├── ComputerArchitecture/     # ISA, pipelining, memory, parallelism, security
├── OperatingSystems/         # Procs, sched, mem, FS, I/O, virt, security, RT
├── NetworkSecurity/          # Layered + perimeter + crypto protocols + monitoring
├── Cybersecurity/            # Full: offensive, defensive, forensics, IoT/OT, Web3, AI-sec + 26 case studies
├── ElectronicsCommunication_Embedded/  # Digital logic, VLSI, DSP, comm, MCU, RTOS, sensors, IoT
├── ProgrammingLanguages/     # Top langs + paradigms + advanced techniques (meta, SIMD, lock-free, GPU)
├── Frontend/                 # HTML/CSS/JS/TS + frameworks + perf + a11y + sec + PWA + 3D + DS
├── Backend/                  # Runtimes + APIs + data + messaging + auth + serverless + microservices
├── NLP/                      # Fundamentals → LLM era → evals → frameworks → multilingual → code models → safety
├── Robotics/                 # Kinematics, perception, SLAM, control, planning, manipulation, VLA, ROS 2
├── HPC/                      # Parallelism, NCCL/MPI, accelerators, train/infer frameworks, clusters, profiling
├── Mobile/                   # iOS, Android, cross-platform, on-device AI, perf/UX, security, release
├── XR_ARVR/                  # 6DoF/SLAM, Quest/Vision Pro, engines, rendering, input, AI in XR, industry apps
├── Blockchain_Web3/          # Fundamentals, consensus, Ethereum/rollups, other chains, DeFi, tooling, ZK
├── Testing/                  # Unit → integration → E2E → property → fuzz → mutation → perf → sec → chaos → ML
├── QuantumProgramming/       # SDKs, algorithms, error correction, hardware, compilers, simulation, apps
├── GameDev/                  # Unity / Unreal / Godot — rendering, physics, AI, netcode, platforms
├── Bioinformatics/           # Sequencing, structural bio, omics, clinical, AI drug discovery
├── QuantFinance/             # Market structure, strategies, modeling, HFT tech, ML trading, risk
├── Compilers/                # Frontend, IR, optimization, backend, runtime, projects, references
├── CompetitiveProgramming/   # DSA topics, contests, training, languages, tools
├── ProductEngineeringManagement/  # PM + EM skills, process, strategy, communication
├── Career_InterviewPrep/     # Ladder signals, DSA prep, sysdesign, behavioral, offers, resume
├── Research/                 # Paper reading, reproducibility, experimentation, open science
├── TechWriting_DevRel/       # Docs, blogging, talks, community, DevRel practice
├── OpenSource_Contribution/  # First PR → maintainership → licensing → governance
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
├── goku/                     # Claude coding agent — plans functionality from this repo
│   └── Uses Anthropic API to build Domain→Concept→Chapter→Topic→Rule plans with Why at every node
│
└── _REFERENCE/               # Cross-cutting references
    ├── Activations_5Ws.md          # Sigmoid → SwiGLU — 5Ws each
    ├── NeuralNet_Derivations.md    # One-iteration math per arch
    ├── Pseudocode_and_Flowcharts.md# All algos: pseudocode + mermaid flows
    ├── When_To_Use.md              # Scenario rules for every algorithm
    ├── sample_linear_regression.drawio # draw.io XML template
    ├── Hyperparameter_Tuning.md    # Search algos, tooling, domain defaults
    ├── Training_Optimization.md    # Optimizers, LR schedules, stability, distributed
    ├── Model_Performance_Metrics.md# Metrics across ML/DL/CV/LLM
    ├── Confusion_Matrix.md         # Binary + multiclass + imbalance + thresholds
    ├── LLM_Evals.md                # Capability, preference, agent, safety, ops evals
    ├── Prompt_Engineering_Patterns.md # Structural patterns, CoT family, guardrails
    ├── Model_Compression.md        # Quantization, pruning, distillation, serving tricks
    ├── RAPIDS.md                   # GPU-accelerated data science (cuDF, cuML, cuGraph)
    ├── Rivermax.md                 # NVIDIA low-latency media + RoCE I/O
    ├── Streaming_Frameworks.md     # GStreamer, DeepStream, DL Streamer, NNStreamer...
    ├── ONNX.md                     # ONNX + Runtime + EPs + accessories
    ├── Beginners_Project_Guide.md  # Robust/secure/reliable/scalable project planning
    ├── build_pdf.py                # Script to build the PDF from the markdown source
    ├── Beginners_Project_Guide.pdf # Rendered PDF version
    └── CaseStudy_IdenticalBottles_MultiCamera.md # Tracking identical objects across N cams
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
