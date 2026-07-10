import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { listSourcesCsv } from "@/lib/network";

export const dynamic = "force-dynamic";

export default function SourcesPage() {
  const sources = listSourcesCsv();
  return (
    <Shell title="Sources">
      <p className="mb-3 text-sm text-zinc-300">
        Approved knowledge sources from <code>metadata/source_registry.csv</code>.
        Planner may only use approved sources.
      </p>
      <Card>
        <CardHeader title="Source registry" description={`${sources.length} rows`} />
        <CardBody className="overflow-x-auto p-0">
          <table className="w-full min-w-[800px] text-left text-xs">
            <thead className="border-b border-zinc-800 text-[10px] uppercase text-zinc-500">
              <tr>
                <th className="px-3 py-2">ID</th>
                <th className="px-3 py-2">Name</th>
                <th className="px-3 py-2">Category</th>
                <th className="px-3 py-2">Trust</th>
                <th className="px-3 py-2">Status</th>
                <th className="px-3 py-2">Allowed</th>
              </tr>
            </thead>
            <tbody>
              {sources.length === 0 ? (
                <tr>
                  <td colSpan={6} className="px-3 py-4 text-zinc-500">
                    Waiting for first execution
                  </td>
                </tr>
              ) : (
                sources.map((s) => (
                  <tr key={s["Source ID"]} className="border-b border-zinc-900">
                    <td className="px-3 py-2 font-mono text-[11px] text-zinc-300">
                      {s["Source ID"]}
                    </td>
                    <td className="px-3 py-2 text-zinc-100">{s["Source Name"]}</td>
                    <td className="px-3 py-2 text-zinc-400">{s["Category"]}</td>
                    <td className="px-3 py-2 text-zinc-300">{s["Trust Score"]}</td>
                    <td className="px-3 py-2">
                      <Badge>{s["Status"]}</Badge>
                    </td>
                    <td className="px-3 py-2 text-zinc-400">{s["Allowed"]}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </CardBody>
      </Card>
    </Shell>
  );
}
