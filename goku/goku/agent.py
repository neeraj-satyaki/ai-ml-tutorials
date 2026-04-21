"""Thin wrapper around the Anthropic API that returns structured JSON."""
from __future__ import annotations
import json
import os
import time
from typing import Type, TypeVar

import anthropic
from pydantic import BaseModel, ValidationError

T = TypeVar("T", bound=BaseModel)

DEFAULT_MODEL = os.environ.get("GOKU_MODEL", "claude-opus-4-7")


class Agent:
    def __init__(self, model: str = DEFAULT_MODEL, max_tokens: int = 8000):
        self.client = anthropic.Anthropic()
        self.model = model
        self.max_tokens = max_tokens

    def call_json(
        self,
        system: str,
        user: str,
        schema_cls: Type[T],
        retries: int = 2,
    ) -> T:
        """Call Claude; parse response as JSON; validate against pydantic schema."""
        last_err: Exception | None = None
        for attempt in range(retries + 1):
            try:
                resp = self.client.messages.create(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    system=system,
                    messages=[{"role": "user", "content": user}],
                )
                text = "".join(b.text for b in resp.content if b.type == "text").strip()

                # strip accidental fences
                if text.startswith("```"):
                    text = text.split("```", 2)[1]
                    if text.startswith("json"):
                        text = text[4:].lstrip("\n")
                    text = text.rsplit("```", 1)[0].strip()

                data = json.loads(text)
                return schema_cls.model_validate(data)
            except (json.JSONDecodeError, ValidationError) as e:
                last_err = e
                if attempt < retries:
                    time.sleep(1.0 * (attempt + 1))
                    user = (
                        user
                        + f"\n\nPrior response was invalid: {e}. "
                        "Return ONLY valid JSON matching the schema."
                    )
                    continue
                raise
        raise RuntimeError(f"unreachable; last_err={last_err}")
