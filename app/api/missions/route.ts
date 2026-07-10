import { NextResponse } from "next/server";
import { listContracts, listMissions, listLearningReports } from "@/lib/learning";

export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json({
    missions: listMissions(),
    contracts: listContracts(),
    reports: listLearningReports(),
  });
}
