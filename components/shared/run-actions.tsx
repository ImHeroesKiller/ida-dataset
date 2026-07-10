"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Play, ShieldCheck, ListChecks, Upload } from "lucide-react";

export function RunActions({ compact = false }: { compact?: boolean }) {
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);

  async function run(action: string) {
    setBusy(true);
    setMsg(`Queued ${action}…`);
    try {
      const res = await fetch("/api/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action, environment: "development" }),
      });
      const data = await res.json();
      if (!res.ok) {
        setMsg(data.error ?? "Failed");
      } else {
        setMsg(
          `${action} → ${data.progress?.status ?? "done"} (${data.progress?.message ?? ""})`
        );
      }
    } catch (e) {
      setMsg(e instanceof Error ? e.message : "Request failed");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className={compact ? "space-y-2" : "space-y-2"}>
      <div className="flex flex-wrap gap-2">
        <Button
          size="sm"
          variant="secondary"
          disabled={busy}
          onClick={() => run("planner_dry_run")}
        >
          <ListChecks className="h-3.5 w-3.5" />
          Planner dry-run
        </Button>
        <Button
          size="sm"
          variant="secondary"
          disabled={busy}
          onClick={() => run("validate")}
        >
          <ShieldCheck className="h-3.5 w-3.5" />
          Validate
        </Button>
        <Button
          size="sm"
          variant="secondary"
          disabled={busy}
          onClick={() => run("review_summary")}
        >
          Review summary
        </Button>
        <Button
          size="sm"
          variant="outline"
          disabled={busy}
          onClick={() => run("publish_dry_run")}
        >
          <Upload className="h-3.5 w-3.5" />
          Publish dry-run
        </Button>
        <Button
          size="sm"
          disabled={busy}
          onClick={() => run("full_dry_chain")}
        >
          <Play className="h-3.5 w-3.5" />
          Full dry chain
        </Button>
      </div>
      <p className="text-[10px] text-zinc-500">
        Always through Planner → Policy → Pipeline → Review → Publisher. No
        crawler. Publish is dry-run only from ECC.
      </p>
      {msg ? <p className="text-[11px] text-zinc-400">{msg}</p> : null}
    </div>
  );
}
