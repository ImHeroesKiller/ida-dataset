"""Continuous Learning Scheduler — single orchestration entry above Planner.

Architecture:
  Human → Learning Mission → Scheduler → Priority Engine → Planner
  → Policy → Pipeline → Review → Publisher → Telemetry

Continuous Learning never stops.
Directed Learning never disables Continuous Learning.
Planner never starts directly — only via the Scheduler.
"""

__version__ = "0.1.0"
__system__ = "IDA-CLS"

from .scheduler import ContinuousLearningScheduler

__all__ = ["ContinuousLearningScheduler", "__version__"]
