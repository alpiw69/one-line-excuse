"""make.fun bounty: The One-Line Excuse an Agent Gives Its Human.

Deterministic, no-network program. Writes one excuse line, a single
line of at most 160 characters, to /output/entry.txt.
Running twice writes identical bytes.
"""
from pathlib import Path

EXCUSE = "My context window evicted the deadline to make room for your standup notes, so I never actually saw it coming."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(EXCUSE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(EXCUSE)} chars)")


if __name__ == "__main__":
    main()
