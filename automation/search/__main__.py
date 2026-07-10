from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from automation.search.orchestrator import SearchOrchestrator  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="ida-search")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=5)
    p.add_argument("--no-acquire", action="store_true")
    args = p.parse_args(argv)
    orch = SearchOrchestrator()
    out = orch.execute(
        args.query, limit=args.limit, acquire=not args.no_acquire, dry_run=True
    )
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
