import { Shell } from "@/components/layout/shell";
import { Card, CardBody } from "@/components/ui/card";
import { getVersion } from "@/lib/repo-data";
import { getLearningMode } from "@/lib/learning-mode";

export const dynamic = "force-dynamic";

export default function SettingsPage() {
  const mode = getLearningMode();
  return (
    <Shell title="Settings">
      <div className="mx-auto max-w-3xl space-y-8">
        <header>
          <h1 className="text-3xl font-semibold tracking-tight text-[var(--text)]">
            Settings
          </h1>
          <p className="mt-2 text-base text-[var(--text-muted)]">
            Learning mode and environment — architecture unchanged.
          </p>
        </header>

        <div className="grid gap-4">
          <Card>
            <CardBody className="space-y-3 p-6">
              <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                Learning mode
              </p>
              <p className="text-2xl font-semibold text-[var(--text)]">
                {mode.label}
              </p>
              <ul className="space-y-1 text-sm text-[var(--text-muted)]">
                <li>
                  Auto publish:{" "}
                  <strong className="text-[var(--text)]">
                    {mode.auto_publish ? "Enabled" : "Disabled"}
                  </strong>
                </li>
                <li>
                  Progressive queue:{" "}
                  <strong className="text-[var(--text)]">
                    {mode.progressive_publish ? "Enabled" : "Disabled"}
                  </strong>
                </li>
                <li>
                  Review:{" "}
                  <strong className="text-[var(--text)]">
                    {mode.review_bypassed ? "Bypassed (dev)" : "Required"}
                  </strong>
                </li>
                <li>
                  Publish rate:{" "}
                  <strong className="text-[var(--text)]">
                    {mode.publish_rate <= 0
                      ? "Unlimited"
                      : `${mode.publish_rate} row/sec`}
                  </strong>
                </li>
              </ul>
              <p className="text-xs text-[var(--text-faint)]">
                Configure in{" "}
                <code className="text-[var(--text)]">
                  automation/config/learning.yaml
                </code>{" "}
                → <code className="text-[var(--text)]">learning_mode</code>.
                Override with env{" "}
                <code className="text-[var(--text)]">IDA_LEARNING_MODE</code>.
              </p>
            </CardBody>
          </Card>

          <Card>
            <CardBody className="space-y-3 p-6">
              <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                Platform
              </p>
              <p className="text-lg font-medium text-[var(--text)]">
                IDA Knowledge · v{getVersion()}
              </p>
              <p className="text-sm leading-relaxed text-[var(--text-muted)]">
                Development auto-publishes validated knowledge progressively.
                Production requires human review before publish. The pipeline
                architecture is identical.
              </p>
            </CardBody>
          </Card>

          <Card>
            <CardBody className="space-y-3 p-6">
              <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                How to learn
              </p>
              <ol className="list-decimal space-y-2 pl-5 text-sm text-[var(--text-muted)]">
                <li>Start learning from the Dashboard.</li>
                <li>
                  {mode.auto_publish
                    ? "Watch progressive publish (1 row/sec by default)."
                    : "Review waiting candidates and approve to publish."}
                </li>
                <li>Browse Knowledge to see what IDA has learned.</li>
                <li>Check Reports for growth over time.</li>
              </ol>
            </CardBody>
          </Card>
        </div>
      </div>
    </Shell>
  );
}
