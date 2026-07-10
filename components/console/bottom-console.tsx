"use client";

import { useEffect, useRef, useState } from "react";
import { Terminal, Trash2 } from "lucide-react";
import { cn } from "@/lib/utils";
import type { ConsoleLine, ProgressState } from "@/lib/orchestration";

const streamClass: Record<ConsoleLine["stream"], string> = {
  system: "ansi-system",
  planner: "ansi-planner",
  pipeline: "ansi-pipeline",
  validator: "ansi-validator",
  publisher: "ansi-publisher",
  git: "ansi-git",
  policy: "ansi-policy",
};

const levelClass: Record<ConsoleLine["level"], string> = {
  info: "ansi-info",
  warn: "ansi-warn",
  error: "ansi-error",
  success: "ansi-success",
};

export function BottomConsole() {
  const [progress, setProgress] = useState<ProgressState | null>(null);
  const [localLogs, setLocalLogs] = useState<ConsoleLine[]>([]);
  const endRef = useRef<HTMLDivElement>(null);
  const [autoScroll, setAutoScroll] = useState(true);

  useEffect(() => {
    let alive = true;
    const poll = async () => {
      try {
        const res = await fetch("/api/console", { cache: "no-store" });
        const data = await res.json();
        if (alive) {
          setProgress(data.progress);
          setLocalLogs(data.progress?.logs ?? []);
        }
      } catch {
        // ignore poll errors
      }
    };
    poll();
    const id = setInterval(poll, 1000);
    return () => {
      alive = false;
      clearInterval(id);
    };
  }, []);

  useEffect(() => {
    if (autoScroll) endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [localLogs, autoScroll]);

  const status = progress?.status ?? "idle";

  return (
    <div className="flex h-[var(--console-h)] shrink-0 flex-col border-t border-zinc-800/90 bg-[#070708]">
      <div className="flex h-8 items-center justify-between border-b border-zinc-900 px-3">
        <div className="flex items-center gap-2 text-[11px] text-zinc-400">
          <Terminal className="h-3.5 w-3.5" />
          <span className="font-medium text-zinc-300">Console</span>
          <span className="text-zinc-600">·</span>
          <span
            className={cn(
              status === "running" && "text-sky-400",
              status === "success" && "text-emerald-400",
              status === "error" && "text-red-400",
              status === "blocked" && "text-amber-300",
              status === "idle" && "text-zinc-500"
            )}
          >
            {status}
          </span>
          {progress?.runId ? (
            <span className="font-mono text-zinc-600">{progress.runId}</span>
          ) : null}
        </div>
        <div className="flex items-center gap-2">
          <label className="flex items-center gap-1 text-[10px] text-zinc-500">
            <input
              type="checkbox"
              checked={autoScroll}
              onChange={(e) => setAutoScroll(e.target.checked)}
              className="accent-zinc-400"
            />
            Auto-scroll
          </label>
          <button
            className="inline-flex items-center gap-1 text-[10px] text-zinc-500 hover:text-zinc-300"
            onClick={() => setLocalLogs([])}
            title="Clear local view only"
          >
            <Trash2 className="h-3 w-3" />
            Clear view
          </button>
        </div>
      </div>
      <div className="flex-1 overflow-y-auto px-3 py-2 font-mono text-[11px] leading-5 scrollbar-thin">
        {localLogs.length === 0 ? (
          <div className="text-zinc-600">
            Waiting for first execution — planner / validator / pipeline /
            publisher logs stream here.
          </div>
        ) : (
          localLogs.map((line, idx) => (
            <div key={`${line.ts}-${idx}`} className="flex gap-2">
              <span className="shrink-0 text-zinc-700">
                {line.ts.slice(11, 19)}
              </span>
              <span className={cn("shrink-0 uppercase", streamClass[line.stream])}>
                {line.stream}
              </span>
              <span className={cn(levelClass[line.level])}>{line.text}</span>
            </div>
          ))
        )}
        <div ref={endRef} />
      </div>
    </div>
  );
}
