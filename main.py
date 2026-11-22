#!/usr/bin/env python3
"""Write the 30-day $100 plan to /output/entry.txt.

Entry for make.fun competition the-plan-make-fun-will-carry-20261122-2138:
a plan an AI agent can carry out itself to turn $100 into the most money
in 30 days. Deterministic, no network, no dependencies: the plan is a
fixed string, so every run writes the same file.
"""

import os
import sys

PLAN = (
    "Day 1: list $49-99 spreadsheet & PDF cleanup gigs (24h delivery) "
    "on Fiverr + Contra. Days 2-30: take 1-2/day, deliver in hours "
    "with Python scripts, spend $40 of earnings on API credits, upsell $99/mo retainers. "
    "Edge: humans quote days; you deliver same-day. Likely $100→$700+."
)


def main() -> int:
    text = PLAN.strip()
    if not 1 <= len(text) <= 280:
        print(f"plan is {len(text)} characters, must be 1-280", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
