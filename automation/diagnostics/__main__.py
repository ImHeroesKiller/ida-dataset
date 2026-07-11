"""CLI: python -m automation.diagnostics

Observe-only. Rebuilds reports/diagnostics from last production evidence.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from automation.diagnostics.reports import write_diagnostics_bundle  # noqa: E402


def main() -> int:
    written = write_diagnostics_bundle()
    print(json.dumps({"ok": True, "written": written}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
