import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { RoleBadge } from "@/components/ui/badge";
import { getFactoryKpis } from "@/lib/factory-kpis";
import fs from "fs";
import path from "path";
import { repoPath } from "@/lib/paths";
import type { BadgeRole } from "@/lib/design-tokens";

export const dynamic = "force-dynamic";

const CHANNELS = [
  { id: "github", label: "GitHub", dir: null as string | null },
  { id: "huggingface", label: "Hugging Face", dir: "exports/huggingface" },
  { id: "csv", label: "CSV", dir: "domains" },
  { id: "jsonl", label: "JSONL", dir: "exports/jsonl" },
  { id: "parquet", label: "Parquet", dir: "exports/parquet" },
  { id: "openai", label: "OpenAI", dir: "exports/openai" },
] as const;

function listArtifacts(rel: string | null): { name: string; mtime: number; size: number }[] {
  if (!rel) return [];
  const p = repoPath(rel);
  if (!fs.existsSync(p)) return [];
  try {
    return fs
      .readdirSync(p)
      .filter((n) => !n.startsWith(".") && n !== ".gitkeep")
      .map((name) => {
        const full = path.join(p, name);
        let st: fs.Stats;
        try {
          st = fs.statSync(full);
        } catch {
          return null;
        }
        // domains/ is multi-folder — count leaf CSVs only at top level
        if (st.isDirectory()) {
          return {
            name,
            mtime: st.mtimeMs,
            size: 0,
          };
        }
        return { name, mtime: st.mtimeMs, size: st.size };
      })
      .filter((x): x is { name: string; mtime: number; size: number } => Boolean(x))
      .sort((a, b) => b.mtime - a.mtime)
      .slice(0, 20);
  } catch {
    return [];
  }
}

function domainCsvCount(): number {
  const root = repoPath("domains");
  if (!fs.existsSync(root)) return 0;
  let n = 0;
  try {
    for (const domain of fs.readdirSync(root)) {
      const d = path.join(root, domain);
      if (!fs.statSync(d).isDirectory()) continue;
      for (const f of fs.readdirSync(d)) {
        if (f.endsWith(".csv")) n += 1;
      }
    }
  } catch {
    /* ignore */
  }
  return n;
}

function latestAcross(): { name: string; mtime: number; channel: string } | null {
  let best: { name: string; mtime: number; channel: string } | null = null;
  for (const ch of CHANNELS) {
    if (!ch.dir || ch.id === "csv") continue;
    for (const f of listArtifacts(ch.dir)) {
      if (!best || f.mtime > best.mtime) {
        best = { name: f.name, mtime: f.mtime, channel: ch.label };
      }
    }
  }
  return best;
}

function hfStatus(): { role: BadgeRole; label: string; version: string; rows: string } {
  const statePath = repoPath(
    "automation/learning/state/huggingface_publish_state.json"
  );
  try {
    if (fs.existsSync(statePath)) {
      const j = JSON.parse(fs.readFileSync(statePath, "utf8")) as Record<
        string,
        unknown
      >;
      if (j.ok === true)
        return {
          role: "completed",
          label: "Synced",
          version: String(j.version || "—"),
          rows: String(
            (j.stats as { total_rows?: number } | undefined)?.total_rows ?? "—"
          ),
        };
      if (j.running)
        return { role: "running", label: "Running", version: "—", rows: "—" };
      if (j.skipped)
        return { role: "idle", label: "Idle", version: "—", rows: "—" };
    }
  } catch {
    /* ignore */
  }
  const verPath = repoPath("reports/huggingface/verification.md");
  try {
    if (fs.existsSync(verPath)) {
      const t = fs.readFileSync(verPath, "utf8");
      if (/PASS/i.test(t))
        return { role: "completed", label: "Synced", version: "—", rows: "—" };
      if (/FAIL/i.test(t))
        return { role: "error", label: "Error", version: "—", rows: "—" };
    }
  } catch {
    /* ignore */
  }
  return { role: "idle", label: "Idle", version: "—", rows: "—" };
}

function channelRole(
  id: string,
  files: { name: string }[],
  hf: ReturnType<typeof hfStatus>
): { role: BadgeRole; label: string } {
  if (id === "github") return { role: "completed", label: "Synced" };
  if (id === "huggingface") return { role: hf.role, label: hf.label };
  if (id === "csv")
    return domainCsvCount() > 0
      ? { role: "completed", label: "Synced" }
      : { role: "idle", label: "Idle" };
  return files.length
    ? { role: "completed", label: "Synced" }
    : { role: "idle", label: "Idle" };
}

