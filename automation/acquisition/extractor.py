"""Grounded extraction — document → knowledge candidates.

Never invents business facts. Every candidate field is either:
  - literal document evidence (title, abstract, snippet), or
  - structural provenance (source, mission, dates, confidence), or
  - an industry name matched by alias that appears in the document text.
"""

from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path
from typing import Any, Optional

from automation.acquisition.normalize import (
    evidence_snippets,
    match_industry_mentions,
    normalize_country,
    normalize_text,
)
from automation.acquisition.pdf_extract import extract_pdf
from automation.lib.models import CandidateRecord, Provenance, ValidationStatus, utc_now_iso
from automation.lib.paths import find_repo_root

EXTRACTION_VERSION = "acquisition-grounded-2.0.0"


def _next_industry_id(csv_path: Path) -> str:
    max_n = 0
    if csv_path.exists():
        with csv_path.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                m = re.match(r"IND-(\d+)", (row.get("Industry ID") or "").strip(), re.I)
                if m:
                    max_n = max(max_n, int(m.group(1)))
    return f"IND-{max_n + 1:06d}"


def _existing_industry_names(csv_path: Path) -> dict[str, str]:
    """name_lower → Industry ID"""
    out: dict[str, str] = {}
    if not csv_path.exists():
        return out
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            name = (row.get("Industry Name") or "").strip()
            iid = (row.get("Industry ID") or "").strip()
            if name and iid:
                out[name.lower()] = iid
    return out


def document_text(doc: dict[str, Any]) -> str:
    """Assemble readable text from document metadata / local file."""
    parts: list[str] = []
    title = str(doc.get("title") or "")
    if title:
        parts.append(title)
    meta = doc.get("metadata") or {}
    for key in ("text_excerpt", "snippet", "abstract"):
        v = meta.get(key) or doc.get(key)
        if v:
            parts.append(str(v))
    # concepts from OpenAlex
    concepts = meta.get("concepts")
    if isinstance(concepts, list) and concepts:
        parts.append("Concepts: " + ", ".join(str(c) for c in concepts))

    local = doc.get("local_path")
    if local:
        p = Path(str(local))
        if p.exists() and p.is_file():
            suffix = p.suffix.lower()
            if suffix == ".pdf":
                pdf = extract_pdf(p)
                if pdf.get("ok") and pdf.get("text"):
                    parts.append(str(pdf["text"])[:50000])
            else:
                try:
                    if p.stat().st_size < 2_000_000:
                        raw = p.read_text(encoding="utf-8", errors="replace")
                        # strip html tags lightly
                        raw = re.sub(r"<script[\s\S]*?</script>", " ", raw, flags=re.I)
                        raw = re.sub(r"<style[\s\S]*?</style>", " ", raw, flags=re.I)
                        parts.append(normalize_text(raw)[:50000])
                except Exception:  # noqa: BLE001
                    pass
    return normalize_text("\n\n".join(parts))


