import { redirect } from "next/navigation";

/** Logs live in bottom console (operator UI simplification). */
export default function LogsRedirectPage() {
  redirect("/");
}
