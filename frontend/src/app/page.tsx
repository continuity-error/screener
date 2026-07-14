import { AnimatedSection } from "@/components/animated-section";
import { MarketTicker } from "@/components/market-ticker";
import { PerformanceChart } from "@/components/performance-chart";
import { getSnapshots, getTicker } from "@/lib/api";

export default async function Home() {
  const [snapshots, ticker] = await Promise.all([getSnapshots(), getTicker()]);

  return (
    <div className="space-y-10">
      <AnimatedSection>
        <div className="rounded-2xl border border-zinc-800 bg-gradient-to-br from-zinc-900 to-zinc-950 p-8">
          <h1 className="text-4xl font-bold tracking-tight">Custom Scheme Screener for Indian Markets</h1>
          <p className="mt-3 max-w-3xl text-zinc-300">
            Premium stock and scheme analytics across NSE and BSE with strategy automation and live market pulse.
          </p>
        </div>
      </AnimatedSection>

      <MarketTicker items={ticker} />

      <AnimatedSection>
        <div className="grid gap-4 md:grid-cols-3">
          {snapshots.map((item) => (
            <article key={item.index_name} className="rounded-xl border border-zinc-800 bg-zinc-950/60 p-5">
              <p className="text-sm text-zinc-400">{item.index_name}</p>
              <p className="mt-2 text-2xl font-semibold">{item.last_price.toFixed(2)}</p>
              <p className={item.change_pct >= 0 ? "text-emerald-400" : "text-rose-400"}>
                {item.change_pct >= 0 ? "+" : ""}
                {item.change_pct.toFixed(2)}%
              </p>
            </article>
          ))}
        </div>
      </AnimatedSection>

      <AnimatedSection>
        <PerformanceChart />
      </AnimatedSection>
    </div>
  );
}
