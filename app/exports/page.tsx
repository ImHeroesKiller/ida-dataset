import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge, RoleBadge } from "@/components/ui/badge";
import { getFactoryKpis } from "@/lib/factory-kpis";
import fs from "fs";
import path from "path";
import { repoPath } from "@/lib/paths";

export const dynamic = "force-dynamic";

const FORMATS = [
  { id: "csv", label: "CSV (domains)", dir: "domains", format: "csv" },
  { id: "jsonl", label: "JSONL", dir: "exports/jsonl", format: "jsonl" },
  { id: "parquet", label: "Parquet", dir: "exports/parquet", format: "parquet" },
  {
    id: "embeddings",
    label: "Embeddings / HF prep",
    dir: "exports/embeddings",
    format: "embeddings",
  },
  { id: "openai", label: "OpenAI fine-tuning", dir: "exports/openai", format: "jsonl" },
  {
    id: "huggingface",
    label: "Hugging Face",
    dir: "exports/huggingface",
    format: "json",
  },
];

function listArtifacts(rel: string): { name: string; mtime: number; size: number }[] {
  const p = repoPath(rel);
  if (!fs.existsSync(p)) return [];
  try {
    return fs
      .readdirSync(p)
      .filter((n) => !n.startsWith(".") && n !== ".gitkeep")
      .map((name) => {
        const full = path.join(p, name);
        const st = fs.statSync(full);
        return {
          name,
          mtime: st.mtimeMs,
          size: st.isFile() ? st.size : 0,
        };
      })
      .sort((a, b) => b.mtime - a.mtime)
      .slice(0, 40);
  } catch {
    return [];
  }
}

function fmtBytes(n: number): string {
  if (n < 1024) return `${n} B`;
  if (n < 1024 * 1024) return `${(n / 1024).toFixed(1)} KB`;
  return `${(n / (1024 * 1024)).toFixed(1)} MB`;
}

function readTextIfExists(rel: string): string | null {
  const p = repoPath(rel);
  try {
    if (!fs.existsSync(p)) return null;
    return fs.readFileSync(p, "utf8");
  } catch {
    return null;
  }
}

function hfPublishStatus(): {
  status: string;
  version: string;
  rows: string;
  repo: string;
} {
  const statePath = repoPath(
    "automation/learning/state/huggingface_publish_state.json"
  );
  try {
    if (fs.existsSync(statePath)) {
      const j = JSON.parse(fs.readFileSync(statePath, "utf8")) as Record<
        string,
        unknown
      >;
      return {
        status: String(j.ok === true ? "OK" : j.skipped ? "SKIP" : "FAIL"),
        version: String(j.version || "—"),
        rows: String(
          (j.stats as { total_rows?: number } | undefined)?.total_rows ??
            j.rows ??
            "—"
        ),
        repo: String(j.repo_id || "ariew/ida-dataset"),
      };
    }
  } catch {
    /* ignore */
  }
  const ver = readTextIfExists("reports/huggingface/verification.md") || "";
  const status = /PASS/i.test(ver)
    ? "PASS"
    : /FAIL/i.test(ver)
      ? "FAIL"
      : "unknown";
  const kpis = getFactoryKpis();
  const totalRows =
    kpis.datasets?.reduce((s, d) => s + (d.current_rows || 0), 0) || 0;
  return {
    status,
    version: "—",
    rows: String(totalRows || "—"),
    repo: "ariew/ida-dataset",
  };
}

