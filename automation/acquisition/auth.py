"""API authentication helpers — environment variables only, never hardcode secrets."""

from __future__ import annotations

import base64
import os
from typing import Any, Optional


def resolve_auth_headers(auth_config: dict[str, Any] | None) -> dict[str, str]:
    """Build auth headers from source/connector config referencing env vars.

    Supported types:
      none | anonymous | api_key | bearer | basic | oauth2 | service_account
    """
    cfg = auth_config or {}
    auth_type = str(cfg.get("type") or cfg.get("authentication") or "none").lower()
    if auth_type in {"none", "anonymous", ""}:
        return {}

    headers: dict[str, str] = {}

    if auth_type in {"api_key", "apikey"}:
        env_name = str(cfg.get("env") or cfg.get("api_key_env") or "IDA_API_KEY")
        key = os.environ.get(env_name, "").strip()
        if not key:
            return {}
        header_name = str(cfg.get("header") or "X-API-Key")
        prefix = str(cfg.get("prefix") or "")
        headers[header_name] = f"{prefix}{key}" if prefix else key
        # query param style keys are handled by callers via resolve_auth_query
        return headers

    if auth_type == "bearer":
        env_name = str(cfg.get("env") or cfg.get("token_env") or "IDA_BEARER_TOKEN")
        token = os.environ.get(env_name, "").strip()
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    if auth_type == "basic":
        user_env = str(cfg.get("username_env") or "IDA_BASIC_USER")
        pass_env = str(cfg.get("password_env") or "IDA_BASIC_PASS")
        user = os.environ.get(user_env, "").strip()
        password = os.environ.get(pass_env, "").strip()
        if user:
            raw = f"{user}:{password}".encode("utf-8")
            headers["Authorization"] = "Basic " + base64.b64encode(raw).decode("ascii")
        return headers

    if auth_type in {"oauth2", "service_account"}:
        # Token must be pre-minted into env (factory does not run OAuth dances)
        env_name = str(cfg.get("env") or cfg.get("token_env") or "IDA_OAUTH_TOKEN")
        token = os.environ.get(env_name, "").strip()
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    return headers


def resolve_auth_query(auth_config: dict[str, Any] | None) -> dict[str, str]:
    """Optional query-string API keys (e.g. ?api_key=)."""
    cfg = auth_config or {}
    auth_type = str(cfg.get("type") or cfg.get("authentication") or "none").lower()
    if auth_type not in {"api_key", "apikey"}:
        return {}
    if str(cfg.get("placement") or "header").lower() != "query":
        return {}
    env_name = str(cfg.get("env") or cfg.get("api_key_env") or "IDA_API_KEY")
    key = os.environ.get(env_name, "").strip()
    if not key:
        return {}
    param = str(cfg.get("query_param") or "api_key")
    return {param: key}
