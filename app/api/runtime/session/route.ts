import { NextRequest } from "next/server";
import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import { readSessionInfo } from "@/lib/runtime-manager";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/runtime/session[?session_id=]
 */
export async function GET(req: NextRequest) {
  return withApiJson("api.runtime.session", async () => {
    try {
      const sessionId = req.nextUrl.searchParams.get("session_id");
      const info = readSessionInfo(sessionId);
      if (info.error === "session_not_found") {
        return jsonFailure({
          component: "api.runtime.session",
          reason: `Session not found: ${sessionId}`,
          error_code: "SESSION_NOT_FOUND",
          session_id: sessionId,
          httpStatus: 404,
          recovery_suggestion: "List sessions via /api/live/replay without session_id.",
        });
      }
      return jsonSuccess({
        status: String(info.status || info.runtime_status || "ok"),
        session_id: (info.session_id as string) ?? sessionId,
        correlation_id: (info.correlation_id as string) ?? null,
        data: info,
      });
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.runtime.session",
        reason: err.message,
        error_code: "SESSION_READ_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
      });
    }
  });
}
