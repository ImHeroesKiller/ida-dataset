"""Built-in connector plugins — production API + placeholder fallbacks."""

from automation.connectors.builtin.api_connectors import API_CONNECTOR_CLASSES
from automation.connectors.builtin.stubs import CONNECTOR_CLASSES as STUB_CLASSES
from automation.connectors.base_connector import BaseConnector

# Prefer real API implementations; fall back to stubs for unknown keys
CONNECTOR_CLASSES: dict[str, type[BaseConnector]] = {
    **STUB_CLASSES,
    **API_CONNECTOR_CLASSES,
}

__all__ = ["CONNECTOR_CLASSES"]
