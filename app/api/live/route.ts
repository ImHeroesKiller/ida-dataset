import { NextRequest } from "next/server";
import fs from "fs";
import path from "path";
import { getRepoRoot } from "@/lib/paths";
import { getKnowledgeKpis } from "@/lib/knowledge-kpis";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * Server-Sent Events stream for live learning journal + activity.
 *
 * Cleanup contract (no MaxListenersExceededWarning):
 *  - clearInterval on abort AND cancel
 *  - remove abort listener on teardown
 *  - never leave timers running after client disconnect
 *  - never call setMaxListeners — fix ownership instead
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

  const fromStart = req.nextUrl.searchParams.get("from") === "0";
  if (fromStart) offset = 0;

  let timer: ReturnType<typeof setInterval> | null = null;
  let beat: ReturnType<typeof setInterval> | null = null;
  let abortHandler: (() => void) | null = null;

  const stream = new ReadableStream({
    start(controller) {
      const enc = new TextEncoder();
      const send = (event: string, data: unknown) => {
        if (closed) return;
        try {
          controller.enqueue(
            enc.encode(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`)
          );
        } catch {
          // controller already closed
          teardown();
        }
      };

      const teardown = () => {
        if (closed) return;
        closed = true;
        if (timer) {
          clearInterval(timer);
          timer = null;
        }
        if (beat) {
          clearInterval(beat);
          beat = null;
        }
        if (abortHandler) {
          try {
            req.signal.removeEventListener("abort", abortHandler);
          } catch {
            /* ignore */
          }
          abortHandler = null;
        }
        try {
          controller.close();
        } catch {
          /* already closed */
        }
      };

      send("hello", {
        ts: new Date().toISOString(),
        message: "Learning stream connected",
      });

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

      timer = setInterval(() => {
        if (closed) {
          if (timer) clearInterval(timer);
          timer = null;
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

      beat = setInterval(() => {
        if (closed) {
          if (beat) clearInterval(beat);
          beat = null;
          return;
        }
        send("ping", { ts: new Date().toISOString() });
      }, 15000);

      abortHandler = () => teardown();
      req.signal.addEventListener("abort", abortHandler);

      // Store teardown on controller via closure for cancel()
      (controller as unknown as { __teardown?: () => void }).__teardown =
        teardown;
    },
    cancel() {
      // Client disconnected — release all resources immediately
      closed = true;
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
      if (beat) {
        clearInterval(beat);
        beat = null;
      }
      if (abortHandler) {
        try {
          req.signal.removeEventListener("abort", abortHandler);
        } catch {
          /* ignore */
        }
        abortHandler = null;
      }
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
