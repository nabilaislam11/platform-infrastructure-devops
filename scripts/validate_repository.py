#!/usr/bin/env python3
"""Validate local Markdown links, repository layout, and obvious sensitive patterns.

This is a heuristic safety check, not a guarantee that published material is safe.
Run from the repository root: python3 scripts/validate_repository.py
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = sorted(ROOT.rglob("*.md"))
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SENSITIVE = [
    ("private key header", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("AWS access key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    ("internal IPv4 address", re.compile(r"(?<![\d.])(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})(?![\d.])")),
]
errors = []
warnings = []
for path in MARKDOWN:
    body = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    for raw in LINK.findall(body):
        target = raw.strip().split(' "', 1)[0].strip("<>")
        if not target or target.startswith(("#", "mailto:")):
            continue
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        target_path = unquote(parsed.path)
        if not target_path:
            continue
        candidate = (path.parent / target_path).resolve()
        if not candidate.is_relative_to(ROOT.resolve()) or not candidate.exists():
            errors.append(f"{rel}: missing/unsafe relative link: {target}")
    for name, pattern in SENSITIVE:
        for match in pattern.finditer(body):
            # A pattern may appear in an educational explanation; review manually.
            warnings.append(f"{rel}: review potential {name} on line {body.count(chr(10), 0, match.start()) + 1}")

if not MARKDOWN:
    errors.append("No Markdown files found")
print(f"Checked {len(MARKDOWN)} Markdown files.")
for issue in errors:
    print("ERROR:", issue)
for issue in warnings:
    print("REVIEW:", issue)
if warnings:
    print("Sensitive-pattern matches require human review; they do not prove exposure.")
if errors:
    sys.exit(1)
print("Local Markdown path checks passed.")
