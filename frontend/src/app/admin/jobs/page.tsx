export default function AdminJobsPage() {
  return (
    <section className="space-y-6">
      <h1 className="text-3xl font-semibold">Admin Jobs Console</h1>
      <p className="text-zinc-300">
        Trigger import jobs, monitor run history, inspect failures, and run data quality checks.
      </p>
      <div className="grid gap-4 md:grid-cols-3">
        {[
          ["Market refresh", "Every 5 min"],
          ["Scheme refresh", "Every 60 min"],
          ["Last status", "Healthy"],
        ].map(([label, value]) => (
          <article key={label} className="rounded-xl border border-zinc-800 bg-zinc-950/50 p-4">
            <p className="text-zinc-400">{label}</p>
            <p className="mt-2 text-xl font-semibold">{value}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
