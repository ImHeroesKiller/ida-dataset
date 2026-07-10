import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import fs from "fs";
import { repoPath } from "@/lib/paths";
import { parseCsv } from "@/lib/csv";

export const dynamic = "force-dynamic";

export default function SourcesPage() {
  let rows: Record<string, string>[] = [];
  try {
    const p = repoPath("metadata/source_registry.csv");
    if (fs.existsSync(p)) {
      rows = parseCsv(fs.readFileSync(p, "utf8")).rows;
    }
  } catch {
    rows = [];
  }

  const active = rows.filter(
    (r) =>
      String(r.Status || "").toLowerCase() === "active" &&
      String(r.Allowed || "").toLowerCase() === "true"
  );

  return (
    <Shell title="Sources">
      <div className="mx-auto max-w-5xl space-y-6">
        <header>
          <h1 className="text-2xl font-semibold text-[var(--text)]">
            Trusted Sources
          </h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            Phase-1 allow list for automatic collection. {active.length} active
            of {rows.length} registered.
          </p>
        </header>

        <Card>
          <CardHeader title="Source registry" description="metadata/source_registry.csv" />
          <CardBody className="overflow-x-auto">
            <table className="w-full min-w-[640px] text-left text-sm">
              <thead className="text-xs uppercase text-[var(--text-faint)]">
                <tr>
                  <th className="pb-2 pr-3">ID</th>
                  <th className="pb-2 pr-3">Name</th>
                  <th className="pb-2 pr-3">Category</th>
                  <th className="pb-2 pr-3">Trust</th>
                  <th className="pb-2">Status</th>
                </tr>
              </thead>
              <tbody>
                {rows.map((r) => (
                  <tr
                    key={r["Source ID"]}
                    className="border-t border-[var(--border)] text-[var(--text-muted)]"
                  >
                    <td className="py-2 pr-3 font-mono text-xs">
                      {r["Source ID"]}
                    </td>
                    <td className="py-2 pr-3 text-[var(--text)]">
                      {r["Source Name"]}
                    </td>
                    <td className="py-2 pr-3">{r.Category}</td>
                    <td className="py-2 pr-3">{r["Trust Score"]}</td>
                    <td className="py-2">
                      {r.Status}/{r.Allowed}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}
