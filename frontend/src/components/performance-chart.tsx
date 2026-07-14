"use client";

import { Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

const demo = [
  { month: "Jan", value: 100 },
  { month: "Feb", value: 104 },
  { month: "Mar", value: 103 },
  { month: "Apr", value: 108 },
  { month: "May", value: 112 },
  { month: "Jun", value: 110 },
  { month: "Jul", value: 116 },
];

export function PerformanceChart() {
  return (
    <div className="h-72 w-full rounded-xl border border-zinc-800 bg-zinc-950/40 p-4">
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={demo}>
          <XAxis dataKey="month" stroke="#a1a1aa" />
          <YAxis stroke="#a1a1aa" />
          <Tooltip />
          <Line type="monotone" dataKey="value" stroke="#22c55e" strokeWidth={2} dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
