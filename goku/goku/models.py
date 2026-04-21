"""Typed hierarchy: Domain -> Concept -> Chapter -> Topic -> Rule.

Every node carries `why` (design rationale). Used by planner for structured output
and by writer for deterministic markdown rendering.
"""
from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class Rule(BaseModel):
    name: str = Field(..., description="Short imperative name, e.g. 'Use RS256 signing'")
    why: str = Field(..., description="Rationale. Non-obvious constraint, invariant, or tradeoff.")
    enforcement: Optional[str] = Field(
        None,
        description="How to enforce (lint rule, test, config, policy).",
    )


class Topic(BaseModel):
    name: str
    why: str
    rules: List[Rule] = Field(default_factory=list)
    references: List[str] = Field(
        default_factory=list,
        description="Repo paths consulted (e.g. 'Backend/Auth/JWT_Design_Security/').",
    )


class Chapter(BaseModel):
    name: str
    why: str
    topics: List[Topic] = Field(default_factory=list)


class Concept(BaseModel):
    name: str
    why: str
    chapters: List[Chapter] = Field(default_factory=list)


class Domain(BaseModel):
    name: str = Field(..., description="Top-level area, e.g. 'Backend'")
    why: str = Field(..., description="Why this domain is relevant to the functionality")
    concepts: List[Concept] = Field(default_factory=list)


class Plan(BaseModel):
    functionality: str = Field(..., description="The requested functionality")
    summary: str = Field(..., description="One-paragraph plain-English summary of the plan")
    domains: List[Domain] = Field(default_factory=list)
    open_questions: List[str] = Field(default_factory=list)
    non_goals: List[str] = Field(default_factory=list)


class ShortlistItem(BaseModel):
    path: str = Field(..., description="Repo relative path to a README or folder")
    relevance: float = Field(..., ge=0.0, le=1.0)
    why: str


class Shortlist(BaseModel):
    items: List[ShortlistItem]
