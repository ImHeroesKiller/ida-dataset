# Hard Limit Audit

**Generated:** 2026-07-20T16:04:55+00:00
**Occurrences found:** 305

Search covers acquisition, config, learning, search, and CI paths.

| File | Line | Snippet |
|------|-----:|---------|
| `automation/acquisition/trace.py` | 216 | `"evidence_snippet": evidence_snippet[:400],` |
| `automation/acquisition/extractor.py` | 79 | `parts.append(str(pdf["text"])[:50000])` |
| `automation/acquisition/extractor.py` | 87 | `parts.append(normalize_text(raw)[:50000])` |
| `automation/acquisition/extractor.py` | 147 | `evidence_blob = " … ".join(snips)[:1200]` |
| `automation/acquisition/extractor.py` | 168 | `)[:2000],` |
| `automation/acquisition/extractor.py` | 201 | `"Last Updated": utc_now_iso()[:10],` |
| `automation/acquisition/extractor.py` | 209 | `f"evidence={evidence_blob[:400]}"` |
| `automation/acquisition/extractor.py` | 290 | `evidence = text[:500]` |
| `automation/acquisition/extractor.py` | 293 | `"Signal Name": title[:200],` |
| `automation/acquisition/extractor.py` | 331 | `canonical_name=title[:120],` |
| `automation/acquisition/performance.py` | 56 | `for r in rows[:30]` |
| `automation/acquisition/performance.py` | 158 | `f"{(c.get('error') or '—')[:40]} \|"` |
| `automation/acquisition/discovery.py` | 37 | `"title": (title or "")[:200],` |
| `automation/acquisition/discovery.py` | 121 | `published = (child.text or "").strip()[:40]` |
| `automation/acquisition/discovery.py` | 144 | `lastmod = child.text.strip()[:40]` |
| `automation/acquisition/reports.py` | 60 | `errs = "; ".join(st.get("errors") or [])[:80] or "—"` |
| `automation/acquisition/reports.py` | 95 | `f"{(c.get('error') or '—')[:60]} \|"` |
| `automation/acquisition/reports.py` | 106 | `cl.append(f"- urls_sample: {', '.join((c.get('urls') or [])[:3]) or '—'}")` |
| `automation/acquisition/reports.py` | 135 | `f"{d.get('size') or d.get('bytes') or 0} \| {(d.get('url') or '')[:80]} \|"` |
| `automation/acquisition/reports.py` | 159 | `f"{(c.get('reject_reason') or '—')[:50]} \|"` |
| `automation/acquisition/reports.py` | 170 | `candl.append(f"> {snip[:500]}")` |
| `automation/acquisition/reports.py` | 234 | `el.append(f"> {ch['evidence_snippet'][:500]}")` |
| `automation/acquisition/pipeline.py` | 31 | `process_budget,` |
| `automation/acquisition/pipeline.py` | 152 | `selected = [cid for cid, c in enabled_cfgs.items() if not c.get("dry_run")][:6]` |
| `automation/acquisition/pipeline.py` | 154 | `selected = list(enabled_cfgs.keys())[:4]` |
| `automation/acquisition/pipeline.py` | 179 | `{"id": s.get("id"), "score": s.get("_rank_score")} for s in sources[:12]` |
| `automation/acquisition/pipeline.py` | 205 | `emit("Mission", f"Target dataset={dataset} · query={query_text[:100]}")` |
| `automation/acquisition/pipeline.py` | 288 | `row["urls"] = [r.url for r in found[:5]]` |
| `automation/acquisition/pipeline.py` | 454 | `if _lim.get("max_documents") is not None:` |
| `automation/acquisition/pipeline.py` | 455 | `policy_hard = int(_lim["max_documents"])` |
| `automation/acquisition/pipeline.py` | 456 | `if _lim.get("max_documents_per_session") is not None:` |
| `automation/acquisition/pipeline.py` | 457 | `policy_soft = int(_lim["max_documents_per_session"])` |
| `automation/acquisition/pipeline.py` | 463 | `budget = process_budget(` |
| `automation/acquisition/pipeline.py` | 465 | `soft_limit=max(int(limit or 0), int(policy_soft or 0)) or None,` |
| `automation/acquisition/pipeline.py` | 466 | `hard_limit=policy_hard,` |
| `automation/acquisition/pipeline.py` | 497 | `"process_budget": budget,` |
| `automation/acquisition/pipeline.py` | 541 | `emit("Downloading", f"Downloading report {str(res.title or '')[:80]}")` |
| `automation/acquisition/pipeline.py` | 569 | `d.setdefault("metadata", {})["text_excerpt"] = str(dm["text"])[:8000]` |
| `automation/acquisition/pipeline.py` | 664 | `text=text_fp[:5000],` |
| `automation/acquisition/pipeline.py` | 777 | `for p in sorted(alt_incoming.glob("*.json"))[:24]:` |
| `automation/acquisition/pipeline.py` | 835 | `f"Failures: {audit['failures'][:5]}"` |
| `automation/acquisition/pipeline.py` | 930 | `"evidence_snippet": snip[:500],` |
| `automation/acquisition/pipeline.py` | 1596 | `doc_id = f"DOC-{checksum[:12].upper()}"` |
| `automation/acquisition/pipeline.py` | 1617 | `"text_excerpt": text[:8000],` |
| `automation/acquisition/throughput_ops.py` | 51 | `def process_budget(` |
| `automation/acquisition/throughput_ops.py` | 54 | `soft_limit: int \| None = None,` |
| `automation/acquisition/throughput_ops.py` | 55 | `hard_limit: int \| None = None,` |
| `automation/acquisition/throughput_ops.py` | 76 | `elif soft_limit is not None and soft_limit > 0:` |
| `automation/acquisition/throughput_ops.py` | 77 | `ceiling = max(int(soft_limit), adaptive_floor)` |
| `automation/acquisition/throughput_ops.py` | 80 | `if hard_limit is not None and hard_limit > 0:` |
| `automation/acquisition/throughput_ops.py` | 81 | `ceiling = min(ceiling, int(hard_limit))` |
| `automation/acquisition/throughput_ops.py` | 161 | `year = int("".join(c for c in pub[:4] if c.isdigit()) or "0")` |
| `automation/acquisition/throughput_ops.py` | 581 | `"top_mission": top_mission[:80],` |
| `automation/acquisition/throughput_ops.py` | 701 | `for i, r in enumerate(ranked[:25], 1):` |
| `automation/acquisition/throughput_ops.py` | 805 | `for i, r in enumerate(ranked[:20], 1):` |
| `automation/acquisition/download_manager.py` | 142 | `url=url, content_hash=content_hash, text=text[:5000]` |
| `automation/acquisition/download_manager.py` | 162 | `doc_id = f"DOC-{content_hash[:12].upper()}"` |
| `automation/acquisition/download_manager.py` | 184 | `document_id=f"DOC-{content_hash[:12].upper()}",` |
| `automation/acquisition/pdf_extract.py` | 29 | `"text": text[:200000],` |
| `automation/acquisition/pdf_extract.py` | 56 | `"text": text[:200000],` |
| `automation/acquisition/library_extract.py` | 243 | `f"evidence={evidence[:400]}"` |
| `automation/acquisition/library_extract.py` | 290 | `return normalize_text(text[start:end])[:160]` |
| `automation/acquisition/library_extract.py` | 358 | `name = normalize_text(m.group(0))[:120]` |
| `automation/acquisition/library_extract.py` | 376 | `return out[:6]` |
| `automation/acquisition/library_extract.py` | 402 | `pains = _find_terms(text, _PAIN_TERMS, limit=3)` |
| `automation/acquisition/library_extract.py` | 403 | `goals = _find_terms(text, _GOAL_TERMS, limit=3)` |
| `automation/acquisition/library_extract.py` | 416 | `persona_name = f"{role} — {iname or 'Industry'}"[:160]` |
| `automation/acquisition/library_extract.py` | 423 | `evidence_snippets(text, role) or [text[:300]]` |
| `automation/acquisition/library_extract.py` | 424 | `)[:800]` |
| `automation/acquisition/library_extract.py` | 462 | `"Description": evidence[:1500],` |
| `automation/acquisition/library_extract.py` | 464 | `"Last Updated": utc_now_iso()[:10],` |
| `automation/acquisition/library_extract.py` | 488 | `"evidence": [evidence[:400]],` |
| `automation/acquisition/library_extract.py` | 550 | `snips = evidence_snippets(text, role) or [text[:300]]` |
| `automation/acquisition/library_extract.py` | 551 | `evidence = " … ".join(snips)[:800]` |
| `automation/acquisition/library_extract.py` | 566 | `responsibility = snips[0][:300] if snips else ""` |
| `automation/acquisition/library_extract.py` | 592 | `"Description": evidence[:1500],` |
| `automation/acquisition/library_extract.py` | 594 | `"Last Updated": utc_now_iso()[:10],` |
| `automation/acquisition/library_extract.py` | 618 | `"evidence": [evidence[:400]],` |
| `automation/acquisition/library_extract.py` | 669 | `s = normalize_text(m.group(0))[:200]` |
| `automation/acquisition/library_extract.py` | 677 | `matches = [title[:200]]` |
| `automation/acquisition/library_extract.py` | 695 | `snips = evidence_snippets(text, law.split()[0] if law else "regulation") or [text[:300]]` |
| `automation/acquisition/library_extract.py` | 696 | `evidence = " … ".join(snips)[:800]` |
| `automation/acquisition/library_extract.py` | 724 | `effective = published[:10] if published else ""` |
| `automation/acquisition/library_extract.py` | 742 | `"Regulation Name": law[:240],` |
| `automation/acquisition/library_extract.py` | 749 | `"Summary": evidence[:1500],` |
| `automation/acquisition/library_extract.py` | 752 | `"Last Updated": utc_now_iso()[:10],` |
| `automation/acquisition/library_extract.py` | 770 | `canonical_name=law[:120],` |
| `automation/acquisition/library_extract.py` | 776 | `"evidence": [evidence[:400]],` |
| `automation/acquisition/library_extract.py` | 820 | `for rtype in risk_hits[:3]:` |
| `automation/acquisition/library_extract.py` | 823 | `name = f"{rtype.title()} — {iname or 'Industry'}"[:200]` |
| `automation/acquisition/library_extract.py` | 826 | `snips = evidence_snippets(text, rtype.split()[0]) or [text[:300]]` |
| `automation/acquisition/library_extract.py` | 827 | `evidence = " … ".join(snips)[:800]` |
| `automation/acquisition/library_extract.py` | 844 | `mitigation = normalize_text(m.group(0))[:200]` |
| `automation/acquisition/library_extract.py` | 868 | `"Description": evidence[:1500],` |
| `automation/acquisition/library_extract.py` | 870 | `"Last Updated": utc_now_iso()[:10],` |
| `automation/acquisition/library_extract.py` | 894 | `"evidence": [evidence[:400]],` |
| `automation/acquisition/library_extract.py` | 929 | `trend_title = title[:200] if title else f"Industry trend — {hits[0] if hits else 'outlook'}"` |
| `automation/acquisition/library_extract.py` | 946 | `evidence = text[:500]` |
| `automation/acquisition/library_extract.py` | 975 | `"Description": evidence[:1500],` |
| `automation/acquisition/library_extract.py` | 977 | `"Last Updated": utc_now_iso()[:10],` |
| `automation/acquisition/library_extract.py` | 995 | `canonical_name=trend_title[:120],` |
| `automation/acquisition/library_extract.py` | 1001 | `"evidence": [evidence[:400]],` |
| `automation/acquisition/library_extract.py` | 1047 | `snips = evidence_snippets(text, name.split()[0]) or [text[:300]]` |
| `automation/acquisition/library_extract.py` | 1048 | `evidence = " … ".join(snips)[:800]` |
| `automation/acquisition/library_extract.py` | 1056 | `strength = normalize_text(m.group(0))[:200]` |
| `automation/acquisition/library_extract.py` | 1062 | `weakness = normalize_text(m.group(0))[:200]` |
| `automation/acquisition/library_extract.py` | 1069 | `products = normalize_text(m.group(0))[:200]` |
| `automation/acquisition/library_extract.py` | 1087 | `"Competitor Name": name[:200],` |
| `automation/acquisition/library_extract.py` | 1089 | `"Company Description": evidence[:800],` |
| `automation/acquisition/library_extract.py` | 1112 | `"Last Updated": utc_now_iso()[:10],` |
| `automation/acquisition/library_extract.py` | 1130 | `canonical_name=name[:120],` |
| `automation/acquisition/library_extract.py` | 1136 | `"evidence": [evidence[:400]],` |
| `automation/acquisition/discovery_pkg/providers.py` | 30 | `"title": (title or "")[:200],` |
| `automation/acquisition/discovery_pkg/providers.py` | 31 | `"snippet": (snippet or "")[:400],` |
| `automation/acquisition/discovery_pkg/providers.py` | 73 | `"max_results": 1,` |
| `automation/acquisition/discovery_pkg/providers.py` | 277 | `max_results = _provider_page_cap("tavily", limit)` |
| `automation/acquisition/discovery_pkg/providers.py` | 283 | `"max_results": max_results,` |
| `automation/acquisition/discovery_pkg/providers.py` | 310 | `snippet = (raw[:400] if raw else content[:400])` |
| `automation/acquisition/discovery_pkg/providers.py` | 318 | `row["raw_content_preview"] = raw[:2000]` |
| `automation/acquisition/discovery_pkg/audit.py` | 108 | `h_stat = {"ok": False, "status": "error", "message": str(exc)[:120]}` |
| `automation/acquisition/discovery_pkg/audit.py` | 255 | `"text": line.strip()[:200],` |
| `automation/acquisition/discovery_pkg/audit.py` | 509 | `for hit in limits[:400]:` |
| `automation/acquisition/discovery_pkg/audit.py` | 583 | `f"feed-only path + previous hard caps (max_urls=20, discover limit=5).",` |
| `automation/acquisition/discovery_pkg/audit.py` | 624 | `f"{p.get('operational_status')} \| `{json.dumps(p.get('_rank_components') or {})[:80]}` \|"` |
| `automation/acquisition/discovery_pkg/reports.py` | 87 | `for q in (analytics.get("query_stats") or [])[:80]:` |
| `automation/acquisition/discovery_pkg/reports.py` | 89 | `f"\| {q.get('provider_id')} \| `{(q.get('query') or '')[:80]}` \| "` |
| `automation/acquisition/discovery_pkg/reports.py` | 121 | `f"\| {(a.get('url') or '')[:90]} \| {a.get('source_id')} \| "` |
| `automation/acquisition/discovery_pkg/reports.py` | 122 | `f"{a.get('provider_id')} \| {(a.get('title') or '')[:60]} \|"` |
| `automation/acquisition/discovery_pkg/reports.py` | 139 | `f"\| {(r.get('url') or '')[:80]} \| {r.get('reason')} \| "` |
| `automation/acquisition/discovery_pkg/layer.py` | 88 | `"max_documents": int(lim["max_documents"])` |
| `automation/acquisition/discovery_pkg/layer.py` | 89 | `if lim.get("max_documents") is not None` |
| `automation/acquisition/discovery_pkg/layer.py` | 91 | `"max_documents_per_session": int(lim["max_documents_per_session"])` |
| `automation/acquisition/discovery_pkg/layer.py` | 92 | `if lim.get("max_documents_per_session") is not None` |
| `automation/acquisition/discovery_pkg/layer.py` | 173 | `max_queries: int \| None = None,` |
| `automation/acquisition/discovery_pkg/layer.py` | 174 | `max_urls: int \| None = None,` |
| `automation/acquisition/discovery_pkg/layer.py` | 182 | `max_queries / max_urls are optional overrides; default is adaptive budgets.` |
| `automation/acquisition/discovery_pkg/layer.py` | 240 | `policy_max_documents=policy.get("max_documents"),` |
| `automation/acquisition/discovery_pkg/layer.py` | 241 | `policy_max_per_session=policy.get("max_documents_per_session"),` |
| `automation/acquisition/discovery_pkg/layer.py` | 256 | `policy_max_documents=policy.get("max_documents"),` |
| `automation/acquisition/discovery_pkg/layer.py` | 257 | `policy_max_per_session=policy.get("max_documents_per_session"),` |
| `automation/acquisition/discovery_pkg/layer.py` | 261 | `q_budget = int(max_queries) if max_queries is not None else budget.query_budget` |
| `automation/acquisition/discovery_pkg/layer.py` | 262 | `url_budget = int(max_urls) if max_urls is not None else budget.url_budget` |
| `automation/acquisition/discovery_pkg/layer.py` | 264 | `if max_urls is not None and max_urls < budget.url_budget and float(gap.get("knowledge_gap_score") or 0) > 20:` |
| `automation/acquisition/discovery_pkg/layer.py` | 266 | `if max_queries is not None and max_queries < budget.query_budget and float(gap.get("knowledge_gap_score") or 0) > 20:` |
| `automation/acquisition/discovery_pkg/layer.py` | 281 | `max_queries=q_budget,` |
| `automation/acquisition/discovery_pkg/layer.py` | 659 | `title=str(a.get("title") or a.get("url") or "Discovered document")[:200],` |
| `automation/acquisition/discovery_pkg/layer.py` | 721 | `"query_stats": query_stats[:200],` |
| `automation/acquisition/discovery_pkg/layer.py` | 749 | `for a in accepted[:200]` |
| `automation/acquisition/discovery_pkg/layer.py` | 758 | `for r in rejected[:100]` |
| `automation/acquisition/discovery_pkg/cache.py` | 72 | `"results": results[:50],` |
| `automation/acquisition/discovery_pkg/query_engine.py` | 66 | `max_queries: int = 24,` |
| `automation/acquisition/discovery_pkg/query_engine.py` | 78 | `topic = " ".join(terms[:4])` |
| `automation/acquisition/discovery_pkg/query_engine.py` | 104 | `if len(queries) < max_queries and terms:` |
| `automation/acquisition/discovery_pkg/query_engine.py` | 115 | `if len(queries) >= max_queries:` |
| `automation/acquisition/discovery_pkg/query_engine.py` | 119 | `if len(queries) < max_queries:` |
| `automation/acquisition/discovery_pkg/query_engine.py` | 145 | `if len(out) >= max_queries:` |
| `automation/acquisition/fulltext/quality.py` | 27 | `if rep == "pdf" or raw[:4] == b"%PDF":` |
| `automation/acquisition/fulltext/quality.py` | 38 | `if rep == "metadata_json" or "json" in ct or text.lstrip()[:1] in "{[":` |
| `automation/acquisition/fulltext/quality.py` | 45 | `return strip_html(text)[:5000]` |
| `automation/acquisition/fulltext/quality.py` | 57 | `for i in o[:100]:` |
| `automation/acquisition/fulltext/quality.py` | 82 | `tables = len(re.findall(r"(?i)<table\|\btable\b", usable + (raw[:20000].decode("utf-8", errors="replace") if raw else "")))` |
| `automation/acquisition/fulltext/quality.py` | 84 | `figures = len(re.findall(r"(?i)\bfigure\b\|\bfig\.\s*\d\|<img\b", usable + (raw[:10000].decode("utf-8", errors="replace") if raw else "")))` |
| `automation/acquisition/fulltext/chain.py` | 114 | `"records": list(self.records)[:200],` |
| `automation/acquisition/fulltext/chain.py` | 164 | `head = p.read_text(encoding="utf-8", errors="replace")[:200]` |
| `automation/acquisition/fulltext/chain.py` | 176 | `rep = "metadata_json" if "json" in ct.lower() or (raw[:1] in (b"{", b"[")) else (` |
| `automation/acquisition/fulltext/chain.py` | 179 | `if raw[:4] == b"%PDF":` |
| `automation/acquisition/fulltext/chain.py` | 218 | `document_id = str(doc.get("document_id") or f"DOC-{hashlib.sha256(url.encode()).hexdigest()[:12].upper()}")` |
| `automation/acquisition/fulltext/chain.py` | 276 | `chain_log.append({"step": "crossref", "ok": False, "error": str(exc)[:120]})` |
| `automation/acquisition/fulltext/chain.py` | 286 | `chain_log.append({"step": "doi.org", "ok": False, "error": str(exc)[:120]})` |
| `automation/acquisition/fulltext/chain.py` | 296 | `chain_log.append({"step": "openalex_id", "ok": False, "error": str(exc)[:120]})` |
| `automation/acquisition/fulltext/chain.py` | 310 | `chain_log.append({"step": "discover", "ok": False, "error": str(exc)[:120]})` |
| `automation/acquisition/fulltext/chain.py` | 331 | `dl = {"ok": False, "error": str(exc)[:120], "url": u, "failure_kind": "failed"}` |
| `automation/acquisition/fulltext/chain.py` | 340 | `{"step": "download", "url": u[:100], "ok": False, "error": dl.get("error")}` |
| `automation/acquisition/fulltext/chain.py` | 369 | `"url": u[:100],` |
| `automation/acquisition/fulltext/chain.py` | 541 | `meta["text_excerpt"] = readable[:80000]` |
| `automation/acquisition/fulltext/open_access.py` | 143 | `"abstract": abstract[:4000],` |
| `automation/acquisition/fulltext/open_access.py` | 213 | `q = f'ti:"{title[:120]}"'` |
| `automation/acquisition/fulltext/open_access.py` | 216 | `api = "http://export.arxiv.org/api/query?" + urlencode({"search_query": q, "start": 0, "max_results": 3})` |
| `automation/acquisition/fulltext/ranking.py` | 34 | `head = raw[:16] if raw else b""` |
| `automation/acquisition/fulltext/ranking.py` | 42 | `if "xml" in ct or head.startswith(b"<?xml") or (head.startswith(b"<") and b"xmlns" in raw[:500]):` |
| `automation/acquisition/fulltext/ranking.py` | 43 | `if b"<html" in raw[:500].lower() or b"<!doctype html" in raw[:200].lower():` |
| `automation/acquisition/fulltext/ranking.py` | 46 | `if "json" in ct or (raw[:1] in (b"{", b"[") and b'"' in raw[:200]):` |
| `automation/acquisition/fulltext/ranking.py` | 52 | `if "html" in ct or b"<html" in raw[:500].lower() or b"<!doctype html" in raw[:200].lower():` |
| `automation/acquisition/fulltext/reports.py` | 163 | `for r in records[:40]` |
| `automation/acquisition/fulltext/doi.py` | 33 | `blob = str(src)[:8000]` |
| `automation/acquisition/fulltext/doi.py` | 125 | `"title": str(title or "")[:300],` |
| `automation/acquisition/fulltext/doi.py` | 133 | `"abstract": abstract[:4000],` |
| `automation/acquisition/fulltext/doi.py` | 136 | `"raw_message_keys": list(msg.keys())[:40],` |
| `automation/acquisition/fulltext/downloader.py` | 56 | `text_head = raw[:12000].decode("utf-8", errors="replace")` |
| `automation/acquisition/fulltext/downloader.py` | 118 | `h = hashlib.sha256(raw).hexdigest()[:16]` |
| `automation/config/product_targets.yaml` | 3 | `# hard_limit: null means the factory never stops for an arbitrary numeric ceiling.` |
| `automation/config/product_targets.yaml` | 38 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 43 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 48 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 53 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 58 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 63 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 68 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 73 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 78 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 83 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 88 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 93 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 98 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 103 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 108 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 113 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 118 | `hard_limit: null` |
| `automation/config/product_targets.yaml` | 123 | `hard_limit: null` |
| `automation/config/policies.yaml` | 27 | `max_documents: 500` |
| `automation/config/policies.yaml` | 31 | `max_documents_per_session: 200` |
| `automation/learning/live_runtime.py` | 69 | `session_id = f"SES-{utc_now_iso()[:10].replace('-', '')}-{uuid4().hex[:6].upper()}"` |
| `automation/learning/live_runtime.py` | 126 | `correlation_id = correlation_id or f"CORR-{uuid4().hex[:12].upper()}"` |
| `automation/learning/live_runtime.py` | 424 | `current_task=detail[:120],` |
| `automation/learning/live_runtime.py` | 431 | `# process_budget targets ≥90% of discovered docs within adaptive download budget.` |
| `automation/learning/live_runtime.py` | 437 | `limit=64,` |
| `automation/learning/live_runtime.py` | 473 | `console_text[:4000],` |
| `automation/learning/live_runtime.py` | 489 | `for c in (acq.get("connectors") or [])[:12]` |
| `automation/learning/live_runtime.py` | 530 | `"failures": (acq.get("failures") or [])[:10],` |
| `automation/learning/live_runtime.py` | 549 | `task=reason[:120],` |
| `automation/learning/heartbeat.py` | 136 | `data["last_error"] = (error or "production_failed")[:500]` |
| `automation/learning/heartbeat.py` | 139 | `data["last_error"] = str(error)[:500]` |
| `automation/learning/session_store.py` | 41 | `return f"SESSION-{day}-{uuid4().hex[:6].upper()}"` |
| `automation/learning/first_cycle.py` | 145 | `limit=3,` |
| `automation/learning/first_cycle.py` | 187 | `seed["Last Updated"] = utc_now_iso()[:10]` |
| `automation/learning/state/acquisition_performance.json` | 650 | `"process_budget": 97,` |
| `automation/learning/state/manufacturing_state.json` | 64 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 83 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 101 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 112 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 131 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 149 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 160 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 179 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 197 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 208 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 227 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 245 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 256 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 275 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 293 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 304 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 323 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 341 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 352 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 371 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 389 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 400 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 419 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 437 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 448 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 467 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 485 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 496 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 515 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 533 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 544 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 563 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 581 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 592 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 611 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 629 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 640 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 659 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 677 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 688 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 707 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 725 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 736 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 755 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 773 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 784 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 803 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 821 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 832 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 851 | `"hard_limit": null` |
| `automation/learning/state/manufacturing_state.json` | 869 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 884 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 907 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 930 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 953 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 976 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 999 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 1022 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 1045 | `"hard_limit": null,` |
| `automation/learning/state/manufacturing_state.json` | 1069 | `"hard_limit": null,` |
| `automation/search/query_planner.py` | 54 | `limit=5,` |
| `automation/search/query_planner.py` | 63 | `limit=max(1, min(limit, 50)),` |
| `automation/search/orchestrator.py` | 52 | `connectors, preferred_types=preferred_types, limit=8` |
| `automation/ci/learning_session.py` | 119 | `job=(mission or instruction or "production cycle")[:160],` |
| `automation/ci/learning_session.py` | 472 | `summary=str(session.get("summary") or "")[:160],` |
| `automation/ci/learning_session.py` | 477 | `error=str(err0)[:500],` |
| `automation/ci/learning_session.py` | 526 | `lines.append(f"- `{json.dumps(e, ensure_ascii=False)[:500]}`")` |
| `automation/ci/learning_session.py` | 621 | `ctx.messages.append(f"instruction={instruction[:120]}")` |
| `automation/ci/learning_session.py` | 694 | `"sessions": list_sessions(repo_root, limit=50),` |
| `automation/ci/huggingface_publish.py` | 43 | `print(f"GITHUB_SHA: {(os.environ.get('GITHUB_SHA') or 'n/a')[:12]}", flush=True)` |
| `automation/ci/industry_knowledge_cycle.py` | 211 | `"Last Updated": retrieved[:10],` |
| `automation/ci/industry_knowledge_cycle.py` | 319 | `"Last Updated": retrieved[:10],` |
| `automation/ci/industry_knowledge_cycle.py` | 421 | `"Last Updated": retrieved[:10],` |
| `automation/ci/industry_knowledge_cycle.py` | 524 | `"Last Updated": retrieved[:10],` |
| `automation/ci/industry_knowledge_cycle.py` | 616 | `lu = (r.get("Last Updated") or "")[:10]` |
| `automation/ci/planner.py` | 170 | `top = gaps[:10]` |
| `automation/ci/planner.py` | 187 | `"next_sprint_candidates": [g.dataset for g in top[:5]],` |
| `automation/ci/planner.py` | 223 | `for g in gaps[:20]:` |
| `automation/ci/validate_repo.py` | 227 | `if path.parts[:1] == (".github",) or ".github" in path.parts:` |

## Target state

Fixed document caps (5/10/20/50) must not stop discovery. Use adaptive budgets; retain only provider API page-size maxima and optional policy safety rails.
