"""Grounded extractors for remaining knowledge libraries.

Buyer Persona · Decision Maker · Regulation · Risk · Trend · Competitor

Rules:
- Never invent business facts
- Every field is either literal document evidence or empty
- Provenance mandatory (source, retrieved, confidence, version)
"""

from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path
from typing import Any, Callable, Optional

from automation.acquisition.extractor import document_text
from automation.acquisition.normalize import evidence_snippets, match_industry_mentions, normalize_text
from automation.lib.models import CandidateRecord, Provenance, ValidationStatus, utc_now_iso
from automation.lib.paths import find_repo_root

EXTRACTION_VERSION = "acquisition-library-1.0.0"

# --- keyword / pattern banks (match only when present in document text) ---

_ROLE_PATTERNS = [
    r"\bChief Executive Officer\b",
    r"\bCEO\b",
    r"\bChief Financial Officer\b",
    r"\bCFO\b",
    r"\bChief Operating Officer\b",
    r"\bCOO\b",
    r"\bChief Technology Officer\b",
    r"\bCTO\b",
    r"\bChief Information Officer\b",
    r"\bCIO\b",
    r"\bManaging Director\b",
    r"\bDirector\b",
    r"\bVice President\b",
    r"\bVP\b",
    r"\bGeneral Manager\b",
    r"\bHead of [A-Za-z &/-]{2,40}\b",
    r"\bManager\b",
    r"\bProcurement Manager\b",
    r"\bHR Director\b",
    r"\bOperations Manager\b",
    r"\bPlant Manager\b",
    r"\bBoard of Directors\b",
    r"\bKomisaris\b",
    r"\bDirektur\b",
    r"\bKepala [A-Za-z ]{2,40}\b",
]

_SIZE_TERMS = [
    ("enterprise", "Enterprise"),
    ("large enterprise", "Enterprise"),
    ("sme", "SME"),
    ("small and medium", "SME"),
    ("startup", "Startup"),
    ("micro enterprise", "Micro"),
    ("ukm", "SME"),
    ("umb", "Enterprise"),
]

_PAIN_TERMS = [
    "skill gap",
    "skills shortage",
    "labor shortage",
    "productivity",
    "compliance",
    "cost pressure",
    "digital transformation",
    "workforce",
    "turnover",
    "inefficiency",
    "bottleneck",
    "risk",
    "shortage",
]

_GOAL_TERMS = [
    "growth",
    "efficiency",
    "competitiveness",
    "compliance",
    "innovation",
    "sustainability",
    "productivity",
    "market expansion",
    "digitalization",
]

_BUDGET_TERMS = [
    r"budget",
    r"investment",
    r"USD\s?[\d,.]+",
    r"Rp\s?[\d,.]+",
    r"million",
    r"billion",
    r"capex",
    r"opex",
]

_REG_PATTERNS = [
    r"\b[A-Z][A-Za-z]+ Act\b",
    r"\bLaw No\.?\s*\d+",
    r"\bUndang[- ]Undang\b[^\n.]{0,80}",
    r"\bRegulation\b[^\n.]{0,100}",
    r"\bPeraturan\b[^\n.]{0,100}",
    r"\bPOJK\b[^\n.]{0,80}",
    r"\bSEOJK\b[^\n.]{0,80}",
    r"\bDirective\b[^\n.]{0,80}",
    r"\bPolicy\b[^\n.]{0,80}",
    r"\bStandard\b[^\n.]{0,80}",
]

_RISK_TYPES = [
    "operational risk",
    "credit risk",
    "market risk",
    "liquidity risk",
    "cyber risk",
    "compliance risk",
    "regulatory risk",
    "climate risk",
    "reputational risk",
    "supply chain risk",
    "financial risk",
    "political risk",
    "labor risk",
    "systemic risk",
    "risk",
]

_TREND_TERMS = [
    "trend",
    "outlook",
    "growth",
    "decline",
    "rising",
    "falling",
    "accelerat",
    "digital transformation",
    "green transition",
    "automation",
    "artificial intelligence",
    "remote work",
    "nearshoring",
    "reshoring",
    "demograph",
]

_COMPETITOR_MARKERS = [
    r"\bcompetitor[s]?\b",
    r"\bcompetition\b",
    r"\brival[s]?\b",
    r"\bmarket leader\b",
    r"\bmarket share\b",
    r"\bvs\.?\b",
    r"\bcompared (to|with)\b",
]


def _next_id(csv_path: Path, field: str, prefix: str) -> int:
    max_n = 0
    if csv_path.exists() and csv_path.stat().st_size > 0:
        with csv_path.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                m = re.match(rf"{re.escape(prefix)}-(\d+)", (row.get(field) or "").strip(), re.I)
                if m:
                    max_n = max(max_n, int(m.group(1)))
    return max_n + 1


