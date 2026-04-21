# goku — Claude Coding Agent

Plans code structure for a requested functionality by traversing this repo as its knowledge base.

Hierarchy: **Domain → Concept → Chapter → Topic → Rule**. Every node carries a **Why** comment explaining the design choice.

## What it does

1. Takes a one-line functionality description.
2. Crawls the repo folder tree + READMEs.
3. Asks Claude to pick relevant Domain(s).
4. Drills down Concept → Chapter → Topic → Rule.
5. Outputs a structured plan file with rationale at every level.
6. Optionally scaffolds starter code (file tree + stubs).

## Install

```bash
cd goku
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
```

## Use

```bash
python -m goku "build JWT auth with key rotation for a public API"
# → writes plan to goku/output/<slug>.md
```

CLI flags:

```
python -m goku "..." --model claude-opus-4-7 \
                     --depth 5 \
                     --out ./plans \
                     --scaffold           # also emit starter code tree
                     --verbose
```

## Why this design

**Hierarchy** matches how humans plan — from broad stance down to enforceable rules. Matches this repo's layout.

**Why-per-node** = the most valuable artifact. Tells future you WHY not WHAT. Code rots; intent survives.

**Repo as KB** = no external vector DB. Folder tree + READMEs are enough signal for Claude to reason about stack choices, patterns, tradeoffs already captured in this repo.

**Single-shot first, multi-shot later** = prove it works before adding RAG or tools. Agent loop stays minimal.

## Architecture

```
cli.py         → parses args, orchestrates
knowledge.py   → crawls tree, loads READMEs, builds compact index
agent.py       → Anthropic API wrapper w/ retry + caching
planner.py     → two-phase plan (shortlist domains → build full hierarchy)
models.py      → pydantic types for Domain/Concept/Chapter/Topic/Rule
prompts.py     → system + user prompt templates
writer.py      → markdown + optional code scaffold
```

## Example output
See `examples/` directory for pre-generated plans.

## Roadmap
- [ ] Add RAG over leaf `example.py` files for code snippets.
- [ ] Tool use: let agent open files on demand.
- [ ] Validator pass: check each rule against the repo's `When_To_Use.md`.
- [ ] PR-mode: open a PR with scaffold + plan.
