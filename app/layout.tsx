import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { ThemeProvider } from "@/components/theme-provider";
import { ChunkErrorRecovery } from "@/components/chunk-error-recovery";
import { LearningProvider } from "@/hooks/learning-provider";
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

/**
 * LearningProvider mounts at the root so every route (including page
 * components that call useLearning before Shell chrome) shares one monitor
 * instance during SSR/prerender and client navigation.
 */
export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className={`dark ${inter.variable}`} suppressHydrationWarning>
      <body className={`${inter.className} min-h-screen antialiased`}>
        <ChunkErrorRecovery />
        <ThemeProvider>
          <LearningProvider>{children}</LearningProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}
