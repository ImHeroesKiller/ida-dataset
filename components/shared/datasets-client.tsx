"use client";

import { useEffect, useMemo, useState } from "react";
import { Input } from "@/components/ui/input";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { useInspector } from "@/components/layout/inspector-context";
import { cn } from "@/lib/utils";

type DatasetInfo = {
  id: string;
  name: string;
  domain: string;
  relativePath: string;
  rowCount: number;
  columnCount: number;
  isPlaceholder: boolean;
  headers: string[];
  readiness?: number;
  product_target?: number;
  coverage_pct?: number;
  coverage_label?: string;
};

export function DatasetsClient({ datasets }: { datasets: DatasetInfo[] }) {
  const { inspect } = useInspector();
  const [q, setQ] = useState("");
  const [domain, setDomain] = useState("all");
  const [selected, setSelected] = useState<string | null>(
    datasets[0]?.relativePath ?? null
  );
  const [preview, setPreview] = useState<{
    headers: string[];
    previewRows: Record<string, string>[];
    rowCount: number;
    error?: string;
  } | null>(null);

  const domains = useMemo(
    () => Array.from(new Set(datasets.map((d) => d.domain))).sort(),
    [datasets]
  );

  const filtered = useMemo(() => {
    return datasets.filter((d) => {
      const okDomain = domain === "all" || d.domain === domain;
      const blob = `${d.name} ${d.domain} ${d.relativePath}`.toLowerCase();
      return okDomain && blob.includes(q.trim().toLowerCase());
    });
  }, [datasets, domain, q]);

  useEffect(() => {
    if (!selected) return;
    let alive = true;
    (async () => {
      const res = await fetch(
        `/api/datasets?file=${encodeURIComponent(selected)}&limit=50`
      );
      const data = await res.json();
      if (alive) setPreview(data);
    })();
    return () => {
      alive = false;
    };
  }, [selected]);

  return (
    <div className="grid gap-3 xl:grid-cols-[300px_1fr]">
      <Card>
        <CardHeader title="Catalog" description={`${datasets.length} files`} />
        <CardBody className="space-y-2">
          <Input
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="Search datasets…"
          />
          <select
            className="h-8 w-full rounded-md border border-zinc-800 bg-zinc-950 px-2 text-xs"
            value={domain}
            onChange={(e) => setDomain(e.target.value)}
          >
            <option value="all">All domains</option>
            {domains.map((d) => (
              <option key={d} value={d}>
                {d}
              </option>
            ))}
          </select>
          <div className="max-h-[520px] space-y-0.5 overflow-y-auto scrollbar-thin">
            {filtered.map((d) => (
              <button
                key={d.id}
                className={cn(
                  "flex w-full flex-col rounded-md px-2 py-1.5 text-left hover:bg-zinc-900",
                  selected === d.relativePath &&
                    "bg-zinc-900 ring-1 ring-zinc-700"
                )}
                onClick={() => {
                  setSelected(d.relativePath);
                  inspect({
                    kind: "dataset",
                    title: d.name,
                    subtitle: d.coverage_label
                      ? `${d.relativePath} · ${d.coverage_label} · readiness ${d.readiness ?? "—"}`
                      : d.relativePath,
                    meta: {
                      Domain: d.domain,
                      Rows: String(d.rowCount),
                      "Product target":
                        d.product_target != null
                          ? String(d.product_target)
                          : "—",
                      Coverage:
                        d.coverage_label != null
                          ? `${d.coverage_label} (${d.coverage_pct ?? 0}%)`
                          : "—",
                      Readiness:
                        d.readiness != null ? String(d.readiness) : "—",
                      Columns: String(d.columnCount),
                      Placeholder: String(d.isPlaceholder),
                    },
                    body: d.headers.join(", "),
                  });
                }}
              >
                <div className="flex w-full items-start justify-between gap-2">
                  <div className="min-w-0">
                    <span className="text-xs text-zinc-100">{d.name}</span>
                    <span className="mt-0.5 block text-[10px] text-zinc-500">
                      {d.domain}
                      {d.coverage_label
                        ? ` · ${d.coverage_label}`
                        : ` · ${d.rowCount} rows`}
                      {d.coverage_pct != null ? ` · ${d.coverage_pct}%` : ""}
                      {d.isPlaceholder ? " · placeholder" : ""}
                    </span>
                  </div>
                  <span
                    className="shrink-0 text-[10px] font-semibold text-emerald-400"
                    title="Dataset readiness (0–100)"
                  >
                    {d.readiness != null ? d.readiness : "—"}
                  </span>
                </div>
              </button>
            ))}
          </div>
        </CardBody>
      </Card>

      <Card>
        <CardHeader
          title="Preview"
          description="Read-only sample (first 50 rows)"
          action={
            selected ? (
              <Badge className="font-mono text-[10px]">{selected}</Badge>
            ) : null
          }
        />
        <CardBody className="overflow-x-auto">
          {!preview ? (
            <p className="text-xs text-zinc-500">Select a dataset.</p>
          ) : preview.error ? (
            <p className="text-xs text-red-400">{preview.error}</p>
          ) : (
            <>
              <div className="mb-2 flex flex-wrap gap-1.5 text-[11px] text-zinc-500">
                <span>{preview.rowCount} total rows</span>
                <span>·</span>
                <span>{preview.headers.length} columns</span>
                <span>·</span>
                <span>Statistics: non-empty headers only</span>
              </div>
              <table className="w-full min-w-[720px] text-left text-[11px]">
                <thead className="border-b border-zinc-800 text-zinc-500">
                  <tr>
                    {preview.headers.map((h) => (
                      <th key={h} className="px-2 py-1 font-medium whitespace-nowrap">
                        {h}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {preview.previewRows.length === 0 ? (
                    <tr>
                      <td
                        className="px-2 py-3 text-zinc-500"
                        colSpan={Math.max(preview.headers.length, 1)}
                      >
                        Waiting for first execution / header-only placeholder
                      </td>
                    </tr>
                  ) : (
                    preview.previewRows.map((row, idx) => (
                      <tr key={idx} className="border-b border-zinc-900/70">
                        {preview.headers.map((h) => (
                          <td
                            key={h}
                            className="max-w-[220px] truncate px-2 py-1 text-zinc-300"
                            title={row[h]}
                          >
                            {row[h]}
                          </td>
                        ))}
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </>
          )}
        </CardBody>
      </Card>
    </div>
  );
}
