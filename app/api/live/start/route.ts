import { NextRequest, NextResponse } from "next/server";
import { startLiveRuntime } from "@/lib/runtime-manager";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * Start a live learning session (background process).
 *
 * 503 is returned only with a structured failure:
 *   component, exception, correlation_id, recovery_suggestion
 * Never a generic "unavailable" without diagnosis.
 *
 * Root causes documented in docs/runtime_troubleshooting.md:
 *  - host.vercel / host.ecc_disable_python
 *  - host.python_missing / host.python_import
 *  - runtime.lock (already running) → 409
 *  - runtime.spawn / runtime.process early exit
 */
export async function POST(req: NextRequest) {
  const body = (await req.json().catch(() => ({}))) as {
    instruction?: string;
    pace?: number;
  };

  const result = await startLiveRuntime({
    instruction: body.instruction,
    pace: body.pace,
  });

  return NextResponse.json(
    {
      ok: result.ok,
      message: result.message,
      pid: result.pid,
      correlation_id: result.correlation_id,
      session_id: result.session_id ?? result.status?.session_id ?? null,
      instruction: result.instruction,
      stream: result.stream,
      status: result.status,
      failure: result.failure,
      recovery_suggestion: result.recovery_suggestion,
      // keep error field for older clients
      error: result.ok ? undefined : result.message,
    },
    { status: result.status_code }
  );
}
