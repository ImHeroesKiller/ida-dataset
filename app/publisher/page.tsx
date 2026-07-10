import { redirect } from "next/navigation";

/** Publishing consolidated into Review + progressive publish queue. */
export default function PublisherPage() {
  redirect("/review");
}
