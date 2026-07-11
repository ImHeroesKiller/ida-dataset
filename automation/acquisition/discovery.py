"""Smart discovery — RSS / Atom / Sitemap / feed links before blind crawl.

Never fabricates documents. Only extracts URLs/titles from public feeds.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from typing import Any, Optional
from urllib.parse import urljoin

from automation.connectors.http_utils import http_get


def discover_urls(
    *,
    base_url: str = "",
    rss_feed: str | None = None,
    sitemap_url: str | None = None,
    atom_feed: str | None = None,
    limit: int = 20,
    timeout: float = 8.0,
) -> list[dict[str, Any]]:
    """Discover candidate document URLs from preferred discovery channels."""
    out: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add(url: str, title: str = "", source: str = "", published: str = "") -> None:
        u = (url or "").strip()
        if not u or u in seen:
            return
        seen.add(u)
        out.append(
            {
                "url": u,
                "title": (title or "")[:200],
                "discovery": source,
                "published_at": published or "",
            }
        )

    feeds = []
    if rss_feed:
        feeds.append(("rss", rss_feed))
    if atom_feed:
        feeds.append(("atom", atom_feed))
    if sitemap_url:
        feeds.append(("sitemap", sitemap_url))
    # common fallbacks from base_url
    if base_url:
        for path, kind in (
            ("/feed", "rss"),
            ("/rss", "rss"),
            ("/atom.xml", "atom"),
            ("/sitemap.xml", "sitemap"),
        ):
            feeds.append((kind, urljoin(base_url.rstrip("/") + "/", path.lstrip("/"))))

    for kind, feed_url in feeds:
        if len(out) >= limit:
            break
        try:
            res = http_get(feed_url, timeout=timeout, retries=1)
            if not res.get("ok"):
                continue
            text = res.get("text") or ""
            if kind in {"rss", "atom"}:
                for item in _parse_feed_xml(text, kind=kind)[:limit]:
                    add(item["url"], item.get("title", ""), kind, item.get("published_at", ""))
            elif kind == "sitemap":
                for item in _parse_sitemap(text)[:limit]:
                    add(item["url"], "", "sitemap", item.get("published_at", ""))
        except Exception:  # noqa: BLE001
            continue

    return out[:limit]


def _local(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[-1]
    return tag


def _parse_feed_xml(text: str, *, kind: str) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        # regex fallback for broken feeds
        links = re.findall(r"<link[^>]*>(https?://[^<]+)</link>", text, flags=re.I)
        titles = re.findall(r"<title[^>]*>([^<]+)</title>", text, flags=re.I)
        for i, link in enumerate(links):
            out.append(
                {
                    "url": link.strip(),
                    "title": titles[i + 1] if i + 1 < len(titles) else titles[i] if titles else "",
                    "published_at": "",
                }
            )
        return out

    # RSS channel/item or Atom feed/entry
    for el in root.iter():
        name = _local(el.tag).lower()
        if name not in {"item", "entry"}:
            continue
        title = ""
        link = ""
        published = ""
        for child in list(el):
            cn = _local(child.tag).lower()
            if cn == "title" and child.text:
                title = (child.text or "").strip()
            elif cn == "link":
                href = child.attrib.get("href") or (child.text or "").strip()
                if href:
                    link = href
            elif cn in {"pubdate", "published", "updated", "date"} and child.text:
                published = (child.text or "").strip()[:40]
        if link:
            out.append({"url": link, "title": title, "published_at": published})
    return out


def _parse_sitemap(text: str) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        locs = re.findall(r"<loc>\s*(https?://[^<\s]+)\s*</loc>", text, flags=re.I)
        return [{"url": u.strip(), "published_at": ""} for u in locs]
    for el in root.iter():
        if _local(el.tag).lower() != "url":
            continue
        loc = ""
        lastmod = ""
        for child in list(el):
            cn = _local(child.tag).lower()
            if cn == "loc" and child.text:
                loc = child.text.strip()
            elif cn == "lastmod" and child.text:
                lastmod = child.text.strip()[:40]
        if loc:
            out.append({"url": loc, "published_at": lastmod})
    return out
