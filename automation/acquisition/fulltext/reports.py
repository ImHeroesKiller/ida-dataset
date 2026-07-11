"""Full-text acquisition reports under reports/fulltext/."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


def write_fulltext_reports(
    stats: dict[str, Any] | None = None,
    *,
    repo_root: Path | None = None,
    before: dict[str, Any] | None = None,
    after: dict[str, Any] | None = None,
) -> dict[str, str]:
    root = repo_root or find_repo_root()
    out = root / "reports" / "fulltext"
    out.mkdir(parents=True, exist_ok=True)
    written: dict[str, str] = {}

    if stats is None:
        p = root / "automation" / "learning" / "state" / "fulltext_acquisition.json"
        if p.exists():
            try:
                stats = json.loads(p.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                stats = {}
        else:
            stats = {}
    stats = stats or {}

    def w(name: str, body: str) -> None:
        path = out / name
        path.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")
        written[name] = str(path.relative_to(root))

    now = utc_now_iso()
    attempts = int(stats.get("attempts") or 0)
    records = stats.get("records") or []

    w(
        "doi_resolution.md",
        f"""# DOI Resolution

**Generated:** {now}

| Metric | Value |
|--------|------:|
| Attempts | {attempts} |
| DOI available | {stats.get('doi_available', 0)} |
| DOI resolved | {stats.get('doi_resolved', 0)} |
| DOI → full text | {stats.get('doi_fulltext', 0)} |
| DOI resolution rate | {stats.get('doi_resolution_rate', 0)}% |
| DOI full-text rate | {stats.get('doi_fulltext_rate', 0)}% |

## Notes

Resolution uses Crossref works API + doi.org landing, then Unpaywall / OpenAlex / PMC / arXiv / CORE / Zenodo / Semantic Scholar for assets.
""",
    )

    w(
        "publisher_resolution.md",
        f"""# Publisher Resolution

**Generated:** {now}

| Metric | Value |
|--------|------:|
| Publisher-sourced enrichments | {stats.get('publisher', 0)} |
| Blocked downloads | {stats.get('blocked', 0)} |
| Redirect/failure class | {stats.get('redirect', 0)} |

Publisher landing pages and Crossref `link` assets are attempted after DOI resolution.
""",
    )

    w(
        "representation_quality.md",
        f"""# Representation Quality

**Generated:** {now}

| Representation | Count |
|----------------|------:|
| Full HTML | {stats.get('full_html', 0)} |
| PDF | {stats.get('pdf', 0)} |
| XML | {stats.get('xml', 0)} |
| DOCX | {stats.get('docx', 0)} |
| Metadata only (post-chain) | {stats.get('metadata_only', 0)} |

| Quality | Value |
|---------|------:|
| Avg content size (usable chars) | {stats.get('avg_content_size', 0)} |
| Avg richness score | {stats.get('avg_richness', 0)} |

Ranking: HTML full text > PDF > XML > EPUB > DOCX > TXT > metadata JSON.
""",
    )

    w(
        "fulltext_statistics.md",
        f"""# Full Text Statistics

**Generated:** {now}

| Metric | Value |
|--------|------:|
| Attempts | {attempts} |
| Enriched | {stats.get('enriched', 0)} |
| Already rich (skipped) | {stats.get('skipped_already_rich', 0)} |
| Failed / metadata fallback | {stats.get('failed', 0)} |
| Metadata % | {stats.get('metadata_pct', 0)}% |
| Full-text % (HTML+PDF+XML+DOCX) | {stats.get('fulltext_pct', 0)}% |
| PDF % | {stats.get('pdf_pct', 0)}% |
| HTML % | {stats.get('html_pct', 0)}% |
""",
    )

    w(
        "repository_statistics.md",
        f"""# Repository / Open Access Statistics

**Generated:** {now}

| Channel | Count |
|---------|------:|
| Open access enrichments | {stats.get('open_access', 0)} |
| Repository | {stats.get('repository', 0)} |
| Mirror | {stats.get('mirror', 0)} |
| Publisher | {stats.get('publisher', 0)} |

Sources consulted: Unpaywall, OpenAlex locations, Europe PMC, arXiv, CORE, Zenodo, Semantic Scholar, Crossref links.
""",
    )

    w(
        "acquisition_success.md",
        f"""# Acquisition Success

**Generated:** {now}

| Outcome | Count |
|---------|------:|
| Enriched with richer body | {stats.get('enriched', 0)} |
| Already rich | {stats.get('skipped_already_rich', 0)} |
| Metadata fallback | {stats.get('metadata_only', 0)} |
| Failed chain | {stats.get('failed', 0)} |
| Blocked | {stats.get('blocked', 0)} |

## Recent records

