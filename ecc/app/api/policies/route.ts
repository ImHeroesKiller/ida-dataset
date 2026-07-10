import { NextResponse } from "next/server";
import { getPolicies, getSources } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json({ policies: getPolicies(), sources: getSources() });
}
