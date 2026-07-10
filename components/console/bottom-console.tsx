"use client";

import { useEffect, useRef, useState } from "react";
import { BookOpen, Trash2 } from "lucide-react";
import { cn } from "@/lib/utils";

type JournalLine = {
  ts?: string;
  verb?: string;
  detail?: string;
  stage?: string;
  dataset?: string;
};

const verbClass: Record<string, string> = {
  Searching: "text-sky-400",
  Downloading: "text-cyan-400",
  Reading: "text-violet-300",
  Understanding: "text-fuchsia-300",
  Extracting: "text-amber-300",
  Validating: "text-yellow-300",
  Publishing: "text-emerald-400",
  "Learning Completed": "text-emerald-300",
  "Mission Completed": "text-emerald-300",
  "Knowledge Updated": "text-lime-300",
  Mission: "text-indigo-300",
  Learning: "text-zinc-300",
};

export function BottomConsole() {
  const [lines, setLines] = useState<JournalLine[]>([]);
  const endRef = useRef<HTMLDivElement>(null);
  const [autoScroll, setAutoScroll] = useState(true);

  useEffect(() => {
    let alive = true;
    const poll = async () => {
      try {
        const res = await fetch("/api/journal", { cache: "no-store" });
        const data = await res.json();
        if (alive) setLines(data.journal ?? []);
      } catch {
        /* ignore */
      }
    };
    poll();
    const id = setInterval(poll, 1500);
    return () => {
      alive = false;
      clearInterval(id);
    };
  }, []);

  useEffect(() => {
    if (autoScroll) endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [lines, autoScroll]);

  const view = [...lines].slice(-120);

  return (
    <div className="flex h-[var(--console-h)] shrink-0 flex-col border-t border-zinc-800/90 bg-[#070708]">
      <div className="flex h-8 items-center justify-between border-b border-zinc-900 px-3">
        <div className="flex items-center gap-2 text-[11px] text-zinc-400">
          <BookOpen className="h-3.5 w-3.5" />
          <span className="font-medium text-zinc-300">Learning Journal</span>
          <span className="text-zinc-600">·</span>
          <span className="text-zinc-500">
            Searching · Downloading · Reading · Understanding · Extracting ·
            Validating · Publishing
          </span>
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
            onClick={() => setLines([])}
            title="Clear local view only"
          >
            <Trash2 className="h-3 w-3" />
            Clear view
          </button>
        </div>
      </div>
      <div className="flex-1 overflow-y-auto px-3 py-2 font-mono text-[11px] leading-5 scrollbar-thin">
        {view.length === 0 ? (
          <div className="text-zinc-600">
            Learning journal empty — run the first cycle:
            <span className="text-zinc-400">
              {" "}
              python -m automation.learning.first_cycle
            </span>
          </div>
        ) : (
          view.map((line, idx) => {
            const verb = String(line.verb || "Learning");
            return (
              <div key={`${line.ts}-${idx}`} className="flex gap-2">
                <span className="shrink-0 text-zinc-700">
                  {String(line.ts || "").slice(11, 19)}
                </span>
                <span
                  className={cn(
                    "shrink-0 font-medium",
                    verbClass[verb] || "text-zinc-300"
                  )}
                >
                  {verb}
                </span>
                <span className="text-zinc-400">{String(line.detail || "")}</span>
                {line.dataset ? (
                  <span className="text-zinc-600">[{String(line.dataset)}]</span>
                ) : null}
              </div>
            );
          })
        )}
        <div ref={endRef} />
      </div>
    </div>
  );
}
