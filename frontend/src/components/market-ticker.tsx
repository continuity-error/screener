"use client";

import { TickerItem } from "@/lib/types";

export function MarketTicker({ items }: { items: TickerItem[] }) {
  const doubled = [...items, ...items];
  return (
    <div className="overflow-hidden border-y border-zinc-800 bg-zinc-950 py-2">
      <div className="ticker-track flex min-w-max gap-8 text-sm">
        {doubled.map((item, idx) => (
          <div key={`${item.symbol}-${idx}`} className="flex items-center gap-2">
            <span className="font-semibold">{item.symbol}</span>
            <span>₹{item.last_price.toFixed(2)}</span>
            <span className={item.change_pct >= 0 ? "text-emerald-400" : "text-rose-400"}>
              {item.change_pct >= 0 ? "+" : ""}
              {item.change_pct.toFixed(2)}%
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
