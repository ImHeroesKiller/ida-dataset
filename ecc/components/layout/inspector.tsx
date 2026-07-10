"use client";

import { useInspector } from "@/components/layout/inspector-context";
import { Badge } from "@/components/ui/badge";

export function InspectorPanel() {
  const { selection, clear } = useInspector();

  return (
    <aside className="hidden h-full w-[var(--inspector-w)] shrink-0 flex-col border-l border-zinc-800/90 bg-[#0b0b0d] xl:flex">
      <div className="flex h-[var(--topbar-h)] items-center justify-between border-b border-zinc-800/90 px-3">
        <div className="text-xs font-medium text-zinc-200">Inspector</div>
        {selection ? (
          <button
            onClick={clear}
            className="text-[11px] text-zinc-500 hover:text-zinc-300"
          >
            Clear
          </button>
        ) : null}
      </div>
      <div className="flex-1 overflow-y-auto p-3 scrollbar-thin">
        {!selection ? (
          <div className="rounded-md border border-dashed border-zinc-800 p-3 text-xs text-zinc-500">
            Select a dataset, entity, plan, report, or review candidate to
            inspect details here.
          </div>
        ) : (
          <div className="space-y-3">
            <div>
              <div className="mb-1 flex items-center gap-2">
                <Badge>{selection.kind}</Badge>
              </div>
              <h3 className="text-sm font-medium text-zinc-100">
                {selection.title}
              </h3>
              {selection.subtitle ? (
                <p className="mt-1 text-xs text-zinc-500">{selection.subtitle}</p>
              ) : null}
            </div>
            {selection.meta ? (
              <dl className="space-y-1.5 rounded-md border border-zinc-800 bg-zinc-950/70 p-2.5">
                {Object.entries(selection.meta).map(([k, v]) => (
                  <div key={k} className="grid grid-cols-3 gap-2 text-[11px]">
                    <dt className="text-zinc-500">{k}</dt>
                    <dd className="col-span-2 break-all text-zinc-300">{v}</dd>
                  </div>
                ))}
              </dl>
            ) : null}
            {selection.body ? (
              <pre className="overflow-x-auto rounded-md border border-zinc-800 bg-zinc-950 p-2.5 text-[11px] leading-relaxed whitespace-pre-wrap text-zinc-400">
                {selection.body}
              </pre>
            ) : null}
          </div>
        )}
      </div>
    </aside>
  );
}
