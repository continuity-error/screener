import type { Metadata } from "next";
import "./globals.css";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Custom Scheme Screener",
  description: "Screen and compare stocks and investment schemes for NSE and BSE.",
};

const nav = [
  ["Home", "/"],
  ["Stocks", "/stocks"],
  ["Schemes", "/schemes"],
  ["Compare", "/compare"],
  ["Strategy", "/strategy"],
  ["Admin Jobs", "/admin/jobs"],
];

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-zinc-950 text-zinc-100">
        <header className="sticky top-0 z-50 border-b border-zinc-800 bg-zinc-950/90 backdrop-blur">
          <nav className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 text-sm">
            <span className="font-semibold">Custom Scheme Screener</span>
            <div className="flex gap-4">
              {nav.map(([label, href]) => (
                <Link key={href} href={href} className="text-zinc-300 hover:text-white">
                  {label}
                </Link>
              ))}
            </div>
          </nav>
        </header>
        <main className="mx-auto flex w-full max-w-7xl flex-col gap-10 px-4 py-8">{children}</main>
      </body>
    </html>
  );
}
