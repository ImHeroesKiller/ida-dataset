import { NextRequest, NextResponse } from "next/server";
import { listDatasets, readDataset } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  const file = req.nextUrl.searchParams.get("file");
  if (file) {
    const limit = Number(req.nextUrl.searchParams.get("limit") ?? 100);
    return NextResponse.json(readDataset(file, limit));
  }
  return NextResponse.json({ datasets: listDatasets() });
}
