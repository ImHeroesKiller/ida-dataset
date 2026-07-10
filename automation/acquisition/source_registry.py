"""Data-driven Source Registry — add sources via YAML without code changes."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root
from automation.lib.simple_yaml import load_simple_yaml


def load_source_registry(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    path = root / "automation" / "config" / "source_registry.yaml"
    if not path.exists():
        return {"version": "0", "sources": [], "defaults": {}}
    text = path.read_text(encoding="utf-8")
    data = load_simple_yaml(text) or {}
    if not isinstance(data, dict):
        data = {}
    data["_repo_root"] = str(root)
    data["_path"] = str(path)
    return data


class SourceRegistry:
    """Selectable, health-aware registry of trusted sources."""

    def __init__(self, repo_root: Path | None = None, config: dict[str, Any] | None = None):
        self.repo_root = repo_root or find_repo_root()
        self.config = config or load_source_registry(self.repo_root)
        self.defaults = dict(self.config.get("defaults") or {})

    def list_sources(self, *, enabled_only: bool = False) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        for raw in self.config.get("sources") or []:
            if not isinstance(raw, dict):
                continue
            row = {**self.defaults, **raw}
            if enabled_only and not row.get("enabled"):
                continue
            out.append(row)
        out.sort(key=lambda r: int(r.get("priority") or 0), reverse=True)
        return out

    def get(self, source_id: str) -> Optional[dict[str, Any]]:
        for s in self.list_sources():
            if str(s.get("id")) == source_id:
                return s
        return None

    def select_for_mission(
        self,
        *,
        dataset: str = "industry_library",
        preferred_source_ids: Optional[list[str]] = None,
        limit: int = 8,
        min_trust: float = 0.80,
    ) -> list[dict[str, Any]]:
        """Mission selector helper — adaptive ranking (health, yield, latency, freshness)."""
        candidates = self.list_sources(enabled_only=True)
        try:
            from automation.acquisition.source_ranker import rank_sources
            from automation.acquisition.webhook import drain_pending_sources

            # Webhook / feed update events boost preferred sources
            webhook_pref = drain_pending_sources(repo_root=self.repo_root)
            pref = list(preferred_source_ids or [])
            for sid in webhook_pref:
                if sid not in pref:
                    pref.append(sid)
            ranked = rank_sources(
                candidates,
                dataset=dataset,
                preferred_source_ids=pref or None,
                repo_root=self.repo_root,
                min_trust=min_trust,
            )
            # skip exhausted / temporarily disabled (near-zero score after backoff)
            filtered = [s for s in ranked if float(s.get("_rank_score") or 0) >= 5.0]
            return (filtered or ranked)[:limit]
        except Exception:  # noqa: BLE001
            # Fallback: static priority + trust
            scored: list[tuple[float, dict[str, Any]]] = []
            for s in candidates:
                trust = float(s.get("trust_score") or 0)
                if trust < min_trust:
                    continue
                allowed = s.get("allowed_datasets") or []
                if allowed and dataset not in allowed and "*" not in allowed:
                    if trust < 0.90:
                        continue
                score = float(s.get("priority") or 0) + trust * 10
                if preferred_source_ids and s.get("id") in preferred_source_ids:
                    score += 50
                scored.append((score, s))
            scored.sort(key=lambda x: x[0], reverse=True)
            return [s for _, s in scored[:limit]]

    def connector_ids_for(self, sources: list[dict[str, Any]]) -> list[str]:
        ids: list[str] = []
        for s in sources:
            cid = s.get("connector_id")
            if cid:
                ids.append(str(cid))
        return ids
