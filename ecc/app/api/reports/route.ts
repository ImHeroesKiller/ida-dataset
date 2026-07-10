import { NextRequest, NextResponse } from "next/server";
import { listReports, readReport } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  const file = req.nextUrl.searchParams.get("file");
  if (file) return NextResponse.json(readReport(file));
  return NextResponse.json(listReports());
}