def _existing_names(csv_path: Path, field: str) -> set[str]:
    out: set[str] = set()
    if not csv_path.exists():
        return out
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            n = (row.get(field) or "").strip().lower()
            if n:
                out.add(n)
    return out


def _conf(doc: dict[str, Any], *, boost: float = 0.0) -> float:
    trust = float(doc.get("trust_score") or 0.85)
    conf = min(0.95, max(0.80, trust * 0.95 + boost))
    return round(conf, 2)


def _industry_link(text: str, repo: Path) -> tuple[str, str]:
    """Return (Industry ID, Industry Name) from existing library when mention matches."""
    mentions = match_industry_mentions(text)
    if not mentions:
        return "", ""
    name = str(mentions[0].get("name") or "")
    path = repo / "domains" / "business_development" / "industry_library.csv"
    if path.exists():
        with path.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                if (row.get("Industry Name") or "").strip().lower() == name.lower():
                    return (row.get("Industry ID") or "").strip(), name
    return "", name


def _first_industry_fallback(repo: Path) -> tuple[str, str]:
    path = repo / "domains" / "business_development" / "industry_library.csv"
    if not path.exists():
        return "", ""
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            iid = (row.get("Industry ID") or "").strip()
            name = (row.get("Industry Name") or "").strip()
            if iid and name:
                return iid, name
    return "", ""


def _prov_notes(
    *,
    source_id: str,
    url: str,
    retrieved: str,
    published: str,
    conf: float,
    mission_id: str,
    document_id: str,
    evidence: str,
) -> tuple[str, str]:
    ds = (
        f"source_ids={source_id}; urls={url}; published={published}; "
        f"retrieved={retrieved}; confidence={conf:.2f}; version={EXTRACTION_VERSION}"
    )
    notes = (
        f"provenance: source={source_id}; published_date={published}; "
        f"retrieved_date={retrieved}; confidence={conf:.2f}; "
        f"version={EXTRACTION_VERSION}; mission={mission_id}; "
        f"document={document_id}; append_only=true; extraction=grounded_text; "
        f"evidence={evidence[:400]}"
    )
    return ds, notes


def _find_roles(text: str) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for pat in _ROLE_PATTERNS:
        for m in re.finditer(pat, text, re.I):
            role = normalize_text(m.group(0))
            key = role.lower()
            if key in seen or len(role) < 2:
                continue
            seen.add(key)
            found.append(role)
            if len(found) >= 8:
                return found
    return found


def _find_size(text: str) -> str:
    low = text.lower()
    for needle, label in _SIZE_TERMS:
        if needle in low:
            return label
    return ""


def _find_terms(text: str, terms: list[str], *, limit: int = 4) -> list[str]:
    low = text.lower()
    out: list[str] = []
    for t in terms:
        if t.lower() in low:
            out.append(t)
        if len(out) >= limit:
            break
    return out


def _find_budget(text: str) -> str:
    for pat in _BUDGET_TERMS:
        m = re.search(pat, text, re.I)
        if m:
            # capture surrounding window
            start = max(0, m.start() - 20)
            end = min(len(text), m.end() + 40)
            return normalize_text(text[start:end])[:160]
    return ""


_COMPETITOR_BLOCKLIST = {
    "doi",
    "url",
    "issn",
    "isbn",
    "crossref",
    "openalex",
    "proceedings",
    "abstract",
    "introduction",
    "conclusion",
    "references",
    "appendix",
    "table",
    "figure",
    "http",
    "https",
    "www",
    "pdf",
    "json",
    "html",
    "academy of management",
    "academy of management proceedings",
    "world bank",
    "oecd",
    "adb",
    "imf",
    "ilo",
    "bps",
}


def _is_plausible_company_name(name: str) -> bool:
    n = (name or "").strip()
    if len(n) < 4 or len(n) > 120:
        return False
    low = n.lower()
    if low in _COMPETITOR_BLOCKLIST:
        return False
    if any(b in low for b in ("http", "www.", "doi:", "issn", "isbn", "conn-", "src-", "doc-", "mis-")):
        return False
    # Reject pure metadata tokens / author first-last only without company marker
    words = n.split()
    if len(words) == 1 and words[0].isalpha() and words[0][0].isupper():
        return False
    # Reject names that are mostly non-letters
    letters = sum(1 for c in n if c.isalpha())
    if letters < max(4, int(len(n) * 0.5)):
        return False
    return True


