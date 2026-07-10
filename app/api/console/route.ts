import { deprecatedGone } from "@/lib/api/deprecated";

export const dynamic = "force-dynamic";

/** @deprecated Use /api/publish-queue */
export async function GET() {
  return deprecatedGone("/api/console");
}