def extract_industry_candidates(
    documents: list[dict[str, Any]],
    *,
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
    max_candidates: int = 5,
) -> list[CandidateRecord]:
    """Extract new industry candidates grounded in acquired documents."""
    root = repo_root or find_repo_root()
    industry_csv = root / "domains" / "business_development" / "industry_library.csv"
    existing = _existing_industry_names(industry_csv)
    next_id_n = int(_next_industry_id(industry_csv).split("-")[1])

    candidates: list[CandidateRecord] = []
    used_names: set[str] = set()

    for doc in documents:
        if len(candidates) >= max_candidates:
            break
        text = document_text(doc)
        if len(text) < 40:
            continue
        mentions = match_industry_mentions(text)
        # Prefer expandable (new) industries first
        mentions.sort(key=lambda m: (0 if m.get("expandable") else 1, m["name"]))

        trust = float(doc.get("trust_score") or 0.85)
        source_id = str(doc.get("source_id") or "SRC-UNKNOWN")
        url = str(doc.get("original_url") or doc.get("url") or "")
        retrieved = str(doc.get("retrieved_at") or utc_now_iso())
        published = str(
            (doc.get("metadata") or {}).get("published_at")
            or doc.get("published_at")
            or ""
        )
        country = normalize_country(text)

        for mention in mentions:
            if len(candidates) >= max_candidates:
                break
            name = str(mention["name"])
            if name.lower() in existing or name.lower() in used_names:
                continue  # already in dataset — append-only, no overwrite

            # Require evidence snippets for the matched alias
            alias = str(mention.get("matched_alias") or name)
            snips = evidence_snippets(text, alias)
            if not snips:
                snips = evidence_snippets(text, name)
            if not snips:
                continue

            # Description = grounded evidence only (no invented claims)
            evidence_blob = " … ".join(snips)[:1200]
            conf = min(0.95, max(0.80, trust * 0.95))
            if mention.get("expandable") and len(snips) >= 2:
                conf = min(0.95, conf + 0.03)
            # Strong multi-snippet evidence from high-trust sources → auto-publish band (≥0.92)
            if trust >= 0.90 and len(snips) >= 2 and len(evidence_blob) >= 160:
                conf = min(0.95, max(conf, 0.92))
            elif trust >= 0.88 and len(snips) >= 3:
                conf = min(0.95, max(conf, 0.92))

            iid = f"IND-{next_id_n:06d}"
            next_id_n += 1
            used_names.add(name.lower())

            payload = {
                "Industry ID": iid,
                "Industry Name": name,
                "Industry Category": str(mention.get("category") or "Services"),
                "Industry Description": (
                    f"Industry sector identified in trusted source document. "
                    f"Evidence: {evidence_blob}"
                )[:2000],
                "Business Characteristics": "",
                "Typical Company Size": "",
                "Average Employee Range": "",
                "Typical Annual Revenue": "",
                "Main Business Processes": "",
                "Common Departments": "",
                "Digital Maturity Level": "",
                "Common Technologies": "",
                "Common Business Challenges": "",
                "Common Pain Points": "",
                "Business Goals": "",
                "Buying Triggers": "",
                "Buying Criteria": "",
                "Typical Decision Makers": "",
                "Procurement Method": "",
                "Average Sales Cycle": "",
                "Budget Characteristics": "",
                "Major Risks": "",
                "Recommended Products": "",
                "Cross Selling Opportunities": "",
                "Upselling Opportunities": "",
                "Main Competitors": "",
                "Industry Regulations": "",
                "Industry Trends": "",
                "SWOT Summary": "",
                "Data Sources": (
                    f"source_ids={source_id}; urls={url}; "
                    f"published={published}; retrieved={retrieved}; "
                    f"confidence={conf:.2f}; version={EXTRACTION_VERSION}; "
                    f"country={country or 'multi'}; matched_alias={alias}; "
                    f"discovery_provider={(doc.get('metadata') or {}).get('discovery_provider') or 'connector'}"
                ),
                "Last Updated": utc_now_iso()[:10],
                "Notes": (
                    f"provenance: source={source_id}; published_date={published}; "
                    f"retrieved_date={retrieved}; confidence={conf:.2f}; "
                    f"version={EXTRACTION_VERSION}; mission={mission_id}; "
                    f"document={doc.get('document_id')}; entity={name}; "
                    f"discovery_provider={(doc.get('metadata') or {}).get('discovery_provider') or 'connector'}; "
                    f"append_only=true; extraction=grounded_text; "
                    f"evidence={evidence_blob[:400]}"
                ),
            }

            provenance = Provenance(
                source_id=source_id,
                source_url=url,
                retrieved_at=retrieved,
                confidence=conf,
                extraction_version=EXTRACTION_VERSION,
                validation_status=ValidationStatus.PENDING.value,
                published_at=published or None,
            )
            cand = CandidateRecord.create(
                entity_type="industry_library",
                entity_id=iid,
                target_dataset="industry_library",
                payload=payload,
                provenance=provenance,
                canonical_name=name,
                metadata={
                    "mission_id": mission_id,
                    "session_id": session_id,
                    "document_id": doc.get("document_id"),
                    "connector_id": doc.get("connector_id"),
                    "matched_alias": alias,
                    "evidence": snips,
                    "extraction": "grounded_text",
                    "dataset": "industry_library",
                    "schema_version": "1.0",
                },
            )
            candidates.append(cand)

        # If no expandable industry matched, still emit a business_signal candidate
        # grounded in the document title (secondary dataset path).
        if not candidates and text:
            # handled after loop for signals
            pass

    return candidates


