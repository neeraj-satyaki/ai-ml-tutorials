"""Render a Plan to markdown + optional code scaffold."""
from __future__ import annotations
from pathlib import Path

from goku.models import Plan


def plan_to_markdown(plan: Plan) -> str:
    lines = []
    lines.append(f"# Plan — {plan.functionality}\n")
    lines.append(f"> {plan.summary}\n")

    if plan.non_goals:
        lines.append("## Non-goals")
        for ng in plan.non_goals:
            lines.append(f"- {ng}")
        lines.append("")

    if plan.open_questions:
        lines.append("## Open Questions")
        for q in plan.open_questions:
            lines.append(f"- {q}")
        lines.append("")

    for d in plan.domains:
        lines.append(f"## Domain: {d.name}")
        lines.append(f"> **Why:** {d.why}\n")
        for c in d.concepts:
            lines.append(f"### Concept: {c.name}")
            lines.append(f"> **Why:** {c.why}\n")
            for ch in c.chapters:
                lines.append(f"#### Chapter: {ch.name}")
                lines.append(f"> **Why:** {ch.why}\n")
                for t in ch.topics:
                    lines.append(f"##### Topic: {t.name}")
                    lines.append(f"> **Why:** {t.why}")
                    if t.references:
                        lines.append(
                            "> **Refs:** "
                            + ", ".join(f"`{r}`" for r in t.references)
                        )
                    lines.append("")
                    for r in t.rules:
                        lines.append(f"- **Rule:** {r.name}")
                        lines.append(f"  - *Why:* {r.why}")
                        if r.enforcement:
                            lines.append(f"  - *Enforce:* {r.enforcement}")
                    lines.append("")
    return "\n".join(lines)


def scaffold_tree(plan: Plan, out_dir: Path) -> None:
    """Emit a folder tree matching Domain/Concept/Chapter/Topic with stub files."""
    out_dir.mkdir(parents=True, exist_ok=True)
    for d in plan.domains:
        for c in d.concepts:
            for ch in c.chapters:
                for t in ch.topics:
                    p = out_dir / _slug(d.name) / _slug(c.name) / _slug(ch.name) / _slug(t.name)
                    p.mkdir(parents=True, exist_ok=True)
                    readme = p / "README.md"
                    body = (
                        f"# {t.name}\n\n"
                        f"> Why: {t.why}\n\n"
                        "## Rules\n"
                        + "\n".join(
                            f"- [ ] {r.name} — *{r.why}*" for r in t.rules
                        )
                        + "\n"
                    )
                    readme.write_text(body)


def _slug(s: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in s).strip("_")
