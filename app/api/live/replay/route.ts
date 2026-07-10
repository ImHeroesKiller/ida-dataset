import { NextRequest } from "next/server";
import fs from "fs";
import path from "path";
import { getRepoRoot } from "@/lib/paths";
import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

export async function GET(req: NextRequest) {
  return withApiJson("api.live.replay", async () => {
    try {
      const sessionId = req.nextUrl.searchParams.get("session_id");
      const root = getRepoRoot();
      const sessionsDir = path.join(
        root,
        "automation/learning/state/sessions"
      );

      if (!sessionId) {
        if (!fs.existsSync(sessionsDir)) {
          return jsonSuccess({
            status: "ok",
            data: { sessions: [] },
          });
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
          .sort((a, b) =>
            String(b.started).localeCompare(String(a.started))
          );
        return jsonSuccess({
          status: "ok",
          data: { sessions },
        });
      }

      const file = path.join(sessionsDir, `${sessionId}.jsonl`);
      if (!fs.existsSync(file)) {
        return jsonFailure({
          component: "api.live.replay",
          reason: `session not found: ${sessionId}`,
          error_code: "SESSION_NOT_FOUND",
          session_id: sessionId,
          httpStatus: 404,
        });
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

      return jsonSuccess({
        status: "ok",
        session_id: sessionId,
        data: { session_id: sessionId, events },
      });
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.live.replay",
        reason: err.message,
        error_code: "REPLAY_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
      });
    }
  });
}
