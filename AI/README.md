# AI — Basics, Frontier (2024-2026), Agentic, AGI

Four layers: classical AI → modern frontier → agents → AGI.

---

## Basics (`Basics/`) — Russell & Norvig territory

### WhatIsAI
Definitions: acting humanly (Turing), thinking humanly (cog-sci), acting rationally (agents).

### IntelligentAgents
- Agent = perceive → think → act. Sensors, actuators.
- Environments: fully/partially observable, deterministic/stochastic, episodic/sequential, static/dynamic, discrete/continuous, single/multi-agent.

### Search
- **SearchUninformed** — BFS, DFS, Iterative Deepening, Uniform Cost.
- **SearchInformed** — Greedy Best-First, A* (heuristic + admissible).
- **AdversarialSearch** — Minimax, Alpha-Beta pruning, expectimax.
- **ConstraintSatisfaction** — CSPs, backtracking, AC-3, forward checking, min-conflicts.

### Logic
- **LogicPropositional** — truth tables, CNF, resolution, SAT solvers (DPLL, CDCL).
- **LogicFirstOrder** — quantifiers, unification, resolution, forward/backward chaining.

### KnowledgeRepresentation
- Semantic networks, frames, description logic, production rules.
- **OntologiesSemanticWeb** — RDF, OWL, SPARQL, knowledge graphs.

### Planning
STRIPS, PDDL, partial-order planning, HTN, graph plan, SAT planning.

### ExpertSystems
Rule-based (MYCIN, DENDRAL). Inference engine + knowledge base + explanation.

### FuzzyLogic
Degrees of truth [0,1]. Fuzzy sets, fuzzy inference (Mamdani, Sugeno).

### EvolutionaryComputation
GA, GP, Evolution Strategies, NEAT, CMA-ES. Population-based optimization.

### Ethics
Bias, fairness, accountability, dual use, autonomy, privacy.

---

## Frontier 2024-2026 (`Frontier2024_2026/`)

### MambaSSM
Selective State-Space Models. Linear-time sequence modeling. Mamba (Gu, Dao 2023) → Mamba-2 (2024) unifies SSMs and attention. Competitive with Transformers at long context.

### Mamba2 / StateSpaceHybrid
Mamba-2: structured state-space duality. Hybrid models: Jamba (Mamba + Transformer + MoE), Zamba, Griffin, Hymba. Leverage both recall of attention and efficiency of SSM.

### MixtureOfExperts (MoE / MoE_Experts_Sparse)
Route tokens to subset of experts. Sparse activation. Models: Mixtral 8x7B, DeepSeek-V3, Qwen2.5-MoE, GPT-4 (rumored). Efficient scaling.

### FlashAttention
IO-aware exact attention. v1 (2022), v2 (2023), v3 (2024). Reduces HBM reads/writes; ~3-10x speedup.

### LongContextAttention
Ring Attention, Striped Attention, PagedAttention (vLLM), Needle-in-Haystack evals. 1M+ context (Gemini 1.5, Claude Opus 4+).

### RAG
Retrieval Augmented Generation. Retrieve docs → stuff into prompt. Advanced: Self-RAG, CRAG, HyDE, GraphRAG (Microsoft), Agentic RAG.

### RLHF / DPO / GRPO
Align LLMs with preferences.
- **RLHF** — PPO on preference reward model (InstructGPT, ChatGPT).
- **DPO** — direct preference optimization, no reward model, no PPO. (2023)
- **GRPO** — group relative policy optimization (DeepSeek-R1, 2024). Uses group-normalized advantages; no critic.
- Related: IPO, KTO, ORPO, SimPO.

### ConstitutionalAI
Anthropic's method: AI critiques its own outputs vs a "constitution" of principles → RLAIF.

### SpeculativeDecoding
Small draft model proposes N tokens, big model verifies in one pass. 2-3x throughput. Extensions: EAGLE, Medusa, lookahead.

### LoRA / QLoRA
Low-Rank Adapters: train only small ΔW = BA matrices. QLoRA quantizes base to 4-bit. Efficient fine-tuning on consumer GPUs.

### FlowMatching
Generative training via learning vector fields. Simpler than diffusion. Basis of Flux, Stable Diffusion 3, AudioBox.

### ConsistencyModels
Direct one-step generation from noise. OpenAI (Song et al., 2023). LCM (Latent Consistency Models).

### JEPA
Joint-Embedding Predictive Architecture (LeCun). Predict in embedding space, not pixel space. I-JEPA, V-JEPA (2024).

### TestTimeCompute_o1 / ReasoningChains
Scale compute at inference via long CoT rollouts. Models: OpenAI o1 (Sep 2024), o3 (Dec 2024), DeepSeek-R1 (Jan 2025), Claude 3.7/4 extended thinking, Qwen QwQ, Gemini 2.0 Flash Thinking. Training via RL on reasoning traces.

### DiffusionTransformers (DiT)
Replace U-Net with Transformer in diffusion. Backbone of Stable Diffusion 3, Sora, Flux. Scales better.

### Sora_VideoDiffusion
Text-to-video diffusion transformers. Sora, Runway Gen-3, Kling, Veo 3, MovieGen. Long coherent videos.

### KolmogorovArnoldNetworks (KAN)
2024 (Liu et al.). Learnable activation functions on edges (vs fixed activations, learned weights on edges in MLP). Kolmogorov-Arnold representation theorem.

### LiquidNeuralNets
Continuous-time RNN with liquid state (MIT, Hasani et al.). Robust to noise, fewer neurons. Used in Liquid Foundation Models (2024).

### NeuralODEs
dh/dt = f_θ(h,t). Chen et al. 2018. Continuous-depth nets. Basis of diffusion/flow matching.

