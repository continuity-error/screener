import { DataTable } from "@/components/data-table";
import { getSchemes } from "@/lib/api";

export default async function SchemesPage() {
  const schemes = await getSchemes();

  return (
    <section className="space-y-5">
      <h1 className="text-3xl font-semibold">Scheme Screener</h1>
      <p className="text-zinc-300">Filter by category, AUM, returns, risk and compare funds side-by-side.</p>
      <DataTable
        headers={["Name", "Category", "AUM", "Expense", "1Y", "3Y", "5Y", "NAV"]}
        rows={schemes.map((s) => [
          s.name,
          s.category,
          `₹${s.aum.toFixed(2)} Cr`,
          `${s.expense_ratio.toFixed(2)}%`,
          `${s.return_1y.toFixed(2)}%`,
          `${s.return_3y.toFixed(2)}%`,
          `${s.return_5y.toFixed(2)}%`,
          `₹${s.nav.toFixed(2)}`,
        ])}
      />
    </section>
  );
}