| Document | Result | Representation | Source | Chars |
|----------|--------|----------------|--------|------:|
"""
        + "\n".join(
            f"| {r.get('document_id')} | {r.get('result')} | {r.get('representation')} | "
            f"{r.get('source')} | {r.get('usable_chars') or r.get('baseline_chars') or '—'} |"
            for r in records[:40]
        )
        + ("\n| — | no records | — | — | — |" if not records else "")
        + "\n",
    )

    w(
        "content_richness.md",
        f"""# Content Richness

**Generated:** {now}

| Metric | Value |
|--------|------:|
| Average usable characters | {stats.get('avg_content_size', 0)} |
| Average representation score | {stats.get('avg_richness', 0)} |
| Full-text share | {stats.get('fulltext_pct', 0)}% |
| Metadata share | {stats.get('metadata_pct', 0)}% |

Higher usable characters feed the existing extraction engine without extractor changes.
""",
    )

    w(
        "fallback_chain.md",
        f"""# Fallback Chain

**Generated:** {now}

```
DOI
 ↓
Crossref / doi.org landing
 ↓
Publisher assets (HTML / PDF / XML)
 ↓
Open Access (Unpaywall, OpenAlex, PMC, arXiv, …)
 ↓
Institutional / repository (CORE, Zenodo, …)
 ↓
Mirror / original URL
 ↓
Metadata (last resort only)
```

Never prefer metadata when a richer representation downloads successfully.
""",
    )

    # Projection from audit 002 baselines if before/after provided
    before = before or {
        "metadata_pct": 98.1,
        "rows_per_doc": 0.93,
        "potential_rows_per_doc": 6.48,
        "doi_fulltext_rate": 0.0,
        "avg_words": 97,
    }
    after = after or {
        "metadata_pct": stats.get("metadata_pct"),
        "fulltext_pct": stats.get("fulltext_pct"),
        "doi_fulltext_rate": stats.get("doi_fulltext_rate"),
        "avg_content_size": stats.get("avg_content_size"),
        "avg_richness": stats.get("avg_richness"),
    }

    # Simple projection: scale rows/doc by content size uplift proxy
    base_chars = 1152  # audit 002 mean
    new_chars = float(after.get("avg_content_size") or base_chars)
    uplift = min(6.0, max(1.0, new_chars / max(1.0, base_chars)))
    proj_rows = round(0.93 * min(uplift, 5.5), 2)
    # if fulltext high, approach potential
    ft = float(after.get("fulltext_pct") or 0) / 100.0
    proj_rows2 = round(0.93 * (1 - ft) + 6.48 * ft * 0.7, 2)

    w(
        "knowledge_gain_projection.md",
        f"""# Knowledge Gain Projection

**Generated:** {now}

## Before (Forensic Audit 002)

| Metric | Value |
|--------|------:|
| Metadata-only | {before.get('metadata_pct')}% |
| Rows / document | {before.get('rows_per_doc')} |
| Potential rows / document | {before.get('potential_rows_per_doc')} |
| DOI → full text | {before.get('doi_fulltext_rate')}% |
| Mean usable words | {before.get('avg_words')} |

## After (this session / simulation)

| Metric | Value |
|--------|------:|
| Metadata % | {after.get('metadata_pct')} |
| Full-text % | {after.get('fulltext_pct')} |
| DOI full-text rate | {after.get('doi_fulltext_rate')} |
| Avg content size (chars) | {after.get('avg_content_size')} |
| Avg richness | {after.get('avg_richness')} |

## Projected extraction yield (no extractor changes)

| Model | Projected rows/doc |
|-------|-------------------:|
| Content-size uplift proxy | ~{proj_rows} |
| Full-text mix proxy (70% of potential on FT docs) | ~{proj_rows2} |
| Target success criteria | ≥5.0 |

Actual rows still depend on mission-scoped extraction; richer bodies unlock higher potential for a later multi-dataset extract sprint.
""",
    )

    # validation before/after if both detailed
    if before and after and before.get("label") == "simulation":
        pass

    w(
        "validation_before_after.md",
        f"""# Validation — Before / After

**Generated:** {now}

| Metric | Before (Audit 002) | After (framework session) |
|--------|-------------------:|--------------------------:|
| Metadata-only % | {before.get('metadata_pct')} | {after.get('metadata_pct')} |
| Full-text % | ~1 | {after.get('fulltext_pct')} |
| PDF % | 0 | {stats.get('pdf_pct', 0)} |
| HTML % | ~6 | {stats.get('html_pct', 0)} |
| DOI full-text rate | {before.get('doi_fulltext_rate')} | {after.get('doi_fulltext_rate')} |
| Avg content size (chars) | ~1152 | {after.get('avg_content_size')} |
| Avg richness score | low | {after.get('avg_richness')} |

Target: metadata-only **&lt;30%**, DOI full-text **&gt;60%** where legally available, rows/doc **&gt;5** (requires rich bodies + extract; bodies first).
""",
    )

    return written
