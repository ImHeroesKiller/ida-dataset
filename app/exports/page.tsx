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

  return (
    <Shell title="Exports">
      <div className="mx-auto max-w-6xl space-y-8">
        <header>
          <h1 className="text-page-title">Exports</h1>
          <p className="mt-2 max-w-2xl text-body text-[var(--text-secondary)]">
            Factory packaging for LLM fine-tuning and corpus delivery.{" "}
            <span className="font-semibold text-[var(--text)]">
              {kpis.exports_generated}
            </span>{" "}
            export artifacts tracked.
          </p>
        </header>

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
