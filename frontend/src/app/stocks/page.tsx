import { DataTable } from "@/components/data-table";
import { getStocks } from "@/lib/api";

export default async function StocksPage() {
  const stocks = await getStocks();

  return (
    <section className="space-y-5">
      <h1 className="text-3xl font-semibold">Stock Screener (NSE/BSE)</h1>
      <p className="text-zinc-300">Filter-ready screener table with sortable metrics and CSV export from API.</p>
      <DataTable
        headers={["Symbol", "Company", "Exchange", "Sector", "P/E", "ROE", "Price", "% Chg"]}
        rows={stocks.map((s) => [
          s.symbol,
          s.company_name,
          s.exchange,
          s.sector,
          s.pe_ratio.toFixed(2),
          `${s.roe.toFixed(2)}%`,
          `₹${s.last_price.toFixed(2)}`,
          <span key={`${s.symbol}-chg`} className={s.change_pct >= 0 ? "text-emerald-400" : "text-rose-400"}>
            {s.change_pct.toFixed(2)}%
          </span>,
        ])}
      />
    </section>
  );
}
