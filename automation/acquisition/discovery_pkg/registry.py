"""Discovery provider registry — data-driven, separate from trusted sources.

Operational status (never silent):
  ACTIVE        — enabled + credentials/config ready
  DISABLED      — enabled=false in registry
  MISCONFIGURED — enabled but required credentials missing
"""

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


def _env_truthy(name: str, default: str = "") -> bool:
    raw = os.environ.get(name, default)
    return str(raw).strip().lower() in {"1", "true", "yes", "on"}


def _env_falsy_explicit(name: str) -> bool:
    """True when operator explicitly disabled a free provider."""
    if name not in os.environ:
        return False
    return str(os.environ.get(name, "")).strip().lower() in {"0", "false", "no", "off"}


def credentials_available(provider: dict[str, Any]) -> bool:
    """Return False when required env credentials are missing or provider opted out."""
    env_keys = provider.get("env_keys") or []
    api_type = str(provider.get("api_type") or "")

    # Free/toggle providers — default ON; explicit 0/false/no disables
    if api_type in {"rss", "atom", "sitemap", "opensearch", "trusted_site"}:
        if api_type == "rss" and _env_falsy_explicit("RSS_ENABLED"):
            return False
        if api_type == "atom" and _env_falsy_explicit("ATOM_ENABLED"):
            return False
        if api_type == "sitemap" and _env_falsy_explicit("SITEMAP_ENABLED"):
            return False
        return True

    # Common Crawl: free public index — default ON (opt-out COMMONCRAWL_ENABLED=0)
    if api_type == "commoncrawl":
        if "COMMONCRAWL_ENABLED" not in os.environ:
            return True
        if _env_falsy_explicit("COMMONCRAWL_ENABLED"):
            return False
        return _env_truthy("COMMONCRAWL_ENABLED", "1")

    if not env_keys:
        return True
    for key in env_keys:
        if not os.environ.get(str(key), "").strip():
            return False
    # Yandex needs user companion when key present
    if api_type == "yandex" and not os.environ.get("YANDEX_USER", "").strip():
        return False
    return True


def operational_status(provider: dict[str, Any]) -> str:
    """ACTIVE | DISABLED | MISCONFIGURED — never silent."""
    if not provider.get("enabled", True):
        return "DISABLED"
    if not credentials_available(provider):
        return "MISCONFIGURED"
    return "ACTIVE"


def provider_env_status(provider: dict[str, Any]) -> dict[str, Any]:
    """Per-key credential status without revealing secret values."""
    api_type = str(provider.get("api_type") or "")
    keys = list(provider.get("env_keys") or [])
    detail: dict[str, str] = {}
    for k in keys:
        detail[str(k)] = "Loaded" if os.environ.get(str(k), "").strip() else "Missing"
    if api_type == "yandex":
        detail["YANDEX_USER"] = (
            "Loaded" if os.environ.get("YANDEX_USER", "").strip() else "Missing"
        )
    reason = ""
    op = operational_status(provider)
    if op == "DISABLED":
        reason = "enabled=false in discovery_registry.yaml"
    elif op == "MISCONFIGURED":
        missing = [k for k, v in detail.items() if v == "Missing"]
        if api_type == "commoncrawl" and _env_falsy_explicit("COMMONCRAWL_ENABLED"):
            reason = "COMMONCRAWL_ENABLED explicitly disabled"
        elif api_type == "rss" and _env_falsy_explicit("RSS_ENABLED"):
            reason = "RSS_ENABLED explicitly disabled"
        elif api_type == "atom" and _env_falsy_explicit("ATOM_ENABLED"):
            reason = "ATOM_ENABLED explicitly disabled"
        elif api_type == "sitemap" and _env_falsy_explicit("SITEMAP_ENABLED"):
            reason = "SITEMAP_ENABLED explicitly disabled"
        else:
            reason = f"missing credentials: {', '.join(missing) or 'required env'}"
    else:
        reason = "ready"
    return {
        "operational_status": op,
        "credential_loaded": op == "ACTIVE",
        "keys": detail,
        "reason": reason,
    }


class DiscoveryRegistry:
    def __init__(self, repo_root: Path | None = None, config: dict[str, Any] | None = None):
        self.repo_root = repo_root or find_repo_root()
        self.config = config or load_discovery_registry(self.repo_root)
        self.defaults = dict(self.config.get("defaults") or {})

    def list_providers(
        self, *, enabled_only: bool = False, runnable_only: bool = False
    ) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        for raw in self.config.get("providers") or []:
            if not isinstance(raw, dict):
                continue
            row = {**self.defaults, **raw}
            if enabled_only and not row.get("enabled", True):
                continue
            creds_ok = credentials_available(row)
            env_st = provider_env_status(row)
            op = env_st["operational_status"]
            row["credentials_available"] = creds_ok
            row["operational_status"] = op
            row["credential_status"] = env_st
            # Compat fields + explicit statuses
            if op == "ACTIVE":
                row["status"] = "ready"
                row["health"] = "healthy"
            elif op == "DISABLED":
                row["status"] = "disabled"
                row["health"] = "offline"
            else:
                row["status"] = "misconfigured"
                row["health"] = "offline"
            row["disable_reason"] = env_st.get("reason")
            if runnable_only and op != "ACTIVE":
                continue
            out.append(row)
        out.sort(key=lambda r: int(r.get("priority") or 0), reverse=True)
        return out

    def get(self, provider_id: str) -> Optional[dict[str, Any]]:
        for p in self.list_providers():
            if str(p.get("id")) == provider_id:
                return p
        return None
