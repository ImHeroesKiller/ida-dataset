import { redirect } from "next/navigation";

/** Datasets merged into Export (operator UI simplification). */
export default function DatasetsRedirectPage() {
  redirect("/exports");
}
