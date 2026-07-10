"""API connector package — production HTTP/JSON collectors."""

from automation.connectors.builtin.api_connectors import (
    AdbConnector,
    CrossrefConnector,
    GenericWebsiteConnector,
    HttpApiConnector,
    OecdConnector,
    OpenAlexConnector,
    WorldBankConnector,
    BpsConnector,
    API_CONNECTOR_CLASSES,
)

__all__ = [
    "HttpApiConnector",
    "WorldBankConnector",
    "OpenAlexConnector",
    "CrossrefConnector",
    "OecdConnector",
    "AdbConnector",
    "BpsConnector",
    "GenericWebsiteConnector",
    "API_CONNECTOR_CLASSES",
]
