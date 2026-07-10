import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { getFactoryKpis } from "@/lib/factory-kpis";
import fs from "fs";
import path from "path";
import { repoPath } from "@/lib/paths";

export const dynamic = "force-dynamic";

const FORMATS = [
  { id: "csv", label: "CSV", dir: "domains" },
  { id: "jsonl", label: "JSONL", dir: "exports/jsonl" },
  { id: "parquet", label: "Parquet", dir: "exports/parquet" },
  { id: "embeddings", label: "Embeddings / HF prep", dir: "exports/embeddings" },
  { id: "openai", label: "OpenAI fine-tuning", dir: "exports/openai" },
  { id: "huggingface", label: "Hugging Face", dir: "exports/huggingface" },
];

function listDir(rel: string): string[] {
  const p = repoPath(rel);
  if (!fs.existsSync(p)) return [];
  try {
    return fs
      .readdirSync(p)
      .filter((n) => !n.startsWith(".") && n !== ".gitkeep")
      .slice(0, 40);
  } catch {
    return [];
  }
}

export default function ExportsPage() {
  const kpis = getFactoryKpis();
  // Ensure export dirs exist for factory
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
      <div className="mx-auto max-w-5xl space-y-6">
        <header>
          <h1 className="text-2xl font-semibold text-[var(--text)]">Exports</h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            Factory outputs for LLM fine-tuning and corpus packaging. Exports
            generated: {kpis.exports_generated}
          </p>
        </header>

        <div className="grid gap-4 sm:grid-cols-2">
          {FORMATS.map((f) => {
            const files = listDir(f.dir);
            return (
              <Card key={f.id}>
                <CardHeader title={f.label} description={f.dir} />
                <CardBody className="text-sm text-[var(--text-muted)]">
                  {files.length === 0 ? (
                    <p className="text-[var(--text-faint)]">
                      No artifacts yet. Run the export job after publish.
                    </p>
                  ) : (
                    <ul className="max-h-40 space-y-1 overflow-y-auto font-mono text-xs">
                      {files.map((name) => (
                        <li key={name}>{name}</li>
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
