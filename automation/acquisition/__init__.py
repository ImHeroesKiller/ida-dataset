"""Real knowledge acquisition engine — collect → extract → validate → publish."""

from .pipeline import run_acquisition
from .source_registry import SourceRegistry, load_source_registry
from .trace import ProductionTrace, load_latest_trace
from .source_ranker import rank_sources, record_source_performance
from .download_manager import DownloadManager
from .performance import PerformanceCollector

__all__ = [
    "run_acquisition",
    "SourceRegistry",
    "load_source_registry",
    "ProductionTrace",
    "load_latest_trace",
    "rank_sources",
    "record_source_performance",
    "DownloadManager",
    "PerformanceCollector",
]
