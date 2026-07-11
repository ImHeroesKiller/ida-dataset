#!/usr/bin/env python3
"""CI entrypoint: publish IDA datasets to Hugging Face (non-blocking).

Always exits 0 so manufacturing / learning sessions are never failed by HF errors.
Writes reports under reports/huggingface/ and prints a JSON summary.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Ensure repo root on path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish IDA datasets to Hugging Face Hub")
    parser.add_argument("--repo", default=None, help="HF dataset repo (default ariew/ida-dataset)")
    parser.add_argument("--dry-run", action="store_true", help="Build + plan only, no upload")
    parser.add_argument("--force-full", action="store_true", help="Re-upload all files")
    parser.add_argument("--retries", type=int, default=3, help="Upload attempts with backoff")
    parser.add_argument(
        "--fail-on-error",
        action="store_true",
        help="Exit non-zero on failure (default: always 0 for manufacturing safety)",
    )
    args = parser.parse_args()

    from automation.export.hf_publisher import publish_to_huggingface

    result = publish_to_huggingface(
        repo_root=ROOT,
        repo_id=args.repo,
        dry_run=args.dry_run,
        force_full=args.force_full,
        retries=max(1, int(args.retries)),
    )
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))

    # Explicit human-readable line for GHA logs
    status = "OK" if result.get("ok") else ("SKIP" if result.get("skipped") else "FAIL")
    print(
        f"HF_PUBLISH_STATUS={status} version={result.get('version')} "
        f"uploaded={result.get('uploaded_count')} repo={result.get('repo_id')} "
        f"message={result.get('message')}"
    )

    if args.fail_on_error and not result.get("ok") and not result.get("skipped"):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
