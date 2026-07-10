import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { listQueuedDocuments } from "@/lib/network";

export const dynamic = "force-dynamic";

export default function DocumentsPage() {
  const docs = listQueuedDocuments();
  const sections = [
    ["incoming", docs.incoming],
    ["processing", docs.processing],
    ["processed", docs.processed],
    ["failed", docs.failed],
  ] as const;

  return (
    <Shell title="Documents">
      <p className="mb-3 text-sm text-zinc-300">
        Acquired documents only. Nothing enters domain datasets without Review +
        Publisher.
      </p>
      <div className="grid gap-3 lg:grid-cols-2">
        {sections.map(([name, rows]) => (
          <Card key={name}>
            <CardHeader title={name} description={`${rows.length} docs`} />
            <CardBody className="max-h-72 space-y-1 overflow-y-auto text-xs scrollbar-thin">
              {rows.length === 0 ? (
                <p className="text-zinc-500">Waiting for first execution</p>
              ) : (
                rows.map((d) => (
                  <div
                    key={String(d.document_id)}
                    className="border-b border-zinc-900 py-1.5"
                  >
                    <div className="font-mono text-[11px] text-zinc-100">
                      {String(d.document_id)}
                    </div>
                    <div className="truncate text-zinc-500">
                      {String(d.connector_id)} · {String(d.original_url)}
                    </div>
                  </div>
                ))
              )}
            </CardBody>
          </Card>
        ))}
      </div>
    </Shell>
  );
}
