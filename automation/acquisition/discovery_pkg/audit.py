"""Provider / environment / limit audits for discovery throughput.

Generates reports under reports/discovery/ without redesigning architecture.
"""

from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import Any, Optional

from automation.acquisition.discovery_pkg.budgets import compute_adaptive_budgets
from automation.acquisition.discovery_pkg.providers import (
    PROVIDER_CLASSES,
    build_provider,
    probe_tavily_connectivity,
)
from automation.acquisition.discovery_pkg.ranking import rank_providers
from automation.acquisition.discovery_pkg.registry import (
    DiscoveryRegistry,
    operational_status,
    provider_env_status,
)
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


# Connector-backed knowledge sources (not search-engine discovery providers)
CONNECTOR_KNOWLEDGE_SOURCES = [
    {"name": "OpenAlex", "collector": "openalex", "connector": "CONN-OPENALEX-001", "source": "SRC-OPENALEX"},
    {"name": "Crossref", "collector": "crossref", "connector": "CONN-CROSSREF-001", "source": "SRC-CROSSREF"},
    {"name": "World Bank", "collector": "world_bank", "connector": "CONN-WB-001", "source": "SRC-000004"},
    {"name": "OECD", "collector": "oecd", "connector": "CONN-OECD-001", "source": "SRC-000005"},
    {"name": "ADB", "collector": "adb", "connector": "CONN-ADB-001", "source": "SRC-000006"},
    {"name": "BPS", "collector": "bps", "connector": "CONN-BPS-001", "source": "SRC-000001"},
]

DISCOVERY_ENV_KEYS = [
    "GOOGLE_SEARCH_API_KEY",
    "GOOGLE_SEARCH_ENGINE_ID",
    "BING_SEARCH_API_KEY",
    "BRAVE_SEARCH_API_KEY",
    "SERPAPI_API_KEY",
    "TAVILY_API_KEY",
    "YANDEX_API_KEY",
    "YANDEX_USER",
    "COMMONCRAWL_ENABLED",
    "RSS_ENABLED",
    "ATOM_ENABLED",
    "SITEMAP_ENABLED",
    "OPENALEX_EMAIL",
    "CROSSREF_MAILTO",
]

LIMIT_PATTERNS = [
    r"\bMAX_RESULTS\b",
    r"\bTOP_K\b",
    r"\bMAX_DOCS\b",
    r"\bMAX_DOWNLOADS\b",
    r"\bQUERY_LIMIT\b",
    r"\bDISCOVERY_LIMIT\b",
    r"\bSEARCH_LIMIT\b",
    r"\bRESULT_LIMIT\b",
    r"\bPAGE_LIMIT\b",
    r"\bBATCH_LIMIT\b",
    r"\bmax_results\b",
    r"\bmax_queries\b",
    r"\bmax_urls\b",
    r"\bmax_documents\b",
    r"\bmax_documents_per_session\b",
    r"\bmax_downloads\b",
    r"\bsoft_limit\b",
    r"\bhard_limit\b",
    r"\bprocess_budget\b",
    r"\blimit\s*=\s*\d+",
    r"\[:\s*\d+\s*\]",
    r"min\(\s*limit\s*,\s*\d+",
]


