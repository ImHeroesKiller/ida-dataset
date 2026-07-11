"use client";

import { useMemo, useState } from "react";
import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { ChevronDown, ChevronRight } from "lucide-react";
import { useLearning } from "@/hooks/learning-provider";
import { formatWib } from "@/lib/time-wib";
import { cn } from "@/lib/utils";

const GROUPS = [
  { id: "mission", label: "Mission", re: /mission|session|scheduler|planner/i },
  { id: "discovery", label: "Discovery", re: /search|discover|connector|gap|source/i },
  { id: "download", label: "Download", re: /download|document|reading|queue/i },
  { id: "extraction", label: "Extraction", re: /extract|pipeline|entity|understand/i },
  { id: "validation", label: "Validation", re: /validat|review|policy|confidence|integrity/i },
  { id: "publish", label: "Publish", re: /publish|append|knowledge/i },
  { id: "git", label: "Git", re: /git|commit|push|rebase/i },
  { id: "reports", label: "Reports", re: /report|diagnostic|performance|trace/i },
] as const;

export default function LogsPage() {
  const { events: liveEvents, dashboard } = useLearning();
  const [open, setOpen] = useState<Record<string, boolean>>({
    mission: true,
    discovery: true,
    download: false,
    extraction: false,
    validation: false,
    publish: true,
    git: false,
    reports: false,
  });

  const events = useMemo(() => {
    // Prefer live session events; fall back to empty
    return (liveEvents || []).map((ev) => ({
      ts: ev.ts || "",
      verb: ev.verb || "",
      detail: ev.detail || "",
      stage: ev.stage || "",
    }));
  }, [liveEvents]);

  const grouped = useMemo(() => {
    const map: Record<string, typeof events> = Object.fromEntries(
      GROUPS.map((g) => [g.id, []])
    );
    const other: typeof events = [];
    for (const ev of events) {
      const blob = `${ev.verb} ${ev.stage} ${ev.detail}`;
      const hit = GROUPS.find((g) => g.re.test(blob));
      if (hit) map[hit.id].push(ev);
      else other.push(ev);
    }
    return { map, other };
  }, [events]);

  return (
    <Shell title="Logs">
      <div className="mx-auto max-w-5xl space-y-8">
        <header>
          <h1 className="text-page-title">Factory logs</h1>
          <p className="mt-2 text-body text-[var(--text-secondary)]">
            Production console grouped by pipeline stage. Expand groups to
            inspect Mission → Discovery → Download → Extraction → Validation →
            Publish → Git → Reports.
            {dashboard.current_session?.session_id
              ? ` Active session ${dashboard.current_session.session_id}.`
              : " Showing live journal events when a session is active."}
          </p>
        </header>

        <Card>
          <CardHeader
            title="Production console"
            description={`${events.length} events in current stream`}
          />
          <CardBody className="space-y-3">
            {GROUPS.map((g) => {
              const items = grouped.map[g.id] || [];
              const isOpen = open[g.id];
              return (
                <div
                  key={g.id}
                  className="overflow-hidden rounded-[var(--radius-lg)] border border-[var(--border)]"
                >
                  <button
                    type="button"
                    className="flex w-full items-center justify-between gap-3 bg-[var(--panel-2)] px-4 py-3 text-left hover:bg-[var(--panel-2)]/80"
                    onClick={() =>
                      setOpen((s) => ({ ...s, [g.id]: !s[g.id] }))
                    }
                    aria-expanded={isOpen}
                  >
                    <span className="flex items-center gap-2 text-small font-semibold text-[var(--text)]">
                      {isOpen ? (
                        <ChevronDown className="h-4 w-4" aria-hidden />
                      ) : (
                        <ChevronRight className="h-4 w-4" aria-hidden />
                      )}
                      {g.label}
                    </span>
                    <span className="rounded-full bg-[var(--panel)] px-2.5 py-0.5 text-caption font-semibold text-[var(--text-secondary)]">
                      {items.length}
                    </span>
                  </button>
                  {isOpen ? (
                    <div className="max-h-64 space-y-0 overflow-y-auto border-t border-[var(--border)] scrollbar-thin">
                      {!items.length ? (
                        <p className="px-4 py-3 text-small text-[var(--text-muted)]">
                          No events in this group.
                        </p>
                      ) : (
                        items.map((ev, i) => (
                          <div
                            key={`${g.id}-${i}`}
                            className={cn(
                              "flex flex-col gap-1 border-b border-[var(--border)] px-4 py-3 last:border-0 sm:flex-row sm:gap-4"
                            )}
                          >
                            <span className="w-44 shrink-0 text-caption text-[var(--text-muted)]">
                              {formatWib(ev.ts)}
                            </span>
                            <span className="w-36 shrink-0 text-small font-semibold text-[var(--green)]">
                              {ev.verb || "Event"}
                            </span>
                            <span className="min-w-0 break-words text-small text-[var(--text-secondary)]">
                              {ev.detail}
                            </span>
                          </div>
                        ))
                      )}
                    </div>
                  ) : null}
                </div>
              );
            })}

            {grouped.other.length ? (
              <div className="rounded-[var(--radius-lg)] border border-[var(--border)] px-4 py-3">
                <p className="text-caption font-semibold text-[var(--text-muted)]">
                  Other · {grouped.other.length}
                </p>
              </div>
            ) : null}
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}
