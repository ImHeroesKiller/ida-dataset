"""Base connector package — re-exports shared connector base classes."""

from automation.connectors.base_connector import BaseConnector
from automation.connectors.builtin.api_connectors import HttpApiConnector

__all__ = ["BaseConnector", "HttpApiConnector"]
