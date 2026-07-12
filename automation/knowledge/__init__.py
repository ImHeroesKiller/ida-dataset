"""Knowledge manufacturing package (additive).

- Dataset Quality Engine
- Knowledge Atoms (persistent semantic units)
- (next) Entity graph + relationships

Does not redesign frozen pipeline, queue, mission, or CSV schemas.
Does not write dataset rows in Milestone 2.
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
)
from automation.knowledge.mandatory_fields import (
    all_mandatory_catalog,
    load_quality_config,
    mandatory_fields_for,
    thresholds,
)
from automation.knowledge.models import (
    AtomType,
    EnrichmentStatus,
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
    "AtomType",
    "EnrichmentStatus",
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
    "count_atoms",
    "is_empty",
    "iter_all_atoms",
    "list_atomized_documents",
    "load_atoms_for_document",
    "load_quality_config",
    "mandatory_fields_for",
    "may_publish_directly",
    "save_atoms_for_document",
    "score_completeness",
    "thresholds",
]
