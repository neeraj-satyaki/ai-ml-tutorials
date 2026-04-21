"""goku CLI.

    python -m goku "<functionality>" [--out DIR] [--scaffold] [--depth 5] [--verbose]
"""
from __future__ import annotations
import os
import sys
from pathlib import Path

import typer
from dotenv import load_dotenv
from rich import print as rprint
from rich.console import Console

from goku.agent import Agent
from goku.knowledge import build_index
from goku.planner import shortlist_domains, build_plan
from goku.writer import plan_to_markdown, scaffold_tree

app = typer.Typer(add_completion=False, help="goku — Claude coding agent")
console = Console()


@app.command()
def main(
    functionality: str = typer.Argument(..., help="What you want to build"),
    repo_root: Path = typer.Option(
        None, "--repo", help="Tutorials repo root (defaults to parent of goku/)"
    ),
    model: str = typer.Option(
        os.environ.get("GOKU_MODEL", "claude-opus-4-7"), "--model"
    ),
    out: Path = typer.Option(Path("output"), "--out", help="Directory for plan output"),
    scaffold: bool = typer.Option(False, "--scaffold", help="Also emit starter code tree"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        rprint("[red]ANTHROPIC_API_KEY is not set. Copy .env.example -> .env[/red]")
        sys.exit(2)

    repo_root = repo_root or Path(__file__).resolve().parent.parent.parent
    if verbose:
        rprint(f"[dim]repo_root = {repo_root}[/dim]")

    idx = build_index(repo_root)
    if verbose:
        rprint(f"[dim]domains indexed: {len(idx.domains)}[/dim]")

    agent = Agent(model=model)

    with console.status("[bold cyan]Phase 1: shortlisting relevant domains..."):
        short = shortlist_domains(agent, idx, functionality)
    rprint("[green]Shortlist:[/green]")
    for it in short.items:
        rprint(f"  [{it.relevance:.2f}] {it.path} — {it.why}")

    with console.status("[bold cyan]Phase 2: building hierarchical plan..."):
        plan = build_plan(agent, idx, functionality, short)

    out.mkdir(parents=True, exist_ok=True)
    slug = "_".join(functionality.lower().split())[:60].replace("/", "_")
    md_path = out / f"{slug}.md"
    md_path.write_text(plan_to_markdown(plan))
    rprint(f"[green]Plan written:[/green] {md_path}")

    if scaffold:
        scaffold_dir = out / f"{slug}_scaffold"
        scaffold_tree(plan, scaffold_dir)
        rprint(f"[green]Scaffold written:[/green] {scaffold_dir}")


if __name__ == "__main__":
    app()
