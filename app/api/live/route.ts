import { NextRequest } from "next/server";
import fs from "fs";
import path from "path";
import { getRepoRoot, repoPath } from "@/lib/paths";
import { getKnowledgeKpis } from "@/lib/knowledge-kpis";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * Server-Sent Events stream for live learning journal + activity.
 * Clients subscribe (EventSource) — no completed-result polling.
 */
export async function GET(req: NextRequest) {
  const root = getRepoRoot();
  const journalFile = path.join(
    root,
    "automation/learning/state/learning_journal.jsonl"
  );
  const activityFile = path.join(
    root,
    "automation/learning/state/live_activity.json"
  );

  let closed = false;
  let offset = 0;
  if (fs.existsSync(journalFile)) {
    offset = fs.statSync(journalFile).size;
  }

  // optional: replay from beginning if ?from=0
  const fromStart = req.nextUrl.searchParams.get("from") === "0";
  if (fromStart) offset = 0;

  const stream = new ReadableStream({
    start(controller) {
      const enc = new TextEncoder();
      const send = (event: string, data: unknown) => {
        if (closed) return;
        controller.enqueue(
          enc.encode(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`)
        );
      };

      send("hello", {
        ts: new Date().toISOString(),
        message: "Learning stream connected",
      });

      // initial snapshot
      try {
        send("kpis", getKnowledgeKpis());
      } catch {
        /* ignore */
      }
      try {
        if (fs.existsSync(activityFile)) {
          send(
            "activity",
            JSON.parse(fs.readFileSync(activityFile, "utf8"))
          );
        }
      } catch {
        /* ignore */
      }

      const timer = setInterval(() => {
        if (closed) {
          clearInterval(timer);
          return;
        }
        try {
          if (fs.existsSync(journalFile)) {
            const stat = fs.statSync(journalFile);
            if (stat.size > offset) {
              const fd = fs.openSync(journalFile, "r");
              const len = stat.size - offset;
              const buf = Buffer.alloc(len);
              fs.readSync(fd, buf, 0, len, offset);
              fs.closeSync(fd);
              offset = stat.size;
              const chunk = buf.toString("utf8");
              for (const line of chunk.split("\n")) {
                const t = line.trim();
                if (!t) continue;
                try {
                  send("journal", JSON.parse(t));
                } catch {
                  /* skip bad line */
                }
              }
            }
          }
          if (fs.existsSync(activityFile)) {
            send(
              "activity",
              JSON.parse(fs.readFileSync(activityFile, "utf8"))
            );
          }
        } catch {
          /* ignore transient read errors */
        }
      }, 400);

      // heartbeat
      const beat = setInterval(() => {
        if (closed) {
          clearInterval(beat);
          return;
        }
        send("ping", { ts: new Date().toISOString() });
      }, 15000);

      const abort = () => {
        closed = true;
        clearInterval(timer);
        clearInterval(beat);
        try {
          controller.close();
        } catch {
          /* ignore */
        }
      };
      req.signal.addEventListener("abort", abort);
    },
    cancel() {
      closed = true;
    },
  });

  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream; charset=utf-8",
      "Cache-Control": "no-cache, no-transform",
      Connection: "keep-alive",
    },
  });
}
