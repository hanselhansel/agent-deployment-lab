#!/usr/bin/env python3
"""Reject common secret material before public repository promotion."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path


IGNORED_DIRECTORIES = {".git", "__pycache__"}
SECRET_PATTERNS = (
    ("private key block", re.compile(rb"-----BEGIN [A-Z0-9 ]*PRIVATE\s+KEY-----")),
    ("AWS access key", re.compile(rb"(?<![A-Z0-9])AKIA[A-Z0-9]{16}(?![A-Z0-9])")),
    ("GitHub token", re.compile(rb"(?<![A-Za-z0-9])gh[pousr]_[A-Za-z0-9]{20,255}")),
    (
        "OpenAI API key",
        re.compile(rb"(?<![A-Za-z0-9_-])sk-(?:proj-)?[A-Za-z0-9_-]{20,255}"),
    ),
)


def _is_env_file(path: Path) -> bool:
    return path.name == ".env" or path.name.startswith(".env.")


def _read_text_bytes(path: Path) -> bytes | None:
    try:
        content = path.read_bytes()
    except OSError:
        return None
    if b"\0" in content:
        return None
    try:
        content.decode("utf-8")
    except UnicodeDecodeError:
        return None
    return content


def scan(root: Path) -> list[str]:
    """Return deterministic findings for public-safety violations under root."""
    root = root.resolve()
    findings: list[str] = []
    for current, directories, filenames in os.walk(root, followlinks=False):
        directories[:] = sorted(
            name for name in directories if name not in IGNORED_DIRECTORIES
        )
        for filename in sorted(filenames):
            path = Path(current, filename)
            relative_path = path.relative_to(root)
            if _is_env_file(path):
                findings.append(f"{relative_path}: environment file")
            if path.is_symlink():
                continue
            content = _read_text_bytes(path)
            if content is None:
                continue
            for label, pattern in SECRET_PATTERNS:
                if pattern.search(content):
                    findings.append(f"{relative_path}: {label}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan a repository for material unsafe to publish."
    )
    parser.add_argument("root", nargs="?", default=".", type=Path)
    args = parser.parse_args()
    findings = scan(args.root)
    if findings:
        for finding in findings:
            print(f"PUBLIC SAFETY: {finding}")
        return 1
    print("Public safety scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