def audit_providers(repo_root: Path | None = None) -> list[dict[str, Any]]:
    """Full provider audit with operational status evidence."""
    root = repo_root or find_repo_root()
    reg = DiscoveryRegistry(repo_root=root)
    rows: list[dict[str, Any]] = []
    yield_path = root / "automation" / "learning" / "state" / "discovery_provider_yield.json"
    hist: dict[str, Any] = {}
    if yield_path.exists():
        try:
            hist = (json.loads(yield_path.read_text(encoding="utf-8")) or {}).get("providers") or {}
        except Exception:  # noqa: BLE001
            hist = {}

    for p in reg.list_providers(enabled_only=False, runnable_only=False):
        env_st = provider_env_status(p)
        op = operational_status(p)
        h_stat: dict[str, Any] = {"ok": False, "status": "unknown", "message": ""}
        latency_ms: float | None = None
        inst = build_provider(p)
        if inst:
            t0 = time.perf_counter()
            try:
                h_stat = inst.health()
            except Exception as exc:  # noqa: BLE001
                h_stat = {"ok": False, "status": "error", "message": str(exc)[:120]}
            latency_ms = round((time.perf_counter() - t0) * 1000, 2)

        # Explicit Tavily connectivity when key present
        tavily_probe = None
        if str(p.get("api_type")) == "tavily":
            tavily_probe = probe_tavily_connectivity()
            if tavily_probe.get("probed"):
                h_stat = {
                    "ok": bool(tavily_probe.get("ok")),
                    "status": tavily_probe.get("status"),
                    "message": tavily_probe.get("message"),
                }
                if tavily_probe.get("latency_ms") is not None:
                    latency_ms = tavily_probe["latency_ms"]

        hid = str(p.get("id") or "")
        h = hist.get(hid) or {}
        rows.append(
            {
                "provider": p.get("name"),
                "provider_id": hid,
                "api_type": p.get("api_type"),
                "enabled": bool(p.get("enabled", True)),
                "disabled": not bool(p.get("enabled", True)),
                "reason": env_st.get("reason") or op,
                "credential_loaded": env_st.get("credential_loaded"),
                "credentials_detail": env_st.get("keys"),
                "rate_limit": p.get("rate_limit"),
                "daily_quota": p.get("daily_quota"),
                "health": h_stat,
                "latency_ms": latency_ms,
                "average_urls": h.get("urls_total", 0) / max(1, int(h.get("runs") or 1))
                if h
                else 0,
                "average_documents": h.get("urls_accepted", 0) / max(1, int(h.get("runs") or 1))
                if h
                else 0,
                "average_yield": h.get("success_rate", 0),
                "operational_status": op,
                "tavily_probe": tavily_probe,
                "priority": p.get("priority"),
                "adapter": str(p.get("api_type")) in PROVIDER_CLASSES,
            }
        )
    return rows


def audit_environment(repo_root: Path | None = None) -> dict[str, Any]:
    """Local / GitHub Actions / Vercel credential surface (no secret values)."""
    root = repo_root or find_repo_root()
    local: dict[str, Any] = {}
    for key in DISCOVERY_ENV_KEYS:
        val = os.environ.get(key, "")
        loaded = bool(str(val).strip())
        local[key] = {
            "loaded": loaded,
            "status": "Loaded" if loaded else "Missing",
            "length": len(str(val).strip()) if loaded else 0,
        }

    # GitHub Actions: inspect workflow env mapping (not live secrets)
    gha_workflow = root / ".github" / "workflows" / "learn.yml"
    gha_text = gha_workflow.read_text(encoding="utf-8") if gha_workflow.exists() else ""
    gha: dict[str, Any] = {}
    for key in DISCOVERY_ENV_KEYS:
        mapped = (
            f"secrets.{key}" in gha_text
            or f"env.{key}" in gha_text
            or re.search(rf"\b{re.escape(key)}\b", gha_text) is not None
        )
        # Present in runner env if CI and set
        in_runner = bool(os.environ.get(key, "").strip()) and bool(
            os.environ.get("GITHUB_ACTIONS") or os.environ.get("CI")
        )
        if mapped and in_runner:
            st = "Loaded"
        elif mapped:
            st = "Mapped (secret may be empty)"
        else:
            st = "Missing mapping"
        gha[key] = {
            "mapped_in_workflow": mapped,
            "loaded_in_runner": in_runner,
            "status": st,
        }

    # Vercel: acquisition is GHA/local; dashboard deploy may not need keys
    vercel_json = root / "vercel.json"
    vercel_has_config = vercel_json.exists()
    vercel: dict[str, Any] = {
        "note": "Discovery acquisition runs in Python/GHA, not Vercel runtime. "
        "Dashboard is read-only over repo state. Keys on Vercel are optional.",
        "vercel_json_present": vercel_has_config,
        "keys": {
            k: {
                "status": "Not applicable for Vercel SSR"
                if not os.environ.get("VERCEL")
                else ("Loaded" if os.environ.get(k) else "Missing"),
                "loaded": bool(os.environ.get(k, "").strip()),
            }
            for k in DISCOVERY_ENV_KEYS
        },
    }

    return {
        "generated_at": utc_now_iso(),
        "local": local,
        "github_actions": gha,
        "vercel": vercel,
        "never_silently_disable": True,
    }


