import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { ThemeProvider } from "@/components/theme-provider";
import { ChunkErrorRecovery } from "@/components/chunk-error-recovery";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: "IDA Dataset Factory",
  description:
    "Automatic Knowledge Factory — structured datasets for LLM fine-tuning",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className={`dark ${inter.variable}`} suppressHydrationWarning>
      <body className={`${inter.className} min-h-screen antialiased`}>
        <ChunkErrorRecovery />
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  );
}
