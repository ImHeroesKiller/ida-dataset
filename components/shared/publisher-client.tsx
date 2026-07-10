"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardBody, CardHeader } from "@/components/ui/card";

export function PublisherClient({
  approvedCount,
  publishingEnabled,
  reviewRequired,
}: {
  approvedCount: number;
  publishingEnabled: boolean;
  reviewRequired: boolean;
}) {
  const [msg, setMsg] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function dryRun() {
    setBusy(true);
    setMsg("Running publish dry-run via orchestration…");
    try {
      const res = await fetch("/api/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action: "publish_dry_run",
          environment: "development",
        }),
      });
      const data = await res.json();
      setMsg(
        `Result: ${data.progress?.status ?? "unknown"} — ${data.progress?.message ?? ""}`
      );
    } catch (e) {
      setMsg(e instanceof Error ? e.message : "Failed");
    } finally {
      setBusy(false);
    }
  }

  function blockedPublish() {
    setMsg(
      "Live publish is blocked in ECC UI. Use CI publish.yml / publish_ci after Review approvals and policy enablement. Never bypass Planner/Policy/Review."
    );
  }

  return (
    <Card>
      <CardHeader
        title="Publisher controls"
        description="Dry-run only from dashboard. Live publish remains gated."
      />
      <CardBody className="space-y-3">
        <div className="text-xs text-zinc-400">
          approved={approvedCount} · publishing_enabled=
          {String(publishingEnabled)} · review_required=
          {String(reviewRequired)}
        </div>
        <div className="flex flex-wrap gap-2">
          <Button size="sm" disabled={busy} onClick={dryRun}>
            Dry Run
          </Button>
          <Button size="sm" variant="secondary" onClick={blockedPublish}>
            Publish
          </Button>
          <Button size="sm" variant="ghost" disabled title="Placeholder">
            Rollback (disabled)
          </Button>
        </div>
        {msg ? <p className="text-[11px] text-zinc-400">{msg}</p> : null}
      </CardBody>
    </Card>
  );
}
