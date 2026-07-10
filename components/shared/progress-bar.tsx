"use client";

import { useEffect, useState } from "react";
import type { ProgressState } from "@/lib/orchestration";
import { cn } from "@/lib/utils";

function formatMs(ms: number | null | undefined) {
  if (ms == null) return "—";
  const s = Math.floor(ms / 1000);
  const m = Math.floor(s / 60);
  const r = s % 60;
  return m > 0 ? `${m}m ${r}s` : `${r}s`;
}

export function ProgressBar() {
  const [progress, setProgress] = useState<ProgressState | null>(null);

  useEffect(() => {
    let alive = true;
    const poll = async () => {
      try {
        const res = await fetch("/api/console", { cache: "no-store" });
        const data = await res.json();
        if (alive) setProgress(data.progress);
      } catch {
        /* ignore */
      }
    };
    poll();
    const id = setInterval(poll, 1000);
    return () => {
      alive = false;
      clearInterval(id);
    };
  }, []);

  if (!progress) return null;

  return (
    <div className="border-b border-zinc-800/80 bg-zinc-950/50 px-4 py-2">
      <div className="mb-1.5 flex flex-wrap items-center gap-x-4 gap-y-1 text-[11px] text-zinc-400">
        <span>
          Stage:{" "}
          <strong className="text-zinc-200">
            {progress.currentStage ?? "—"}
          </strong>
        </span>
        <span>
          Task:{" "}
          <strong className="text-zinc-200">{progress.currentTask}</strong>
        </span>
        <span>
          Dataset:{" "}
          <strong className="text-zinc-200">
            {progress.currentDataset ?? "—"}
          </strong>
        </span>
        <span>
          Rows:{" "}
          <strong className="text-zinc-200">{progress.rowsProcessed}</strong>
        </span>
        <span>
          Elapsed:{" "}
          <strong className="text-zinc-200">
            {formatMs(progress.elapsedMs)}
          </strong>
        </span>
        <span>
          ETA:{" "}
          <strong className="text-zinc-200">{formatMs(progress.etaMs)}</strong>
        </span>
        <span
          className={cn(
            "ml-auto font-medium",
            progress.status === "running" && "text-sky-400",
            progress.status === "success" && "text-emerald-400",
            progress.status === "error" && "text-red-400",
            progress.status === "blocked" && "text-amber-300",
            progress.status === "idle" && "text-zinc-500"
          )}
        >
          {progress.status} · {progress.progressPct}%
        </span>
      </div>
      <div className="h-1 overflow-hidden rounded-full bg-zinc-900">
        <div
          className={cn(
            "h-full rounded-full transition-all duration-300",
            progress.status === "error"
              ? "bg-red-500"
              : progress.status === "blocked"
                ? "bg-amber-400"
                : progress.status === "success"
                  ? "bg-emerald-500"
                  : "bg-sky-500"
          )}
          style={{ width: `${Math.min(100, progress.progressPct)}%` }}
        />
      </div>
    </div>
  );
}
