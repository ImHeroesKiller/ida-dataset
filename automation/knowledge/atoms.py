"""Knowledge Atom factory — semantic chunking of documents into persistent atoms.

Chunk by meaning (heading, section, paragraph group, table, bullet, FAQ, caption).
NOT by token/character windows.

Stable atom IDs (Commit 2):
  Hash(document_id | section | paragraph_index | normalized_text)

Does not write dataset rows. Does not touch frozen pipelines.
Public API: atomize_text, atomize_document, atom_type_counts (unchanged signatures).
"""

from __future__ import annotations

import hashlib
import re
import unicodedata
from typing import Any, Mapping, Optional, Sequence

from automation.knowledge.models import AtomStatus, AtomType, KnowledgeAtom
from automation.lib.models import utc_now_iso

ATOM_VERSION = "knowledge-atom-1.1.0"
PARSER_VERSION = "semantic-chunker-1.1.0"

_HEADING_MD = re.compile(r"^(#{1,6})\s+(.+)$")
_HEADING_NUM = re.compile(
    r"^((?:\d+\.)+\d*|[IVXLC]+\.|[A-Z]\.)\s+([A-Z].{2,120})$"
)
_HEADING_CAPS = re.compile(r"^[A-Z][A-Z0-9 ,/&\-]{6,100}$")
_BULLET = re.compile(r"^(\s*[-*•]|\s*\d+[.)])\s+(.+)$")
_FAQ_Q = re.compile(r"^(?:Q(?:uestion)?|FAQ)\s*[:.)\-]\s*(.+)$", re.I)
_FAQ_A = re.compile(r"^(?:A(?:nswer)?)\s*[:.)\-]\s*(.+)$", re.I)
_CAPTION = re.compile(
    r"^(?:Figure|Fig\.|Table|Chart|Gambar|Tabel)\s*[\d.IVX]*\s*[:.\-–]?\s*(.+)$",
    re.I,
)
_TABLE_LINE = re.compile(r"\|.+\|")
_SECTION_RULE = re.compile(r"^[-=]{3,}\s*$")
_WS = re.compile(r"\s+")


def normalize_atom_text(text: str) -> str:
    """Normalize text for stable hashing and comparison."""
    s = unicodedata.normalize("NFKC", text or "")
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = _WS.sub(" ", s).strip().lower()
    return s


def atom_knowledge_score(
    *,
    confidence: float,
    text: str,
    atom_type: str,
    has_section: bool,
) -> float:
    """Configurable-style atom richness score (0–1). Not entity knowledge_score."""
    conf = max(0.0, min(1.0, float(confidence or 0.0)))
    length = len((text or "").strip())
    richness = min(1.0, length / 400.0)
    type_boost = {
        AtomType.HEADING.value: 0.05,
        AtomType.TABLE.value: 0.12,
        AtomType.FAQ.value: 0.10,
        AtomType.SECTION.value: 0.08,
        AtomType.BULLET.value: 0.06,
        AtomType.METADATA.value: 0.04,
        AtomType.CAPTION.value: 0.03,
        AtomType.PARAGRAPH.value: 0.05,
    }.get(atom_type, 0.0)
    section_boost = 0.05 if has_section else 0.0
    score = 0.45 * conf + 0.35 * richness + type_boost + section_boost
    return round(max(0.0, min(1.0, score)), 4)


def _atom_id(
    document_id: str,
    section: str,
    paragraph_index: int,
    normalized_text: str,
) -> str:
    """Stable ID — small wording edits in original casing/spacing do not churn IDs."""
    material = f"{document_id}|{section}|{paragraph_index}|{normalized_text}"
    h = hashlib.sha1(material.encode("utf-8")).hexdigest()[:12].upper()
    return f"ATOM-{h}"


def _is_heading(line: str) -> Optional[str]:
    s = line.strip()
    if not s or len(s) > 160:
        return None
    m = _HEADING_MD.match(s)
    if m:
        return m.group(2).strip()
    m = _HEADING_NUM.match(s)
    if m:
        return m.group(2).strip()
    if _HEADING_CAPS.match(s) and not s.endswith("."):
        return s.title() if s.isupper() else s
    return None


def _normalize_lines(text: str) -> list[str]:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")
    return text.split("\n")