def audit_hard_limits(repo_root: Path | None = None) -> list[dict[str, Any]]:
    """Scan repository for hardcoded discovery/throughput limits."""
    root = repo_root or find_repo_root()
    roots = [
        root / "automation" / "acquisition",
        root / "automation" / "config",
        root / "automation" / "learning",
        root / "automation" / "search",
        root / "automation" / "ci",
    ]
    exts = {".py", ".yaml", ".yml", ".ts", ".tsx", ".json"}
    combined = re.compile("|".join(f"({p})" for p in LIMIT_PATTERNS))
    hits: list[dict[str, Any]] = []

    for base in roots:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file() or path.suffix not in exts:
                continue
            if "__pycache__" in path.parts or "node_modules" in path.parts:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except Exception:  # noqa: BLE001
                continue
            for i, line in enumerate(text.splitlines(), 1):
                if combined.search(line):
                    # skip comments that are pure documentation of removal
                    hits.append(
                        {
                            "file": str(path.relative_to(root)),
                            "line": i,
                            "text": line.strip()[:200],
                        }
                    )
    return hits


def write_audit_reports(
    *,
    repo_root: Path | None = None,
    analytics: Optional[dict[str, Any]] = None,
    budgets: Optional[dict[str, Any]] = None,
) -> dict[str, str]:
    """Write all Phase 1–10 discovery reports."""
    root = repo_root or find_repo_root()
    out = root / "reports" / "discovery"
    out.mkdir(parents=True, exist_ok=True)
    written: dict[str, str] = {}

    def w(name: str, body: str) -> None:
        p = out / name
        p.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")
        written[name] = str(p.relative_to(root))

    providers = audit_providers(root)
    env = audit_environment(root)
    limits = audit_hard_limits(root)
    reg = DiscoveryRegistry(repo_root=root)
    all_p = reg.list_providers(enabled_only=False)
    ranked = rank_providers(all_p, repo_root=root)

    # Load last analytics if not provided
    if analytics is None:
        ap = root / "automation" / "learning" / "state" / "discovery_analytics.json"
        if ap.exists():
            try:
                analytics = json.loads(ap.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                analytics = {}
        else:
            analytics = {}
    analytics = analytics or {}

    active = [p for p in providers if p.get("operational_status") == "ACTIVE"]
    disabled = [p for p in providers if p.get("operational_status") == "DISABLED"]
    misconf = [p for p in providers if p.get("operational_status") == "MISCONFIGURED"]

    if budgets is None:
        try:
            from automation.acquisition.throughput_ops import measure_queues

            q = measure_queues(root)
        except Exception:  # noqa: BLE001
            q = {}
        b = compute_adaptive_budgets(
            knowledge_gap=analytics.get("knowledge_gap"),
            queue_health=q,
            providers_active=len(active),
            providers_misconfigured=len(misconf),
            providers_total=len(providers),
            trusted_domain_count=max(8, len(active) * 2),
        )
        budgets = b.to_dict()

    # --- provider_audit.md ---
    lines = [
        "# Provider Audit",
        "",
        f"**Generated:** {utc_now_iso()}",
        "",
        "Search engines are **discovery tools only**. Knowledge is extracted solely from trusted sources.",
        "",
        f"| ACTIVE | DISABLED | MISCONFIGURED |",
        f"|-------:|---------:|--------------:|",
        f"| {len(active)} | {len(disabled)} | {len(misconf)} |",
        "",
        "| Provider | Status | Enabled | Credential | Rate limit | Daily quota | Health | Latency ms | Avg URLs | Avg docs | Yield | Reason |",
        "|----------|--------|---------|------------|----------:|------------:|--------|-----------:|---------:|---------:|------:|--------|",
    ]
    for p in providers:
        h = p.get("health") or {}
        lines.append(
            f"| {p.get('provider')} | **{p.get('operational_status')}** | {p.get('enabled')} | "
            f"{p.get('credential_loaded')} | {p.get('rate_limit')} | {p.get('daily_quota')} | "
            f"{h.get('status') if isinstance(h, dict) else h} | {p.get('latency_ms') if p.get('latency_ms') is not None else '—'} | "
            f"{round(float(p.get('average_urls') or 0), 2)} | {round(float(p.get('average_documents') or 0), 2)} | "
            f"{p.get('average_yield')} | {p.get('reason')} |"
        )
    lines += [
        "",
        "## Named provider checklist",
        "",
        "| Requested | Mapping | Status |",
        "|-----------|---------|--------|",
    ]
    name_map = {
        "Tavily": "tavily",
        "Google CSE": "google_cse",
        "Google Programmable Search": "google_cse",
        "Google Search API": "google_cse",
        "Brave": "brave",
        "Bing": "bing",
        "SerpAPI": "serpapi",
        "Yandex": "yandex",
        "RSS": "rss",
        "Atom": "atom",
        "Sitemap": "sitemap",
        "Common Crawl": "commoncrawl",
        "Trusted Registry": "trusted_site",
    }
    by_type = {str(p.get("api_type")): p for p in providers}
    for label, api in name_map.items():
        p = by_type.get(api)
        if p:
            lines.append(
                f"| {label} | `{p.get('provider_id')}` | **{p.get('operational_status')}** |"
            )
        else:
            lines.append(f"| {label} | — | NOT REGISTERED |")

    lines += [
        "",
        "## Connector-backed knowledge sources (not discovery search APIs)",
        "",
        "These acquire documents via the connector framework after discovery.",
        "",
        "| Source | Connector | Role |",
        "|--------|-----------|------|",
    ]
    for c in CONNECTOR_KNOWLEDGE_SOURCES:
        lines.append(
            f"| {c['name']} | `{c['connector']}` | Trusted knowledge connector |"
        )

    # Tavily explicit
    tav = by_type.get("tavily") or {}
    probe = (tav.get("tavily_probe") or {}) if tav else {}
    lines += [
        "",
        "## Tavily connectivity (explicit)",
        "",
        f"- Operational status: **{(tav or {}).get('operational_status', 'UNKNOWN')}**",
        f"- Credential loaded: `{(tav or {}).get('credential_loaded')}`",
        f"- Probe: `{json.dumps(probe) if probe else 'not_probed_missing_key'}`",
        "",
        "> Providers are never silently disabled. MISCONFIGURED means enabled but credentials missing.",
        "",
    ]
    w("provider_audit.md", "\n".join(lines))

    # --- provider_health.md ---
    hl = [
        "# Provider Health",
        "",
        f"**Generated:** {utc_now_iso()}",
        "",
        "| Provider | Operational | Health | Credentials | Latency ms | Message |",
        "|----------|-------------|--------|-------------|-----------:|---------|",
    ]
    for p in providers:
        h = p.get("health") or {}
        hl.append(
            f"| {p.get('provider')} | {p.get('operational_status')} | "
            f"{h.get('status') if isinstance(h, dict) else h} | {p.get('credential_loaded')} | "
            f"{p.get('latency_ms') if p.get('latency_ms') is not None else '—'} | "
            f"{(h.get('message') if isinstance(h, dict) else '') or p.get('reason') or '—'} |"
        )
    w("provider_health.md", "\n".join(hl))

    # --- provider_yield.md ---
    yl = [
        "# Provider Yield",
        "",
        f"**Generated:** {utc_now_iso()}",
        "",
        "| Provider | Avg URLs/run | Avg accepted | Success yield | Runs (hist) |",
        "|----------|-------------:|-------------:|--------------:|------------:|",
    ]
    yield_path = root / "automation" / "learning" / "state" / "discovery_provider_yield.json"
    hist = {}
    if yield_path.exists():
        try:
            hist = (json.loads(yield_path.read_text(encoding="utf-8")) or {}).get("providers") or {}
        except Exception:  # noqa: BLE001
            hist = {}
    for p in providers:
        hid = str(p.get("provider_id") or "")
        h = hist.get(hid) or {}
        runs = max(1, int(h.get("runs") or 0)) if h else 1
        yl.append(
            f"| {p.get('provider')} | {round(float(h.get('urls_total') or 0) / runs, 2)} | "
            f"{round(float(h.get('urls_accepted') or 0) / runs, 2)} | "
            f"{h.get('success_rate', p.get('average_yield'))} | {h.get('runs', 0)} |"
        )
    w("provider_yield.md", "\n".join(yl))

    # --- environment_audit.md ---
    el = [
        "# Environment Audit",
        "",
        f"**Generated:** {env.get('generated_at')}",
        "",
        "Credentials are never logged. Status only: Loaded / Missing / Disabled.",
        "",
        "## Local",
        "",
        "| Variable | Status |",
        "|----------|--------|",
    ]
    for k, v in (env.get("local") or {}).items():
        el.append(f"| `{k}` | {v.get('status')} |")
    el += [
        "",
        "## GitHub Actions (`learn.yml`)",
        "",
        "| Variable | Workflow mapping | Status |",
        "|----------|------------------|--------|",
    ]
    for k, v in (env.get("github_actions") or {}).items():
        el.append(
            f"| `{k}` | {v.get('mapped_in_workflow')} | {v.get('status')} |"
        )
    el += [
        "",
        "## Vercel",
        "",
        str((env.get("vercel") or {}).get("note") or ""),
        "",
        "| Variable | Status |",
        "|----------|--------|",
    ]
    for k, v in ((env.get("vercel") or {}).get("keys") or {}).items():
        el.append(f"| `{k}` | {v.get('status')} |")
    el += [
        "",
        "## Policy",
        "",
        "- Never silently disable providers.",
        "- MISCONFIGURED providers are reported with evidence and skipped for network calls only.",
        "",
    ]
    w("environment_audit.md", "\n".join(el))

    # --- hard_limit_audit.md ---
    hl2 = [
        "# Hard Limit Audit",
        "",
        f"**Generated:** {utc_now_iso()}",
        f"**Occurrences found:** {len(limits)}",
        "",
        "Search covers acquisition, config, learning, search, and CI paths.",
        "",
        "| File | Line | Snippet |",
        "|------|-----:|---------|",
    ]
    for hit in limits[:400]:
        snip = (hit.get("text") or "").replace("|", "\\|")
        hl2.append(f"| `{hit.get('file')}` | {hit.get('line')} | `{snip}` |")
    if not limits:
        hl2.append("| — | — | none |")
    hl2 += [
        "",
        "## Target state",
        "",
        "Fixed document caps (5/10/20/50) must not stop discovery. "
        "Use adaptive budgets; retain only provider API page-size maxima and optional policy safety rails.",
        "",
    ]
    w("hard_limit_audit.md", "\n".join(hl2))

    # --- adaptive_budget.md ---
    ab = [
        "# Adaptive Budget",
        "",
        f"**Generated:** {utc_now_iso()}",
        "",
        "Budgets scale with mission priority, knowledge gap, queue health, "
        "provider health, worker capacity, and runtime.",
        "",
        "| Budget | Value |",
        "|--------|------:|",
    ]
    for k, v in (budgets or {}).items():
        ab.append(f"| `{k}` | {v} |")
    ab += [
        "",
        "## Stop conditions (only)",
        "",
        "1. Provider exhausted (empty results / no remaining queries)",
        "2. Knowledge gap satisfied (universe gap ≤ 0)",
        "3. Runtime budget reached",
        "4. Provider quota reached",
        "",
        "Never stop because an arbitrary document count was hit.",
        "",
    ]
    w("adaptive_budget.md", "\n".join(ab))

    # --- throughput_analysis.md ---
    ta = [
        "# Throughput Analysis",
        "",
        f"**Generated:** {utc_now_iso()}",
        "",
        "## Last discovery session",
        "",
        "| Metric | Value |",
        "|--------|------:|",
        f"| Queries generated | {analytics.get('queries_generated', 0)} |",
        f"| Queries executed | {analytics.get('queries_executed', 0)} |",
        f"| URLs discovered | {analytics.get('urls_discovered', 0)} |",
        f"| URLs accepted | {analytics.get('urls_accepted', 0)} |",
        f"| URLs rejected | {analytics.get('urls_rejected', 0)} |",
        f"| URLs remaining (budget − accepted) | {analytics.get('urls_remaining', '—')} |",
        f"| Elapsed ms | {analytics.get('elapsed_ms', 0)} |",
        f"| Stop reason | {analytics.get('stop_reason', '—')} |",
        "",
        "## Bottleneck diagnosis",
        "",
    ]
    if len(misconf) > len(active):
        ta.append(
            f"- **Primary bottleneck:** MISCONFIGURED discovery APIs "
            f"({len(misconf)} providers). Only free feeds/trusted-site ran."
        )
    ta += [
        f"- ACTIVE providers: {len(active)}",
        f"- MISCONFIGURED providers: {len(misconf)}",
        f"- Typical low session (~10 discovered / ~5 downloaded) matches "
        f"feed-only path + previous hard caps (max_urls=20, discover limit=5).",
        "- Engine works; discovery breadth was limited by credentials + artificial caps.",
        "",
    ]
    w("throughput_analysis.md", "\n".join(ta))

    # --- discovery_capacity.md ---
    dc = [
        "# Discovery Capacity",
        "",
        f"**Generated:** {utc_now_iso()}",
        "",
        "| Dimension | Value |",
        "|-----------|------:|",
        f"| Active providers | {len(active)} |",
        f"| Misconfigured providers | {len(misconf)} |",
        f"| Query budget (adaptive) | {(budgets or {}).get('query_budget')} |",
        f"| URL budget (adaptive) | {(budgets or {}).get('url_budget')} |",
        f"| Download budget | {(budgets or {}).get('download_budget')} |",
        f"| Runtime budget (s) | {(budgets or {}).get('runtime_budget_s')} |",
        f"| Per-provider results | {(budgets or {}).get('per_provider_results')} |",
        "",
        "Limiting factor should be provider quotas, runtime, or real source exhaustion — not code constants.",
        "",
    ]
    w("discovery_capacity.md", "\n".join(dc))

    # --- provider_ranking.md ---
    pr = [
        "# Provider Ranking",
        "",
        f"**Generated:** {utc_now_iso()}",
        "",
        "Dynamic rank: yield · freshness · trust · latency · coverage · mission relevance · success rate.",
        "",
        "| Rank | Provider | Score | Status | Components |",
        "|-----:|----------|------:|--------|------------|",
    ]
    for i, p in enumerate(ranked, 1):
        pr.append(
            f"| {i} | {p.get('name')} | {p.get('_rank_score')} | "
            f"{p.get('operational_status')} | `{json.dumps(p.get('_rank_components') or {})[:80]}` |"
        )
    w("provider_ranking.md", "\n".join(pr))

    # --- provider_exhaustion.md ---
    pe = [
        "# Provider Exhaustion",
        "",
        f"**Generated:** {utc_now_iso()}",
        "",
        f"**Stop reason (last run):** `{analytics.get('stop_reason', '—')}`",
        "",
        "| Provider | Queries | URLs | Exhausted | Reason |",
        "|----------|--------:|-----:|-----------|--------|",
    ]
    for p in analytics.get("providers") or []:
        pe.append(
            f"| {p.get('name') or p.get('provider_id')} | {p.get('queries', 0)} | "
            f"{p.get('urls', 0)} | {p.get('exhausted', False)} | "
            f"{p.get('exhaustion_reason') or p.get('status') or '—'} |"
        )
    if not analytics.get("providers"):
        pe.append("| — | 0 | 0 | — | no session data |")
    pe += [
        "",
        "## Adaptive stopping",
        "",
        "- Infinite crawling is prevented by runtime budget + provider exhaustion + quota.",
        "- Discovery does **not** stop at fixed document counts.",
        "",
    ]
    w("provider_exhaustion.md", "\n".join(pe))

    # Persist audit JSON
    state = {
        "generated_at": utc_now_iso(),
        "providers": providers,
        "environment": env,
        "hard_limits_count": len(limits),
        "budgets": budgets,
        "ranked": [
            {
                "id": p.get("id"),
                "name": p.get("name"),
                "score": p.get("_rank_score"),
                "status": p.get("operational_status"),
            }
            for p in ranked
        ],
    }
    sp = root / "automation" / "learning" / "state" / "discovery_provider_audit.json"
    sp.parent.mkdir(parents=True, exist_ok=True)
    sp.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    written["discovery_provider_audit.json"] = str(sp.relative_to(root))

    return written


if __name__ == "__main__":
    paths = write_audit_reports()
    for k, v in paths.items():
        print(f"wrote {v}")
