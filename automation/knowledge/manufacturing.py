"""Knowledge Manufacturing Engine — Graph → multi-dataset candidates.

Datasets are OUTPUTS of the knowledge graph.
Does not write domain CSVs. Does not call the frozen publisher.
Candidates are quality-scored and enqueued under automation/queue/manufacturing/.

API:
  manufacture()
  manufacture_entity()
  manufacture_relationship()
  manufacture_document()
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

from automation.knowledge.entity_store import (
    get_entity,
    load_all_entities,
)
from automation.knowledge.manufacturing_queue import (
    enqueue_candidate,
    manufacture_key,
    mark_manufactured,
    queue_stats,
    was_manufactured,
)
from automation.knowledge.models import GraphEntity, GraphRelationship
from automation.knowledge.quality import assess_candidate
from automation.knowledge.relationship_store import load_all_relationships
from automation.knowledge.relationships import incoming, outgoing
from automation.lib.models import CandidateRecord, Provenance, utc_now_iso
from automation.lib.paths import find_repo_root

MANUFACTURING_VERSION = "knowledge-manufacture-1.0.0"

# Entity type → datasets to manufacture (never stop at first match)
ENTITY_DATASET_MAP: dict[str, list[str]] = {
    "Company": [
        "company_profile",
        "competitor_library",
    ],
    "Industry": ["industry_library"],
    "Technology": ["product_catalog", "trend_library"],
    "Framework": ["framework_library"],
    "Standard": ["framework_library"],
    "Regulation": ["regulation_library"],
    "Job Title": ["decision_maker_library", "buyer_persona_library"],
    "Country": [],  # enrich via links only
}

# Relationship type → additional datasets for the edge
REL_DATASET_MAP: dict[str, list[str]] = {
    "provides": ["product_catalog", "solution_library"],
    "offers": ["product_catalog", "solution_library"],
    "manufactures": ["product_catalog"],
    "targets": ["industry_library", "opportunity_analysis"],
    "serves": ["industry_library"],
    "competes_with": ["competitor_library"],
    "uses": ["product_catalog", "trend_library"],
    "implements": ["framework_library"],
    "depends_on": ["product_catalog"],
    "integrates_with": ["product_catalog"],
    "regulated_by": ["regulation_library", "risk_library"],
    "certified_by": ["framework_library"],
    "located_in": ["company_profile"],
    "managed_by": ["decision_maker_library", "buyer_persona_library"],
    "partner_of": ["competitor_library", "case_study_library"],
}


def _provenance_from_entity(ent: GraphEntity) -> Provenance:
    src = (ent.sources or ["GRAPH"])[0] if ent.sources else "GRAPH"
    return Provenance(
        source_id=str(src),
        source_url=str((ent.provenance or {}).get("source_url") or ""),
        retrieved_at=str(ent.last_seen or utc_now_iso()),
        confidence=float(ent.confidence or 0.0),
        extraction_version=MANUFACTURING_VERSION,
    )


def _payload_company(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    industries = neighbors_ctx.get("industries") or []
    countries = neighbors_ctx.get("countries") or []
    techs = neighbors_ctx.get("technologies") or []
    return {
        "Company ID": ent.entity_id,
        "Company Name": ent.canonical_name,
        "Alias": "; ".join(ent.aliases[:5]) if ent.aliases else "",
        "Industry": industries[0] if industries else "",
        "Country": countries[0] if countries else "",
        "Current Technologies": "; ".join(techs[:8]),
        "Main Products/Services": "; ".join(
            (neighbors_ctx.get("products") or [])[:8]
        ),
        "Data Source": "; ".join(ent.sources[:3]),
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_competitor(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    industries = neighbors_ctx.get("industries") or []
    return {
        "Competitor ID": ent.entity_id,
        "Competitor Name": ent.canonical_name,
        "Industry Category": industries[0] if industries else "",
        "Company Description": "",
        "Headquarters": (neighbors_ctx.get("countries") or [""])[0],
        "Main Products/Services": "; ".join(
            (neighbors_ctx.get("products") or neighbors_ctx.get("technologies") or [])[:8]
        ),
        "Information Source": "; ".join(ent.sources[:3]),
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_industry(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    return {
        "Industry ID": ent.entity_id,
        "Industry Name": ent.canonical_name,
        "Industry Category": ent.canonical_name,
        "Industry Description": "",
        "Common Technologies": "; ".join((neighbors_ctx.get("technologies") or [])[:8]),
        "Data Sources": "; ".join(ent.sources[:3]),
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_product(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    industries = neighbors_ctx.get("industries") or []
    return {
        "Product ID": ent.entity_id,
        "Product Name": ent.canonical_name,
        "Product Category": ent.entity_type or "Technology",
        "Product Type": "Technology" if ent.entity_type == "Technology" else "Service",
        "Product Description": "",
        "Target Industry": industries[0] if industries else "",
        "Key Features": "; ".join(ent.aliases[:5]),
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_framework(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    return {
        "Framework ID": ent.entity_id,
        "Framework Name": ent.canonical_name,
        "Framework Category": ent.entity_type or "Framework",
        "Description": "",
        "Related Domains": "; ".join((neighbors_ctx.get("industries") or [])[:5]),
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_regulation(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    countries = neighbors_ctx.get("countries") or []
    return {
        "Regulation ID": ent.entity_id,
        "Regulation Name": ent.canonical_name,
        "Jurisdiction": countries[0] if countries else "",
        "Summary": "",
        "Industry": (neighbors_ctx.get("industries") or [""])[0],
        "Data Sources": "; ".join(ent.sources[:3]),
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_decision_maker(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    industries = neighbors_ctx.get("industries") or []
    return {
        "Decision Maker ID": ent.entity_id,
        "Title": ent.canonical_name,
        "Industry": industries[0] if industries else "",
        "Description": "",
        "Data Sources": "; ".join(ent.sources[:3]),
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_buyer_persona(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    industries = neighbors_ctx.get("industries") or []
    return {
        "Persona ID": ent.entity_id,
        "Persona Name": ent.canonical_name,
        "Industry": industries[0] if industries else "",
        "Job Role": ent.canonical_name,
        "Description": "",
        "Data Sources": "; ".join(ent.sources[:3]),
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_risk(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    return {
        "Risk ID": ent.entity_id,
        "Risk Name": ent.canonical_name,
        "Description": f"Risk associated with {ent.canonical_name}",
        "Industry": (neighbors_ctx.get("industries") or [""])[0],
        "Data Sources": "; ".join(ent.sources[:3]),
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_trend(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    return {
        "Trend ID": ent.entity_id,
        "Trend Title": ent.canonical_name,
        "Description": f"Trend signal: {ent.canonical_name}",
        "Industry": (neighbors_ctx.get("industries") or [""])[0],
        "Data Sources": "; ".join(ent.sources[:3]),
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_case_study(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    partner = (neighbors_ctx.get("technologies") or neighbors_ctx.get("products") or [""])[0]
    return {
        "Case ID": ent.entity_id,
        "Case Name": ent.canonical_name,
        "Challenge": "",
        "Solution Applied": partner or "",
        "Industry": (neighbors_ctx.get("industries") or [""])[0],
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_solution(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    return {
        "Solution ID": ent.entity_id,
        "Solution Name": ent.canonical_name,
        "Solution Description": f"Solution based on {ent.canonical_name}",
        "Suitable Industries": "; ".join((neighbors_ctx.get("industries") or [])[:5]),
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


def _payload_opportunity(ent: GraphEntity, neighbors_ctx: dict[str, Any]) -> dict[str, Any]:
    return {
        "Opportunity ID": ent.entity_id,
        "Opportunity Name": f"{ent.canonical_name} opportunity",
        "Opportunity Description": f"Market opportunity involving {ent.canonical_name}",
        "Industry": (neighbors_ctx.get("industries") or [""])[0],
        "Notes": f"manufactured_from_graph:{ent.entity_id}",
        "Last Updated": (ent.last_seen or "")[:10],
    }


_PAYLOAD_BUILDERS = {
    "company_profile": _payload_company,
    "competitor_library": _payload_competitor,
    "industry_library": _payload_industry,
    "product_catalog": _payload_product,
    "framework_library": _payload_framework,
    "regulation_library": _payload_regulation,
    "decision_maker_library": _payload_decision_maker,
    "buyer_persona_library": _payload_buyer_persona,
    "risk_library": _payload_risk,
    "trend_library": _payload_trend,
    "case_study_library": _payload_case_study,
    "solution_library": _payload_solution,
    "opportunity_analysis": _payload_opportunity,
}


def _neighbor_context(
    ent: GraphEntity,
    *,
    repo_root: Optional[Path] = None,
) -> dict[str, Any]:
    """Collect related entity names via graph edges."""
    ctx: dict[str, list[str]] = {
        "industries": [],
        "countries": [],
        "technologies": [],
        "products": [],
        "regulations": [],
        "frameworks": [],
    }
    entities = load_all_entities(repo_root=repo_root)
    edges = list(outgoing(ent.entity_id, repo_root=repo_root)) + list(
        incoming(ent.entity_id, repo_root=repo_root)
    )
    for edge in edges:
        other_id = (
            edge.target_entity
            if edge.source_entity == ent.entity_id
            else edge.source_entity
        )
        other = entities.get(other_id)
        if not other:
            continue
        name = other.canonical_name
        et = other.entity_type
        if et == "Industry" and name not in ctx["industries"]:
            ctx["industries"].append(name)
        elif et == "Country" and name not in ctx["countries"]:
            ctx["countries"].append(name)
        elif et == "Technology" and name not in ctx["technologies"]:
            ctx["technologies"].append(name)
            ctx["products"].append(name)
        elif et == "Regulation" and name not in ctx["regulations"]:
            ctx["regulations"].append(name)
        elif et in {"Framework", "Standard"} and name not in ctx["frameworks"]:
            ctx["frameworks"].append(name)
    return ctx


def _datasets_for_entity(ent: GraphEntity) -> list[str]:
    return list(ENTITY_DATASET_MAP.get(ent.entity_type, []))


def _build_candidate(
    *,
    ent: GraphEntity,
    target_dataset: str,
    payload: dict[str, Any],
    session_id: str,
    force: bool,
    repo_root: Optional[Path],
) -> Optional[dict[str, Any]]:
    source_id = f"entity:{ent.entity_id}"
    key = manufacture_key(
        source_id=source_id, target_dataset=target_dataset, payload=payload
    )
    if not force and was_manufactured(key, repo_root=repo_root):
        return None

    prov = _provenance_from_entity(ent)
    cand = CandidateRecord.create(
        entity_type=ent.entity_type,
        entity_id=ent.entity_id,
        target_dataset=target_dataset,
        payload=payload,
        provenance=prov,
        canonical_name=ent.canonical_name,
        metadata={
            "manufacturing_version": MANUFACTURING_VERSION,
            "manufacture_key": key,
            "session_id": session_id,
            "graph_entity_id": ent.entity_id,
            "knowledge_score": ent.knowledge_score,
        },
    )
    cand.touch("knowledge_manufacture")
    qa = assess_candidate(cand, repo_root=repo_root)
    disposition = qa.disposition
    path = enqueue_candidate(
        cand.to_dict(), disposition=disposition, repo_root=repo_root
    )
    mark_manufactured(
        key,
        candidate_id=cand.candidate_id,
        target_dataset=target_dataset,
        source_id=source_id,
        repo_root=repo_root,
    )
    return {
        "candidate_id": cand.candidate_id,
        "target_dataset": target_dataset,
        "entity_id": ent.entity_id,
        "disposition": disposition,
        "completeness": qa.completeness,
        "confidence": qa.confidence,
        "path": str(path),
        "reused": False,
    }


def manufacture_entity(
    entity_id: str,
    *,
    session_id: str = "",
    repo_root: Optional[Path] = None,
    force: bool = False,
    datasets: Optional[Sequence[str]] = None,
) -> dict[str, Any]:
    """Manufacture candidates for ALL compatible datasets from one entity."""
    root = repo_root or find_repo_root()
    ent = get_entity(entity_id, repo_root=root)
    if not ent:
        return {"ok": False, "error": "entity_not_found", "entity_id": entity_id}

    targets = list(datasets) if datasets else _datasets_for_entity(ent)
    # Always expand — never stop after first dataset
    ctx = _neighbor_context(ent, repo_root=root)
    produced: list[dict[str, Any]] = []
    skipped = 0

    for ds in targets:
        builder = _PAYLOAD_BUILDERS.get(ds)
        if not builder:
            continue
        try:
            payload = builder(ent, ctx)
        except TypeError:
            payload = builder(ent, ctx)  # type: ignore[misc]
        result = _build_candidate(
            ent=ent,
            target_dataset=ds,
            payload=payload,
            session_id=session_id,
            force=force,
            repo_root=root,
        )
        if result is None:
            skipped += 1
        else:
            produced.append(result)

    return {
        "ok": True,
        "entity_id": entity_id,
        "canonical_name": ent.canonical_name,
        "entity_type": ent.entity_type,
        "datasets_targeted": targets,
        "candidates": produced,
        "skipped_reuse": skipped,
        "datasets_touched": sorted({c["target_dataset"] for c in produced}),
    }


def manufacture_relationship(
    relationship_id: str,
    *,
    session_id: str = "",
    repo_root: Optional[Path] = None,
    force: bool = False,
) -> dict[str, Any]:
    """Manufacture candidates from both ends of a relationship + edge-specific datasets."""
    root = repo_root or find_repo_root()
    rels = load_all_relationships(repo_root=root)
    rel = rels.get(relationship_id)
    if not rel:
        return {"ok": False, "error": "relationship_not_found", "relationship_id": relationship_id}

    produced: list[dict[str, Any]] = []
    # Manufacture both endpoint entities fully
    for eid in (rel.source_entity, rel.target_entity):
        res = manufacture_entity(
            eid, session_id=session_id, repo_root=root, force=force
        )
        if res.get("ok"):
            produced.extend(res.get("candidates") or [])

    # Extra datasets from relationship type
    extra_ds = REL_DATASET_MAP.get(rel.relationship_type, [])
    src = get_entity(rel.source_entity, repo_root=root)
    if src and extra_ds:
        ctx = _neighbor_context(src, repo_root=root)
        for ds in extra_ds:
            builder = _PAYLOAD_BUILDERS.get(ds)
            if not builder:
                continue
            payload = builder(src, ctx)
            # Stamp relationship provenance into notes
            payload["Notes"] = (
                f"{payload.get('Notes') or ''}; rel:{rel.relationship_type}:{rel.relationship_id}"
            ).strip("; ")
            result = _build_candidate(
                ent=src,
                target_dataset=ds,
                payload=payload,
                session_id=session_id,
                force=force,
                repo_root=root,
            )
            if result:
                result["from_relationship"] = rel.relationship_id
                produced.append(result)

    return {
        "ok": True,
        "relationship_id": relationship_id,
        "relationship_type": rel.relationship_type,
        "candidates": produced,
        "datasets_touched": sorted({c["target_dataset"] for c in produced}),
    }


def manufacture_document(
    document_id: str,
    *,
    session_id: str = "",
    repo_root: Optional[Path] = None,
    force: bool = False,
) -> dict[str, Any]:
    """Manufacture from all entities linked to a document (via entity document index)."""
    from automation.knowledge.entity_store import load_indexes

    root = repo_root or find_repo_root()
    idx = load_indexes(repo_root=root)
    entity_ids = list(idx.get("document", {}).get(document_id) or [])
    all_candidates: list[dict[str, Any]] = []
    entity_results: list[dict[str, Any]] = []
    for eid in entity_ids:
        res = manufacture_entity(
            eid, session_id=session_id, repo_root=root, force=force
        )
        entity_results.append(res)
        all_candidates.extend(res.get("candidates") or [])

    # Also walk relationships among these entities
    rels = load_all_relationships(repo_root=root)
    rel_ids = [
        rid
        for rid, r in rels.items()
        if r.source_entity in entity_ids or r.target_entity in entity_ids
    ]
    for rid in rel_ids[:50]:
        res = manufacture_relationship(
            rid, session_id=session_id, repo_root=root, force=force
        )
        all_candidates.extend(res.get("candidates") or [])

    datasets = sorted({c["target_dataset"] for c in all_candidates})
    return {
        "ok": True,
        "document_id": document_id,
        "entities": len(entity_ids),
        "relationships_considered": len(rel_ids),
        "candidates": all_candidates,
        "candidate_count": len(all_candidates),
        "datasets_touched": datasets,
        "entity_results": entity_results,
    }


def manufacture(
    *,
    entity_ids: Optional[Sequence[str]] = None,
    relationship_ids: Optional[Sequence[str]] = None,
    document_ids: Optional[Sequence[str]] = None,
    session_id: str = "",
    repo_root: Optional[Path] = None,
    force: bool = False,
    limit: int = 200,
) -> dict[str, Any]:
    """Batch manufacturing entrypoint — graph → multi-dataset candidates."""
    root = repo_root or find_repo_root()
    candidates: list[dict[str, Any]] = []
    datasets: set[str] = set()
    processed_entities = 0
    processed_rels = 0
    processed_docs = 0

    if document_ids:
        for did in list(document_ids)[:limit]:
            res = manufacture_document(
                did, session_id=session_id, repo_root=root, force=force
            )
            processed_docs += 1
            candidates.extend(res.get("candidates") or [])
            datasets.update(res.get("datasets_touched") or [])

    if entity_ids is None and not document_ids and not relationship_ids:
        # Default: all ACTIVE entities up to limit
        entities = load_all_entities(repo_root=root)
        entity_ids = [
            e.entity_id
            for e in entities.values()
            if e.status == "ACTIVE"
        ][:limit]

    if entity_ids:
        for eid in list(entity_ids)[:limit]:
            res = manufacture_entity(
                eid, session_id=session_id, repo_root=root, force=force
            )
            processed_entities += 1
            candidates.extend(res.get("candidates") or [])
            datasets.update(res.get("datasets_touched") or [])

    if relationship_ids:
        for rid in list(relationship_ids)[:limit]:
            res = manufacture_relationship(
                rid, session_id=session_id, repo_root=root, force=force
            )
            processed_rels += 1
            candidates.extend(res.get("candidates") or [])
            datasets.update(res.get("datasets_touched") or [])

    # Deduplicate candidate list by candidate_id
    by_id = {c["candidate_id"]: c for c in candidates if c.get("candidate_id")}
    unique = list(by_id.values())

    return {
        "ok": True,
        "manufacturing_version": MANUFACTURING_VERSION,
        "session_id": session_id,
        "processed_entities": processed_entities,
        "processed_relationships": processed_rels,
        "processed_documents": processed_docs,
        "candidate_count": len(unique),
        "candidates": unique,
        "datasets_touched": sorted(datasets),
        "queue": queue_stats(repo_root=root),
        "note": "Candidates only — publisher and domain CSVs unchanged",
    }
