#!/usr/bin/env python3
"""Publish CI job.

Runs the KAS publisher (append-only), generates git diff + publish_report.md,
and optionally commits/pushes when environment policy allows and not dry-run.

Publishing is allowed only if:
  - policies.review_required == false, OR
  - approved candidates exist

Never overwrites datasets. Append only.

Exit codes:
  0 success
  2 config error
  3 policy violation
  4 publisher blocked
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from automation.ci import (  # noqa: E402
    EXIT_CONFIG_ERROR,
    EXIT_POLICY_VIOLATION,
    EXIT_PUBLISHER_BLOCKED,
    EXIT_SUCCESS,
)
from automation.ci.common import (  # noqa: E402
    RunContext,
    add_common_args,
    find_repo_root,
    load_environment_config,
    load_yaml_file,
    report_header,
    resolve_dry_run,
    resolve_environment,
    stamp,
    write_json_log,
    write_markdown_report,
)
from automation.lib.io_utils import (  # noqa: E402
    git_diff_stat,
    git_status_porcelain,
    load_candidates,
)
from automation.orchestrator import run_pipeline  # noqa: E402


def load_policies(root: Path, env_config: dict[str, Any]) -> dict[str, Any]:
    rel = env_config.get("paths", {}).get("policies", "automation/config/policies.yaml")
    path = root / rel
    if not path.exists():
        raise FileNotFoundError(f"Policies file not found: {path}")
    return load_yaml_file(path)


def git_run(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=str(root),
        capture_output=True,
        text=True,
        check=False,
    )


def build_report(
    ctx: RunContext,
    *,
    blocked_reason: Optional[str],
    approved_count: int,
    review_required: bool,
    published: bool,
    diff_stat: str,
    status: str,
    pipeline_run_id: Optional[str],
) -> str:
    lines = report_header(ctx, "Publish Report")
    lines += [
        "## Decision",
        "",
        f"- **Review required (policies):** `{review_required}`",
        f"- **Approved candidates:** `{approved_count}`",
        f"- **Published:** `{published}`",
        f"- **Blocked reason:** `{blocked_reason or '—'}`",
        f"- **Pipeline run id:** `{pipeline_run_id or '—'}`",
        f"- **Allow publish (environment):** `{ctx.env_config.get('allow_publish')}`",
        f"- **Allow commit:** `{ctx.env_config.get('allow_commit')}`",
        f"- **Allow push:** `{ctx.env_config.get('allow_push')}`",
        "",
        "## Git status (porcelain)",
        "",
        "```",
        status or "(clean)",
        "```",
        "",
        "## Git diff --stat",
        "",
        "```",
        diff_stat or "(no diff)",
        "```",
        "",
        "## Rules",
        "",
        "- Append only — never overwrite datasets",
        "- Preserve IDs",
        "- Dry-run performs no commits and no pushes",
        "",
    ]
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="IDA publish CI job")
    add_common_args(parser)
    parser.add_argument(
        "--commit",
        action="store_true",
        help="Commit changes after publish (ignored in dry-run)",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push commit after publish (ignored in dry-run)",
    )
    args = parser.parse_args(argv)

    try:
        environment = resolve_environment(args.environment)
    except ValueError as exc:
        print(f"CONFIG ERROR: {exc}", file=sys.stderr)
        return EXIT_CONFIG_ERROR

    root = find_repo_root(args.repo_root)
    try:
        env_config = load_environment_config(root, environment)
    except FileNotFoundError as exc:
        print(f"CONFIG ERROR: {exc}", file=sys.stderr)
        return EXIT_CONFIG_ERROR

    try:
        policies = load_policies(root, env_config)
    except FileNotFoundError as exc:
        print(f"CONFIG ERROR: {exc}", file=sys.stderr)
        return EXIT_CONFIG_ERROR

    dry_run = resolve_dry_run(args, env_config, default=True)
    ctx = RunContext(
        name="publish",
        repo_root=root,
        environment=environment,
        dry_run=dry_run,
        env_config=env_config,
    )

    review_required = bool(policies.get("review_required", True))
    paths = env_config.get("paths", {})
    approved_dir = root / paths.get("queue_approved", "automation/queue/approved")
    approved = load_candidates(approved_dir)
    approved_count = len(approved)

    # Gate: review_required == false OR approved candidates exist
    allowed_by_review_policy = (not review_required) or (approved_count > 0)
    if not allowed_by_review_policy:
        reason = "review_required_and_no_approved_candidates"
        ctx.errors.append(reason)
        ctx.metrics = {"approved_count": approved_count, "review_required": review_required}
        ctx.finish(EXIT_PUBLISHER_BLOCKED, "publisher_blocked")
        report_dir = root / paths.get("publish_reports", "reports/publish")
        ts = stamp()
        write_markdown_report(
            report_dir / "publish_report.md",
            build_report(
                ctx,
                blocked_reason=reason,
                approved_count=approved_count,
                review_required=review_required,
                published=False,
                diff_stat="",
                status="",
                pipeline_run_id=None,
            ),
            ctx,
        )
        write_json_log(report_dir / f"publish_{ts}.json", ctx)
        print(f"PUBLISHER BLOCKED: {reason}", file=sys.stderr)
        return EXIT_PUBLISHER_BLOCKED

    # Environment policy gates
    if not env_config.get("allow_publish", False) and not dry_run:
        reason = "environment_disallows_publish"
        ctx.errors.append(reason)
        ctx.finish(EXIT_POLICY_VIOLATION, "policy_violation")
        report_dir = root / paths.get("publish_reports", "reports/publish")
        ts = stamp()
        write_markdown_report(
            report_dir / "publish_report.md",
            build_report(
                ctx,
                blocked_reason=reason,
                approved_count=approved_count,
                review_required=review_required,
                published=False,
                diff_stat="",
                status="",
                pipeline_run_id=None,
            ),
            ctx,
        )
        write_json_log(report_dir / f"publish_{ts}.json", ctx)
        print(f"POLICY VIOLATION: {reason}", file=sys.stderr)
        return EXIT_POLICY_VIOLATION

    # Features gate from policies
    features = policies.get("features", {})
    if not features.get("publishing_enabled", False) and not dry_run:
        # allow dry-run simulation; real publish needs feature flag
        reason = "policies.features.publishing_enabled_is_false"
        ctx.errors.append(reason)
        ctx.finish(EXIT_PUBLISHER_BLOCKED, "publisher_blocked")
        report_dir = root / paths.get("publish_reports", "reports/publish")
        ts = stamp()
        write_markdown_report(
            report_dir / "publish_report.md",
            build_report(
                ctx,
                blocked_reason=reason,
                approved_count=approved_count,
                review_required=review_required,
                published=False,
                diff_stat="",
                status="",
                pipeline_run_id=None,
            ),
            ctx,
        )
        write_json_log(report_dir / f"publish_{ts}.json", ctx)
        print(f"PUBLISHER BLOCKED: {reason}", file=sys.stderr)
        return EXIT_PUBLISHER_BLOCKED

    # Run publisher stage via orchestrator
    # dry_run=True → publisher will not append rows
    # dry_run=False + publish=True → append if candidates pass gates
    pipeline_ctx = run_pipeline(
        profile="publish_only",
        dry_run=dry_run,
        publish=not dry_run,
        overrides={
            "publishing_enabled": True if not dry_run else False,
        },
        root=root,
    )

    diff_stat = git_diff_stat(root)
    status = git_status_porcelain(root)
    published = (not dry_run) and bool(
        pipeline_ctx.report and pipeline_ctx.report.updated_datasets
    )

    # Commit / push only when explicitly requested and allowed
    did_commit = False
    did_push = False
    if not dry_run and args.commit:
        if not env_config.get("allow_commit", False):
            ctx.warnings.append("commit_requested_but_environment_disallows_commit")
        else:
            pub_cfg = env_config.get("publisher", {})
            prefix = pub_cfg.get(
                "commit_message_prefix",
                "chore(data): publish approved knowledge rows",
            )
            git_run(root, ["add", "domains", "reports/publish", "automation/review"])
            commit = git_run(
                root,
                [
                    "commit",
                    "-m",
                    f"{prefix} [env={environment}]",
                ],
            )
            if commit.returncode == 0:
                did_commit = True
                ctx.messages.append("commit_created")
            else:
                # nothing to commit is not fatal
                ctx.messages.append(
                    f"commit_skipped: {(commit.stdout or commit.stderr or '').strip()}"
                )

            if args.push and did_commit:
                if not env_config.get("allow_push", False):
                    ctx.warnings.append("push_requested_but_environment_disallows_push")
                else:
                    push = git_run(root, ["push"])
                    if push.returncode == 0:
                        did_push = True
                        ctx.messages.append("push_ok")
                    else:
                        ctx.errors.append(
                            f"push_failed: {(push.stderr or push.stdout or '').strip()}"
                        )
                        ctx.finish(EXIT_POLICY_VIOLATION, "push_failed")
                        return EXIT_POLICY_VIOLATION

    if dry_run:
        ctx.messages.append("dry_run: no dataset writes, no commit, no push")

    ctx.metrics = {
        "approved_count": approved_count,
        "review_required": review_required,
        "published": published,
        "did_commit": did_commit,
        "did_push": did_push,
        "pipeline_run_id": pipeline_ctx.run_id,
        "updated_datasets": (
            list(pipeline_ctx.report.updated_datasets)
            if pipeline_ctx.report
            else []
        ),
    }
    ctx.finish(EXIT_SUCCESS)

    report_dir = root / paths.get("publish_reports", "reports/publish")
    ts = stamp()
    write_markdown_report(
        report_dir / "publish_report.md",
        build_report(
            ctx,
            blocked_reason=None,
            approved_count=approved_count,
            review_required=review_required,
            published=published,
            diff_stat=diff_stat,
            status=status,
            pipeline_run_id=pipeline_ctx.run_id,
        ),
        ctx,
    )
    write_json_log(
        report_dir / f"publish_{ts}.json",
        ctx,
        extra={"diff_stat": diff_stat, "git_status": status},
    )

    print(
        f"Publish job complete dry_run={dry_run} published={published} "
        f"approved={approved_count}"
    )
    return EXIT_SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())
