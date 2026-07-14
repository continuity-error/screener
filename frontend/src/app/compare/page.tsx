import { PerformanceChart } from "@/components/performance-chart";

export default function ComparePage() {
  return (
    <section className="space-y-6">
      <h1 className="text-3xl font-semibold">Compare Schemes</h1>
      <p className="text-zinc-300">Select multiple schemes to compare returns, drawdown and volatility.</p>
      <PerformanceChart />
    </section>
  );
}
