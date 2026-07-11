"use client";

import { useInspector } from "@/components/layout/inspector-context";
import { Badge } from "@/components/ui/badge";

export function InspectorPanel() {
  const { selection, clear } = useInspector();

  return (
    <aside className="hidden h-full w-[var(--inspector-w)] shrink-0 flex-col border-l border-[var(--border)] bg-[var(--panel)] xl:flex">
      <div className="flex h-[var(--topbar-h)] items-center justify-between border-b border-[var(--border)] px-3">
        <div className="text-small font-medium text-[var(--text)]">Inspector</div>
        {selection ? (
          <button
            onClick={clear}
            className="text-caption text-[var(--text-muted)] transition-colors hover:text-[var(--text)]"
          >
            Clear
          </button>
        ) : null}
      </div>
      <div className="flex-1 overflow-y-auto p-3 scrollbar-thin">
        {!selection ? (
          <div className="rounded-[var(--radius-lg)] border border-dashed border-[var(--border)] bg-[var(--panel-2)] p-3 text-small text-[var(--text-muted)]">
            Select a dataset, entity, plan, report, or review candidate to
            inspect details here.
          </div>
        ) : (
          <div className="space-y-3">
            <div>
              <div className="mb-1 flex items-center gap-2">
                <Badge>{selection.kind}</Badge>
              </div>
              <h3 className="text-card-title text-[var(--text)]">
                {selection.title}
              </h3>
              {selection.subtitle ? (
                <p className="mt-1 text-caption text-[var(--text-muted)]">
                  {selection.subtitle}
                </p>
              ) : null}
            </div>
            {selection.meta ? (
              <dl className="space-y-1.5 rounded-[var(--radius-lg)] border border-[var(--border)] bg-[var(--panel-2)] p-2.5">
                {Object.entries(selection.meta).map(([k, v]) => (
                  <div key={k} className="grid grid-cols-3 gap-2 text-caption">
                    <dt className="text-[var(--text-muted)]">{k}</dt>
                    <dd className="col-span-2 break-all text-[var(--text-secondary)]">
                      {v}
                    </dd>
                  </div>
                ))}
              </dl>
            ) : null}
            {selection.body ? (
              <pre className="overflow-x-auto rounded-[var(--radius-lg)] border border-[var(--border)] bg-[var(--panel-2)] p-2.5 text-caption leading-relaxed whitespace-pre-wrap text-[var(--text-secondary)]">
                {selection.body}
              </pre>
            ) : null}
          </div>
        )}
      </div>
    </aside>
  );
}
