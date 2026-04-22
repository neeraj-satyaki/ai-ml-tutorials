# Prompt Engineering Patterns

Not tricks — reusable structures that make LLM outputs consistent, steerable, and eval-able.

## 1. Always define

Every production prompt specifies:
1. **Role** — who is the model.
2. **Objective** — what outcome matters.
3. **Context** — background + data.
4. **Constraints** — output format, length, tone, forbidden behaviors.
5. **Output schema** — explicit JSON / Markdown / XML shape.

Missing any one → inconsistent output.

## 2. Structure patterns

### XML-tagged sections (Claude-favored)
```
<context>...</context>
<instructions>...</instructions>
<examples>...</examples>
<input>...</input>
```
Tag names aren't magic; disambiguating sections is.

### JSON mode / Structured Outputs
Prefer provider features (OpenAI `response_format=json_schema`, Anthropic structured tool call) over "respond as JSON" in prose. Validate every time anyway.

### Pydantic / Zod schema as prompt contract
Include the schema verbatim in the prompt. Post-validate with the same schema. One source of truth.

## 3. Few-shot

- 0-shot works for strong models on simple tasks.
- 1-3 shot: best bang-for-buck on structured tasks.
- >5 shot: diminishing returns on 4-class models; more hurts latency + cost.
- Diverse examples > redundant ones.
- Order matters — last example has highest weight.

## 4. Chain-of-Thought family

- **CoT**: "think step by step" — default for non-reasoning models.
- **Zero-shot CoT**: add that phrase, no examples.
- **Plan-and-Solve**: plan → steps → execute.
- **Self-Consistency**: sample N CoTs, majority vote.
- **Tree-of-Thoughts**: explore branches, vote/prune.
- **Graph-of-Thoughts**.
- **Reflection / Self-Refine** — critique own output then revise.
- **Reasoning models (o1, R1, Claude extended thinking)** — do NOT tell them to CoT; they do it internally. Short task prompt + let them think.

## 5. Tool use + agents

- Describe tools with typed schemas; include one worked example per tool.
- Constrain when to call ("call X only if Y").
- Name outputs of tools clearly — model reasons over names.
- **ReAct** interleaves thought → action → observation.
- **Reflexion** adds self-critique on failure.
- Short loop bounds (max_iterations) prevent runaway.

## 6. Retrieval-Augmented (RAG)

- Put retrieved passages in an explicit block:
  ```
  <context>
  [source: file.md#L30]
  ...
  </context>
  ```
- Instruct: "Answer ONLY from context. If not in context, say you don't know."
- Include source IDs; require citation in output.
- Rank + rerank — first pass retrieval is rarely enough.

## 7. Guardrails-in-prompt

- "If the user asks X, refuse with Y."
- Classifier LLM upstream ("is this request in-policy?") often better than in-prompt rules.
- Use **system prompt** for immutable rules; **developer messages** for turn-specific.
- Post-filter output through a safety classifier (Llama Guard, OpenAI moderation).

## 8. Long context patterns

- **Needle placement**: model performance drops in the middle. Put critical info at top or bottom.
- **Summarize and retrieve**: compress far-back chunks; keep recent verbatim.
- Explicit table of contents if > 50k tokens.
- Prompt caching for repeated prefixes (Anthropic cache, OpenAI prompt cache).

## 9. Multi-step decomposition

Don't pile everything into one prompt. Decompose:
```
plan → extract → analyze → write
```
Separate prompts, smaller context each, easier to eval each stage.

## 10. Determinism knobs

- `temperature=0` → most deterministic but not truly repeatable with all providers.
- `seed` parameter (OpenAI) — best effort.
- Lower temperature for extraction, higher for generation.
- Top-p 0.95 default is fine; change only with reason.

## 11. Role patterns

- **Expert persona** ("You are a senior auditor…") biases vocabulary, helpful for tone.
- Avoid "act as <name>" — hallucination risk.
- **Simulated user** for testing agents.
- **Adversarial evaluator** for red-teaming.

## 12. Output-control patterns

- **Start-of-answer prefix**: put `<json>` or `{` as assistant prefill to force format.
- **Thinking tags**: `<thinking>...</thinking>` hidden from end user.
- **Output pinning**: "Respond with ONLY the following JSON and nothing else."
- **Enumerated choices**: "Respond with exactly one of: LOW, MEDIUM, HIGH."

## 13. Error handling

- Add a "respond with `{\"error\": \"...\"}` if you can't answer" clause.
- Retry with clarification on parse failure.
- Log raw model output alongside parsed — debugging later requires it.

## 14. Caching

- Cache long system prompts + tool defs + rarely-changing context.
- Anthropic: up to 4 `cache_control` breakpoints, 5-min TTL (1-hr tier available).
- OpenAI: automatic for prefixes ≥ 1024 tokens.
- Rule: put *stable* content first, *volatile* content last.

## 15. Evaluating a prompt

- 10-30 examples graded. Baseline.
- Change one variable (instruction, example order, schema).
- Re-grade. Keep only if significantly better.
- Track prompt versions in git + logs.

## 16. Anti-patterns

- "Please" / "thanks" sprinkled everywhere — no effect; noise.
- Contradictory instructions.
- No format spec → hope for the best.
- Mega-prompts with 50 bullet points — model ignores middle.
- Hand-designed jailbreak-ish tricks instead of provider guardrails.
- No examples on complex tasks.

## 17. Test harness

For any non-trivial prompt:
- Golden inputs + expected outputs.
- Automated grader (exact-match / regex / schema / LLM-judge).
- Run on every prompt change.
- Version prompts in git with Semver-style bumps.

## Refs
- Anthropic prompt engineering guide.
- OpenAI prompting cookbook.
- *Designing Machine Learning Systems* — Chip Huyen (LLM chapter).
- Eugene Yan blog (`eugeneyan.com`).
- Lilian Weng blog (`lilianweng.github.io`).
- `prompts.chat`.
