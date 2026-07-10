"""Intelligent discovery query generation for trusted domains only."""

from __future__ import annotations

import re
from typing import Any, Optional
from urllib.parse import urlparse


# Keywords extracted from mission text for site-scoped queries
_STOP = {
    "expand", "produce", "dataset", "indonesia", "the", "and", "for", "with",
    "toward", "product", "target", "learn", "knowledge", "library", "mission",
}


def extract_topic_terms(instruction: str, *, max_terms: int = 6) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9\-]{2,}", instruction or "")
    out: list[str] = []
    for w in words:
        low = w.lower()
        if low in _STOP:
            continue
        if low not in out:
            out.append(low)
        if len(out) >= max_terms:
            break
    if not out:
        out = ["industry"]
    return out


def trusted_domains_from_sources(sources: list[dict[str, Any]]) -> list[dict[str, str]]:
    """Extract domains + source_id from trusted source registry entries."""
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for s in sources:
        domains: list[str] = []
        base = str(s.get("base_url") or "").strip()
        if base:
            host = (urlparse(base).hostname or "").lower()
            if host.startswith("www."):
                host = host[4:]
            if host:
                domains.append(host)
        # also allow listed domains from notes? keep base_url only
        for d in domains:
            if d in seen:
                continue
            seen.add(d)
            rows.append(
                {
                    "domain": d,
                    "source_id": str(s.get("id") or ""),
                    "source_name": str(s.get("name") or d),
                    "category": str(s.get("category") or ""),
                }
            )
    return rows


def build_discovery_queries(
    instruction: str,
    *,
    trusted_domains: list[dict[str, str]],
    max_queries: int = 24,
    language: str = "",
    country: str = "",
    after: str = "",
    before: str = "",
    filetype: str = "",
) -> list[dict[str, Any]]:
    """Generate site-scoped and filtered discovery queries.

    Example: site:worldbank.org outsourcing indonesia
    """
    terms = extract_topic_terms(instruction)
    topic = " ".join(terms[:4])
    if "indonesia" not in topic.lower() and "indonesia" in (instruction or "").lower():
        topic = f"{topic} indonesia".strip()

    queries: list[dict[str, Any]] = []
    # Per trusted domain site: queries (highest value)
    for row in trusted_domains:
        domain = row["domain"]
        q = f"site:{domain} {topic}".strip()
        if filetype:
            q += f" filetype:{filetype}"
        if after:
            q += f" after:{after}"
        if before:
            q += f" before:{before}"
        queries.append(
            {
                "query": q,
                "domain": domain,
                "source_id": row.get("source_id"),
                "source_name": row.get("source_name"),
                "kind": "site",
                "topic": topic,
            }
        )
        # intitle variant for a few high-priority domains
        if len(queries) < max_queries and terms:
            queries.append(
                {
                    "query": f"site:{domain} intitle:{terms[0]} {topic}",
                    "domain": domain,
                    "source_id": row.get("source_id"),
                    "source_name": row.get("source_name"),
                    "kind": "intitle",
                    "topic": topic,
                }
            )
        if len(queries) >= max_queries:
            break

    # Open topic query (still filtered later by trusted domain)
    if len(queries) < max_queries:
        q = topic
        if language:
            q += f" language:{language}"
        if country:
            q += f" country:{country}"
        queries.append(
            {
                "query": q,
                "domain": "",
                "source_id": "",
                "source_name": "",
                "kind": "open",
                "topic": topic,
            }
        )

    # de-dupe
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for item in queries:
        key = item["query"].lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
        if len(out) >= max_queries:
            break
    return out
