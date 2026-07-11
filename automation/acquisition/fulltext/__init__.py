"""Full Text Acquisition Framework — extend acquisition only.

Resolves DOI → publisher / open-access / repository assets, ranks representations,
downloads the richest legal public body, and attaches it for existing extractors.

Metadata remains a last-resort fallback, never the preferred representation.
"""

from .chain import FullTextSession, enrich_document_dict, enrich_document_ref
from .reports import write_fulltext_reports
from .quality import score_content

__all__ = [
    "FullTextSession",
    "enrich_document_dict",
    "enrich_document_ref",
    "write_fulltext_reports",
    "score_content",
]
