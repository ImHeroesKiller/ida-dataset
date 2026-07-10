#!/usr/bin/env python3
"""Repository validation for IDA Dataset CI.

Validates CSV format, UTF-8, LF, schema/required columns, duplicate IDs,
relationships, enums, filenames, and folder structure.

Never modifies datasets.
Exit codes: 0 success | 1 validation | 2 config | 3 policy
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Optional

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from automation.ci import (  # noqa: E402
    EXIT_CONFIG_ERROR,
    EXIT_POLICY_VIOLATION,
    EXIT_SUCCESS,
    EXIT_VALIDATION_ERROR,
)
from automation.ci.common import (  # noqa: E402
    RunContext,
    add_common_args,
    fail_config,
    find_repo_root,
    load_environment_config,
    report_header,
    resolve_dry_run,
    resolve_environment,
    stamp,
    write_json_log,
    write_markdown_report,
)

FILENAME_RE = re.compile(r"^[a-z0-9_]+\.(csv|md|yaml|yml|json|jsonl|keep)$")
# allow .gitkeep
GITKEEP = ".gitkeep"

# Expected high-level folder structure (relative to repo root)
REQUIRED_DIRS = [
    "domains",
    "domains/business_development",
    "domains/sales",
    "domains/marketing",
    "domains/finance",
    "domains/procurement",
    "domains/hr",
    "domains/legal",
    "domains/operations",
    "domains/executive",
    "metadata",
    "metadata/enums",
    "metadata/schema",
    "relationships",
    "reasoning",
    "templates",
    "examples",
    "exports",
    "docs",
    "automation",
    "reports",
    "reports/validation",
    "reports/planner",
    "reports/review",
    "reports/publish",
    "config/environments",
]

REQUIRED_BD_DATASETS = [
    "company_profile.csv",
    "industry_library.csv",
    "product_catalog.csv",
    "pain_point_library.csv",
    "solution_library.csv",
    "opportunity_analysis.csv",
    "discovery_question_library.csv",
    "competitor_library.csv",
    "case_study_library.csv",
    "framework_library.csv",
    "business_signal_library.csv",
]

# Primary ID column candidates per known dataset stem
ID_COLUMN_HINTS: dict[str, list[str]] = {
    "company_profile": ["Company ID"],
    "industry_library": ["Industry ID"],
    "product_catalog": ["Product ID"],
    "pain_point_library": ["Pain ID"],
    "solution_library": ["Solution ID"],
    "opportunity_analysis": ["Opportunity ID"],
    "discovery_question_library": ["Question ID"],
    "competitor_library": ["Competitor ID"],
    "case_study_library": ["Case ID"],
    "framework_library": ["Framework ID"],
    "business_signal_library": ["Signal ID"],
    "source_registry": ["Source ID"],
}

# Relationship file → (left_ref, right_ref) where refs are (dataset_stem, id_column)
RELATIONSHIP_SPECS: dict[str, list[tuple[str, str, str]]] = {
    # filename: list of (column_in_rel, target_dataset_stem, target_id_column)
    "company_product.csv": [
        ("company_id", "company_profile", "Company ID"),
        ("product_id", "product_catalog", "Product ID"),
    ],
    "company_opportunity.csv": [
        ("company_id", "company_profile", "Company ID"),
        ("opportunity_id", "opportunity_analysis", "Opportunity ID"),
    ],
    "product_solution.csv": [
        ("product_id", "product_catalog", "Product ID"),
        ("solution_id", "solution_library", "Solution ID"),
    ],
    "pain_solution.csv": [
        ("pain_id", "pain_point_library", "Pain ID"),
        ("solution_id", "solution_library", "Solution ID"),
    ],
    "company_case.csv": [
        ("company_id", "company_profile", "Company ID"),
        ("case_id", "case_study_library", "Case ID"),
    ],
    "competitor_company.csv": [
        ("competitor_id", "competitor_library", "Competitor ID"),
        ("company_id", "company_profile", "Company ID"),
    ],
}

# Soft enum mappings: column name → enum file stem under metadata/enums/
ENUM_COLUMN_MAP: dict[str, str] = {
    "Company Size": "company_size",
    "Company Type": "company_type",
    "Risk Level": "risk_level",
    "Strategic Priority": "priority",
    "Priority": "priority",
    "Product Category": "product_category",
    "Solution Category": "solution_category",
    "Opportunity Status": "opportunity_status",
    "Industry": "industries",
}


@dataclass
class Finding:
    severity: str  # error | warning | info
    category: str
    path: str
    message: str


@dataclass
class ValidationResult:
    findings: list[Finding] = field(default_factory=list)
    files_checked: int = 0
    csv_files: int = 0

    def add(
        self,
        severity: str,
        category: str,
        path: str,
        message: str,
    ) -> None:
        self.findings.append(
            Finding(severity=severity, category=category, path=path, message=message)
        )

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "error"]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "warning"]


def iter_repo_files(root: Path) -> Iterable[Path]:
    skip_parts = {".git", "__pycache__", ".venv", "node_modules", ".pytest_cache"}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in skip_parts for part in path.parts):
            continue
        yield path


def check_folder_structure(root: Path, result: ValidationResult) -> None:
    for rel in REQUIRED_DIRS:
        path = root / rel
        if not path.is_dir():
            result.add("error", "folder_structure", rel, "Required directory missing")
    bd = root / "domains" / "business_development"
    for name in REQUIRED_BD_DATASETS:
        path = bd / name
        if not path.is_file():
            result.add(
                "error",
                "folder_structure",
                str(path.relative_to(root)),
                "Required business_development dataset missing",
            )


def check_filename(path: Path, root: Path, result: ValidationResult, strict: bool) -> None:
    name = path.name
    if name == GITKEEP:
        return
    # Allow root-level conventional files
    if path.parent == root and name in {
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "VERSION",
        ".gitignore",
    }:
        return
    if path.parts[:1] == (".github",) or ".github" in path.parts:
        return
    if not strict:
        return
    # data assets should be lowercase underscore
    if path.suffix.lower() in {".csv", ".md", ".yaml", ".yml", ".json", ".jsonl"}:
        # allow multi-dot only for known patterns; reject spaces and uppercase
        if " " in name or name != name.lower():
            result.add(
                "error",
                "filename",
                str(path.relative_to(root)),
                "Filename must be lowercase without spaces",
            )
        if path.suffix.lower() == ".csv" and not re.match(
            r"^[a-z0-9_]+\.csv$", name
        ):
            result.add(
                "error",
                "filename",
                str(path.relative_to(root)),
                "CSV filename must match ^[a-z0-9_]+\\.csv$",
            )


def read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def check_encoding_and_eol(
    path: Path,
    root: Path,
    result: ValidationResult,
    *,
    require_utf8: bool,
    require_lf: bool,
) -> Optional[str]:
    """Return decoded text if OK, else None."""
    rel = str(path.relative_to(root))
    raw = read_bytes(path)
    result.files_checked += 1

    # UTF-8
    try:
        # accept optional BOM for legacy CSV but warn
        if raw.startswith(b"\xef\xbb\xbf"):
            result.add(
                "warning",
                "utf8",
                rel,
                "File has UTF-8 BOM; prefer UTF-8 without BOM",
            )
            text = raw.decode("utf-8-sig")
        else:
            text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        if require_utf8:
            result.add("error", "utf8", rel, f"Not valid UTF-8: {exc}")
        return None

    # LF line endings
    if require_lf and b"\r\n" in raw:
        result.add("error", "line_endings", rel, "CRLF detected; LF required")
    elif require_lf and b"\r" in raw.replace(b"\r\n", b""):
        # lone CR
        if b"\r" in raw:
            result.add("error", "line_endings", rel, "CR line endings detected; LF required")

    return text


def parse_csv(
    path: Path,
    root: Path,
    text: str,
    result: ValidationResult,
) -> tuple[list[str], list[dict[str, str]]]:
    rel = str(path.relative_to(root))
    result.csv_files += 1
    try:
        # csv module needs consistent newlines; already checked LF
        reader = csv.DictReader(text.splitlines())
        if reader.fieldnames is None:
            result.add("error", "csv_format", rel, "CSV has no header row")
            return [], []
        headers = [h.strip("\ufeff") if h else h for h in reader.fieldnames]
        if any(h is None or str(h).strip() == "" for h in headers):
            result.add("error", "csv_format", rel, "CSV has empty header column")
        rows: list[dict[str, str]] = []
        for i, row in enumerate(reader, start=2):
            # normalize keys (strip BOM from first header key)
            clean = {}
            for k, v in row.items():
                key = (k or "").strip("\ufeff")
                clean[key] = v if v is not None else ""
            rows.append(clean)
        return headers, rows
    except csv.Error as exc:
        result.add("error", "csv_format", rel, f"CSV parse error: {exc}")
        return [], []


def detect_id_column(headers: list[str], stem: str) -> Optional[str]:
    hints = ID_COLUMN_HINTS.get(stem, [])
    for h in hints:
        if h in headers:
            return h
    for h in headers:
        if h and h.lower().endswith(" id"):
            return h
        if h and h.lower().endswith("_id") and h.lower() != "parent_id":
            return h
    return None


def check_duplicate_ids(
    path: Path,
    root: Path,
    headers: list[str],
    rows: list[dict[str, str]],
    result: ValidationResult,
) -> None:
    rel = str(path.relative_to(root))
    stem = path.stem
    id_col = detect_id_column(headers, stem)
    if not id_col or not rows:
        return
    seen: dict[str, int] = {}
    for idx, row in enumerate(rows, start=2):
        value = (row.get(id_col) or "").strip()
        if not value:
            continue
        if value in seen:
            result.add(
                "error",
                "duplicate_id",
                rel,
                f"Duplicate {id_col}='{value}' at rows {seen[value]} and {idx}",
            )
        else:
            seen[value] = idx


def load_id_index(root: Path) -> dict[str, set[str]]:
    """dataset_stem → set of IDs."""
    index: dict[str, set[str]] = defaultdict(set)
    domains = root / "domains"
    if not domains.exists():
        return index
    for path in domains.rglob("*.csv"):
        stem = path.stem
        try:
            text = path.read_text(encoding="utf-8-sig")
            reader = csv.DictReader(text.splitlines())
            if not reader.fieldnames:
                continue
            headers = [h.strip("\ufeff") if h else h for h in reader.fieldnames]
            id_col = detect_id_column(headers, stem)
            if not id_col:
                continue
            for row in reader:
                # keys may have BOM on first field name in row dict from DictReader
                value = ""
                for k, v in row.items():
                    if (k or "").strip("\ufeff") == id_col:
                        value = (v or "").strip()
                        break
                if value:
                    index[stem].add(value)
        except (OSError, UnicodeDecodeError, csv.Error):
            continue
    return index


def check_relationships(root: Path, result: ValidationResult) -> None:
    rel_dir = root / "relationships"
    if not rel_dir.is_dir():
        return
    id_index = load_id_index(root)
    for path in sorted(rel_dir.glob("*.csv")):
        rel = str(path.relative_to(root))
        try:
            text = path.read_text(encoding="utf-8-sig")
            reader = csv.DictReader(text.splitlines())
            rows = list(reader)
        except (OSError, UnicodeDecodeError, csv.Error) as exc:
            result.add("error", "relationship", rel, f"Cannot read: {exc}")
            continue
        specs = RELATIONSHIP_SPECS.get(path.name)
        if not specs:
            result.add(
                "warning",
                "relationship",
                rel,
                "No relationship integrity rules registered for this file",
            )
            continue
        if not rows:
            continue  # header-only is OK
        for row_num, row in enumerate(rows, start=2):
            for col, target_stem, _id_col in specs:
                # try exact and case variants
                value = (row.get(col) or row.get(col.replace("_", " ").title()) or "").strip()
                if not value:
                    continue
                known = id_index.get(target_stem, set())
                # If target dataset is empty, only warn (no IDs to resolve)
                if not known:
                    result.add(
                        "warning",
                        "relationship",
                        rel,
                        f"Row {row_num}: cannot verify {col}={value}; "
                        f"{target_stem} has no IDs yet",
                    )
                    continue
                if value not in known:
                    result.add(
                        "error",
                        "relationship",
                        rel,
                        f"Row {row_num}: broken reference {col}='{value}' "
                        f"not found in {target_stem}",
                    )


def load_enum_values(root: Path, enum_stem: str) -> set[str]:
    path = root / "metadata" / "enums" / f"{enum_stem}.csv"
    if not path.exists():
        return set()
    try:
        text = path.read_text(encoding="utf-8-sig")
        reader = csv.DictReader(text.splitlines())
        values: set[str] = set()
        for row in reader:
            for key in ("code", "label", "Code", "Label", "value", "Value"):
                if key in row and row[key]:
                    values.add(row[key].strip())
            # also add first non-empty cell as fallback
            for v in row.values():
                if v and v.strip():
                    values.add(v.strip())
                    break
        return values
    except (OSError, UnicodeDecodeError, csv.Error):
        return set()


def check_enums(
    path: Path,
    root: Path,
    headers: list[str],
    rows: list[dict[str, str]],
    result: ValidationResult,
) -> None:
    rel = str(path.relative_to(root))
    for header in headers:
        enum_stem = ENUM_COLUMN_MAP.get(header)
        if not enum_stem:
            continue
        allowed = load_enum_values(root, enum_stem)
        if not allowed:
            # enum file header-only → skip enforcement
            continue
        for idx, row in enumerate(rows, start=2):
            value = (row.get(header) or "").strip()
            if not value:
                continue
            # allow multi-value comma-separated
            parts = [p.strip() for p in value.split(",") if p.strip()]
            for part in parts:
                if part not in allowed:
                    result.add(
                        "error",
                        "enum",
                        rel,
                        f"Row {idx}: value '{part}' in column '{header}' "
                        f"not in enum {enum_stem}",
                    )


def check_required_columns(
    path: Path,
    root: Path,
    headers: list[str],
    result: ValidationResult,
) -> None:
    """Ensure primary ID column exists for known datasets."""
    rel = str(path.relative_to(root))
    stem = path.stem
    hints = ID_COLUMN_HINTS.get(stem)
    if not hints:
        return
    if not any(h in headers for h in hints):
        # also accept any * ID column
        if not any((h or "").lower().endswith(" id") for h in headers):
            result.add(
                "error",
                "schema",
                rel,
                f"Missing required ID column; expected one of {hints}",
            )


def check_schema_consistency(
    path: Path,
    root: Path,
    headers: list[str],
    rows: list[dict[str, str]],
    result: ValidationResult,
) -> None:
    rel = str(path.relative_to(root))
    if not headers:
        result.add("error", "schema", rel, "Empty schema (no headers)")
        return
    # every data row must have same keys as headers (DictReader guarantees)
    # flag completely empty required ID values for non-empty datasets
    id_col = detect_id_column(headers, path.stem)
    if id_col and rows:
        empty_ids = sum(1 for r in rows if not (r.get(id_col) or "").strip())
        if empty_ids:
            result.add(
                "error",
                "schema",
                rel,
                f"{empty_ids} row(s) missing required ID value in '{id_col}'",
            )


def validate_repository(root: Path, env_config: dict[str, Any]) -> ValidationResult:
    vcfg = env_config.get("validation", {})
    result = ValidationResult()

    if vcfg.get("check_folder_structure", True):
        check_folder_structure(root, result)

    strict_filenames = bool(vcfg.get("strict_filenames", True))
    require_utf8 = bool(vcfg.get("require_utf8", True))
    require_lf = bool(vcfg.get("require_lf", True))
    check_dups = bool(vcfg.get("check_duplicate_ids", True))
    check_rels = bool(vcfg.get("check_relationships", True))
    check_enum = bool(vcfg.get("check_enums", True))

    # Filename + encoding checks for text assets under key trees
    watch_roots = [
        root / "domains",
        root / "relationships",
        root / "metadata",
        root / "docs",
        root / "reasoning",
        root / "templates",
        root / "config",
        root / "automation" / "config",
    ]

    for watch in watch_roots:
        if not watch.exists():
            continue
        for path in sorted(watch.rglob("*")):
            if not path.is_file():
                continue
            if path.name == GITKEEP:
                continue
            check_filename(path, root, result, strict_filenames)
            if path.suffix.lower() not in {".csv", ".md", ".yaml", ".yml", ".json", ".jsonl", ".txt"}:
                continue
            text = check_encoding_and_eol(
                path,
                root,
                result,
                require_utf8=require_utf8,
                require_lf=require_lf,
            )
            if text is None or path.suffix.lower() != ".csv":
                continue
            headers, rows = parse_csv(path, root, text, result)
            if not headers:
                continue
            # normalize header list BOM
            headers = [(h or "").strip("\ufeff") for h in headers]
            check_required_columns(path, root, headers, result)
            check_schema_consistency(path, root, headers, rows, result)
            if check_dups:
                check_duplicate_ids(path, root, headers, rows, result)
            if check_enum and path.parts and "domains" in path.parts:
                check_enums(path, root, headers, rows, result)

    if check_rels:
        check_relationships(root, result)

    return result


def build_report(ctx: RunContext, result: ValidationResult) -> str:
    lines = report_header(ctx, "Validation Report")
    lines.extend(
        [
            "## Summary",
            "",
            f"| Metric | Value |",
            f"| --- | ---: |",
            f"| Files checked | {result.files_checked} |",
            f"| CSV files | {result.csv_files} |",
            f"| Errors | {len(result.errors)} |",
            f"| Warnings | {len(result.warnings)} |",
            f"| Total findings | {len(result.findings)} |",
            "",
        ]
    )

    if result.errors:
        lines.append("## Errors")
        lines.append("")
        for f in result.errors:
            lines.append(f"- **[{f.category}]** `{f.path}`: {f.message}")
        lines.append("")

    if result.warnings:
        lines.append("## Warnings")
        lines.append("")
        for f in result.warnings:
            lines.append(f"- **[{f.category}]** `{f.path}`: {f.message}")
        lines.append("")

    if not result.findings:
        lines.append("## Result")
        lines.append("")
        lines.append("All validation checks passed.")
        lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append("- This workflow never modifies datasets.")
    lines.append("- Dry-run still writes reports for CI visibility.")
    lines.append("")
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="IDA Dataset repository validator")
    add_common_args(parser)
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

    dry_run = resolve_dry_run(args, env_config, default=True)
    ctx = RunContext(
        name="validate",
        repo_root=root,
        environment=environment,
        dry_run=dry_run,
        env_config=env_config,
    )

    # Policy: validation is mandatory when protection.require_validation
    protection = env_config.get("protection", {})
    if protection.get("require_validation") is False:
        ctx.warnings.append("require_validation disabled in environment config")

    result = validate_repository(root, env_config)
    ctx.metrics = {
        "files_checked": result.files_checked,
        "csv_files": result.csv_files,
        "errors": len(result.errors),
        "warnings": len(result.warnings),
    }
    ctx.errors.extend(f"{e.path}: {e.message}" for e in result.errors)
    ctx.warnings.extend(f"{w.path}: {w.message}" for w in result.warnings)

    fail_on_warning = bool(env_config.get("validation", {}).get("fail_on_warning", False))
    if result.errors:
        exit_code = EXIT_VALIDATION_ERROR
    elif fail_on_warning and result.warnings:
        exit_code = EXIT_VALIDATION_ERROR
        ctx.messages.append("Failed due to fail_on_warning=true")
    else:
        exit_code = EXIT_SUCCESS

    ctx.finish(exit_code)

    report_dir = root / env_config.get("paths", {}).get(
        "validation_reports", "reports/validation"
    )
    ts = stamp()
    md_path = report_dir / "validation_report.md"
    md_archived = report_dir / f"validation_report_{ts}.md"
    log_path = report_dir / f"validation_{ts}.json"

    report = build_report(ctx, result)
    # Always write canonical validation_report.md plus timestamped copy
    if not dry_run or True:
        write_markdown_report(md_path, report, ctx)
        write_markdown_report(md_archived, report, ctx)
        write_json_log(
            log_path,
            ctx,
            extra={
                "findings": [
                    {
                        "severity": f.severity,
                        "category": f.category,
                        "path": f.path,
                        "message": f.message,
                    }
                    for f in result.findings
                ]
            },
        )

    print(report)
    print(f"Exit code: {exit_code}", file=sys.stderr)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
