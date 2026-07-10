"""CLI: python -m automation.connectors ..."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from automation.connectors.manager import ConnectorManager  # noqa: E402
from automation.connectors.scheduler_bridge import SchedulerBridge  # noqa: E402
from automation.connectors.types import SearchQuery  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ida-ikn", description="IDA Knowledge Network CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list")
    sub.add_parser("health")
    sub.add_parser("dashboard")
    sub.add_parser("connect")

    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=5)
    s.add_argument("--acquire", action="store_true")

    r = sub.add_parser("request")
    r.add_argument("query")
    r.add_argument("--limit", type=int, default=5)
    r.add_argument("--mission-id", default=None)

    args = parser.parse_args(argv)
    mgr = ConnectorManager()

    if args.cmd == "list":
        print(json.dumps(mgr.list_connectors(), indent=2, ensure_ascii=False))
        return 0
    if args.cmd == "health":
        print(json.dumps(mgr.health_check_all(), indent=2, ensure_ascii=False))
        return 0
    if args.cmd == "dashboard":
        print(json.dumps(mgr.dashboard(), indent=2, ensure_ascii=False))
        return 0
    if args.cmd == "connect":
        print(json.dumps(mgr.connect_all(), indent=2, ensure_ascii=False))
        return 0
    if args.cmd == "search":
        q = SearchQuery(query=args.query, limit=args.limit, dry_run=True)
        results = mgr.search(q)
        docs = []
        if args.acquire:
            for res in results[: args.limit]:
                docs.append(mgr.acquire(res).to_dict())
        print(
            json.dumps(
                {"results": [r.to_dict() for r in results], "documents": docs},
                indent=2,
                ensure_ascii=False,
            )
        )
        return 0
    if args.cmd == "request":
        bridge = SchedulerBridge()
        out = bridge.request_documents(
            args.query,
            limit=args.limit,
            mission_id=args.mission_id,
            dry_run=True,
            acquire=True,
        )
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
