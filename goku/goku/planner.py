"""Two-phase planner.

Phase 1 (shortlist): ask Claude which top-level domains matter for the task.
Phase 2 (plan):       load those domain READMEs, build full hierarchy.
"""
from __future__ import annotations
from typing import List

from goku.agent import Agent
from goku.knowledge import KnowledgeIndex
from goku.models import Plan, Shortlist
from goku.prompts import SYSTEM, SHORTLIST_USER, PLAN_USER


def one_line(text: str, max_chars: int = 240) -> str:
    first = text.strip().split("\n\n", 1)[0].replace("\n", " ").replace("#", "")
    return (first[:max_chars] + "...") if len(first) > max_chars else first


def shortlist_domains(
    agent: Agent, idx: KnowledgeIndex, functionality: str, top_k: int = 6
) -> Shortlist:
    domain_summaries = "\n".join(
        f"- {name}/: {one_line(idx.readmes.get(name, '(no README)'))}"
        for name in sorted(idx.readmes.keys())
    )
    user = SHORTLIST_USER.format(
        functionality=functionality, domain_summaries=domain_summaries
    )
    short = agent.call_json(SYSTEM, user, Shortlist)
    short.items = sorted(short.items, key=lambda x: x.relevance, reverse=True)[:top_k]
    return short


def build_plan(
    agent: Agent, idx: KnowledgeIndex, functionality: str, shortlist: Shortlist
) -> Plan:
    blocks: List[str] = []
    for item in shortlist.items:
        text = idx.load_readme(item.path) or idx.readmes.get(item.path.split("/")[0], "")
        if text:
            blocks.append(f"--- {item.path} (relevance={item.relevance:.2f}) ---\n{text}")
    readmes = "\n\n".join(blocks) if blocks else "(no readmes loaded)"
    user = PLAN_USER.format(functionality=functionality, readmes=readmes)
    return agent.call_json(SYSTEM, user, Plan)
