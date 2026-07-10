"""Stage 6 — Duplicate Detection.

Flags candidates that collide with existing domain rows or with each other.
Duplicates are rejected into automation/queue/rejected/ when policy requires.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from automation.lib.io_utils import read_csv_rows, save_candidate, write_json
from automation.lib.models import PipelineStage, StageResult, ValidationStatus

if TYPE_CHECKING:
    from automation.lib.models import CandidateRecord, PipelineContext

STAGE = PipelineStage.DEDUPLICATE.value


def _normalize_name(name: str) -> str:
    return " ".join((name or "").lower().split())


def _existing_entity_keys(ctx: "PipelineContext", target_dataset: str) -> set[str]:
    """Build keys from production CSVs without modifying them."""
    domains = ctx.paths.domains_root
    keys: set[str] = set()
    for path in domains.glob(f"**/{target_dataset}.csv"):
        rows = read_csv_rows(path)
        for row in rows:
            # try common ID column patterns
            for col in row:
                if col.lower().endswith(" id") or col.lower().endswith("_id"):
                    value = (row.get(col) or "").strip()
                    if value:
                        keys.add(f"{target_dataset}:{value}".lower())
            # name-based soft key
            for name_col in ("Company Name", "Product Name", "Industry Name", "Name"):
                if name_col in row and row[name_col]:
                    keys.add(
                        f"{target_dataset}:name:{_normalize_name(row[name_col])}"
                    )
    return keys


def run(ctx: "PipelineContext") -> StageResult:
    paths = ctx.paths
    policies = ctx.config.get("policies", {})
    dedupe_cfg = policies.get("deduplication", {})
    reject_duplicates = bool(
        policies.get("validation", {}).get("reject_duplicates", True)
    )
    strategy = str(dedupe_cfg.get("strategy", "entity_key"))

    unique: list[Any] = []
    duplicates: list[Any] = []
    seen_in_batch: dict[str, str] = {}

    # Preload production keys per target dataset
    prod_keys_cache: dict[str, set[str]] = {}

    for candidate in ctx.candidates:
        candidate.touch(STAGE)
        target = candidate.target_dataset
        if target not in prod_keys_cache:
            prod_keys_cache[target] = _existing_entity_keys(ctx, target)

        entity_key = candidate.entity_key()
        name_key = f"{target}:name:{_normalize_name(candidate.canonical_name)}"

        duplicate_of = None
        if strategy in {"entity_key", "hybrid"}:
            if entity_key in seen_in_batch:
                duplicate_of = seen_in_batch[entity_key]
            elif entity_key in prod_keys_cache[target]:
                duplicate_of = f"production:{entity_key}"

        if strategy in {"fuzzy", "hybrid"} and not duplicate_of:
            if name_key in seen_in_batch:
                duplicate_of = seen_in_batch[name_key]
            elif name_key in prod_keys_cache[target]:
                duplicate_of = f"production:{name_key}"

        if duplicate_of:
            candidate.duplicate_of = duplicate_of
            candidate.rejection_reasons = list(
                set(candidate.rejection_reasons + ["duplicate_entity"])
            )
            candidate.provenance.validation_status = ValidationStatus.DUPLICATE.value
            duplicates.append(candidate)
            if reject_duplicates:
                save_candidate(paths.queue_rejected, candidate)
            continue

        seen_in_batch[entity_key] = candidate.candidate_id
        if candidate.canonical_name:
            seen_in_batch[name_key] = candidate.candidate_id
        unique.append(candidate)

    ctx.candidates = unique
    if ctx.report is not None:
        ctx.report.duplicates += len(duplicates)
        if reject_duplicates:
            ctx.report.rows_rejected += len(duplicates)

    artifact = paths.cache / f"{ctx.run_id}_deduplicate.json"
    write_json(
        artifact,
        {
            "run_id": ctx.run_id,
            "strategy": strategy,
            "unique": [c.candidate_id for c in unique],
            "duplicates": [
                {
                    "candidate_id": c.candidate_id,
                    "duplicate_of": c.duplicate_of,
                }
                for c in duplicates
            ],
        },
    )

    result = StageResult(
        stage=STAGE,
        success=True,
        message=f"Deduplicated: {len(unique)} unique, {len(duplicates)} duplicate(s)",
        input_count=len(unique) + len(duplicates),
        output_count=len(unique),
        rejected_count=len(duplicates) if reject_duplicates else 0,
        artifacts=[str(artifact)],
        details={"strategy": strategy},
    )
    ctx.add_stage_result(result)
    return result