def _guess_language(text: str) -> str:
    sample = (text or "")[:2000].lower()
    id_hits = sum(
        1
        for w in ("dan", "yang", "dengan", "untuk", "pada", "adalah", "perusahaan")
        if f" {w} " in f" {sample} "
    )
    en_hits = sum(
        1
        for w in ("the", "and", "with", "for", "from", "company", "industry")
        if f" {w} " in f" {sample} "
    )
    if id_hits >= en_hits and id_hits >= 2:
        return "id"
    if en_hits >= 2:
        return "en"
    return ""


def atomize_text(
    text: str,
    *,
    document_id: str,
    source: str = "",
    source_url: str = "",
    base_confidence: float = 0.75,
    provenance: Optional[Mapping[str, Any]] = None,
    include_metadata: Optional[Mapping[str, Any]] = None,
    # Optional document context (Commit 2) — ignored by older callers
    language: str = "",
    document_type: str = "",
    mime_type: str = "",
    publisher: str = "",
    published_date: str = "",
    crawl_date: str = "",
) -> list[KnowledgeAtom]:
    """Split plain text into Knowledge Atoms by semantic structure."""
    lines = _normalize_lines(text)
    atoms: list[KnowledgeAtom] = []
    order = 0
    heading_path: list[str] = []
    ts = utc_now_iso()
    prov = dict(provenance or {})
    prov.setdefault("atom_version", ATOM_VERSION)
    lang = language or _guess_language(text)

    def emit(
        atom_type: str,
        body: str,
        *,
        conf: Optional[float] = None,
        extra: Optional[dict[str, Any]] = None,
    ) -> None:
        nonlocal order
        original = (body or "").strip()
        if not original:
            return
        section = heading_path[-1] if heading_path else ""
        norm = normalize_atom_text(original)
        conf_v = float(conf if conf is not None else base_confidence)
        kscore = atom_knowledge_score(
            confidence=conf_v,
            text=original,
            atom_type=atom_type,
            has_section=bool(section),
        )
        atom = KnowledgeAtom(
            atom_id=_atom_id(document_id, section, order, norm),
            document_id=document_id,
            atom_type=atom_type,
            text=original,
            source=source,
            source_url=source_url,
            section=section,
            heading_path=list(heading_path),
            order=order,
            timestamp=ts,
            confidence=conf_v,
            provenance=dict(prov),
            metadata=dict(extra or {}),
            created_at=ts,
            knowledge_score=kscore,
            normalized_text=norm,
            original_text=original,
            language=lang,
            document_type=document_type,
            mime_type=mime_type,
            publisher=publisher,
            published_date=published_date,
            crawl_date=crawl_date or ts,
            parser_version=PARSER_VERSION,
            extractor_version=ATOM_VERSION,
            status=AtomStatus.ACTIVE.value,
            paragraph_index=order,
        )
        atoms.append(atom)
        order += 1

    if include_metadata:
        for key in ("title", "abstract", "snippet", "text_excerpt"):
            val = include_metadata.get(key)
            if val and str(val).strip():
                emit(
                    AtomType.METADATA.value,
                    f"{key}: {str(val).strip()}",
                    conf=min(0.95, base_confidence + 0.1),
                    extra={"meta_key": key},
                )

    i = 0
    para_buf: list[str] = []
    bullet_buf: list[str] = []
    table_buf: list[str] = []
    faq_q: Optional[str] = None

    def flush_para() -> None:
        nonlocal para_buf
        if not para_buf:
            return
        text_block = " ".join(p.strip() for p in para_buf if p.strip())
        if heading_path and len(text_block) > 280:
            emit(AtomType.SECTION.value, text_block)
        else:
            emit(AtomType.PARAGRAPH.value, text_block)
        para_buf = []

    def flush_bullets() -> None:
        nonlocal bullet_buf
        if not bullet_buf:
            return
        emit(AtomType.BULLET.value, "\n".join(bullet_buf))
        bullet_buf = []

    def flush_table() -> None:
        nonlocal table_buf
        if not table_buf:
            return
        emit(AtomType.TABLE.value, "\n".join(table_buf), conf=base_confidence)
        table_buf = []

    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped or _SECTION_RULE.match(stripped):
            flush_table()
            flush_bullets()
            flush_para()
            i += 1
            continue

        if _TABLE_LINE.search(stripped) or (
            stripped.count("\t") >= 2 and len(stripped) > 8
        ):
            flush_para()
            flush_bullets()
            table_buf.append(stripped)
            i += 1
            continue
        else:
            flush_table()

        cap = _CAPTION.match(stripped)
        if cap:
            flush_para()
            flush_bullets()
            emit(AtomType.CAPTION.value, stripped, conf=base_confidence)
            i += 1
            continue

        mq = _FAQ_Q.match(stripped)
        if mq:
            flush_para()
            flush_bullets()
            faq_q = mq.group(1).strip()
            i += 1
            continue
        ma = _FAQ_A.match(stripped)
        if ma and faq_q:
            emit(
                AtomType.FAQ.value,
                f"Q: {faq_q}\nA: {ma.group(1).strip()}",
                conf=base_confidence,
            )
            faq_q = None
            i += 1
            continue
        if faq_q and not ma:
            emit(AtomType.FAQ.value, f"Q: {faq_q}", conf=base_confidence * 0.9)
            faq_q = None

        h = _is_heading(stripped)
        if h:
            flush_para()
            flush_bullets()
            if not (heading_path and heading_path[-1] == h):
                if len(h) < 80:
                    heading_path = (heading_path + [h])[-4:]
            emit(AtomType.HEADING.value, h, conf=min(0.95, base_confidence + 0.05))
            i += 1
            continue

        bm = _BULLET.match(line)
        if bm:
            flush_para()
            bullet_buf.append(stripped)
            i += 1
            continue
        else:
            flush_bullets()

        para_buf.append(stripped)
        i += 1

    flush_table()
    flush_bullets()
    flush_para()
    if faq_q:
        emit(AtomType.FAQ.value, f"Q: {faq_q}", conf=base_confidence * 0.9)

    return atoms


