"""Real knowledge acquisition engine — collect → extract → validate → publish."""

from .pipeline import run_acquisition
from .source_registry import SourceRegistry, load_source_registry

__all__ = ["run_acquisition", "SourceRegistry", "load_source_registry"]