def extract_business_signal_candidates(
    documents: list[dict[str, Any]],
    *,
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
    max_candidates: int = 3,
) -> list[CandidateRecord]:
    """Extract business signals from document titles/abstracts (grounded only)."""
    root = repo_root or find_repo_root()
    signal_csv = root / "domains" / "business_development" / "business_signal_library.csv"
    # determine next signal id
    max_n = 0
    if signal_csv.exists():
        with signal_csv.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                m = re.match(r"SIG-(\d+)", (row.get("Signal ID") or "").strip(), re.I)
                if m:
                    max_n = max(max_n, int(m.group(1)))

    # headers if empty file
    candidates: list[CandidateRecord] = []
    for doc in documents[: max_candidates * 2]:
        if len(candidates) >= max_candidates:
            break
        title = str(doc.get("title") or "").strip()
        if not title or title.startswith("[dry-run]"):
            continue
        text = document_text(doc)
        if len(text) < 30:
            continue
        max_n += 1
        sid = f"SIG-{max_n:06d}"
        source_id = str(doc.get("source_id") or "SRC-UNKNOWN")
        url = str(doc.get("original_url") or doc.get("url") or "")
        retrieved = str(doc.get("retrieved_at") or utc_now_iso())
        published = str((doc.get("metadata") or {}).get("published_at") or "")
        conf = min(0.92, max(0.80, float(doc.get("trust_score") or 0.85)))
        evidence = text[:500]
        payload = {
            "Signal ID": sid,
            "Signal Name": title[:200],
            "Signal Type": "document_derived",
            "Description": evidence,
            "Industry": "",
            "Source": source_id,
            "Source URL": url,
            "Published Date": published,
            "Retrieved Date": retrieved,
            "Confidence": f"{conf:.2f}",
            "Mission ID": mission_id,
            "Version": EXTRACTION_VERSION,
            "Data Sources": (
                f"source_ids={source_id}; urls={url}; published={published}; "
                f"retrieved={retrieved}; confidence={conf:.2f}; version={EXTRACTION_VERSION}; "
                f"discovery_provider={(doc.get('metadata') or {}).get('discovery_provider') or 'connector'}"
            ),
            "Notes": (
                f"provenance: source={source_id}; document={doc.get('document_id')}; "
                f"mission={mission_id}; "
                f"discovery_provider={(doc.get('metadata') or {}).get('discovery_provider') or 'connector'}; "
                f"append_only=true; extraction=grounded_text"
            ),
        }
        provenance = Provenance(
            source_id=source_id,
            source_url=url,
            retrieved_at=retrieved,
            confidence=conf,
            extraction_version=EXTRACTION_VERSION,
            validation_status=ValidationStatus.PENDING.value,
        )
        candidates.append(
            CandidateRecord.create(
                entity_type="business_signal_library",
                entity_id=sid,
                target_dataset="business_signal_library",
                payload=payload,
                provenance=provenance,
                canonical_name=title[:120],
                metadata={
                    "mission_id": mission_id,
                    "session_id": session_id,
                    "document_id": doc.get("document_id"),
                    "dataset": "business_signal_library",
                    "schema_version": "1.0",
                },
            )
        )
    return candidates


def save_candidate_queue(
    candidates: list[CandidateRecord],
    *,
    repo_root: Path | None = None,
    stage: str = "pending",
) -> list[Path]:
    """Write candidates to automation/queue/candidates/{stage}/ and legacy pending/approved."""
    root = repo_root or find_repo_root()
    # dual path: new candidates queue + existing queue folders
    paths_out: list[Path] = []
    for stage_name in (stage,):
        folders = [
            root / "automation" / "queue" / "candidates" / stage_name,
            root / "automation" / "queue" / stage_name,
        ]
        for folder in folders:
            folder.mkdir(parents=True, exist_ok=True)
        for cand in candidates:
            data = cand.to_dict()
            # ensure required candidate fields
            data.setdefault("dataset", cand.target_dataset)
            data.setdefault("entity", cand.canonical_name)
            data.setdefault("confidence", cand.provenance.confidence)
            data.setdefault("evidence", (cand.metadata or {}).get("evidence") or [])
            data.setdefault("schema_version", (cand.metadata or {}).get("schema_version") or "1.0")
            data.setdefault("mission", (cand.metadata or {}).get("mission_id") or "")
            for folder in folders:
                path = folder / f"{cand.candidate_id}.json"
                import json

                path.write_text(
                    json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                    newline="\n",
                )
                paths_out.append(path)
    return paths_out
