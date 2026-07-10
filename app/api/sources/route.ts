import { NextResponse } from "next/server";
import { getSourceHealthDashboard } from "@/lib/source-health";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/** GET /api/sources — trusted source health & production metrics */
export async function GET() {
  try {
    const dash = getSourceHealthDashboard();
    return NextResponse.json({
      ok: true,
      factory: "IDA Dataset Factory",
      ...dash,
    });
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    return NextResponse.json(
      { ok: false, error: err.message },
      { status: 500 }
    );
  }
}
