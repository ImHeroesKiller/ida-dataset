import { NextResponse } from "next/server";
import fs from "fs";
import { getFactoryKpis } from "@/lib/factory-kpis";
import { getExecutiveFactoryView } from "@/lib/executive-factory";
import { repoPath } from "@/lib/paths";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

function syncStatus(): {
  github: string;
  huggingface: string;
  export: string;
} {
  let huggingface = "Idle";
  try {
    const statePath = repoPath(
      "automation/learning/state/huggingface_publish_state.json"
    );
    if (fs.existsSync(statePath)) {
      const j = JSON.parse(fs.readFileSync(statePath, "utf8")) as Record<
        string,
        unknown
      >;
      if (j.ok === true) huggingface = "Synced";
      else if (j.skipped) huggingface = "Idle";
      else if (j.running) huggingface = "Running";
      else huggingface = "Idle";
    } else {
      const ver = repoPath("reports/huggingface/verification.md");
      if (fs.existsSync(ver)) {
        const t = fs.readFileSync(ver, "utf8");
        if (/PASS/i.test(t)) huggingface = "Synced";
        else if (/FAIL/i.test(t)) huggingface = "Failed";
      }
    }
  } catch {
    /* ignore */
  }

  let exportLabel = "Idle";
  try {
    const roots = [
      "exports/jsonl",
      "exports/openai",
      "exports/huggingface",
      "exports/parquet",
    ];
    let n = 0;
    for (const r of roots) {
      const p = repoPath(r);
      if (!fs.existsSync(p)) continue;
      n += fs.readdirSync(p).filter((f) => !f.startsWith(".")).length;
    }
    if (n > 0) exportLabel = "Synced";
  } catch {
    /* ignore */
  }

  return {
    github: "Synced",
    huggingface,
    export: exportLabel,
  };
}

export async function GET() {
  try {
    const kpis = getFactoryKpis();
    let executive = null;
    try {
      executive = getExecutiveFactoryView();
    } catch {
      executive = null;
    }
    return NextResponse.json({
      ok: true,
      factory: "IDA Dataset Factory",
      version: "2.0",
      kpis,
      executive,
      sync: syncStatus(),
    });
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    return NextResponse.json(
      { ok: false, error: err.message },
      { status: 500 }
    );
  }
}
