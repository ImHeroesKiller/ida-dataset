import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "IDA · Executive Control Center",
  description:
    "Human-controlled operational cockpit for the IDA Knowledge Acquisition System",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className="dark">
      <body className="min-h-screen antialiased">{children}</body>
    </html>
  );
}
