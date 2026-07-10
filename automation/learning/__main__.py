"""python -m automation.learning [first_cycle|live]

Default: live runtime session.
"""

from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"live", "live_runtime"}:
        from automation.learning.live_runtime import main as live_main

        return live_main(args[1:] if args and args[0] in {"live", "live_runtime"} else args)
    if args[0] in {"first", "first_cycle"}:
        from automation.learning.first_cycle import main as first_main

        return first_main(args[1:])
    # treat as live with custom instruction flag passthrough
    from automation.learning.live_runtime import main as live_main

    return live_main(args)


if __name__ == "__main__":
    raise SystemExit(main())
