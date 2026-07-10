import { deprecatedGone } from "@/lib/api/deprecated";

export const dynamic = "force-dynamic";

/** @deprecated Use /api/sessions?session_id= */
export async function GET() {
  return deprecatedGone("/api/live/replay");
}
