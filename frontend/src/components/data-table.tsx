import { ReactNode } from "react";

export function DataTable({ headers, rows }: { headers: string[]; rows: ReactNode[][] }) {
  return (
    <div className="overflow-x-auto rounded-xl border border-zinc-800 bg-zinc-950/50">
      <table className="w-full text-left text-sm">
        <thead className="bg-zinc-900 text-zinc-300">
          <tr>
            {headers.map((h) => (
              <th key={h} className="px-4 py-3 font-medium">
                {h}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, idx) => (
            <tr key={idx} className="border-t border-zinc-800 hover:bg-zinc-900/60">
              {row.map((cell, cIdx) => (
                <td key={cIdx} className="px-4 py-3 text-zinc-100">
                  {cell}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
