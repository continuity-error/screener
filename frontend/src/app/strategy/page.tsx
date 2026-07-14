export default function StrategyPage() {
  return (
    <section className="space-y-6">
      <h1 className="text-3xl font-semibold">Custom Strategy Builder</h1>
      <p className="text-zinc-300">
        Define screening rules, save named strategies, and execute on latest stock/scheme snapshots.
      </p>
      <div className="rounded-xl border border-zinc-800 bg-zinc-950/50 p-5">
        <ul className="list-disc space-y-2 pl-5 text-zinc-300">
          <li>Rule expressions such as ROE &gt; 15 and 3Y return &gt; 12.</li>
          <li>Save strategy with role-based controls.</li>
          <li>Execute and rank matching results by computed score.</li>
        </ul>
      </div>
    </section>
  );
}
