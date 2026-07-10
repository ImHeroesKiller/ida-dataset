import { NextRequest, NextResponse } from "next/server";
import { readRuntimeLogs } from "@/lib/runtime-manager";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/runtime/logs?channel=errors&limit=50&session_id=&correlation_id=
 * Channels: system | learning | runtime | errors | publish | review | telemetry | all
 */
export async function GET(req: NextRequest) {
  const sp = req.nextUrl.searchParams;
  const channel = sp.get("channel") || "all";
  const limit = Math.min(500, Math.max(1, Number(sp.get("limit") || 100)));
  const session_id = sp.get("session_id");
  const correlation_id = sp.get("correlation_id");

  const result = readRuntimeLogs({
    channel,
    limit,
    session_id,
    correlation_id,
  });

  return NextResponse.json({
    channel: result.channel,
    count: result.entries.length,
    entries: result.entries,
  });
}
