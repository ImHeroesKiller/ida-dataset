import { deprecatedGone } from "@/lib/api/deprecated";

export const dynamic = "force-dynamic";

/** @deprecated */
export async function GET() {
  return deprecatedGone("/api/ontology");
}
