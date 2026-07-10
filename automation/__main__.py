"""Allow `python -m automation` to invoke the orchestrator CLI."""

from automation.orchestrator import main

raise SystemExit(main())
