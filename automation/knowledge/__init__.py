"""Knowledge manufacturing package (additive).

Dataset Quality Engine + (later) Knowledge Atoms, Graph, Enrichment.

Does not redesign frozen pipeline, queue, mission, or CSV schemas.
Quality metadata lives on CandidateRecord.metadata and automation/queue/enrichment.
"""

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
    "completeness_report_lines",
    "is_empty",
    "load_quality_config",
    "mandatory_fields_for",
    "may_publish_directly",
    "score_completeness",
    "thresholds",
]
