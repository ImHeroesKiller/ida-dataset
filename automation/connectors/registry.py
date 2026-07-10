"""Connector registry — config + CSV metadata."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from automation.lib.paths import find_repo_root
from automation.lib.simple_yaml import load_simple_yaml


def load_connectors_config(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    path = root / "automation" / "config" / "connectors.yaml"
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
    except ImportError:
        data = load_simple_yaml(text)
    if not isinstance(data, dict):
        raise ValueError("connectors.yaml must be a mapping")
    data["_repo_root"] = str(root)
    data["_config_path"] = str(path)
    return data


class ConnectorRegistry:
    def __init__(self, config: dict[str, Any]):
        self.config = config
        self.repo_root = Path(config["_repo_root"])
        self.defaults = dict(config.get("defaults") or {})
        paths = config.get("paths") or {}
        self.registry_csv = self.repo_root / paths.get(
            "registry", "metadata/connectors/registry.csv"
        )

    def list_configs(self, *, enabled_only: bool = False) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        for raw in self.config.get("connectors") or []:
            item = {**self.defaults, **dict(raw)}
            if enabled_only and not item.get("enabled"):
                continue
            rows.append(item)
        rows.sort(key=lambda r: int(r.get("priority") or 0), reverse=True)
        return rows

    def get(self, connector_id: str) -> dict[str, Any] | None:
        for item in self.list_configs():
            if item.get("connector_id") == connector_id:
                return item
        return None

    def read_registry_csv(self) -> list[dict[str, str]]:
        if not self.registry_csv.exists():
            return []
        with self.registry_csv.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))

    def approved_source_ids(self) -> set[str]:
        path = self.repo_root / (
            (self.config.get("paths") or {}).get(
                "source_registry", "metadata/source_registry.csv"
            )
        )
        if not path.exists():
            return set()
        allowed: set[str] = set()
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                flag = str(row.get("Allowed", "")).strip().lower()
                status = str(row.get("Status", "")).strip().lower()
                if flag in {"1", "true", "yes", "y"} and status in {
                    "active",
                    "enabled",
                    "",
                }:
                    sid = row.get("Source ID", "").strip()
                    if sid:
                        allowed.add(sid)
        # also allow connector-declared source ids that are active connectors
        for item in self.list_configs(enabled_only=True):
            sid = str(item.get("source_id") or "")
            if sid:
                allowed.add(sid)
        return allowed
