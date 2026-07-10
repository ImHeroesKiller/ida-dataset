import { NextRequest, NextResponse } from "next/server";
import { runOrchestration, type RunRequest } from "@/lib/orchestration";

export const dynamic = "force-dynamic";

const ALLOWED = new Set([
  "planner_dry_run",
  "validate",
  "review_summary",
  "publish_dry_run",
  "full_dry_chain",
]);

/**
 * Orchestration endpoint.
 * Never starts crawler.
 * Never publishes without dry-run (forced in orchestration layer).
 * Flow: Planner → Policy → Pipeline → Review → Publisher
 */
export async function POST(req: NextRequest) {
  const body = (await req.json().catch(() => ({}))) as Partial<RunRequest>;
  const action = body.action;
  if (!action || !ALLOWED.has(action)) {
    return NextResponse.json(
      {
        error: "Invalid action",
        allowed: Array.from(ALLOWED),
        note: "Crawler and non-dry publish are not exposed via ECC.",
      },
      { status: 400 }
    );
  }

  // Fire async for long runs but await here for simplicity in Sprint 3
  const progress = await runOrchestration({
    action: action as RunRequest["action"],
    environment: body.environment ?? "development",
  });

  return NextResponse.json({ ok: true, progress });
}
