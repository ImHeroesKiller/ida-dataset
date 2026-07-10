import { NextResponse } from "next/server";
import { getFactoryKpis } from "@/lib/factory-kpis";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

export async function GET() {
  try {
    const kpis = getFactoryKpis();
    return NextResponse.json({
      ok: true,
      factory: "IDA Dataset Factory",
      version: "2.0",
      kpis,
    });
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    return NextResponse.json(
      { ok: false, error: err.message },
      { status: 500 }
    );
  }
}