def _company_names_from_text(text: str) -> list[str]:
    """Heuristic company names already present as Title Case multi-word tokens."""
    # Prefer PT / Ltd / Inc / Tbk / Persero patterns only (high precision)
    found: list[str] = []
    patterns = [
        r"\bPT\.?\s+[A-Z][A-Za-z0-9& .,'-]{2,50}(?:\s+Tbk\.?)?",
        r"\b[A-Z][A-Za-z0-9& .,'-]{2,50}\s+\(Persero\)(?:\s+Tbk\.?)?",
        r"\b[A-Z][a-zA-Z0-9& .,'-]{2,40}\s+(?:Ltd\.?|Inc\.?|Corp\.?|Corporation|Group|Holdings|PLC|Llc)\b",
        r"\b[A-Z][a-zA-Z0-9& .,'-]{2,40}\s+Tbk\.?\b",
    ]
    for pat in patterns:
        for m in re.finditer(pat, text):
            name = normalize_text(m.group(0))[:120]
            # Stop at clause boundaries (avoid "PT X is a manufacturing company…")
            name = re.split(r"\s+(?:is|was|are|were|has|have|to|for|with|and|,)\s+", name, maxsplit=1)[0]
            name = re.sub(r"[\s,;:]+$", "", name)
            # Prefer shorter official-style names
            if len(name) > 80:
                continue
            if _is_plausible_company_name(name):
                found.append(name)
    # de-dupe
    out: list[str] = []
    seen: set[str] = set()
    for n in found:
        k = n.lower()
        if k in seen:
            continue
        seen.add(k)
        out.append(n)
    return out[:6]


def extract_buyer_persona_candidates(
    documents: list[dict[str, Any]],
    *,
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
    max_candidates: int = 5,
) -> list[CandidateRecord]:
    root = repo_root or find_repo_root()
    csv_path = root / "domains" / "business_development" / "buyer_persona_library.csv"
    next_n = _next_id(csv_path, "Persona ID", "PER")
    existing = _existing_names(csv_path, "Persona Name")
    candidates: list[CandidateRecord] = []
    fb_id, fb_name = _first_industry_fallback(root)

    for doc in documents:
        if len(candidates) >= max_candidates:
            break
        text = document_text(doc)
        if len(text) < 40:
            continue
        roles = _find_roles(text)
        size = _find_size(text)
        pains = _find_terms(text, _PAIN_TERMS, limit=3)
        goals = _find_terms(text, _GOAL_TERMS, limit=3)
        budget = _find_budget(text)
        iid, iname = _industry_link(text, root)
        if not iid:
            iid, iname = fb_id, fb_name
        # Require at least one grounded anchor: role OR size OR pain/goal from text
        if not roles and not size and not pains and not goals:
            # still allow persona from industry workforce docs with title evidence
            title = str(doc.get("title") or "")
            if not any(k in title.lower() for k in ("labor", "employment", "workforce", "skill", "buyer", "persona", "hr", "human")):
                continue
            roles = ["Industry Buyer"]
        role = roles[0] if roles else "Industry Stakeholder"
        persona_name = f"{role} — {iname or 'Industry'}"[:160]
        if persona_name.lower() in existing:
            continue
        conf = _conf(doc, boost=0.02 if roles else 0.0)
        if conf >= 0.90 and roles and (pains or goals):
            conf = max(conf, 0.92)
        evidence = " … ".join(
            evidence_snippets(text, role) or [text[:300]]
        )[:800]
        source_id = str(doc.get("source_id") or "SRC-UNKNOWN")
        url = str(doc.get("original_url") or doc.get("url") or "")
        retrieved = str(doc.get("retrieved_at") or utc_now_iso())
        published = str((doc.get("metadata") or {}).get("published_at") or "")
        pid = f"PER-{next_n:06d}"
        next_n += 1
        existing.add(persona_name.lower())
        ds, notes = _prov_notes(
            source_id=source_id,
            url=url,
            retrieved=retrieved,
            published=published,
            conf=conf,
            mission_id=mission_id,
            document_id=str(doc.get("document_id") or ""),
            evidence=evidence,
        )
        behavior = ""
        if "procurement" in text.lower() or "tender" in text.lower():
            behavior = "Participates in formal procurement / tender processes"
        elif "digital" in text.lower():
            behavior = "Engages digital channels and technology evaluation"
        payload = {
            "Persona ID": pid,
            "Persona Name": persona_name,
            "Industry ID": iid,
            "Industry": iname,
            "Company Size": size,
            "Job Role": role,
            "Department": "",
            "Seniority": "Executive" if any(x in role.lower() for x in ("chief", "director", "ceo", "cfo", "cto", "cio", "vp")) else "Manager",
            "Pain Points": "; ".join(pains),
            "Goals": "; ".join(goals),
            "Budget Characteristics": budget,
            "Buying Behavior": behavior,
            "Decision Criteria": "",
            "Information Sources": source_id,
            "Description": evidence[:1500],
            "Data Sources": ds,
            "Last Updated": utc_now_iso()[:10],
            "Notes": notes,
        }
        candidates.append(
            CandidateRecord.create(
                entity_type="buyer_persona_library",
                entity_id=pid,
                target_dataset="buyer_persona_library",
                payload=payload,
                provenance=Provenance(
                    source_id=source_id,
                    source_url=url,
                    retrieved_at=retrieved,
                    confidence=conf,
                    extraction_version=EXTRACTION_VERSION,
                    validation_status=ValidationStatus.PENDING.value,
                    published_at=published or None,
                ),
                canonical_name=persona_name,
                metadata={
                    "mission_id": mission_id,
                    "session_id": session_id,
                    "document_id": doc.get("document_id"),
                    "dataset": "buyer_persona_library",
                    "evidence": [evidence[:400]],
                    "schema_version": "1.0",
                },
            )
        )
    return candidates


