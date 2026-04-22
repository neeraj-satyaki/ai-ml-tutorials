"""Smoke tests that don't hit the API."""
from pathlib import Path

from goku.knowledge import build_index
from goku.models import Plan, Domain, Concept, Chapter, Topic, Rule
from goku.writer import plan_to_markdown, _slug


def test_knowledge_index_finds_domains():
    root = Path(__file__).resolve().parent.parent.parent
    idx = build_index(root)
    assert len(idx.domains) >= 5
    # at least some top-level domains should have READMEs
    assert any("## " in v or "# " in v for v in idx.readmes.values())


def test_markdown_render_roundtrip():
    plan = Plan(
        functionality="toy",
        summary="toy plan",
        domains=[
            Domain(
                name="Backend",
                why="the functionality is server-side",
                concepts=[
                    Concept(
                        name="Auth",
                        why="every API needs it",
                        chapters=[
                            Chapter(
                                name="Tokens",
                                why="stateless scales",
                                topics=[
                                    Topic(
                                        name="JWT",
                                        why="widely supported",
                                        references=["Backend/Auth/JWT_Design_Security/"],
                                        rules=[
                                            Rule(
                                                name="Rotate signing keys",
                                                why="limit blast radius of a leak",
                                                enforcement="JWKS rotation job",
                                            )
                                        ],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            )
        ],
    )
    md = plan_to_markdown(plan)
    assert "Domain: Backend" in md
    assert "Rotate signing keys" in md
    assert "JWKS" in md


def test_slug():
    assert _slug("Hello World!") == "Hello_World"
    assert _slug("API/Auth") == "API_Auth"
