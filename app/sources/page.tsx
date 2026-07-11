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

function SourceTable({
  sources,
  empty,
}: {
  sources: ReturnType<typeof getSourceHealthDashboard>["sources"];
  empty: string;
}) {
  if (!sources.length) {
    return (
      <p className="rounded-[var(--radius-lg)] bg-[var(--panel-2)] px-4 py-3 text-small text-[var(--text-secondary)]">
        {empty}
      </p>
    );
  }
  return (
    <div className="overflow-x-auto">
      <table className="ds-table min-w-[1100px]">
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
            <th>Status</th>
            <th>Priority</th>
          </tr>
        </thead>
        <tbody>
          {sources.map((s) => (
            <tr key={s.source_id}>
              <td>
                <div className="font-semibold text-[var(--text)]">{s.name}</div>
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
              <td className="text-small capitalize">
                {s.status}
                {!s.allowed ? " / blocked" : ""}
              </td>
              <td className="tabular-nums text-small">
                {s.mission_usage > 0 ? "preferred" : s.allowed ? "trusted" : "—"}
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
  // Preferred: high mission usage or high yield
  const preferred = all
    .filter((s) => s.allowed && (s.mission_usage > 0 || s.rows_produced > 0))
    .sort(
      (a, b) =>
        b.mission_usage - a.mission_usage ||
        b.rows_produced - a.rows_produced ||
        b.trust_score - a.trust_score
    );
  // Trusted: registered + allowed
  const trusted = all
    .filter((s) => s.allowed)
    .sort((a, b) => b.trust_score - a.trust_score || a.name.localeCompare(b.name));
  // Random discovery pool: healthy trusted sources eligible for random selection
  const randomPool = trusted
    .filter((s) => s.health_status === "healthy" || s.health_status === "unknown")
    .slice()
    .sort((a, b) => a.source_id.localeCompare(b.source_id));

  return (
    <Shell title="Sources">
      <div className="mx-auto max-w-7xl space-y-8">
        <header>
          <h1 className="text-page-title">Sources</h1>
          <p className="mt-2 max-w-3xl text-body text-[var(--text-secondary)]">
            Preferred · Trusted · Random discovery.{" "}
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
          <p className="mt-1 text-small text-[var(--text-muted)]">
            Selection prefers mission relevance · coverage · freshness · confidence.
            Discovery uses Tavily-first (max 10 searches/session); knowledge only from
            trusted registry domains.
          </p>
        </header>

        <div className="grid gap-4 sm:grid-cols-3">
          <Card>
            <CardHeader title="Preferred Sources" description="High mission / yield" />
            <CardBody className="text-page-title tabular-nums text-[var(--text)]">
              {preferred.length}
            </CardBody>
          </Card>
          <Card>
            <CardHeader title="Trusted Sources" description="Registry allowlist" />
            <CardBody className="text-page-title tabular-nums text-[var(--text)]">
              {trusted.length}
            </CardBody>
          </Card>
          <Card>
            <CardHeader title="Random Discovery" description="Healthy pool" />
            <CardBody className="text-page-title tabular-nums text-[var(--text)]">
              {randomPool.length}
            </CardBody>
          </Card>
        </div>

        <Card>
          <CardHeader
            title="Preferred Sources"
            description="Operator / mission-weighted sources with production yield"
          />
          <CardBody>
            <SourceTable
              sources={preferred.slice(0, 40)}
              empty="No preferred sources yet — mission usage and row yield will populate this list."
            />
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Trusted Sources"
            description="Full allowlisted registry — enable/disable via source registry config"
          />
          <CardBody>
            <SourceTable
              sources={trusted.slice(0, 80)}
              empty="No trusted sources in registry."
            />
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Random Discovery pool"
            description="Healthy trusted sources eligible for random / gap-driven discovery"
          />
          <CardBody>
            <SourceTable
              sources={randomPool.slice(0, 40)}
              empty="No healthy sources available for random discovery."
            />
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}
