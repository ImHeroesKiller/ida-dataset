#!/usr/bin/env python3
"""Lightweight Knowledge Ontology Engine (KOE) validator.

CSV-only checks:
  - duplicate entities / relationships
  - missing parents
  - orphan entities (warning)
  - invalid relationship types
  - cyclic parent hierarchy
  - invalid references
  - synonym/alias integrity
  - allowed/forbidden rule conflicts

Never modifies ontology or datasets.
Exit codes: 0 success | 1 validation | 2 config
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from automation.ci import EXIT_CONFIG_ERROR, EXIT_SUCCESS, EXIT_VALIDATION_ERROR  # noqa: E402


REQUIRED_FILES = [
    "entities.csv",
    "entity_types.csv",
    "entity_properties.csv",
    "entity_aliases.csv",
    "entity_synonyms.csv",
    "relationships.csv",
    "relationship_types.csv",
    "relationship_rules.csv",
    "domains.csv",
    "categories.csv",
    "ontology_version.json",
]


@dataclass
class Finding:
    severity: str
    category: str
    message: str


@dataclass
class Result:
    findings: list[Finding] = field(default_factory=list)

    def error(self, category: str, message: str) -> None:
        self.findings.append(Finding("error", category, message))

    def warning(self, category: str, message: str) -> None:
        self.findings.append(Finding("warning", category, message))

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "error"]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_ontology(ont_dir: Path, result: Result) -> dict[str, Any]:
    data: dict[str, Any] = {}
    for name in REQUIRED_FILES:
        path = ont_dir / name
        if not path.exists():
            result.error("config", f"Missing required ontology file: {name}")
            continue
        if name.endswith(".json"):
            try:
                data[name] = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                result.error("config", f"Invalid JSON in {name}: {exc}")
        else:
            try:
                data[name] = read_csv(path)
            except csv.Error as exc:
                result.error("csv", f"Invalid CSV {name}: {exc}")
    return data


def index_by(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        value = (row.get(key) or "").strip()
        if value:
            out[value] = row
    return out


def validate_entities(data: dict[str, Any], result: Result) -> None:
    entities = data.get("entities.csv") or []
    types = index_by(data.get("entity_types.csv") or [], "Entity Type ID")
    categories = index_by(data.get("categories.csv") or [], "Category ID")

    seen_ids: dict[str, int] = {}
    seen_names: dict[str, int] = {}
    by_id: dict[str, dict[str, str]] = {}
    by_name: dict[str, dict[str, str]] = {}

    for i, row in enumerate(entities, start=2):
        eid = (row.get("Entity ID") or "").strip()
        name = (row.get("Entity Name") or "").strip()
        if not eid:
            result.error("entity", f"entities.csv row {i}: missing Entity ID")
            continue
        if not name:
            result.error("entity", f"entities.csv row {i}: missing Entity Name for {eid}")
        if eid in seen_ids:
            result.error(
                "duplicate_entity",
                f"Duplicate Entity ID '{eid}' at rows {seen_ids[eid]} and {i}",
            )
        else:
            seen_ids[eid] = i
        if name:
            if name in seen_names:
                result.error(
                    "duplicate_entity",
                    f"Duplicate Entity Name '{name}' at rows {seen_names[name]} and {i}",
                )
            else:
                seen_names[name] = i
        by_id[eid] = row
        if name:
            by_name[name] = row

        type_id = (row.get("Entity Type ID") or "").strip()
        if type_id and type_id not in types:
            result.error(
                "invalid_reference",
                f"Entity {eid}: Entity Type ID '{type_id}' not found",
            )
        cat_id = (row.get("Category ID") or "").strip()
        if cat_id and cat_id not in categories:
            result.error(
                "invalid_reference",
                f"Entity {eid}: Category ID '{cat_id}' not found",
            )

    # Parent resolution + cycles
    for eid, row in by_id.items():
        parent_id = (row.get("Parent Entity ID") or "").strip()
        parent_name = (row.get("Parent Entity") or "").strip()
        if parent_name and not parent_id:
            # try resolve by name
            if parent_name not in by_name:
                result.error(
                    "missing_parent",
                    f"Entity {eid}: Parent Entity '{parent_name}' not found",
                )
            else:
                result.error(
                    "missing_parent",
                    f"Entity {eid}: Parent Entity set but Parent Entity ID empty",
                )
        if parent_id and parent_id not in by_id:
            result.error(
                "missing_parent",
                f"Entity {eid}: Parent Entity ID '{parent_id}' not found",
            )

    # Cycle detection via DFS
    graph: dict[str, Optional[str]] = {
        eid: (row.get("Parent Entity ID") or "").strip() or None for eid, row in by_id.items()
    }

    visiting: set[str] = set()
    visited: set[str] = set()

    def dfs(node: str, stack: list[str]) -> None:
        if node in visited:
            return
        if node in visiting:
            cycle_start = stack.index(node) if node in stack else 0
            cycle = " -> ".join(stack[cycle_start:] + [node])
            result.error("cyclic_parent", f"Cyclic parent hierarchy: {cycle}")
            return
        visiting.add(node)
        parent = graph.get(node)
        if parent:
            dfs(parent, stack + [node])
        visiting.remove(node)
        visited.add(node)

    for eid in graph:
        dfs(eid, [])

    data["_entity_by_id"] = by_id
    data["_entity_by_name"] = by_name


def validate_relationships(data: dict[str, Any], result: Result) -> None:
    rels = data.get("relationships.csv") or []
    rtypes = index_by(data.get("relationship_types.csv") or [], "Relationship Type ID")
    rtype_names = {
        (r.get("Relationship Type Name") or "").strip()
        for r in (data.get("relationship_types.csv") or [])
    }
    entities = data.get("_entity_by_id") or {}
    entities_by_name = data.get("_entity_by_name") or {}

    seen_triples: dict[tuple[str, str, str], int] = {}

    for i, row in enumerate(rels, start=2):
        rid = (row.get("Relationship ID") or "").strip()
        src = (row.get("Source Entity") or "").strip()
        rel = (row.get("Relationship") or "").strip()
        tgt = (row.get("Target Entity") or "").strip()
        src_id = (row.get("Source Entity ID") or "").strip()
        tgt_id = (row.get("Target Entity ID") or "").strip()
        rtype_id = (row.get("Relationship Type ID") or "").strip()

        if not rid:
            result.error("relationship", f"relationships.csv row {i}: missing Relationship ID")
        if rel not in rtype_names:
            result.error(
                "invalid_relationship_type",
                f"Relationship {rid or i}: '{rel}' not in relationship_types.csv",
            )
        if rtype_id and rtype_id not in rtypes:
            result.error(
                "invalid_reference",
                f"Relationship {rid or i}: Relationship Type ID '{rtype_id}' not found",
            )
        if src_id and src_id not in entities:
            result.error(
                "invalid_reference",
                f"Relationship {rid or i}: Source Entity ID '{src_id}' not found",
            )
        if tgt_id and tgt_id not in entities:
            result.error(
                "invalid_reference",
                f"Relationship {rid or i}: Target Entity ID '{tgt_id}' not found",
            )
        if src and src not in entities_by_name:
            result.error(
                "invalid_reference",
                f"Relationship {rid or i}: Source Entity '{src}' not found",
            )
        if tgt and tgt not in entities_by_name:
            result.error(
                "invalid_reference",
                f"Relationship {rid or i}: Target Entity '{tgt}' not found",
            )

        triple = (src, rel, tgt)
        if all(triple):
            if triple in seen_triples:
                result.error(
                    "duplicate_relationship",
                    f"Duplicate relationship {src} {rel} {tgt} "
                    f"at rows {seen_triples[triple]} and {i}",
                )
            else:
                seen_triples[triple] = i


def validate_rules(data: dict[str, Any], result: Result) -> None:
    rules = data.get("relationship_rules.csv") or []
    entities = data.get("_entity_by_id") or {}
    rtypes = index_by(data.get("relationship_types.csv") or [], "Relationship Type ID")
    rtype_names = {
        (r.get("Relationship Type Name") or "").strip()
        for r in (data.get("relationship_types.csv") or [])
    }

    constraints: dict[tuple[str, str, str], set[str]] = defaultdict(set)

    for i, row in enumerate(rules, start=2):
        src = (row.get("Source Entity") or "").strip()
        rel = (row.get("Relationship") or "").strip()
        tgt = (row.get("Target Entity") or "").strip()
        constraint = (row.get("Constraint") or "").strip()
        src_id = (row.get("Source Entity ID") or "").strip()
        tgt_id = (row.get("Target Entity ID") or "").strip()
        rtype_id = (row.get("Relationship Type ID") or "").strip()

        if constraint not in {"Allowed", "Forbidden"}:
            result.error(
                "rule",
                f"relationship_rules.csv row {i}: Constraint must be Allowed or Forbidden",
            )
        if rel and rel not in rtype_names:
            result.error(
                "invalid_relationship_type",
                f"Rule row {i}: relationship '{rel}' not in relationship_types.csv",
            )
        if src_id and src_id not in entities:
            result.error("invalid_reference", f"Rule row {i}: source id '{src_id}' missing")
        if tgt_id and tgt_id not in entities:
            result.error("invalid_reference", f"Rule row {i}: target id '{tgt_id}' missing")
        if rtype_id and rtype_id not in rtypes:
            result.error("invalid_reference", f"Rule row {i}: type id '{rtype_id}' missing")

        if src and rel and tgt and constraint:
            constraints[(src, rel, tgt)].add(constraint)

    for triple, flags in constraints.items():
        if "Allowed" in flags and "Forbidden" in flags:
            src, rel, tgt = triple
            result.error(
                "rule_conflict",
                f"Triple {src} {rel} {tgt} is both Allowed and Forbidden",
            )


def validate_properties(data: dict[str, Any], result: Result) -> None:
    props = data.get("entity_properties.csv") or []
    entities = data.get("_entity_by_id") or {}
    seen: dict[str, int] = {}
    for i, row in enumerate(props, start=2):
        pid = (row.get("Property ID") or "").strip()
        eid = (row.get("Entity ID") or "").strip()
        if pid:
            if pid in seen:
                result.error(
                    "duplicate",
                    f"Duplicate Property ID '{pid}' at rows {seen[pid]} and {i}",
                )
            else:
                seen[pid] = i
        if eid and eid not in entities:
            result.error(
                "invalid_reference",
                f"Property {pid or i}: Entity ID '{eid}' not found",
            )


def validate_synonyms_aliases(data: dict[str, Any], result: Result) -> None:
    entities = data.get("_entity_by_id") or {}
    synonyms = data.get("entity_synonyms.csv") or []
    aliases = data.get("entity_aliases.csv") or []

    syn_map: dict[str, str] = {}
    for i, row in enumerate(synonyms, start=2):
        syn = (row.get("Synonym") or "").strip()
        eid = (row.get("Canonical Entity ID") or "").strip()
        if not syn:
            result.error("synonym", f"entity_synonyms.csv row {i}: empty Synonym")
            continue
        if eid and eid not in entities:
            result.error(
                "invalid_reference",
                f"Synonym '{syn}': Canonical Entity ID '{eid}' not found",
            )
        key = syn.casefold()
        if key in syn_map and syn_map[key] != eid:
            result.error(
                "synonym",
                f"Synonym '{syn}' maps to multiple entities: {syn_map[key]} and {eid}",
            )
        else:
            syn_map[key] = eid

    for i, row in enumerate(aliases, start=2):
        alias = (row.get("Alias") or "").strip()
        eid = (row.get("Entity ID") or "").strip()
        if not alias:
            result.error("alias", f"entity_aliases.csv row {i}: empty Alias")
        if eid and eid not in entities:
            result.error(
                "invalid_reference",
                f"Alias '{alias}': Entity ID '{eid}' not found",
            )


def validate_orphans(data: dict[str, Any], result: Result) -> None:
    entities = data.get("_entity_by_id") or {}
    used: set[str] = set()

    for row in data.get("relationships.csv") or []:
        used.add((row.get("Source Entity ID") or "").strip())
        used.add((row.get("Target Entity ID") or "").strip())
    for row in data.get("entity_properties.csv") or []:
        used.add((row.get("Entity ID") or "").strip())
    for row in data.get("entity_synonyms.csv") or []:
        used.add((row.get("Canonical Entity ID") or "").strip())
    for row in data.get("entity_aliases.csv") or []:
        used.add((row.get("Entity ID") or "").strip())
    for row in data.get("relationship_rules.csv") or []:
        used.add((row.get("Source Entity ID") or "").strip())
        used.add((row.get("Target Entity ID") or "").strip())
    # parents count as usage for children, and children for parents
    for row in entities.values():
        parent = (row.get("Parent Entity ID") or "").strip()
        if parent:
            used.add(parent)
            used.add((row.get("Entity ID") or "").strip())

    used.discard("")
    for eid, row in entities.items():
        if eid not in used:
            result.warning(
                "orphan_entity",
                f"Entity {eid} ({row.get('Entity Name')}) is not referenced by "
                f"relationships, properties, synonyms, aliases, or parent links",
            )


def validate_version(data: dict[str, Any], result: Result) -> None:
    version = data.get("ontology_version.json")
    if not isinstance(version, dict):
        return
    for key in ("version", "created", "updated", "compatible_dataset_version", "compatible_kas_version"):
        if key not in version:
            result.warning("version", f"ontology_version.json missing key '{key}'")


def run_validation(ont_dir: Path) -> Result:
    result = Result()
    if not ont_dir.is_dir():
        result.error("config", f"Ontology directory not found: {ont_dir}")
        return result

    data = load_ontology(ont_dir, result)
    if result.errors:
        return result

    validate_entities(data, result)
    validate_relationships(data, result)
    validate_rules(data, result)
    validate_properties(data, result)
    validate_synonyms_aliases(data, result)
    validate_orphans(data, result)
    validate_version(data, result)
    return result


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Validate IDA Knowledge Ontology Engine CSVs")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Repository root (default: auto)",
    )
    parser.add_argument(
        "--ontology-dir",
        type=Path,
        default=None,
        help="Path to metadata/ontology (default: <repo>/metadata/ontology)",
    )
    args = parser.parse_args(argv)

    root = args.repo_root or _REPO
    ont_dir = args.ontology_dir or (root / "metadata" / "ontology")

    if not ont_dir.exists():
        print(f"CONFIG ERROR: ontology dir missing: {ont_dir}", file=sys.stderr)
        return EXIT_CONFIG_ERROR

    result = run_validation(ont_dir)

    errors = result.errors
    warnings = [f for f in result.findings if f.severity == "warning"]

    print("# Ontology Validation Report")
    print()
    print(f"- Ontology dir: `{ont_dir}`")
    print(f"- Errors: {len(errors)}")
    print(f"- Warnings: {len(warnings)}")
    print()

    if errors:
        print("## Errors")
        print()
        for f in errors:
            print(f"- **[{f.category}]** {f.message}")
        print()
    if warnings:
        print("## Warnings")
        print()
        for f in warnings:
            print(f"- **[{f.category}]** {f.message}")
        print()
    if not result.findings:
        print("All ontology checks passed.")
        print()

    if errors:
        return EXIT_VALIDATION_ERROR
    return EXIT_SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())