export default function ExportsPage() {
  const kpis = getFactoryKpis();
  for (const d of [
    "exports/jsonl",
    "exports/parquet",
    "exports/embeddings",
    "exports/openai",
    "exports/huggingface",
  ]) {
    const p = repoPath(d);
    if (!fs.existsSync(p)) {
      try {
        fs.mkdirSync(p, { recursive: true });
        fs.writeFileSync(path.join(p, ".gitkeep"), "");
      } catch {
        /* read-only ok */
      }
    }
  }

  const hf = hfPublishStatus();
  const totalRows =
    kpis.datasets?.reduce((s, d) => s + (d.current_rows || 0), 0) || 0;
  const version = (() => {
    try {
      return fs.readFileSync(repoPath("VERSION"), "utf8").trim();
    } catch {
      return "—";
    }
  })();

  return (
    <Shell title="Export">
      <div className="mx-auto max-w-6xl space-y-8">
        <header>
          <h1 className="text-page-title">Export</h1>
          <p className="mt-2 max-w-2xl text-body text-[var(--text-secondary)]">
            Real export monitor — GitHub · Hugging Face · JSONL · Parquet · CSV ·
            OpenAI.{" "}
            <span className="font-semibold text-[var(--text)]">
              {kpis.exports_generated}
            </span>{" "}
            artifacts · factory v{version} ·{" "}
            <span className="font-semibold text-[var(--text)]">
              {totalRows}
            </span>{" "}
            rows.
          </p>
        </header>

        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          <Card>
            <CardHeader title="GitHub" description="Dataset commit + push" />
            <CardBody className="space-y-1 text-small">
              <div className="font-semibold text-[var(--text)]">
                main · append-only
              </div>
              <div className="text-[var(--text-secondary)]">
                Publish via learn.yml certify + safe push
              </div>
            </CardBody>
          </Card>
          <Card>
            <CardHeader
              title="Hugging Face"
              description={hf.repo}
              action={
                <RoleBadge
                  role={
                    hf.status === "OK" || hf.status === "PASS"
                      ? "completed"
                      : hf.status === "FAIL"
                        ? "error"
                        : "idle"
                  }
                >
                  {hf.status}
                </RoleBadge>
              }
            />
            <CardBody className="space-y-1 text-small">
              <div className="text-[var(--text-secondary)]">
                Version {hf.version} · rows {hf.rows}
              </div>
              <a
                className="text-[var(--accent)] underline-offset-2 hover:underline"
                href={`https://huggingface.co/datasets/${hf.repo}`}
                target="_blank"
                rel="noreferrer"
              >
                Open dataset ↗
              </a>
            </CardBody>
          </Card>
          <Card>
            <CardHeader title="Latest version" description="Factory VERSION" />
            <CardBody className="text-page-title tabular-nums text-[var(--text)]">
              {version}
            </CardBody>
          </Card>
          <Card>
            <CardHeader title="Rows exported" description="Domain corpus total" />
            <CardBody className="text-page-title tabular-nums text-[var(--text)]">
              {totalRows}
            </CardBody>
          </Card>
        </div>

        <div className="grid gap-6 sm:grid-cols-2">
          {FORMATS.map((f) => {
            const files = listArtifacts(f.dir);
            const latest = files[0];
            return (
              <Card key={f.id}>
                <CardHeader
                  title={f.label}
                  description={f.dir}
                  action={
                    <RoleBadge role={files.length ? "completed" : "idle"}>
                      {files.length ? "Ready" : "Empty"}
                    </RoleBadge>
                  }
                />
                <CardBody className="space-y-4">
                  <div className="grid grid-cols-2 gap-3 text-small">
                    <div>
                      <div className="text-caption text-[var(--text-muted)]">
                        Format
                      </div>
                      <div className="font-semibold text-[var(--text)]">
                        {f.format}
                      </div>
                    </div>
                    <div>
                      <div className="text-caption text-[var(--text-muted)]">
                        Artifacts
                      </div>
                      <div className="font-semibold text-[var(--text)]">
                        {files.length}
                      </div>
                    </div>
                    <div>
                      <div className="text-caption text-[var(--text-muted)]">
                        Last export
                      </div>
                      <div className="font-semibold text-[var(--text)]">
                        {latest
                          ? new Date(latest.mtime).toISOString().slice(0, 16)
                          : "—"}
                      </div>
                    </div>
                    <div>
                      <div className="text-caption text-[var(--text-muted)]">
                        Size
                      </div>
                      <div className="font-semibold text-[var(--text)]">
                        {latest ? fmtBytes(latest.size) : "—"}
                      </div>
                    </div>
                  </div>

                  {files.length === 0 ? (
                    <p className="rounded-[var(--radius-lg)] bg-[var(--panel-2)] px-4 py-3 text-small text-[var(--text-secondary)]">
                      No artifacts yet. Exports appear after the export job runs
                      post-publish (GHA export workflow or packager CLI). Empty
                      because packaging has not been executed for this format.
                    </p>
                  ) : (
                    <ul className="max-h-40 space-y-2 overflow-y-auto font-mono text-caption text-[var(--text-secondary)] scrollbar-thin">
                      {files.map((file) => (
                        <li
                          key={file.name}
                          className="flex items-center justify-between gap-2 rounded-md border border-[var(--border)] px-3 py-2"
                        >
                          <span className="truncate">{file.name}</span>
                          <Badge>{fmtBytes(file.size)}</Badge>
                        </li>
                      ))}
                    </ul>
                  )}
                </CardBody>
              </Card>
            );
          })}
        </div>
      </div>
    </Shell>
  );
}