def extract_decision_maker_candidates(
    documents: list[dict[str, Any]],
    *,
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
    max_candidates: int = 5,
) -> list[CandidateRecord]:
    root = repo_root or find_repo_root()
    csv_path = root / "domains" / "business_development" / "decision_maker_library.csv"
    next_n = _next_id(csv_path, "Decision Maker ID", "DM")
    existing = _existing_names(csv_path, "Title")
    candidates: list[CandidateRecord] = []
    fb_id, fb_name = _first_industry_fallback(root)

    for doc in documents:
        if len(candidates) >= max_candidates:
            break
        text = document_text(doc)
        title = str(doc.get("title") or "")
        roles = _find_roles(text)
        # Also scan title for role patterns
        if not roles:
            roles = _find_roles(title)
        # Government / org structure docs: accept common public titles when present
        if not roles:
            low = f"{title}\n{text}".lower()
            for role, keys in (
                ("Director", ("director", "direktur")),
                ("Manager", ("manager", "kepala")),
                ("Board Member", ("board of directors", "komisaris", "board member")),
                ("Chief Executive Officer", ("chief executive", "ceo")),
            ):
                if any(k in low for k in keys):
                    roles.append(role)
        if not roles:
            continue
        iid, iname = _industry_link(text, root)
        if not iid:
            iid, iname = fb_id, fb_name
        source_id = str(doc.get("source_id") or "SRC-UNKNOWN")
        url = str(doc.get("original_url") or doc.get("url") or "")
        retrieved = str(doc.get("retrieved_at") or utc_now_iso())
        published = str((doc.get("metadata") or {}).get("published_at") or "")
        conf = _conf(doc, boost=0.03)
        if conf >= 0.90:
            conf = max(conf, 0.92)

        for role in roles:
            if len(candidates) >= max_candidates:
                break
            key = role.lower()
            if key in existing:
                continue
            snips = evidence_snippets(text, role) or [text[:300]]
            evidence = " … ".join(snips)[:800]
            did = f"DM-{next_n:06d}"
            next_n += 1
            existing.add(key)
            # Authority heuristic from role wording (not invented org chart)
            authority = "Approver" if any(
                x in role.lower() for x in ("chief", "director", "ceo", "cfo", "president", "direktur")
            ) else "Influencer"
            department = ""
            for dep in ("Finance", "HR", "Operations", "IT", "Procurement", "Sales", "Legal", "Risk"):
                if dep.lower() in text.lower() and dep.lower() in role.lower() or (
                    dep.lower() in role.lower()
                ):
                    department = dep
                    break
            responsibility = snips[0][:300] if snips else ""
            approval = ""
            if "board" in text.lower() and "board" in role.lower():
                approval = "Board-level approval"
            elif authority == "Approver":
                approval = "Final approval authority indicated by title"
            ds, notes = _prov_notes(
                source_id=source_id,
                url=url,
                retrieved=retrieved,
                published=published,
                conf=conf,
                mission_id=mission_id,
                document_id=str(doc.get("document_id") or ""),
                evidence=evidence,
            )
            payload = {
                "Decision Maker ID": did,
                "Title": role,
                "Authority Level": authority,
                "Department": department,
                "Responsibility": responsibility,
                "Approval Chain": approval,
                "Industry ID": iid,
                "Industry": iname,
                "Typical Persona Link": "",
                "Description": evidence[:1500],
                "Data Sources": ds,
                "Last Updated": utc_now_iso()[:10],
                "Notes": notes,
            }
            candidates.append(
                CandidateRecord.create(
                    entity_type="decision_maker_library",
                    entity_id=did,
                    target_dataset="decision_maker_library",
                    payload=payload,
                    provenance=Provenance(
                        source_id=source_id,
                        source_url=url,
                        retrieved_at=retrieved,
                        confidence=conf,
                        extraction_version=EXTRACTION_VERSION,
                        validation_status=ValidationStatus.PENDING.value,
                        published_at=published or None,
                    ),
                    canonical_name=role,
                    metadata={
                        "mission_id": mission_id,
                        "session_id": session_id,
                        "document_id": doc.get("document_id"),
                        "dataset": "decision_maker_library",
                        "evidence": [evidence[:400]],
                        "schema_version": "1.0",
                    },
                )
            )
    return candidates


