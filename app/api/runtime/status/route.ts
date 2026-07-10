import { NextResponse } from "next/server";
import {
  computeHealthBundle,
  readRuntimeStatus,
} from "@/lib/runtime-manager";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/runtime/status
 * Structured lifecycle + health for dashboard diagnostics.
 */
export async function GET() {
  const status = readRuntimeStatus();
  const health = computeHealthBundle();

  return NextResponse.json({
    status: status.status,
    session_id: status.session_id,
    correlation_id: status.correlation_id,
    started_at: status.started_at,
    stopped_at: status.stopped_at,
    current_stage: status.current_stage,
    current_task: status.current_task,
    documents_processed: status.documents_processed,
    knowledge_candidates: status.knowledge_candidates,
    uptime_seconds: status.uptime_seconds,
    pid: status.pid,
    instruction: status.instruction,
    last_error: status.last_error,
    health: health.components,
    overall_health: health.overall,
    health_details: health.details,
    host_capabilities: status.host_capabilities,
    updated_at: status.updated_at,
  });
}
