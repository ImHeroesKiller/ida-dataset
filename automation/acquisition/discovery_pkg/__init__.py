"""Knowledge Discovery Layer — search engines discover URLs only.

Trusted Source Registry is the sole authority for knowledge extraction.
"""

from .layer import run_discovery
from .registry import DiscoveryRegistry, load_discovery_registry

__all__ = ["run_discovery", "DiscoveryRegistry", "load_discovery_registry"]
