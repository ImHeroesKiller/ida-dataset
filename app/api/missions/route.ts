import { NextRequest, NextResponse } from "next/server";
import {
  listContracts,
  listMissions,
  listLearningReports,
  runSchedulerCli,
} from "@/lib/learning";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

export async function GET() {
  return NextResponse.json({
    missions: listMissions(),
    contracts: listContracts(),
    reports: listLearningReports(),
  });
}

/**
 * POST /api/missions — create directed mission via existing scheduler CLI.
 * Replaces broken /api/learning mission dispatch.
 */
export async function POST(req: NextRequest) {
  const body = (await req.json().catch(() => ({}))) as {
    action?: string;
    text?: string;
    mission?: string;
  };
  const text = (body.text || body.mission || "").trim();
  if (!text) {
    return NextResponse.json(
      { ok: false, error: "text required" },
      { status: 400 }
    );
  }

  const result = runSchedulerCli(["mission", text]);
  if (!result.ok) {
    // On Vercel / no Python: still surface clearly (no silent 404)
    return NextResponse.json(
      {
        ok: false,
        error: result.stderr || "Mission creation unavailable on this runtime",
        result: result.data,
        hint: "Use GitHub Actions learn.yml for production missions",
      },
      { status: 422 }
    );
  }

  return NextResponse.json({
    ok: true,
    result: result.data,
    missions: listMissions(),
  });
}
