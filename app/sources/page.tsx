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

function healthRole(status: string): BadgeRole {
  if (status === "healthy") return "healthy";
  if (status === "degraded") return "warning";
  if (status === "down") return "error";
  return "idle";
}

function SourceTable({
  sources,
  empty,
}: {
  sources: ReturnType<typeof getSourceHealthDashboard>["sources"];
  empty: string;
}) {
  if (!sources.length) {
    return (
      <p className="rounded-[var(--radius-md)] bg-[var(--panel-2)] px-3 py-2 text-xs text-[var(--text-secondary)]">
        {empty}
      </p>
    );
  }
  return (
    <div className="overflow-x-auto">
      <table className="ds-table min-w-[720px]">
        <thead>
          <tr>
            <th>Name</th>
            <th>Health</th>
            <th>Trust</th>
            <th>Rows</th>
            <th>Last sync</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {sources.map((s) => (
            <tr key={s.source_id}>
              <td>
                <div className="font-semibold text-[var(--text)]">{s.name}</div>
                <div className="font-mono text-[10px] text-[var(--text-muted)]">
                  {s.source_id}
                </div>
              </td>
              <td>
                <RoleBadge role={healthRole(s.health_status)}>
                  {s.health_status === "healthy"
                    ? "Healthy"
                    : s.health_status === "degraded"
                      ? "Warning"
                      : s.health_status === "down"
                        ? "Error"
                        : "Idle"}
                </RoleBadge>
              </td>
              <td className="tabular-nums">{s.trust_score.toFixed(2)}</td>
              <td className="font-semibold tabular-nums text-[var(--text)]">
                {s.rows_produced}
              </td>
              <td className="whitespace-nowrap text-[var(--text-muted)]">
                {fmtTs(s.last_successful_sync)}
              </td>
              <td className="capitalize text-[var(--text-muted)]">
                {s.status}
                {!s.allowed ? " / blocked" : ""}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default function SourcesPage() {
  const dash = getSourceHealthDashboard();
  const all = dash.sources.filter(
    (s) => s.allowed || s.status === "active" || s.rows_produced > 0
  );
  const preferred = all
    .filter((s) => s.allowed && (s.mission_usage > 0 || s.rows_produced > 0))
    .sort(
      (a, b) =>
        b.mission_usage - a.mission_usage ||
        b.rows_produced - a.rows_produced ||
        b.trust_score - a.trust_score
    );
  const trusted = all
    .filter((s) => s.allowed)
    .sort((a, b) => b.trust_score - a.trust_score || a.name.localeCompare(b.name));
  const randomPool = trusted
    .filter((s) => s.health_status === "healthy" || s.health_status === "unknown")
    .slice()
    .sort((a, b) => a.source_id.localeCompare(b.source_id));

  return (
    <Shell title="Sources">
      <div className="op-page max-w-6xl">
        <header className="op-page-header">
          <div>
            <h1 className="text-page-title">Sources</h1>
            <p>
              Preferred · Trusted · Random discovery · {dash.totals.active} active ·{" "}
              {dash.totals.healthy} healthy
            </p>
          </div>
        </header>

        <div className="grid gap-2 sm:grid-cols-3">
          <Card>
            <CardBody className="text-center">
              <p className="text-[10px] font-semibold uppercase tracking-wide text-[var(--text-muted)]">
                Preferred
              </p>
              <p className="text-kpi tabular-nums">{preferred.length}</p>
            </CardBody>
          </Card>
          <Card>
            <CardBody className="text-center">
              <p className="text-[10px] font-semibold uppercase tracking-wide text-[var(--text-muted)]">
                Trusted
              </p>
              <p className="text-kpi tabular-nums">{trusted.length}</p>
            </CardBody>
          </Card>
          <Card>
            <CardBody className="text-center">
              <p className="text-[10px] font-semibold uppercase tracking-wide text-[var(--text-muted)]">
                Random pool
              </p>
              <p className="text-kpi tabular-nums">{randomPool.length}</p>
            </CardBody>
          </Card>
        </div>

        <Card>
          <CardHeader title="Preferred Sources" description="Mission / yield weighted" />
          <CardBody>
            <SourceTable
              sources={preferred.slice(0, 40)}
              empty="No preferred sources yet."
            />
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Trusted Sources" description="Registry allowlist" />
          <CardBody>
            <SourceTable
              sources={trusted.slice(0, 80)}
              empty="No trusted sources."
            />
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Random Discovery"
            description="Healthy pool for gap-driven selection"
          />
          <CardBody>
            <SourceTable
              sources={randomPool.slice(0, 40)}
              empty="No healthy sources for random discovery."
            />
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}
