import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { getVersion } from "@/lib/repo-data";
import { getLearningMode } from "@/lib/learning-mode";
import { FACTORY_PIPELINE, PRODUCT } from "@/lib/nav";

export const dynamic = "force-dynamic";

function Row({ label, value }: { label: string; value: React.ReactNode }) {
  return (
    <div className="flex flex-col gap-1 border-b border-[var(--border)] py-3 last:border-0 sm:flex-row sm:items-center sm:justify-between">
      <dt className="text-small font-medium text-[var(--text-muted)]">{label}</dt>
      <dd className="text-small font-semibold text-[var(--text)]">{value}</dd>
    </div>
  );
}

export default function SettingsPage() {
  const version = getVersion();
  const mode = getLearningMode();

  return (
    <Shell title="Settings">
      <div className="mx-auto max-w-4xl space-y-8">
        <header>
          <h1 className="text-page-title">Settings</h1>
          <p className="mt-2 text-body text-[var(--text-secondary)]">
            Factory configuration (read-only where enforced by production freeze).
          </p>
        </header>

        <section className="space-y-6">
          <h2 className="text-section-title">Factory</h2>
          <Card>
            <CardHeader title="Product identity" />
            <CardBody>
              <dl>
                <Row label="Name" value={PRODUCT.name} />
                <Row label="Version" value={version || "2.0.0"} />
                <Row
                  label="Purpose"
                  value="Automatic dataset generation for LLM fine-tuning"
                />
              </dl>
            </CardBody>
          </Card>
        </section>

        <section className="space-y-6">
          <h2 className="text-section-title">Production</h2>
          <Card>
            <CardHeader title="Factory mode" />
            <CardBody>
              <dl>
                <Row label="Mode" value={<Badge>{mode.label}</Badge>} />
                <Row
                  label="Auto publish"
                  value={mode.auto_publish ? "Enabled" : "Disabled"}
                />
                <Row
                  label="Publish rate"
                  value={`${mode.publish_rate ?? "—"} ${mode.publish_rate_unit ?? ""}`}
                />
              </dl>
            </CardBody>
          </Card>
        </section>

        <section className="space-y-6">
          <h2 className="text-section-title">Scheduler</h2>
          <Card>
            <CardHeader
              title="Continuous production"
              description="GitHub Actions learn.yml · concurrency factory-production"
            />
            <CardBody>
              <dl>
                <Row label="Cadence" value="Every 15 minutes (UTC)" />
                <Row label="Overlap prevention" value="factory-production group" />
                <Row label="Daily deep pass" value="06:00 UTC" />
              </dl>
            </CardBody>
          </Card>
        </section>

        <section className="space-y-6">
          <h2 className="text-section-title">Discovery · Sources · Validation</h2>
          <div className="grid gap-6 sm:grid-cols-2">
            <Card>
              <CardHeader title="Discovery" description="Trusted domains only" />
              <CardBody className="text-small text-[var(--text-secondary)]">
                Search engines discover URLs. Knowledge is acquired only from
                registered trusted sources (Source Policy).
              </CardBody>
            </Card>
            <Card>
              <CardHeader title="Sources" description="Registry + health" />
              <CardBody className="text-small text-[var(--text-secondary)]">
                Runtime list in metadata/source_registry.csv. Trust score and
                allowlist enforced by SOURCE_POLICY.
              </CardBody>
            </Card>
            <Card>
              <CardHeader title="Validation" description="DPS + integrity guard" />
              <CardBody className="text-small text-[var(--text-secondary)]">
                Confidence floor, provenance, schema, and duplicate checks before
                append. Thresholds are frozen for production quality.
              </CardBody>
            </Card>
            <Card>
              <CardHeader title="Publishing" description="Append-only" />
              <CardBody className="text-small text-[var(--text-secondary)]">
                Domain CSVs are append-only. Corrections produce new versioned
                rows — never silent overwrite.
              </CardBody>
            </Card>
          </div>
        </section>

        <section className="space-y-6">
          <h2 className="text-section-title">LLM · Export · Diagnostics</h2>
          <div className="grid gap-6 sm:grid-cols-2">
            <Card>
              <CardHeader title="LLM extraction" />
              <CardBody className="text-small text-[var(--text-secondary)]">
                Factory core uses deterministic extraction first. LLM path is
                skipped when grounded text is sufficient (cost/latency).
              </CardBody>
            </Card>
            <Card>
              <CardHeader title="Export" />
              <CardBody className="text-small text-[var(--text-secondary)]">
                Formats: JSONL, OpenAI fine-tune, Hugging Face. Generated via
                export CI job after publish.
              </CardBody>
            </Card>
            <Card>
              <CardHeader title="Diagnostics" />
              <CardBody className="text-small text-[var(--text-secondary)]">
                reports/diagnostics — mission, candidate lifecycle, integrity
                traces. CLI: python -m automation.diagnostics
              </CardBody>
            </Card>
            <Card>
              <CardHeader title="Observability" />
              <CardBody className="text-small text-[var(--text-secondary)]">
                Scheduler heartbeat, production traces, source health, 30s
                dashboard auto-refresh (no WebSocket).
              </CardBody>
            </Card>
          </div>
        </section>

        <section className="space-y-6">
          <h2 className="text-section-title">Official pipeline</h2>
          <Card>
            <CardBody>
              <ol className="list-decimal space-y-2 pl-5 text-small text-[var(--text-secondary)]">
                {FACTORY_PIPELINE.map((s) => (
                  <li key={s} className="font-medium text-[var(--text)]">
                    {s}
                  </li>
                ))}
              </ol>
            </CardBody>
          </Card>
        </section>
      </div>
    </Shell>
  );
}
