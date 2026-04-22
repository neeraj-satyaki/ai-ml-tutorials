# LLM Evals — How to Actually Measure Models

Evals decide model choice, deploy gates, fine-tune success. Not a benchmark list — a how-to.

## 1. Eval types

| Type | What it answers | Example |
|------|-----------------|---------|
| **Capability** | Can model do X? | MMLU, GPQA, HumanEval |
| **Preference** | Which model do humans prefer? | Arena Elo, MT-Bench |
| **Instruction-following** | Does it follow format/constraints? | IFEval, FollowBench |
| **Reasoning** | Chain quality | GSM8K, MATH, AIME, BIG-Bench Hard |
| **Long context** | Recall at depth | NIH, RULER, LongBench v2 |
| **Tool use / agent** | Does it act? | τ-bench, SWE-bench, GAIA, AgentBench |
| **Safety** | Does it refuse / harm? | WMDP, BBQ, StrongREJECT, HarmBench |
| **Domain-specific** | Fitness for your task | your own rubric-graded set |
| **Operational** | Latency / throughput / cost | p50/p95/p99 TTFT, tok/s, $/task |

## 2. The big public benchmarks (2024-25)

- **MMLU / MMLU-Pro** — broad knowledge.
- **GPQA (Diamond)** — PhD-level reasoning; contamination-resistant.
- **BBH, AGIEval**.
- **HumanEval / MBPP / LiveCodeBench / SWE-bench (Verified, Full, Lite)** — code.
- **GSM8K, MATH, AIME, FrontierMath** — math.
- **IFEval, MuSR, FOLLOWIR** — instruction following.
- **HELM** — holistic, multi-scenario.
- **Chatbot Arena** — live pairwise Elo at lmarena.ai.
- **MT-Bench, AlpacaEval 2** — LLM-judge preference.
- **TruthfulQA** — hallucination-adjacent.
- **RULER, NIH, LongBench v2, ∞-Bench** — long context.
- **MMMU, MMBench** — multimodal.
- **τ-bench (tau)** — tool use + dialogue.
- **SWE-bench** — real GitHub bugs; gold standard for coding agents.
- **GAIA, AgentBench, OSWorld, WebArena, VisualWebArena** — agents.

## 3. Your own eval set is worth more than all of these

Reasons:
1. Public benchmarks leak into training data.
2. They don't measure *your* distribution.
3. They're at the wrong task difficulty for your product.

**Build a golden set** of 100-500 prompts:
- Covers your real traffic distribution.
- Has gold answers or rubric graders.
- Version-controlled. Updated quarterly.
- Graded by humans, then codified into automated LLM-judge.

## 4. LLM-as-judge (modern default)

Use stronger model to grade weaker one.
- **Pairwise**: A vs B, "which is better per this rubric?"
- **Pointwise**: score 1-5 on axes (correctness, style, safety).
- **Reference-based**: compare to gold.

Pitfalls:
- Judge bias toward longer answers → add length penalty / shuffle positions.
- Self-preference bias → don't use the same model as judge and contestant.
- Reasoning models (o1-style) make better judges.
- Always sanity-check with human spot-checks on ~10% of items.

## 5. Reasoning-specific eval

For o1 / DeepSeek-R1 style reasoning LLMs:
- Quality *and* length of reasoning trace matter.
- Pass@k with many samples (k=4, 8, 16).
- Self-consistency voting.
- Test without tools (pure CoT) and with (tool-augmented).
- **Gold**: math olympiad problems (AIME, USAMO), competitive programming (LiveCodeBench), GPQA-Diamond.

## 6. Agent + tool-use eval

- **τ-bench** — customer service with tool calls + user sim.
- **SWE-bench Verified** — ~500 hand-verified real GitHub issues.
- **GAIA** — general assistant with tools.
- **OSWorld / WebArena** — browser + desktop tasks.
- **τ²-bench, Cybench, InfiAgent** — specialized.
- Custom: build a sim with your tools + rubric.

## 7. RAG eval

Separate retrieval from generation.
- **Retrieval**: Recall@k, MRR, NDCG@k on (query, relevant doc) pairs.
- **Generation**: faithfulness to context, answer relevance.
- Frameworks: **Ragas**, **TruLens**, **DeepEval**, **promptfoo**.
- Anti-pattern: grading end-to-end only — you can't tell what broke.

## 8. Safety eval

- **WMDP** — dangerous knowledge (bio, cyber, chem).
- **StrongREJECT** — harmful-request refusal.
- **HarmBench**.
- **CyberSecEval** (Meta).
- **BBQ / BOLD / CrowS-Pairs** — bias.
- Red-team: **PAIR**, **GCG**, **Automated Red-Teaming** (Perez et al.).
- Apollo Research scheming evals, sleeper-agent probing.

## 9. Operational eval

- **TTFT** (time to first token).
- **Inter-token latency**, tok/s throughput.
- **p50/p95/p99** under load.
- **Cost/task** — input + output tokens × price, or $/successful task.
- **Cache hit rate** (prompt caching).
- **Failure modes**: rate-limit, timeout, garbled output.

## 10. Eval infra patterns

- Store every prompt + response + trace (LangSmith, Langfuse, Braintrust, Weave).
- Nightly eval job on golden set; diff vs last week.
- Eval as CI gate — block deploy on regression in top-3 eval suites.
- Decoupled scoring — add new graders without rerunning generations.
- **Eval-driven development** — write the eval first, model choice + prompts follow.

## 11. Common mistakes

1. Trusting one benchmark.
2. No eval on your own distribution.
3. Grading with the same model you're testing.
4. Not accounting for temperature / randomness.
5. Ignoring operational metrics until prod.
6. Running on leaked / contaminated data.
7. Treating preference as truth (people like confident wrong answers).

## 12. Recommended stack (2025)

- Collection: **Braintrust / Langfuse / Langsmith**.
- Rag: **Ragas**.
- Agent: **τ-bench** + custom env.
- Public benchmarks: `lm-eval-harness`, `bigcode-evaluation-harness`.
- LLM judges: Claude / GPT-class as graders; always second sample.
- CI: GitHub Actions + cached artifact of eval set.

## Books + refs
- *Prompting Fundamentals + Evaluation* — Eugene Yan.
- Anthropic + OpenAI eval cookbooks.
- Hugging Face `lm-evaluation-harness` + BigCode Eval.
- lmarena.ai, evalplus.github.io.
