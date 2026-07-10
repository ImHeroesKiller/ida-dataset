"""KAS pipeline stages.

Order is fixed and must never be skipped:

1. discover
2. collect
3. extract
4. normalize
5. validate
6. deduplicate
7. entity_link
8. reviewer
9. publisher
"""

from . import (
    collect,
    deduplicate,
    discover,
    entity_link,
    extract,
    normalize,
    publisher,
    reviewer,
    validate,
)

STAGE_ORDER = [
    "discover",
    "collect",
    "extract",
    "normalize",
    "validate",
    "deduplicate",
    "entity_link",
    "reviewer",
    "publisher",
]

STAGE_MODULES = {
    "discover": discover,
    "collect": collect,
    "extract": extract,
    "normalize": normalize,
    "validate": validate,
    "deduplicate": deduplicate,
    "entity_link": entity_link,
    "reviewer": reviewer,
    "publisher": publisher,
}

__all__ = ["STAGE_ORDER", "STAGE_MODULES"]