def atomize_document(
    doc: Mapping[str, Any],
    *,
    text: Optional[str] = None,
    base_confidence: Optional[float] = None,
) -> list[KnowledgeAtom]:
    """Atomize a processed document dict (production document record)."""
    document_id = str(doc.get("document_id") or doc.get("id") or "DOC-UNKNOWN")
    source = str(doc.get("source_id") or doc.get("connector_id") or "")
    meta = doc.get("metadata") if isinstance(doc.get("metadata"), dict) else {}
    source_url = str(
        doc.get("original_url")
        or doc.get("source_url")
        or meta.get("url")
        or ""
    )
    conf = (
        float(base_confidence)
        if base_confidence is not None
        else float(doc.get("trust_score") or meta.get("confidence") or 0.75)
    )
    conf = max(0.0, min(1.0, conf))

    body = text
    if body is None:
        try:
            from automation.acquisition.extractor import document_text

            body = document_text(dict(doc))
        except Exception:  # noqa: BLE001
            parts = [
                str(doc.get("title") or ""),
                str(meta.get("text_excerpt") or meta.get("snippet") or ""),
            ]
            body = "\n\n".join(p for p in parts if p)

    include_meta = {
        "title": doc.get("title") or meta.get("title"),
        "abstract": meta.get("abstract"),
        "snippet": meta.get("snippet"),
        "text_excerpt": meta.get("text_excerpt"),
    }

    content_type = str(doc.get("content_type") or meta.get("content_type") or "")
    mime = content_type.split(";")[0].strip() if content_type else ""
    doc_type = "pdf" if "pdf" in mime.lower() else ("html" if "html" in mime.lower() else "text")

    return atomize_text(
        body or "",
        document_id=document_id,
        source=source,
        source_url=source_url,
        base_confidence=conf,
        provenance={
            "source_id": source,
            "source_url": source_url,
            "document_id": document_id,
            "retrieved_at": str(doc.get("retrieved_at") or ""),
            "mission_id": str(doc.get("mission_id") or ""),
            "atom_version": ATOM_VERSION,
        },
        include_metadata=include_meta,
        document_type=doc_type,
        mime_type=mime or "text/plain",
        publisher=str(meta.get("publisher") or meta.get("host") or ""),
        published_date=str(meta.get("published_date") or meta.get("date") or ""),
        crawl_date=str(doc.get("retrieved_at") or ""),
    )


def atom_type_counts(atoms: Sequence[KnowledgeAtom]) -> dict[str, int]:
    out: dict[str, int] = {}
    for a in atoms:
        out[a.atom_type] = out.get(a.atom_type, 0) + 1
    return out
