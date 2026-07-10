#!/usr/bin/env python3
"""CLI for Continuous Learning Scheduler.

Examples:
  python -m automation.scheduler.cli tick --dry-run
  python -m automation.scheduler.cli mission "Learn everything about SAP ERP."
  python -m automation.scheduler.cli dashboard
  python -m automation.scheduler.cli complete MIS-...
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional, Sequence

# repo root on path
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from automation.scheduler.scheduler import ContinuousLearningScheduler  # noqa: E402


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ida-scheduler",
        description="IDA Continuous Learning Scheduler — single orchestration entry",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    tick = sub.add_parser("tick", help="Run one scheduler cycle")
    tick.add_argument("--dry-run", action="store_true", default=True)
    tick.add_argument("--no-dry-run", action="store_true")
    tick.add_argument("--root", type=Path, default=None)

    mis = sub.add_parser("mission", help="Create mission from natural language")
    mis.add_argument("text", help="Human instruction")
    mis.add_argument("--requester", default="human")
    mis.add_argument("--priority", default=None)
    mis.add_argument("--no-queue", action="store_true")
    mis.add_argument("--root", type=Path, default=None)

    q = sub.add_parser("queue-mission", help="Queue an existing mission id")
    q.add_argument("mission_id")
    q.add_argument("--root", type=Path, default=None)

    d = sub.add_parser("dashboard", help="Print learning dashboard JSON")
    d.add_argument("--root", type=Path, default=None)

    c = sub.add_parser("complete", help="Mark mission completed")
    c.add_argument("mission_id")
    c.add_argument("--result", default="")
    c.add_argument("--root", type=Path, default=None)

    g = sub.add_parser("growth-report", help="Write learning growth report")
    g.add_argument("--root", type=Path, default=None)

    ls = sub.add_parser("list-missions", help="List missions")
    ls.add_argument("--root", type=Path, default=None)

    args = parser.parse_args(argv)
    root = getattr(args, "root", None)
    sched = ContinuousLearningScheduler(repo_root=root)

    if args.command == "tick":
        dry = not args.no_dry_run
        out = sched.tick(dry_run=dry)
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0 if out.get("ok") else 1

    if args.command == "mission":
        out = sched.submit_mission_text(
            args.text,
            requester=args.requester,
            priority=args.priority,
            auto_queue=not args.no_queue,
        )
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0

    if args.command == "queue-mission":
        out = sched.queue_mission(args.mission_id)
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0

    if args.command == "dashboard":
        print(json.dumps(sched.dashboard(), indent=2, ensure_ascii=False))
        return 0

    if args.command == "complete":
        out = sched.complete_mission(args.mission_id, result=args.result)
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0

    if args.command == "growth-report":
        path = sched.write_growth_report()
        print(json.dumps({"report": str(path)}, indent=2))
        return 0

    if args.command == "list-missions":
        missions = [m.to_dict() for m in sched.missions.list_missions()]
        print(json.dumps({"missions": missions}, indent=2, ensure_ascii=False))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