### WorldModels
Learn latent dynamics; agents plan in imagined rollouts. Dreamer V3, Genie (DeepMind), Genie 2, GameNGen (Google video-game simulation).

### VisionLanguageModels (VLMs)
CLIP (2021) → Flamingo → BLIP-2 → LLaVA → GPT-4V → Claude 3 → Gemini → Qwen2-VL → Molmo → Pixtral. Image+text in, text out.

### AlphaProof_AlphaGeometry
DeepMind 2024. Formal math at IMO silver-medal level. AlphaGeometry 2 (2024). AlphaProof uses Lean + reinforcement learning over proofs.

### MultimodalFusion
Unified models across modalities. GPT-4o, Gemini 2.0, Chameleon, Unified-IO. Speech + text + vision + code in one model.

---

## Agentic (`Agentic/`)

### AgentLoop
Core pattern: `while not done: obs = sense(); thought = llm(obs + history); action = tool(thought); reward_or_feedback = execute(action)`.

### ToolUse / FunctionCalling
Model emits structured call. OpenAI function calling, Anthropic tool use. Native in GPT-4/Claude/Gemini.

### ReAct
Reason + Act interleaved (Yao et al. 2022). `Thought → Action → Observation → Thought...`.

### Reflexion
Verbal self-reflection on failures; update memory between trials (Shinn et al. 2023).

### ChainOfThought / TreeOfThoughts / GraphOfThoughts
- **CoT** — linear step-by-step (Wei et al. 2022).
- **ToT** — explore branches, vote/prune (Yao et al. 2023).
- **GoT** — arbitrary graph of thoughts, aggregate.

### Planning_LLM
Hierarchical: high-level plan → sub-goals → actions. ADaPT, Plan-and-Solve, Voyager.

### Memory
- **MemoryShortLong** — context window vs external store.
- **VectorMemory** — embed + retrieve. Integrated via RAG.
- **Episodic / semantic / procedural** memory abstractions.

### MCP_ModelContextProtocol
Anthropic 2024. Standard protocol for tools/resources/prompts between LLMs and apps. Like USB-C for AI context.

### MultiAgentOrchestration
Multiple specialized agents coordinate. Frameworks: AutoGen, CrewAI, LangGraph, Swarm (OpenAI), Claude subagents.

### LangGraph
Stateful graph-based agent orchestration (LangChain, 2024).

### AutoGPT / BabyAGI
Early autonomous agent demos (2023). Goal → self-generated subtasks → execute loop.

### ComputerUseAgents
Agents that control GUIs. Claude Computer Use (Oct 2024), OpenAI Operator, Project Mariner. Screen + mouse + keyboard.

### CodeAgents
Agents that write/execute code. Devin, Cursor agent, Claude Code, Aider, OpenDevin, SWE-agent. Benchmarked on SWE-bench.

### SelfImprovement
Self-play (AlphaZero), self-refine, STaR (self-taught reasoner), Quiet-STaR, RLAIF.

### AgentEvals
- SWE-bench (code), WebArena, VisualWebArena, OSWorld, GAIA, τ-bench, AgentBench, Cybench.

### Guardrails
Input/output filtering, tool allow-lists, sandboxing, rate-limits, policy LLMs, jailbreak detection.

---

## AGI (`AGI/`)

### Definitions
"General" = broad competence across domains, transfer, novel tasks. Debated thresholds: human-level, economically valuable work, self-improvement.

### ScalingLaws
Kaplan 2020, Chinchilla (Hoffmann 2022): optimal compute budget splits roughly evenly between params and tokens. Extensions: inference scaling laws (o1).

### EmergentAbilities
Abilities that appear only above threshold scale (Wei et al. 2022). Debated: some are measurement artifacts (Schaeffer et al. 2023).

### Generalization / TransferLearning / ContinualLearning / MetaLearning
Cross-task competence core to AGI.

### MultimodalAGI / Embodiment
Argument: AGI needs grounded physical interaction (embodied cognition). Projects: Figure, 1X, Optimus; RT-2, PaLM-E, Open X-Embodiment.

### Consciousness
Open. Global Workspace Theory, IIT, Attention Schema. Distinct from capability.

### Alignment
Make AI do what humans intend.
- Outer alignment: specify goals correctly.
- Inner alignment: model internals pursue that goal, not a proxy (mesa-optimization).

### MechanisticInterpretability
Reverse-engineer networks into circuits. Anthropic (features, superposition, SAE), Neel Nanda, Chris Olah. Activation steering.

### RLHF_alignment / ConstitutionalAI_align
Training-time alignment methods. See Frontier.

### RedTeaming
Adversarial probing. Automated red-teaming (Perez et al.), jailbreaks (DAN, PAIR, GCG).

### CapabilitiesEvals / SafetyEvals
- MMLU, GPQA, SWE-bench (capabilities)
- HELM, WMDP, CyberSecEval, BioS, agentic uplift evals (dangerous capabilities)

### PowerSeeking_Deception
Turner et al. — instrumental convergence argues sufficiently capable optimizers seek power. Sleeper Agents (Anthropic 2024), Apollo Research scheming evals.

### CorrigibilityOrthogonality
- **Orthogonality thesis** — intelligence and goals are independent.
- **Corrigibility** — system accepts correction/shutdown.

### AGItimelines
Forecasts vary: Metaculus (~2030 weak AGI), AI Impacts surveys, Epoch AI compute projections. Short- vs long-timeline debate.

### ExistentialRisk
Yudkowsky, Bostrom arguments. Takeoff speeds (slow/fast/discontinuous). CAIS vs monolithic agent views.

### Superalignment
Aligning systems smarter than us. Weak-to-strong generalization (OpenAI 2023), debate (Irving et al.), iterated amplification, recursive reward modeling.
