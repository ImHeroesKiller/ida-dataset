import { NextResponse } from "next/server";
import { buildPlannerView } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json(buildPlannerView());
}