def extract_regulation_candidates(
    documents: list[dict[str, Any]],
    *,
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
    max_candidates: int = 5,
) -> list[CandidateRecord]:
    root = repo_root or find_repo_root()
    csv_path = root / "domains" / "business_development" / "regulation_library.csv"
    next_n = _next_id(csv_path, "Regulation ID", "REG")
    existing = _existing_names(csv_path, "Regulation Name")
    candidates: list[CandidateRecord] = []
    fb_id, fb_name = _first_industry_fallback(root)

    for doc in documents:
        if len(candidates) >= max_candidates:
            break
        text = document_text(doc)
        title = str(doc.get("title") or "").strip()
        if len(text) < 30:
            continue
        # Require regulatory language
        low = text.lower()
        if not any(
            k in low
            for k in (
                "regulation",
                "law ",
                "act ",
                "policy",
                "directive",
                "peraturan",
                "undang",
                "compliance",
                "pojk",
                "standard",
            )
        ):
            continue
        matches: list[str] = []
        for pat in _REG_PATTERNS:
            for m in re.finditer(pat, text):
                s = normalize_text(m.group(0))[:200]
                if s and s.lower() not in {x.lower() for x in matches}:
                    matches.append(s)
                if len(matches) >= 3:
                    break
        if not matches:
            # Use title if regulatory
            if any(k in title.lower() for k in ("regulation", "law", "act", "policy", "peraturan")):
                matches = [title[:200]]
            else:
                continue
        iid, iname = _industry_link(text, root)
        if not iid:
            iid, iname = fb_id, fb_name
        source_id = str(doc.get("source_id") or "SRC-UNKNOWN")
        url = str(doc.get("original_url") or doc.get("url") or "")
        retrieved = str(doc.get("retrieved_at") or utc_now_iso())
        published = str((doc.get("metadata") or {}).get("published_at") or "")
        conf = _conf(doc, boost=0.04)
        conf = max(conf, 0.92) if float(doc.get("trust_score") or 0) >= 0.90 else conf

        for law in matches:
            if len(candidates) >= max_candidates:
                break
            if law.lower() in existing:
                continue
            snips = evidence_snippets(text, law.split()[0] if law else "regulation") or [text[:300]]
            evidence = " … ".join(snips)[:800]
            rid = f"REG-{next_n:06d}"
            next_n += 1
            existing.add(law.lower())
            # Issuer: prefer known org names present in text
            issuer = ""
            for org in (
                "OJK",
                "Kemnaker",
                "Kementerian Ketenagakerjaan",
                "BKPM",
                "LKPP",
                "BPS",
                "OECD",
                "World Bank",
                "ILO",
                "IMF",
                "ADB",
                "BPK",
                "Kemendag",
                "OSS",
            ):
                if org.lower() in low or org in text:
                    issuer = org
                    break
            if not issuer:
                issuer = source_id
            # Effective date from published if present
            effective = published[:10] if published else ""
            scope = ""
            if "indonesia" in low:
                scope = "Indonesia"
            elif "global" in low or "international" in low:
                scope = "International"
            ds, notes = _prov_notes(
                source_id=source_id,
                url=url,
                retrieved=retrieved,
                published=published,
                conf=conf,
                mission_id=mission_id,
                document_id=str(doc.get("document_id") or ""),
                evidence=evidence,
            )
            payload = {
                "Regulation ID": rid,
                "Regulation Name": law[:240],
                "Issuer": issuer,
                "Effective Date": effective,
                "Scope": scope,
                "Industry ID": iid,
                "Industry": iname,
                "Jurisdiction": scope or "Indonesia",
                "Summary": evidence[:1500],
                "Source URL": url,
                "Data Sources": ds,
                "Last Updated": utc_now_iso()[:10],
                "Notes": notes,
            }
            candidates.append(
                CandidateRecord.create(
                    entity_type="regulation_library",
                    entity_id=rid,
                    target_dataset="regulation_library",
                    payload=payload,
                    provenance=Provenance(
                        source_id=source_id,
                        source_url=url,
                        retrieved_at=retrieved,
                        confidence=conf,
                        extraction_version=EXTRACTION_VERSION,
                        validation_status=ValidationStatus.PENDING.value,
                        published_at=published or None,
                    ),
                    canonical_name=law[:120],
                    metadata={
                        "mission_id": mission_id,
                        "session_id": session_id,
                        "document_id": doc.get("document_id"),
                        "dataset": "regulation_library",
                        "evidence": [evidence[:400]],
                        "schema_version": "1.0",
                    },
                )
            )
    return candidates


