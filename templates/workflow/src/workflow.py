"""Fail-closed starter workflow for synthetic public evidence."""

from __future__ import annotations

from collections.abc import Mapping


REQUIRED_FIELDS = ("case_id", "summary")


def process_case(case: Mapping[str, object]) -> dict[str, object]:
    """Route every starter case to a human without inventing a decision."""
    missing_fields = [field for field in REQUIRED_FIELDS if not case.get(field)]
    if missing_fields:
        return {
            "status": "needs_human",
            "reason": "missing required fields",
            "missing_fields": missing_fields,
        }
    return {
        "status": "needs_human",
        "reason": "starter has no evaluated automation",
    }
