"""Build blinded A/B pairs from evals/rewrite/ for judging.

    python evals/make_pairs.py

Reads the (name, old-file, new-file) table below, shuffles A/B per pair with a
fresh random key, writes evals/blind/<name>-pair.md (no version labels) and
evals/blind/key.json. Re-running re-blinds with a new key.
"""

import json
import random
import secrets
from pathlib import Path

ROOT = Path(__file__).parent
PAIRS = [
    ("essay", "essay_v310.md", "essay_v330.md"),
    ("howto", "howto_v310.md", "howto_v330.md"),
    ("email", "email_v310.md", "email_v330.md"),
]


def body(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].startswith("#"):
        lines = lines[1:]
    return "\n".join(lines).strip()


def main():
    out = ROOT / "blind"
    out.mkdir(exist_ok=True)
    key = {}
    for name, old, new in PAIRS:
        a, b = (old, new) if random.random() < 0.5 else (new, old)
        token = secrets.token_hex(4)
        (out / f"{name}-{token}.md").write_text(
            f"# Pair {token}: which is the better piece of writing?\n\n"
            f"## A\n\n{body(ROOT / 'rewrite' / a)}\n\n## B\n\n{body(ROOT / 'rewrite' / b)}\n",
            encoding="utf-8",
        )
        key[f"{name}-{token}"] = {"A": old, "B": new}
    (out / "key.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
    print(json.dumps(key, indent=2))


if __name__ == "__main__":
    main()