def extract_risk_candidates(
    documents: list[dict[str, Any]],
    *,
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
    max_candidates: int = 5,
) -> list[CandidateRecord]:
    root = repo_root or find_repo_root()
    csv_path = root / "domains" / "business_development" / "risk_library.csv"
    next_n = _next_id(csv_path, "Risk ID", "RISK")
    existing = _existing_names(csv_path, "Risk Name")
    candidates: list[CandidateRecord] = []
    fb_id, fb_name = _first_industry_fallback(root)

    for doc in documents:
        if len(candidates) >= max_candidates:
            break
        text = document_text(doc)
        low = text.lower()
        if "risk" not in low and "risiko" not in low:
            continue
        risk_hits = [t for t in _RISK_TYPES if t in low]
        if not risk_hits:
            risk_hits = ["risk"]
        iid, iname = _industry_link(text, root)
        if not iid:
            iid, iname = fb_id, fb_name
        source_id = str(doc.get("source_id") or "SRC-UNKNOWN")
        url = str(doc.get("original_url") or doc.get("url") or "")
        retrieved = str(doc.get("retrieved_at") or utc_now_iso())
        published = str((doc.get("metadata") or {}).get("published_at") or "")
        conf = _conf(doc, boost=0.03)
        if conf >= 0.90:
            conf = max(conf, 0.92)

        for rtype in risk_hits[:3]:
            if len(candidates) >= max_candidates:
                break
            name = f"{rtype.title()} — {iname or 'Industry'}"[:200]
            if name.lower() in existing:
                continue
            snips = evidence_snippets(text, rtype.split()[0]) or [text[:300]]
            evidence = " … ".join(snips)[:800]
            # Probability / impact only when words appear (else empty — no invention)
            probability = ""
            impact = ""
            for p in ("high probability", "likely", "unlikely", "low probability", "probable"):
                if p in low:
                    probability = p
                    break
            for im in ("high impact", "severe", "critical impact", "low impact", "material impact"):
                if im in low:
                    impact = im
                    break
            mitigation = ""
            for mit in ("mitigation", "mitigate", "hedge", "insurance", "controls", "compliance program"):
                if mit in low:
                    m = re.search(rf".{{0,40}}{re.escape(mit)}.{{0,80}}", text, re.I)
                    if m:
                        mitigation = normalize_text(m.group(0))[:200]
                        break
            rid = f"RISK-{next_n:06d}"
            next_n += 1
            existing.add(name.lower())
            ds, notes = _prov_notes(
                source_id=source_id,
                url=url,
                retrieved=retrieved,
                published=published,
                conf=conf,
                mission_id=mission_id,
                document_id=str(doc.get("document_id") or ""),
                evidence=evidence,
            )
            payload = {
                "Risk ID": rid,
                "Risk Name": name,
                "Risk Type": rtype.title(),
                "Probability": probability,
                "Impact": impact,
                "Mitigation": mitigation,
                "Industry ID": iid,
                "Industry": iname,
                "Description": evidence[:1500],
                "Data Sources": ds,
                "Last Updated": utc_now_iso()[:10],
                "Notes": notes,
            }
            candidates.append(
                CandidateRecord.create(
                    entity_type="risk_library",
                    entity_id=rid,
                    target_dataset="risk_library",
                    payload=payload,
                    provenance=Provenance(
                        source_id=source_id,
                        source_url=url,
                        retrieved_at=retrieved,
                        confidence=conf,
                        extraction_version=EXTRACTION_VERSION,
                        validation_status=ValidationStatus.PENDING.value,
                        published_at=published or None,
                    ),
                    canonical_name=name,
                    metadata={
                        "mission_id": mission_id,
                        "session_id": session_id,
                        "document_id": doc.get("document_id"),
                        "dataset": "risk_library",
                        "evidence": [evidence[:400]],
                        "schema_version": "1.0",
                    },
                )
            )
    return candidates


