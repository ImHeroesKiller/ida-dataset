import { deprecatedGone } from "@/lib/api/deprecated";

export const dynamic = "force-dynamic";

/** @deprecated Unused git API */
export async function GET() {
  return deprecatedGone("/api/git");
}
