import { NextRequest, NextResponse } from "next/server";
import { readSessionInfo } from "@/lib/runtime-manager";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/runtime/session
 * GET /api/runtime/session?session_id=SES-...
 */
export async function GET(req: NextRequest) {
  const sessionId = req.nextUrl.searchParams.get("session_id");
  const info = readSessionInfo(sessionId);
  if (info.error === "session_not_found") {
    return NextResponse.json(info, { status: 404 });
  }
  return NextResponse.json(info);
}