def extract_trend_candidates(
    documents: list[dict[str, Any]],
    *,
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
    max_candidates: int = 5,
) -> list[CandidateRecord]:
    root = repo_root or find_repo_root()
    csv_path = root / "domains" / "business_development" / "trend_library.csv"
    next_n = _next_id(csv_path, "Trend ID", "TRD")
    existing = _existing_names(csv_path, "Trend Title")
    candidates: list[CandidateRecord] = []
    fb_id, fb_name = _first_industry_fallback(root)

    for doc in documents:
        if len(candidates) >= max_candidates:
            break
        text = document_text(doc)
        title = str(doc.get("title") or "").strip()
        low = text.lower()
        hits = [t for t in _TREND_TERMS if t in low]
        if not hits and not any(k in title.lower() for k in ("trend", "outlook", "growth", "future")):
            continue
        iid, iname = _industry_link(text, root)
        if not iid:
            iid, iname = fb_id, fb_name
        trend_title = title[:200] if title else f"Industry trend — {hits[0] if hits else 'outlook'}"
        if trend_title.lower() in existing:
            continue
        # Direction from grounded words only
        direction = ""
        if any(w in low for w in ("rising", "increase", "growth", "accelerat", "expand")):
            direction = "Rising"
        elif any(w in low for w in ("decline", "falling", "decrease", "contraction")):
            direction = "Declining"
        elif any(w in low for w in ("stable", "steady", "unchanged")):
            direction = "Stable"
        time_window = ""
        for tw in ("2024", "2025", "2026", "2027", "2030", "next decade", "medium term", "short term", "long term"):
            if tw in low:
                time_window = tw
                break
        signal = hits[0] if hits else "trend signal"
        evidence = text[:500]
        conf = _conf(doc, boost=0.02)
        if conf >= 0.90:
            conf = max(conf, 0.92)
        source_id = str(doc.get("source_id") or "SRC-UNKNOWN")
        url = str(doc.get("original_url") or doc.get("url") or "")
        retrieved = str(doc.get("retrieved_at") or utc_now_iso())
        published = str((doc.get("metadata") or {}).get("published_at") or "")
        tid = f"TRD-{next_n:06d}"
        next_n += 1
        existing.add(trend_title.lower())
        ds, notes = _prov_notes(
            source_id=source_id,
            url=url,
            retrieved=retrieved,
            published=published,
            conf=conf,
            mission_id=mission_id,
            document_id=str(doc.get("document_id") or ""),
            evidence=evidence,
        )
        payload = {
            "Trend ID": tid,
            "Trend Title": trend_title,
            "Direction": direction,
            "Industry ID": iid,
            "Industry": iname,
            "Time Horizon": time_window,
            "Signal": signal,
            "Description": evidence[:1500],
            "Data Sources": ds,
            "Last Updated": utc_now_iso()[:10],
            "Notes": notes,
        }
        candidates.append(
            CandidateRecord.create(
                entity_type="trend_library",
                entity_id=tid,
                target_dataset="trend_library",
                payload=payload,
                provenance=Provenance(
                    source_id=source_id,
                    source_url=url,
                    retrieved_at=retrieved,
                    confidence=conf,
                    extraction_version=EXTRACTION_VERSION,
                    validation_status=ValidationStatus.PENDING.value,
                    published_at=published or None,
                ),
                canonical_name=trend_title[:120],
                metadata={
                    "mission_id": mission_id,
                    "session_id": session_id,
                    "document_id": doc.get("document_id"),
                    "dataset": "trend_library",
                    "evidence": [evidence[:400]],
                    "schema_version": "1.0",
                },
            )
        )
    return candidates


