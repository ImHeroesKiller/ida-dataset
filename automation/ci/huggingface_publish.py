#!/usr/bin/env python3
"""CI entrypoint: publish IDA datasets to Hugging Face (non-blocking for manufacturing).

Prints full diagnostics. Default exit 0 so learning never fails on HF errors.
Use --fail-on-error only for dedicated smoke tests.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import traceback
from pathlib import Path

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

    print("=" * 72, flush=True)
    print("IDA → Hugging Face continuous publish", flush=True)
    print("=" * 72, flush=True)
    print(f"cwd={Path.cwd()}", flush=True)
    print(f"repo_root={ROOT}", flush=True)
    print(f"HF_TOKEN: {'Detected' if (os.environ.get('HF_TOKEN') or os.environ.get('HUGGINGFACE_TOKEN')) else 'Missing'}", flush=True)
    print(f"HF_DATASET_REPO: {os.environ.get('HF_DATASET_REPO') or '(default ariew/ida-dataset)'}", flush=True)
    print(f"GITHUB_REF_NAME: {os.environ.get('GITHUB_REF_NAME') or 'n/a'}", flush=True)
    print(f"GITHUB_SHA: {(os.environ.get('GITHUB_SHA') or 'n/a')[:12]}", flush=True)
    print(f"DRY_RUN env: {os.environ.get('DRY_RUN') or os.environ.get('IDA_LEARNING_DRY_RUN') or 'n/a'}", flush=True)
    print(f"args dry_run={args.dry_run} force_full={args.force_full} retries={args.retries}", flush=True)

    try:
        from automation.export.hf_publisher import publish_to_huggingface

        result = publish_to_huggingface(
            repo_root=ROOT,
            repo_id=args.repo,
            dry_run=args.dry_run,
            force_full=args.force_full,
            retries=max(1, int(args.retries)),
            gate={
                "commit_session": os.environ.get("IDA_COMMIT_SESSION", "n/a"),
                "dry_run": os.environ.get("IDA_LEARNING_DRY_RUN")
                or os.environ.get("DRY_RUN")
                or "n/a",
                "exit_code": os.environ.get("IDA_LEARN_EXIT_CODE", "n/a"),
            },
        )
    except Exception as exc:  # noqa: BLE001
        print("FATAL uncaught exception in HF publish:", flush=True)
        print(traceback.format_exc(), flush=True)
        result = {
            "ok": False,
            "executed": True,
            "skipped": False,
            "message": f"fatal:{type(exc).__name__}: {exc}",
            "errors": [str(exc)],
            "uploaded_count": 0,
        }

    # Compact + full JSON
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str), flush=True)

    status = "OK" if result.get("ok") else ("SKIP" if result.get("skipped") else "FAIL")
    print(
        f"HF_PUBLISH_STATUS={status} "
        f"executed={result.get('executed')} "
        f"version={result.get('version')} "
        f"uploaded={result.get('uploaded_count')} "
        f"datasets={(result.get('stats') or {}).get('total_datasets')} "
        f"rows={(result.get('stats') or {}).get('total_rows')} "
        f"repo={result.get('repo_id')} "
        f"hf_sha={result.get('hf_commit_sha')} "
        f"verify={(result.get('verification') or {}).get('ok')} "
        f"message={result.get('message')}",
        flush=True,
    )

    if args.fail_on_error and not result.get("ok") and not result.get("skipped"):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