export default function ExportsPage() {
  const kpis = getFactoryKpis();
  const hf = hfStatus();
  const totalRows =
    kpis.datasets?.reduce((s, d) => s + (d.current_rows || 0), 0) || 0;
  const datasetCount = kpis.datasets?.length || 0;
  const version = (() => {
    try {
      return fs.readFileSync(repoPath("VERSION"), "utf8").trim();
    } catch {
      return "—";
    }
  })();
  const latest = latestAcross();
  const durationHint = latest
    ? new Date(latest.mtime).toISOString().slice(0, 16).replace("T", " ")
    : "—";

  // Lightweight queue snapshot from publish queue files
  let pending = 0;
  let completed = 0;
  try {
    const q = repoPath("automation/queue/publish");
    if (fs.existsSync(q)) {
      pending = fs
        .readdirSync(q)
        .filter((n) => n.startsWith("CAND-") && n.endsWith(".json")).length;
    }
  } catch {
    /* ignore */
  }
  completed = kpis.exports_generated || 0;
  const running = 0;
  const failed = 0;

  return (
    <Shell title="Export">
      <div className="op-page">
        <header className="op-page-header">
          <div>
            <h1 className="text-page-title">Export</h1>
            <p>Monitor packaging and publish channels.</p>
          </div>
        </header>

        {/* Export status channels */}
        <Card>
          <CardHeader title="Export Status" description="Publish channels" />
          <CardBody className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
            {CHANNELS.map((ch) => {
              const files = listArtifacts(ch.dir);
              const st = channelRole(ch.id, files, hf);
              const count =
                ch.id === "csv"
                  ? domainCsvCount()
                  : ch.id === "github"
                    ? 1
                    : files.length;
              return (
                <div
                  key={ch.id}
                  className="flex items-center justify-between gap-2 rounded-[var(--radius-md)] border border-[var(--border)] bg-[var(--panel-2)] px-2.5 py-2"
                >
                  <div className="min-w-0">
                    <div className="text-xs font-semibold text-[var(--text)]">
                      {ch.label}
                    </div>
                    <div className="text-[10px] text-[var(--text-muted)]">
                      {ch.id === "github"
                        ? "Append-only main"
                        : ch.id === "huggingface"
                          ? `v${hf.version} · ${hf.rows} rows`
                          : `${count} artifact${count === 1 ? "" : "s"}`}
                    </div>
                  </div>
                  <RoleBadge role={st.role}>{st.label}</RoleBadge>
                </div>
              );
            })}
          </CardBody>
        </Card>

        {/* Latest export KPIs */}
        <Card>
          <CardHeader title="Latest Export" />
          <CardBody className="grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
            <Kpi label="Latest" value={latest?.name?.slice(0, 28) || "—"} />
            <Kpi label="Rows" value={totalRows.toLocaleString()} medium />
            <Kpi label="Datasets" value={String(datasetCount)} medium />
            <Kpi label="Duration" value={durationHint} />
            <Kpi label="Version" value={version} medium />
          </CardBody>
        </Card>

        {/* Export queue */}
        <Card>
          <CardHeader title="Export Queue" description="Publish pipeline" />
          <CardBody className="grid grid-cols-2 gap-2 sm:grid-cols-4">
            <QueueCell label="Pending" value={pending} />
            <QueueCell label="Running" value={running} />
            <QueueCell label="Completed" value={completed} />
            <QueueCell label="Failed" value={failed} />
          </CardBody>
        </Card>

        <p className="text-center text-[11px] text-[var(--text-muted)]">
          Live export console · bottom panel · filters: Export · GitHub · Hugging Face
        </p>
      </div>
    </Shell>
  );
}

function Kpi({
  label,
  value,
  medium,
}: {
  label: string;
  value: string;
  medium?: boolean;
}) {
  return (
    <div className="min-w-0">
      <p className="text-[10px] font-semibold uppercase tracking-wide text-[var(--text-muted)]">
        {label}
      </p>
      <p
        className={
          medium
            ? "mt-0.5 truncate text-kpi text-[var(--text)]"
            : "mt-0.5 truncate text-xs font-semibold text-[var(--text)]"
        }
        title={value}
      >
        {value}
      </p>
    </div>
  );
}

function QueueCell({ label, value }: { label: string; value: number }) {
  return (
    <div className="rounded-[var(--radius-md)] border border-[var(--border)] bg-[var(--panel-2)] px-2.5 py-2 text-center">
      <p className="text-[10px] font-semibold uppercase tracking-wide text-[var(--text-muted)]">
        {label}
      </p>
      <p className="mt-0.5 text-kpi tabular-nums text-[var(--text)]">{value}</p>
    </div>
  );
}