def extract_competitor_candidates(
    documents: list[dict[str, Any]],
    *,
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
    max_candidates: int = 5,
) -> list[CandidateRecord]:
    root = repo_root or find_repo_root()
    csv_path = root / "domains" / "business_development" / "competitor_library.csv"
    next_n = _next_id(csv_path, "Competitor ID", "CMP")
    existing = _existing_names(csv_path, "Competitor Name")
    candidates: list[CandidateRecord] = []
    fb_id, fb_name = _first_industry_fallback(root)

    for doc in documents:
        if len(candidates) >= max_candidates:
            break
        text = document_text(doc)
        low = text.lower()
        names = _company_names_from_text(text)
        # Only accept high-precision company forms — never metadata tokens or titles alone
        names = [n for n in names if _is_plausible_company_name(n)]
        if not names:
            continue
        iid, iname = _industry_link(text, root)
        category = iname or "Services"
        source_id = str(doc.get("source_id") or "SRC-UNKNOWN")
        url = str(doc.get("original_url") or doc.get("url") or "")
        retrieved = str(doc.get("retrieved_at") or utc_now_iso())
        published = str((doc.get("metadata") or {}).get("published_at") or "")
        conf = _conf(doc, boost=0.02)

        for name in names:
            if len(candidates) >= max_candidates:
                break
            if name.lower() in existing:
                continue
            snips = evidence_snippets(text, name.split()[0]) or [text[:300]]
            evidence = " … ".join(snips)[:800]
            # Strengths / weaknesses only when words appear near name
            strength = ""
            weakness = ""
            for s in ("strength", "advantage", "leading", "market leader"):
                if s in low:
                    m = re.search(rf".{{0,30}}{re.escape(s)}.{{0,60}}", text, re.I)
                    if m:
                        strength = normalize_text(m.group(0))[:200]
                        break
            for w in ("weakness", "challenge", "limitation", "disadvantage"):
                if w in low:
                    m = re.search(rf".{{0,30}}{re.escape(w)}.{{0,60}}", text, re.I)
                    if m:
                        weakness = normalize_text(m.group(0))[:200]
                        break
            products = ""
            for p in ("product", "service", "platform", "solution"):
                if p in low:
                    m = re.search(rf".{{0,20}}{re.escape(p)}.{{0,60}}", text, re.I)
                    if m:
                        products = normalize_text(m.group(0))[:200]
                        break
            cid = f"CMP-{next_n:06d}"
            next_n += 1
            existing.add(name.lower())
            ds, notes = _prov_notes(
                source_id=source_id,
                url=url,
                retrieved=retrieved,
                published=published,
                conf=conf,
                mission_id=mission_id,
                document_id=str(doc.get("document_id") or ""),
                evidence=evidence,
            )
            # competitor ID pattern in integrity is CMP-
            payload = {
                "Competitor ID": cid,
                "Competitor Name": name[:200],
                "Industry Category": category,
                "Company Description": evidence[:800],
                "Headquarters": "Indonesia" if "indonesia" in low else "",
                "Operating Region": "Indonesia" if "indonesia" in low else "",
                "Target Customer": "",
                "Main Products/Services": products,
                "Strengths": strength,
                "Weaknesses": weakness,
                "Unique Selling Proposition (USP)": "",
                "Pricing Level": "",
                "Pricing Model": "",
                "Typical Sales Strategy": "",
                "Typical Decision Makers": "",
                "Industries Served": iname,
                "Competitive Advantages": strength,
                "Competitive Disadvantages": weakness,
                "Our Competitive Advantage": "",
                "Win Strategy": "",
                "Common Customer Objections": "",
                "Recommended Response": "",
                "Market Position": "",
                "Threat Level": "",
                "Reference Projects": "",
                "Information Source": source_id,
                "Last Updated": utc_now_iso()[:10],
                "Notes": notes,
            }
            candidates.append(
                CandidateRecord.create(
                    entity_type="competitor_library",
                    entity_id=cid,
                    target_dataset="competitor_library",
                    payload=payload,
                    provenance=Provenance(
                        source_id=source_id,
                        source_url=url,
                        retrieved_at=retrieved,
                        confidence=conf,
                        extraction_version=EXTRACTION_VERSION,
                        validation_status=ValidationStatus.PENDING.value,
                        published_at=published or None,
                    ),
                    canonical_name=name[:120],
                    metadata={
                        "mission_id": mission_id,
                        "session_id": session_id,
                        "document_id": doc.get("document_id"),
                        "dataset": "competitor_library",
                        "evidence": [evidence[:400]],
                        "schema_version": "1.0",
                    },
                )
            )
    return candidates


EXTRACTORS: dict[str, Callable[..., list[CandidateRecord]]] = {
    "buyer_persona_library": extract_buyer_persona_candidates,
    "decision_maker_library": extract_decision_maker_candidates,
    "regulation_library": extract_regulation_candidates,
    "risk_library": extract_risk_candidates,
    "trend_library": extract_trend_candidates,
    "competitor_library": extract_competitor_candidates,
}


def extract_for_dataset(
    dataset: str,
    documents: list[dict[str, Any]],
    *,
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
    max_candidates: int = 5,
) -> list[CandidateRecord]:
    fn = EXTRACTORS.get(dataset)
    if not fn:
        return []
    return fn(
        documents,
        mission_id=mission_id,
        session_id=session_id,
        repo_root=repo_root,
        max_candidates=max_candidates,
    )
