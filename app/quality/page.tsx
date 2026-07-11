import { redirect } from "next/navigation";

/** Quality metrics live on Dashboard + bottom console (operator UI simplification). */
export default function QualityRedirectPage() {
  redirect("/");
}
