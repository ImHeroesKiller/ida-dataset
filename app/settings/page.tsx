import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { getVersion } from "@/lib/repo-data";
import { getLearningMode } from "@/lib/learning-mode";
import { FACTORY_PIPELINE, PRODUCT } from "@/lib/nav";

export const dynamic = "force-dynamic";

export default function SettingsPage() {
  const version = getVersion();
  const mode = getLearningMode();

  return (
    <Shell title="Settings">
      <div className="mx-auto max-w-3xl space-y-6">
        <header>
          <h1 className="text-2xl font-semibold text-[var(--text)]">Settings</h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            {PRODUCT.name} configuration
          </p>
        </header>

        <Card>
          <CardHeader title="Product" />
          <CardBody className="space-y-2 text-sm text-[var(--text-muted)]">
            <p>
              <span className="text-[var(--text-faint)]">Name · </span>
              {PRODUCT.name}
            </p>
            <p>
              <span className="text-[var(--text-faint)]">Version · </span>
              {version || "0.2.0"}
            </p>
            <p>
              <span className="text-[var(--text-faint)]">Purpose · </span>
              Automatic dataset generation for LLM fine-tuning
            </p>
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Factory mode" />
          <CardBody className="space-y-2 text-sm text-[var(--text-muted)]">
            <p>
              <span className="text-[var(--text-faint)]">Mode · </span>
              {mode.label}
            </p>
            <p>
              <span className="text-[var(--text-faint)]">Auto publish · </span>
              {mode.auto_publish ? "enabled" : "disabled"}
            </p>
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Official pipeline" />
          <CardBody>
            <ol className="list-decimal space-y-1 pl-5 text-sm text-[var(--text-muted)]">
              {FACTORY_PIPELINE.map((s) => (
                <li key={s}>{s}</li>
              ))}
            </ol>
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}
