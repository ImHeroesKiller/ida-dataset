import { NextResponse } from "next/server";
import { buildDashboardSnapshot } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json(buildDashboardSnapshot());
}
