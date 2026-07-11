"use client";

import { useEffect, useMemo, useState } from "react";
import { Input } from "@/components/ui/input";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge, RoleBadge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
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

function healthFromReadiness(r?: number): "healthy" | "warning" | "idle" {
  if (r == null) return "idle";
  if (r >= 70) return "healthy";
  if (r >= 40) return "warning";
  return "idle";
}

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

  const selectedMeta = datasets.find((d) => d.relativePath === selected);

  return (
    <div className="space-y-6">
      <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
        <div className="flex flex-1 flex-col gap-3 sm:max-w-md">
          <label className="text-caption font-semibold uppercase tracking-wide text-[var(--text-muted)]">
            Search catalog
          </label>
          <Input
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="Search datasets by name or domain…"
            aria-label="Search datasets"
          />
        </div>
        <div className="w-full sm:w-56">
          <label className="text-caption font-semibold uppercase tracking-wide text-[var(--text-muted)]">
            Domain
          </label>
          <select
            className="mt-2 h-11 w-full rounded-[var(--radius-lg)] border border-[var(--border)] bg-[var(--panel)] px-4 text-small text-[var(--text)]"
            value={domain}
            onChange={(e) => setDomain(e.target.value)}
            aria-label="Filter by domain"
          >
            <option value="all">All domains</option>
            {domains.map((d) => (
              <option key={d} value={d}>
                {d}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="grid gap-6 sm:grid-cols-2 xl:grid-cols-3">
        {filtered.map((d) => {
          const target = d.product_target ?? 0;
          const gap = Math.max(0, target - d.rowCount);
          const cov = d.coverage_pct ?? 0;
          const active = selected === d.relativePath;
          const health = healthFromReadiness(d.readiness);
          return (
            <button
              key={d.id}
              type="button"
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
                      d.product_target != null ? String(d.product_target) : "—",
                    Coverage:
                      d.coverage_label != null
                        ? `${d.coverage_label} (${d.coverage_pct ?? 0}%)`
                        : "—",
                    Readiness: d.readiness != null ? String(d.readiness) : "—",
                    Columns: String(d.columnCount),
                    Placeholder: String(d.isPlaceholder),
                  },
                  body: d.headers.join(", "),
                });
              }}
              className={cn(
                "rounded-[var(--radius-xl)] border bg-[var(--panel)] p-6 text-left shadow-[var(--shadow)] transition-all",
                active
                  ? "border-[var(--blue)] ring-2 ring-[var(--blue)]/25"
                  : "border-[var(--border)] hover:border-[var(--blue)]/40 hover:shadow-[var(--shadow-md)]"
              )}
            >
              <div className="flex items-start justify-between gap-3">
                <div className="min-w-0">
                  <h3 className="text-card-title truncate">{d.name}</h3>
                  <p className="mt-1 text-caption text-[var(--text-muted)]">
                    {d.domain}
                    {d.isPlaceholder ? " · placeholder" : ""}
                  </p>
                </div>
                <RoleBadge role={health} />
              </div>

              <div className="mt-5 grid grid-cols-2 gap-3 text-small">
                <div>
                  <div className="text-caption text-[var(--text-muted)]">Rows</div>
                  <div className="font-semibold tabular-nums text-[var(--text)]">
                    {d.rowCount.toLocaleString()}
                  </div>
                </div>
                <div>
                  <div className="text-caption text-[var(--text-muted)]">Target</div>
                  <div className="font-semibold tabular-nums text-[var(--text)]">
                    {target ? target.toLocaleString() : "—"}
                  </div>
                </div>
                <div>
                  <div className="text-caption text-[var(--text-muted)]">Gap</div>
                  <div className="font-semibold tabular-nums text-[var(--text)]">
                    {target ? gap.toLocaleString() : "—"}
                  </div>
                </div>
                <div>
                  <div className="text-caption text-[var(--text-muted)]">Readiness</div>
                  <div className="font-semibold tabular-nums text-[var(--text)]">
                    {d.readiness != null ? d.readiness : "—"}
                  </div>
                </div>
              </div>

              <div className="mt-5">
                <div className="mb-2 flex items-center justify-between text-caption">
                  <span className="text-[var(--text-muted)]">Coverage</span>
                  <span className="font-semibold text-[var(--text-secondary)]">
                    {cov}%
                    {d.coverage_label ? ` · ${d.coverage_label}` : ""}
                  </span>
                </div>
                <Progress value={cov} />
              </div>

              <div className="mt-4 flex flex-wrap gap-2">
                <Badge>{d.columnCount} columns</Badge>
                <Badge>{d.relativePath.split("/").pop()}</Badge>
              </div>
            </button>
          );
        })}
      </div>

      {selectedMeta ? (
        <Card>
          <CardHeader
            title={`Preview · ${selectedMeta.name}`}
            description={selectedMeta.relativePath}
          />
          <CardBody className="overflow-x-auto">
            {preview?.error ? (
              <p className="text-small text-[var(--red)]">{preview.error}</p>
            ) : preview?.headers?.length ? (
              <table className="ds-table min-w-[640px]">
                <thead>
                  <tr>
                    {preview.headers.slice(0, 8).map((h) => (
                      <th key={h}>{h}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {(preview.previewRows || []).slice(0, 12).map((row, i) => (
                    <tr key={i}>
                      {preview.headers.slice(0, 8).map((h) => (
                        <td key={h} className="max-w-[180px] truncate">
                          {row[h] ?? ""}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <p className="text-small text-[var(--text-muted)]">
                Select a dataset card to preview rows.
              </p>
            )}
          </CardBody>
        </Card>
      ) : null}
    </div>
  );
}
