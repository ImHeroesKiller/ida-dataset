"""Discovery provider registry — data-driven, separate from trusted sources."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root
from automation.lib.simple_yaml import load_simple_yaml


def load_discovery_registry(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    path = root / "automation" / "config" / "discovery_registry.yaml"
    if not path.exists():
        return {"version": "0", "providers": [], "defaults": {}}
    data = load_simple_yaml(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        data = {}
    data["_repo_root"] = str(root)
    return data


def credentials_available(provider: dict[str, Any]) -> bool:
    """Return False when required env credentials are missing."""
    env_keys = provider.get("env_keys") or []
    api_type = str(provider.get("api_type") or "")
    # Free/toggle providers
    if api_type in {"rss", "atom", "sitemap", "opensearch", "trusted_site"}:
        if api_type == "rss" and os.environ.get("RSS_ENABLED", "1").strip() in {"0", "false", "no"}:
            return False
        if api_type == "atom" and os.environ.get("ATOM_ENABLED", "1").strip() in {"0", "false", "no"}:
            return False
        if api_type == "sitemap" and os.environ.get("SITEMAP_ENABLED", "1").strip() in {"0", "false", "no"}:
            return False
        return True
    if api_type == "commoncrawl":
        return os.environ.get("COMMONCRAWL_ENABLED", "").strip() in {"1", "true", "yes"}
    if not env_keys:
        return True
    # all listed keys must be non-empty
    for key in env_keys:
        if not os.environ.get(str(key), "").strip():
            return False
    return True


class DiscoveryRegistry:
    def __init__(self, repo_root: Path | None = None, config: dict[str, Any] | None = None):
        self.repo_root = repo_root or find_repo_root()
        self.config = config or load_discovery_registry(self.repo_root)
        self.defaults = dict(self.config.get("defaults") or {})

    def list_providers(self, *, enabled_only: bool = False, runnable_only: bool = False) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        for raw in self.config.get("providers") or []:
            if not isinstance(raw, dict):
                continue
            row = {**self.defaults, **raw}
            if enabled_only and not row.get("enabled", True):
                continue
            creds_ok = credentials_available(row)
            row["credentials_available"] = creds_ok
            row["status"] = "ready" if creds_ok and row.get("enabled", True) else (
                "disabled_no_credentials" if not creds_ok else "disabled"
            )
            row["health"] = "healthy" if creds_ok else "offline"
            if runnable_only and (not row.get("enabled", True) or not creds_ok):
                continue
            out.append(row)
        out.sort(key=lambda r: int(r.get("priority") or 0), reverse=True)
        return out

    def get(self, provider_id: str) -> Optional[dict[str, Any]]:
        for p in self.list_providers():
            if str(p.get("id")) == provider_id:
                return p
        return None
