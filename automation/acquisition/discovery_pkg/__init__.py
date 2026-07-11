"""Knowledge Discovery Layer — search engines discover URLs only.

Trusted Source Registry is the sole authority for knowledge extraction.
"""

from .layer import run_discovery
from .registry import DiscoveryRegistry, load_discovery_registry, operational_status
from .budgets import compute_adaptive_budgets, AdaptiveBudgets
from .audit import write_audit_reports, audit_providers

__all__ = [
    "run_discovery",
    "DiscoveryRegistry",
    "load_discovery_registry",
    "operational_status",
    "compute_adaptive_budgets",
    "AdaptiveBudgets",
    "write_audit_reports",
    "audit_providers",
]
