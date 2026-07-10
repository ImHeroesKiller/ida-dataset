"""IDA Knowledge Network — controlled connector framework."""

__version__ = "0.1.0"
__system__ = "IDA-IKN"

from .manager import ConnectorManager
from .scheduler_bridge import SchedulerBridge

__all__ = ["ConnectorManager", "SchedulerBridge", "__version__"]
