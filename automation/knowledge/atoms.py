"""Knowledge Atom factory — semantic chunking of documents into persistent atoms.

Chunk by meaning (heading, section, paragraph group, table, bullet, FAQ, caption).
NOT by token/character windows.

Does not write dataset rows. Does not touch frozen pipelines.
"""

from __future__ import annotations

import hashlib
import re
from typing import Any, Mapping, Optional, Sequence

from automation.knowledge.models import AtomType, KnowledgeAtom
from automation.lib.models import utc_now_iso

ATOM_VERSION = "knowledge-atom-1.0.0"

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


def _atom_id(document_id: str, order: int, atom_type: str, text: str) -> str:
    h = hashlib.sha1(
        f"{document_id}|{order}|{atom_type}|{text[:200]}".encode("utf-8")
    ).hexdigest()[:12].upper()
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


def atomize_text(
    text: str,
    *,
    document_id: str,
    source: str = "",
    source_url: str = "",
    base_confidence: float = 0.75,
    provenance: Optional[Mapping[str, Any]] = None,
    include_metadata: Optional[Mapping[str, Any]] = None,
) -> list[KnowledgeAtom]:
    """Split plain text into Knowledge Atoms by semantic structure."""
    lines = _normalize_lines(text)
    atoms: list[KnowledgeAtom] = []
    order = 0
    heading_path: list[str] = []
    ts = utc_now_iso()
    prov = dict(provenance or {})
    prov.setdefault("atom_version", ATOM_VERSION)

    def emit(
        atom_type: str,
        body: str,
        *,
        conf: Optional[float] = None,
        extra: Optional[dict[str, Any]] = None,
    ) -> None:
        nonlocal order
        body = (body or "").strip()
        if not body:
            return
        section = heading_path[-1] if heading_path else ""
        atom = KnowledgeAtom(
            atom_id=_atom_id(document_id, order, atom_type, body),
            document_id=document_id,
            atom_type=atom_type,
            text=body,
            source=source,
            source_url=source_url,
            section=section,
            heading_path=list(heading_path),
            order=order,
            timestamp=ts,
            confidence=float(conf if conf is not None else base_confidence),
            provenance=dict(prov),
            metadata=dict(extra or {}),
            created_at=ts,
        )
        atoms.append(atom)
        order += 1

    # Metadata atoms first
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
        # Paragraph group under a heading → section if multi-sentence and headed
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

        # Horizontal rule / blank → paragraph boundary
        if not stripped or _SECTION_RULE.match(stripped):
            flush_table()
            flush_bullets()
            flush_para()
            i += 1
            continue

        # Table rows
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

        # Caption
        cap = _CAPTION.match(stripped)
        if cap:
            flush_para()
            flush_bullets()
            emit(AtomType.CAPTION.value, stripped, conf=base_confidence)
            i += 1
            continue

        # FAQ
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
            # lone question without immediate answer
            emit(AtomType.FAQ.value, f"Q: {faq_q}", conf=base_confidence * 0.9)
            faq_q = None

        # Heading
        h = _is_heading(stripped)
        if h:
            flush_para()
            flush_bullets()
            # Maintain shallow path (last heading is current section)
            if heading_path and heading_path[-1] == h:
                pass
            else:
                # Replace path depth simply: single-level trail + new
                if len(h) < 80:
                    heading_path = (heading_path + [h])[-4:]
            emit(AtomType.HEADING.value, h, conf=min(0.95, base_confidence + 0.05))
            i += 1
            continue

        # Bullet
        bm = _BULLET.match(line)
        if bm:
            flush_para()
            bullet_buf.append(stripped)
            i += 1
            continue
        else:
            flush_bullets()

        # Regular paragraph line
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
    )


def atom_type_counts(atoms: Sequence[KnowledgeAtom]) -> dict[str, int]:
    out: dict[str, int] = {}
    for a in atoms:
        out[a.atom_type] = out.get(a.atom_type, 0) + 1
    return out
