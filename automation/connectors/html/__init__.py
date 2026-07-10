"""HTML connector package."""

from automation.connectors.builtin.api_connectors import (
    AdbConnector,
    BpsConnector,
    GenericWebsiteConnector,
    OecdConnector,
)

__all__ = ["AdbConnector", "BpsConnector", "GenericWebsiteConnector", "OecdConnector"]
