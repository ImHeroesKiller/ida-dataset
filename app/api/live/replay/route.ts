import { NextRequest, NextResponse } from "next/server";
import fs from "fs";
import path from "path";
import { getRepoRoot } from "@/lib/paths";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  const sessionId = req.nextUrl.searchParams.get("session_id");
  const root = getRepoRoot();
  const sessionsDir = path.join(
    root,
    "automation/learning/state/sessions"
  );

  if (!sessionId) {
    // list sessions
    if (!fs.existsSync(sessionsDir)) {
      return NextResponse.json({ sessions: [] });
    }
    const sessions = fs
      .readdirSync(sessionsDir)
      .filter((f) => f.endsWith(".jsonl"))
      .map((f) => {
        const full = path.join(sessionsDir, f);
        const lines = fs
          .readFileSync(full, "utf8")
          .split("\n")
          .filter(Boolean);
        let first: Record<string, unknown> | null = null;
        let last: Record<string, unknown> | null = null;
        try {
          first = JSON.parse(lines[0] || "{}");
          last = JSON.parse(lines[lines.length - 1] || "{}");
        } catch {
          /* ignore */
        }
        return {
          session_id: f.replace(/\.jsonl$/, ""),
          events: lines.length,
          started: first?.ts ?? null,
          ended: last?.ts ?? null,
          last_verb: last?.verb ?? null,
        };
      })
      .sort((a, b) => String(b.started).localeCompare(String(a.started)));
    return NextResponse.json({ sessions });
  }

  const file = path.join(sessionsDir, `${sessionId}.jsonl`);
  if (!fs.existsSync(file)) {
    return NextResponse.json({ error: "session not found" }, { status: 404 });
  }
  const events = fs
    .readFileSync(file, "utf8")
    .split("\n")
    .filter(Boolean)
    .map((line) => {
      try {
        return JSON.parse(line);
      } catch {
        return null;
      }
    })
    .filter(Boolean);

  return NextResponse.json({ session_id: sessionId, events });
}
