/**
 * Deprecated API surface — single source of truth for sunset endpoints.
 * Returns 410 Gone with migration guidance. Behavior: explicit failure, not silent.
 */

import { NextResponse } from "next/server";

export const DEPRECATED_ENDPOINTS: Record<
  string,
  { successor: string; reason: string }
> = {
  "/api/runtime/status": {
    successor: "/api/sessions",
    reason: "Local runtime removed; use GitHub Actions session monitor",
  },
  "/api/runtime/logs": {
    successor: "/api/sessions?session_id=",
    reason: "Session files supersede runtime log channels",
  },
  "/api/runtime/session": {
    successor: "/api/sessions",
    reason: "Use sessions API",
  },
  "/api/runtime/debug": {
    successor: "/api/sessions",
    reason: "Runtime manager removed",
  },
  "/api/console": {
    successor: "/api/publish-queue",
    reason: "Progress bar / console API retired; journal uses sessions + publish-queue",
  },
  "/api/status": {
    successor: "/api/sessions",
    reason: "Generic status retired",
  },
  "/api/git": {
    successor: "none",
    reason: "Unused; git metadata available via Vercel env if needed",
  },
  "/api/connectors": {
    successor: "/api/sources",
    reason: "Unused endpoint; use sources health API",
  },
  "/api/learning": {
    successor: "/api/missions",
    reason: "Mission dispatch moved to POST /api/missions; learn via /api/run",
  },
  "/api/network": {
    successor: "/api/sources",
    reason: "Network API removed; use sources",
  },
  "/api/documents": {
    successor: "none",
    reason: "Documents page reads via lib/network",
  },
  "/api/ontology": {
    successor: "none",
    reason: "Ontology page uses lib/repo-data",
  },
  "/api/planner": {
    successor: "none",
    reason: "Planner page uses lib/repo-data",
  },
  "/api/policies": {
    successor: "none",
    reason: "Policies page uses lib/repo-data",
  },
  "/api/reports": {
    successor: "/api/sessions",
    reason: "Reports page uses lib/sessions history",
  },
  "/api/live": {
    successor: "/api/sessions",
    reason: "SSE live stream retired; poll sessions",
  },
  "/api/live/replay": {
    successor: "/api/sessions?session_id=",
    reason: "Replay via sessions API",
  },
};

export function deprecatedGone(path: string): NextResponse {
  const meta = DEPRECATED_ENDPOINTS[path] || {
    successor: "/api/sessions",
    reason: "Deprecated",
  };
  return NextResponse.json(
    {
      ok: false,
      deprecated: true,
      error: "GONE",
      path,
      reason: meta.reason,
      successor: meta.successor,
      message: `This endpoint is deprecated. Use ${meta.successor}. (${meta.reason})`,
    },
    {
      status: 410,
      headers: {
        "Content-Type": "application/json; charset=utf-8",
        "Cache-Control": "no-store",
        Deprecation: "true",
        Sunset: "true",
      },
    }
  );
}
