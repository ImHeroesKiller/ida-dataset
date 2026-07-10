import { deprecatedGone } from "@/lib/api/deprecated";

export const dynamic = "force-dynamic";

/** @deprecated Use /api/sessions — SSE live stream retired */
export async function GET() {
  return deprecatedGone("/api/live");
}
