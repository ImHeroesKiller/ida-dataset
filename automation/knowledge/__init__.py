"""Knowledge manufacturing package (additive).

- Dataset Quality Engine
- Knowledge Atoms (persistent semantic units)
- Canonical Entity Layer (resolve + aliases + indexes)
- (next) Relationships / graph traversal

Does not redesign frozen pipeline, queue, mission, or CSV schemas.
Does not write dataset rows in Milestone 2.
Does not extract relationships in Commit 2.
"""

from automation.knowledge.atom_store import (
    atomize_and_persist_document,
    count_atoms,
    iter_all_atoms,
    list_atomized_documents,
    load_atoms_for_document,
    save_atoms_for_document,
)
from automation.knowledge.atoms import (
    ATOM_VERSION,
    atom_type_counts,
    atomize_document,
    atomize_text,
    normalize_atom_text,
)
from automation.knowledge.entities import (
    compute_knowledge_score,
    extract_and_resolve_atoms,
    extract_mentions_from_atom,
    process_document_entities,
    resolve_mention,
)
from automation.knowledge.entity_store import (
    entities_for_document,
    entity_stats,
    find_by_alias,
    find_by_canonical,
    get_entity,
    load_all_entities,
    load_indexes,
    normalize_name,
    upsert_entities_batch,
    upsert_entity,
)
from automation.knowledge.mandatory_fields import (
    all_mandatory_catalog,
    load_quality_config,
    mandatory_fields_for,
    thresholds,
)
from automation.knowledge.models import (
    AtomStatus,
    AtomType,
    CanonicalEntity,
    EnrichmentStatus,
    EntityStatus,
    FieldPresence,
    GraphEntity,
    GraphRelationship,
    KnowledgeAtom,
    PublishDisposition,
    QualityAssessment,
    QualityValidationStatus,
)
from automation.knowledge.quality import (
    assess_candidate,
    assess_row,
    completeness_report_lines,
    is_empty,
    may_publish_directly,
    score_completeness,
)

__all__ = [
    "ATOM_VERSION",
    "AtomStatus",
    "AtomType",
    "CanonicalEntity",
    "EnrichmentStatus",
    "EntityStatus",
    "FieldPresence",
    "GraphEntity",
    "GraphRelationship",
    "KnowledgeAtom",
    "PublishDisposition",
    "QualityAssessment",
    "QualityValidationStatus",
    "all_mandatory_catalog",
    "assess_candidate",
    "assess_row",
    "atom_type_counts",
    "atomize_and_persist_document",
    "atomize_document",
    "atomize_text",
    "completeness_report_lines",
    "compute_knowledge_score",
    "count_atoms",
    "entities_for_document",
    "entity_stats",
    "extract_and_resolve_atoms",
    "extract_mentions_from_atom",
    "find_by_alias",
    "find_by_canonical",
    "get_entity",
    "is_empty",
    "iter_all_atoms",
    "list_atomized_documents",
    "load_all_entities",
    "load_atoms_for_document",
    "load_indexes",
    "load_quality_config",
    "mandatory_fields_for",
    "may_publish_directly",
    "normalize_atom_text",
    "normalize_name",
    "process_document_entities",
    "resolve_mention",
    "save_atoms_for_document",
    "score_completeness",
    "thresholds",
    "upsert_entities_batch",
    "upsert_entity",
]
