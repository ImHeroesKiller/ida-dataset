import { NextResponse } from "next/server";
import { getGitStatus } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json(getGitStatus());
}
