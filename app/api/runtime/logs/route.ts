import { NextRequest } from "next/server";
import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import { readRuntimeLogs } from "@/lib/runtime-manager";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/runtime/logs?channel=errors&limit=50&session_id=&correlation_id=
 */
export async function GET(req: NextRequest) {
  return withApiJson("api.runtime.logs", async () => {
    try {
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

      return jsonSuccess({
        status: "ok",
        session_id,
        correlation_id,
        data: {
          channel: result.channel,
          count: result.entries.length,
          entries: result.entries,
        },
      });
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.runtime.logs",
        reason: err.message,
        error_code: "LOGS_READ_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
      });
    }
  });
}
