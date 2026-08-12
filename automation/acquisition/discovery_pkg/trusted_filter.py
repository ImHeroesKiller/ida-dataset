"""Trusted Source Filter — only allow URLs on verified registry domains."""

from __future__ import annotations

import re
from typing import Any
from urllib.parse import urlparse

# Hard reject patterns (never knowledge sources via discovery)
_REJECT_HOST_SNIPPETS = (
    "facebook.com",
    "twitter.com",
    "x.com",
    "instagram.com",
    "tiktok.com",
    "youtube.com",
    "reddit.com",
    "medium.com",
    "blogspot.",
    "wordpress.com",
    "tumblr.com",
    "pinterest.",
    "linkedin.com",
    "quora.com",
    "stackoverflow.com",
    "stackexchange.com",
    "wikipedia.org",  # encyclopedia — not our trusted registry path
    "wikihow.com",
    "news.google.",
    "news.yahoo.",
    "msn.com",
    "chatgpt.com",
    "openai.com",
    "perplexity.ai",
    "gemini.google.",
    "bard.google.",
    "pastebin.",
    "scribd.com",
    "slideshare.",
    "archive.org",  # mirrors unless explicitly trusted
)


def host_of(url: str) -> str:
    host = (urlparse(url or "").hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    return host


def build_allowlist(sources: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
    """domain → source meta."""
    allow: dict[str, dict[str, str]] = {}
    for s in sources:
        base = str(s.get("base_url") or "").strip()
        if not base:
            continue
        host = host_of(base)
        if not host:
            continue
        allow[host] = {
            "source_id": str(s.get("id") or ""),
            "source_name": str(s.get("name") or host),
            "category": str(s.get("category") or ""),
            "trust_score": str(s.get("trust_score") or ""),
        }
    return allow


def is_rejected_domain(host: str) -> tuple[bool, str]:
    h = (host or "").lower()
    for snip in _REJECT_HOST_SNIPPETS:
        if snip in h:
            return True, f"rejected_class:{snip}"
    if re.search(r"(^|\.)blog\.", h) or h.startswith("blog."):
        return True, "rejected_blog"
    if "forum" in h or "bbs." in h:
        return True, "rejected_forum"
    return False, ""


def domain_matches_allowlist(host: str, allow: dict[str, dict[str, str]]) -> tuple[bool, dict[str, str] | None]:
    h = (host or "").lower()
    if h.startswith("www."):
        h = h[4:]
    if h in allow:
        return True, allow[h]
    for domain, meta in allow.items():
        if h.endswith("." + domain) or domain.endswith("." + h):
            return True, meta
    return False, None


def verify_url(
    url: str,
    *,
    allowlist: dict[str, dict[str, str]],
) -> dict[str, Any]:
    """Return verification result for a discovered URL."""
    host = host_of(url)
    if not host or not url.startswith("http"):
        return {
            "accepted": False,
            "reason": "invalid_url",
            "host": host,
            "url": url,
        }
    rej, why = is_rejected_domain(host)
    if rej:
        return {"accepted": False, "reason": why, "host": host, "url": url}
    ok, meta = domain_matches_allowlist(host, allowlist)
    if not ok or not meta:
        return {
            "accepted": False,
            "reason": "domain_not_in_trusted_registry",
            "host": host,
            "url": url,
        }
    return {
        "accepted": True,
        "reason": "trusted_domain",
        "host": host,
        "url": url,
        "source_id": meta.get("source_id"),
        "source_name": meta.get("source_name"),
        "category": meta.get("category"),
        "trust_score": meta.get("trust_score"),
    }


def verify_url_soft(
    url: str,
    *,
    allowlist: dict[str, dict[str, str]],
    allow_untrusted: bool = True,
) -> dict[str, Any]:
    """Soft verification for multi-table bootstrap.

    Trusted registry domains still preferred. When allow_untrusted=True,
    non-rejected public http(s) URLs are accepted with lower trust tag
    so free DDG discovery can feed all datasheet tables.
    """
    hard = verify_url(url, allowlist=allowlist)
    if hard.get("accepted"):
        return hard
    host = host_of(url)
    if not host or not (url or "").startswith("http"):
        return hard
    rej, why = is_rejected_domain(host)
    if rej:
        return hard
    if not allow_untrusted:
        return hard
    return {
        "accepted": True,
        "reason": "bootstrap_untrusted_ok",
        "host": host,
        "url": url,
        "source_id": f"BOOTSTRAP-{host[:40]}",
        "source_name": host,
        "category": "bootstrap",
        "trust_score": "0.50",
    }


def filter_discovered_urls(
    candidates: list[dict[str, Any]],
    *,
    sources: list[dict[str, Any]],
) -> dict[str, Any]:
    """Split candidates into accepted / rejected with reasons."""
    allow = build_allowlist(sources)
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    seen: set[str] = set()
    duplicates = 0
    for c in candidates:
        url = str(c.get("url") or "").strip()
        key = url.lower().split("#")[0]
        if not key:
            rejected.append({**c, "reject_reason": "empty_url"})
            continue
        if key in seen:
            duplicates += 1
            rejected.append({**c, "reject_reason": "duplicate_url"})
            continue
        seen.add(key)
        v = verify_url_soft(url, allowlist=allow, allow_untrusted=True)
        if v.get("accepted"):
            verification = (
                "trusted_registry"
                if v.get("reason") == "trusted_domain"
                else "bootstrap_untrusted"
            )
            accepted.append(
                {
                    **c,
                    "url": url,
                    "source_id": v.get("source_id"),
                    "source_name": v.get("source_name"),
                    "verified_host": v.get("host"),
                    "verification": verification,
                    "trust_score": v.get("trust_score") or "",
                }
            )
        else:
            rejected.append({**c, "reject_reason": v.get("reason"), "host": v.get("host")})
    return {
        "accepted": accepted,
        "rejected": rejected,
        "duplicates": duplicates,
        "allowlist_size": len(allow),
    }
