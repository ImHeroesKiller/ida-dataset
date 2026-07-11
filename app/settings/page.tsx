import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { getVersion } from "@/lib/repo-data";
import { getLearningMode } from "@/lib/learning-mode";
import { PRODUCT } from "@/lib/nav";
import fs from "fs";
import { repoPath } from "@/lib/paths";
import { loadSimpleYaml } from "@/lib/simple-yaml";

export const dynamic = "force-dynamic";

function Row({ label, value }: { label: string; value: React.ReactNode }) {
  return (
    <div className="flex flex-col gap-0.5 border-b border-[var(--border)] py-2 last:border-0 sm:flex-row sm:items-center sm:justify-between sm:gap-4">
      <dt className="text-[11px] font-medium text-[var(--text-muted)]">{label}</dt>
      <dd className="text-xs font-semibold text-[var(--text)] sm:text-right">
        {value}
      </dd>
    </div>
  );
}

function Section({
  title,
  description,
  children,
}: {
  title: string;
  description?: string;
  children: React.ReactNode;
}) {
  return (
    <Card>
      <CardHeader title={title} description={description} />
      <CardBody>
        <dl>{children}</dl>
      </CardBody>
    </Card>
  );
}

function readPolicies(): Record<string, unknown> {
  try {
    const p = repoPath("automation/config/policies.yaml");
    if (!fs.existsSync(p)) return {};
    return (loadSimpleYaml(fs.readFileSync(p, "utf8")) || {}) as Record<
      string,
      unknown
    >;
  } catch {
    return {};
  }
}

export default function SettingsPage() {
  const version = getVersion();
  const mode = getLearningMode();
  const policies = readPolicies();
  const discovery = (policies.discovery || {}) as Record<string, unknown>;
  const validation = (policies.validation || {}) as Record<string, unknown>;
  const confidence = policies.confidence_threshold ?? 0.8;

  return (
    <Shell title="Settings">
      <div className="op-page max-w-3xl">
        <header className="op-page-header">
          <div>
            <h1 className="text-page-title">Settings</h1>
            <p>
              Operator configuration (read-only where production freeze applies).
            </p>
          </div>
        </header>

        <Section title="Dashboard" description="Operator display">
          <Row label="Refresh interval" value="30 seconds" />
          <Row label="Console rows" value="200" />
          <Row label="Graph duration" value="14 sessions" />
          <Row label="Default page" value="Dashboard" />
          <Row label="Compact mode" value="On (UI v1.0)" />
          <Row label="Dark mode" value="System / toggle in sidebar" />
        </Section>

        <Section title="Scheduler" description="Learning cadence">
          <Row label="Learning interval" value="1 hour" />
          <Row label="Hourly schedule" value="UTC :00" />
          <Row label="Daily deep learning" value="06:00 UTC" />
          <Row label="Concurrent sessions" value="1 (no overlap)" />
          <Row label="Retry count" value="3" />
          <Row label="Timeout" value="Session concurrency queue" />
        </Section>

        <Section title="Discovery" description="Source finding">
          <Row
            label="Preferred source"
            value={
              Array.isArray(discovery.source_strategy)
                ? String((discovery.source_strategy as string[])[0] || "operator")
                : "operator_selected"
            }
          />
          <Row label="Random discovery" value="Enabled (trusted pool)" />
          <Row
            label="Maximum Tavily searches"
            value={String(discovery.max_tavily_searches_per_session ?? 10)}
          />
          <Row label="Discovery timeout" value="Runtime budget per session" />
          <Row label="Crawler workers" value="Adaptive download pool" />
        </Section>

        <Section title="Export" description="Publish channels">
          <Row label="GitHub" value="Enabled · append-only main" />
          <Row label="Hugging Face" value="Enabled · continuous sync" />
          <Row
            label="Auto export"
            value={mode.auto_publish ? "Enabled" : "Manual / gated"}
          />
          <Row label="Retry" value="Workflow retries" />
          <Row label="Versioning" value={`Factory ${version || "2.0"}`} />
        </Section>

        <Section title="Knowledge" description="Quality gates">
          <Row label="Minimum confidence" value={String(confidence)} />
          <Row
            label="Duplicate threshold"
            value={
              validation.reject_duplicates === false ? "Off" : "Reject duplicates"
            }
          />
          <Row
            label="Auto publish"
            value={mode.auto_publish ? "Enabled" : "Disabled"}
          />
          <Row label="Quality threshold" value="DPS + integrity guard" />
        </Section>

        <Section title="Advanced" description="Environment">
          <Row label="Product" value={PRODUCT.name} />
          <Row label="Factory version" value={version || "2.0.0"} />
          <Row label="Mode" value={<Badge>{mode.label}</Badge>} />
          <Row label="Environment diagnostics" value="reports/ · bottom console" />
          <Row label="Build info" value="Next.js App Router · Operator UI v1.0" />
          <Row label="UI freeze" value="Active — Dataset Engine only after this" />
        </Section>
      </div>
    </Shell>
  );
}
