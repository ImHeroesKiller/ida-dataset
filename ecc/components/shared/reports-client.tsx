"use client";

import { useEffect, useMemo, useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { useInspector } from "@/components/layout/inspector-context";
import { cn } from "@/lib/utils";

type Item = {
  kind: string;
  name: string;
  relativePath: string;
  mtime: string | null;
  size: number;
};

export function ReportsClient({
  items,
  waiting,
  message,
}: {
  items: Item[];
  waiting: boolean;
  message: string | null;
}) {
  const { inspect } = useInspector();
  const [kind, setKind] = useState("all");
  const [selected, setSelected] = useState<string | null>(null);
  const [content, setContent] = useState<string | null>(null);

  const kinds = useMemo(
    () => Array.from(new Set(items.map((i) => i.kind))).sort(),
    [items]
  );

  const filtered = useMemo(
    () => items.filter((i) => kind === "all" || i.kind === kind),
    [items, kind]
  );

  useEffect(() => {
    if (!selected) return;
    let alive = true;
    (async () => {
      const res = await fetch(
        `/api/reports?file=${encodeURIComponent(selected)}`
      );
      const data = await res.json();
      if (alive) setContent(data.content ?? data.error ?? "");
    })();
    return () => {
      alive = false;
    };
  }, [selected]);

  function download(path: string, name: string, body: string) {
    const blob = new Blob([body], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = name;
    a.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div className="grid gap-3 xl:grid-cols-[320px_1fr]">
      <Card>
        <CardHeader title="Run history" description="reports/** artifacts" />
        <CardBody className="space-y-2">
          <div className="flex flex-wrap gap-1">
            <Button
              size="sm"
              variant={kind === "all" ? "default" : "ghost"}
              onClick={() => setKind("all")}
            >
              all
            </Button>
            {kinds.map((k) => (
              <Button
                key={k}
                size="sm"
                variant={kind === k ? "default" : "ghost"}
                onClick={() => setKind(k)}
              >
                {k}
              </Button>
            ))}
          </div>
          {waiting ? (
            <p className="text-xs text-zinc-500">{message}</p>
          ) : (
            <div className="max-h-[520px] space-y-0.5 overflow-y-auto scrollbar-thin">
              {filtered.map((item) => (
                <button
                  key={item.relativePath}
                  className={cn(
                    "flex w-full flex-col rounded-md px-2 py-1.5 text-left hover:bg-zinc-900",
                    selected === item.relativePath &&
                      "bg-zinc-900 ring-1 ring-zinc-700"
                  )}
                  onClick={() => {
                    setSelected(item.relativePath);
                    inspect({
                      kind: "report",
                      title: item.name,
                      subtitle: item.relativePath,
                      meta: {
                        Kind: item.kind,
                        Size: String(item.size),
                        Modified: item.mtime ?? "—",
                      },
                    });
                  }}
                >
                  <span className="text-xs text-zinc-100">{item.name}</span>
                  <span className="text-[10px] text-zinc-500">
                    {item.kind}
                    {item.mtime ? ` · ${item.mtime.slice(0, 19)}` : ""}
                  </span>
                </button>
              ))}
            </div>
          )}
        </CardBody>
      </Card>

      <Card>
        <CardHeader
          title="Open report"
          description={selected ?? "Select a report"}
          action={
            content && selected ? (
              <Button
                size="sm"
                variant="secondary"
                onClick={() =>
                  download(
                    selected,
                    selected.split("/").pop() ?? "report.txt",
                    content
                  )
                }
              >
                Download
              </Button>
            ) : null
          }
        />
        <CardBody>
          {!selected ? (
            <p className="text-xs text-zinc-500">
              Waiting for first execution / select a report
            </p>
          ) : (
            <pre className="max-h-[640px] overflow-auto rounded-md border border-zinc-900 bg-zinc-950 p-3 font-mono text-[11px] leading-relaxed whitespace-pre-wrap text-zinc-400 scrollbar-thin">
              {content ?? "Loading…"}
            </pre>
          )}
        </CardBody>
      </Card>
    </div>
  );
}
