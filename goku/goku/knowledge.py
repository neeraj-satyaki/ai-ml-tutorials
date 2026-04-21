"""Crawl the Tutorials repo to build a compact index for Claude.

We want: cheap context. Give model folder tree + just the top-level README.md per
domain. Deeper READMEs are loaded on demand once a domain is shortlisted.
"""
from __future__ import annotations
from pathlib import Path
from typing import Dict, List
from dataclasses import dataclass, field

TOP_LEVEL_DOMAINS = {
    "ML", "DL", "RL", "AI", "CS", "Math",
    "DataScience", "SystemDesign", "Ops",
    "DesignPatterns", "DBMS", "ComputerArchitecture",
    "OperatingSystems", "NetworkSecurity", "Cybersecurity",
    "ElectronicsCommunication_Embedded",
    "ProgrammingLanguages", "Frontend", "Backend",
    "_REFERENCE",
}

MAX_README_CHARS = 15_000


@dataclass
class Node:
    path: Path
    kind: str  # "dir" | "readme" | "example" | "reference"
    summary: str = ""


@dataclass
class KnowledgeIndex:
    root: Path
    domains: Dict[str, Node] = field(default_factory=dict)
    readmes: Dict[str, str] = field(default_factory=dict)

    def folder_tree(self, max_depth: int = 3) -> str:
        """Return a trimmed folder tree as a string (readable by LLM)."""
        lines: List[str] = []

        def walk(p: Path, depth: int):
            if depth > max_depth:
                return
            try:
                children = sorted(
                    [c for c in p.iterdir() if not c.name.startswith(".") and c.name != "output"]
                )
            except (PermissionError, FileNotFoundError):
                return
            for c in children:
                if c.is_dir():
                    lines.append("  " * depth + f"- {c.name}/")
                    walk(c, depth + 1)

        walk(self.root, 0)
        return "\n".join(lines)

    def load_top_readmes(self) -> Dict[str, str]:
        """Return {domain_name: first N chars of README.md}."""
        out: Dict[str, str] = {}
        for name in sorted(TOP_LEVEL_DOMAINS):
            candidate = self.root / name / "README.md"
            if candidate.exists():
                text = candidate.read_text(errors="replace")
                out[name] = text[:MAX_README_CHARS]
        return out

    def load_readme(self, relative_path: str) -> str:
        """Load a specific README or markdown file safely."""
        target = (self.root / relative_path).resolve()
        if self.root.resolve() not in target.parents and target != self.root.resolve():
            raise ValueError(f"Refusing to read outside repo root: {relative_path}")
        if target.is_dir():
            target = target / "README.md"
        if not target.exists():
            return ""
        return target.read_text(errors="replace")[:MAX_README_CHARS]


def build_index(root: Path) -> KnowledgeIndex:
    """Construct the repo index."""
    root = root.resolve()
    idx = KnowledgeIndex(root=root)
    for name in TOP_LEVEL_DOMAINS:
        p = root / name
        if p.exists():
            idx.domains[name] = Node(path=p, kind="dir")
    idx.readmes = idx.load_top_readmes()
    return idx
