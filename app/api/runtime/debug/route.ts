import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import { collectRuntimeDebug } from "@/lib/runtime-manager";
import { getSseListenerStats } from "@/lib/sse-registry";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/runtime/debug
 *
 * Returns runtime state, scheduler state, active session, active listeners,
 * worker status, connector status, last exception.
 * Always valid JSON.
 */
export async function GET() {
  return withApiJson("api.runtime.debug", async () => {
    try {
      const debug = collectRuntimeDebug();
      const listeners = getSseListenerStats();
      const session = debug.active_session as {
        session_id?: string | null;
        status?: string | null;
      };

      return jsonSuccess({
        status: String(session?.status || "ok"),
        session_id: session?.session_id ?? null,
        data: {
          ...debug,
          active_listeners: listeners,
        },
      });
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.runtime.debug",
        reason: err.message,
        error_code: "DEBUG_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
        recovery_suggestion:
          "Debug collector failed — check disk and automation/runtime permissions.",
      });
    }
  });
}
