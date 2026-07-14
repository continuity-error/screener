import { MarketSnapshot, Scheme, Stock, TickerItem } from "@/lib/types";

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000/api/v1";

async function fetchJson<T>(path: string, fallback: T): Promise<T> {
  try {
    const res = await fetch(`${API_BASE}${path}`, { next: { revalidate: 30 } });
    if (!res.ok) return fallback;
    return (await res.json()) as T;
  } catch {
    return fallback;
  }
}

export const getSnapshots = () =>
  fetchJson<MarketSnapshot[]>("/market/snapshots", [
    { index_name: "Demo NIFTY 50", last_price: 0, change_pct: 0, captured_at: new Date().toISOString() },
    { index_name: "Demo SENSEX", last_price: 0, change_pct: 0, captured_at: new Date().toISOString() },
  ]);

export const getTicker = () =>
  fetchJson<TickerItem[]>("/market/ticker", [
    { symbol: "DEMO1", last_price: 0, change_pct: 0 },
    { symbol: "DEMO2", last_price: 0, change_pct: 0 },
  ]);

export const getStocks = () => fetchJson<Stock[]>("/stocks", []);
export const getSchemes = () => fetchJson<Scheme[]>("/schemes", []);
