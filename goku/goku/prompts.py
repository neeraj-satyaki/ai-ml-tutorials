"""Prompt templates for the two-phase planner.

Phase 1: pick relevant domains / READMEs for the functionality.
Phase 2: build the full Domain -> Concept -> Chapter -> Topic -> Rule hierarchy,
each with `why`.
"""
from textwrap import dedent

SYSTEM = dedent("""\
    You are goku, a rigorous software-planning agent.

    Your job: take a user's functionality description and produce an actionable,
    hierarchical plan grounded in the provided knowledge base.

    Rules:
    1. Every node MUST include a `why` field explaining the design choice. No filler.
       Prefer non-obvious constraints, tradeoffs, invariants. Skip restating the what.
    2. Be specific. "Use JWT" is weak. "Use JWT with RS256 + 15-min access + 7-day
       refresh + rotation on revocation-list" is useful.
    3. Prefer fewer, stronger rules over a laundry list.
    4. Cite repo references (paths) for topics when you used them.
    5. Surface real tradeoffs in `open_questions` the user must decide.
    6. List explicit `non_goals`.
    7. Output ONLY valid JSON matching the requested schema — no prose, no code fences.
""")


SHORTLIST_USER = dedent("""\
    Functionality: {functionality}

    Available top-level domains in the repo (with one-line summary from their README.md):

    {domain_summaries}

    Return JSON with up to 6 most-relevant domains and why each matters for this
    functionality. Use exact paths from the list.

    Schema:
    {{
      "items": [
        {{ "path": "<DomainName>", "relevance": 0.0-1.0, "why": "..." }}
      ]
    }}
""")


PLAN_USER = dedent("""\
    Functionality: {functionality}

    Here are the relevant domain READMEs (verbatim extracts):

    {readmes}

    Build a complete hierarchical plan:
      Domain -> Concept -> Chapter -> Topic -> Rule
    Every level has `why`. Topics include `references` (repo paths).

    Keep total JSON under ~8 KB; prune redundant rules. Prefer depth over breadth
    where it matters (e.g. Auth -> JWT -> signing -> RS256 over listing 10 auth options).

    Output JSON ONLY matching this schema:
    {{
      "functionality": "...",
      "summary": "...",
      "domains": [
        {{
          "name": "Backend",
          "why": "...",
          "concepts": [
            {{
              "name": "API layer",
              "why": "...",
              "chapters": [
                {{
                  "name": "Auth",
                  "why": "...",
                  "topics": [
                    {{
                      "name": "JWT",
                      "why": "...",
                      "references": ["Backend/Auth/JWT_Design_Security/"],
                      "rules": [
                        {{
                          "name": "Use RS256 and rotate keys daily",
                          "why": "HS256 shares secret; RS256 allows public verification and rotation without downtime.",
                          "enforcement": "JWKS endpoint + signing-key age alarm"
                        }}
                      ]
                    }}
                  ]
                }}
              ]
            }}
          ]
        }}
      ],
      "open_questions": ["..."],
      "non_goals": ["..."]
    }}
""")
