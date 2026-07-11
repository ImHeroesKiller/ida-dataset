import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { RoleBadge } from "@/components/ui/badge";
import { getSourceHealthDashboard } from "@/lib/source-health";
import { formatWib } from "@/lib/time-wib";
import type { BadgeRole } from "@/lib/design-tokens";

export const dynamic = "force-dynamic";

function fmtTs(v: string | null): string {
  return formatWib(v);
}

function pct(n: number): string {
  return `${Math.round(n * 1000) / 10}%`;
}

function healthRole(status: string): BadgeRole {
  if (status === "healthy") return "healthy";
  if (status === "degraded") return "warning";
  if (status === "down") return "error";
  return "idle";
}

export default function SourcesPage() {
  const dash = getSourceHealthDashboard();
  const sources = dash.sources.filter(
    (s) => s.allowed || s.status === "active" || s.rows_produced > 0
  );

  return (
    <Shell title="Sources">
      <div className="mx-auto max-w-7xl space-y-8">
        <header>
          <h1 className="text-page-title">Trusted sources</h1>
          <p className="mt-2 max-w-3xl text-body text-[var(--text-secondary)]">
            Operational monitor for factory production sources.{" "}
            <span className="font-semibold text-[var(--text)]">
              {dash.totals.active}
            </span>{" "}
            active ·{" "}
            <span className="font-semibold text-[var(--text)]">
              {dash.totals.healthy}
            </span>{" "}
            healthy ·{" "}
            <span className="font-semibold text-[var(--text)]">
              {dash.totals.rows_produced}
            </span>{" "}
            rows attributed
            {dash.updated_at ? ` · metrics ${fmtTs(dash.updated_at)}` : ""}
          </p>
        </header>

        <Card>
          <CardHeader
            title="Source production monitor"
            description="Health · coverage · yield · latency · success rate · last sync · mission usage"
          />
          <CardBody className="overflow-x-auto">
            <table className="ds-table min-w-[1200px]">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Category</th>
                  <th>Trust</th>
                  <th>Coverage</th>
                  <th>Health</th>
                  <th>Last sync</th>
                  <th>Rows</th>
                  <th>Docs</th>
                  <th>Success</th>
                  <th>Latency</th>
                  <th>Status</th>
                  <th>Missions</th>
                </tr>
              </thead>
              <tbody>
                {sources.map((s) => (
                  <tr key={s.source_id}>
                    <td>
                      <div className="font-semibold text-[var(--text)]">
                        {s.name}
                      </div>
                      <div className="font-mono text-caption text-[var(--text-muted)]">
                        {s.source_id}
                      </div>
                    </td>
                    <td className="text-small">{s.category}</td>
                    <td className="tabular-nums">{s.trust_score.toFixed(2)}</td>
                    <td className="tabular-nums">{pct(s.coverage)}</td>
                    <td>
                      <RoleBadge role={healthRole(s.health_status)}>
                        {s.health_status || "unknown"}
                      </RoleBadge>
                    </td>
                    <td className="whitespace-nowrap text-small">
                      {fmtTs(s.last_successful_sync)}
                    </td>
                    <td className="font-semibold tabular-nums text-[var(--text)]">
                      {s.rows_produced}
                    </td>
                    <td className="tabular-nums">{s.documents_processed}</td>
                    <td className="tabular-nums">{pct(s.success_rate)}</td>
                    <td className="tabular-nums">
                      {s.average_processing_time_ms
                        ? `${Math.round(s.average_processing_time_ms)} ms`
                        : "—"}
                    </td>
                    <td className="text-small capitalize">
                      {s.status}
                      {!s.allowed ? " / blocked" : ""}
                    </td>
                    <td className="tabular-nums">{s.mission_usage}</td>
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
