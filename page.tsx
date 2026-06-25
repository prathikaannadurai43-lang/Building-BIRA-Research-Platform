"use client";
import { MOCK_BUSINESSES } from "@/lib/mockData";

export default function Dashboard() {
  const total = MOCK_BUSINESSES.length;
  const highTrust = MOCK_BUSINESSES.filter((b) => b.trust_score >= 80).length;
  const conflicts = MOCK_BUSINESSES.filter((b) => b.confidence === "conflict").length;
  const flagged = MOCK_BUSINESSES.filter((b) => b.fraud_risk === "High").length;
  const avgScore = Math.round(MOCK_BUSINESSES.reduce((s, b) => s + b.trust_score, 0) / total);

  return (
    <div className="max-w-6xl mx-auto p-6 space-y-8 pb-16">
      <div>
        <h1 className="text-3xl font-bold" style={{ fontFamily: "Space Grotesk" }}>Data Quality Dashboard</h1>
        <p className="text-sm text-[#7B8BA5] mt-1">Pipeline accuracy and verification overview</p>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-5 gap-4">
        <KPI label="Businesses Found" value={total} color="#00D4FF" />
        <KPI label="High Trust (80+)" value={highTrust} color="#10B981" />
        <KPI label="Avg Trust Score" value={avgScore} color="#00D4FF" />
        <KPI label="Conflicts" value={conflicts} color="#F59E0B" />
        <KPI label="Flagged (High Risk)" value={flagged} color="#EF4444" />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Trust Distribution */}
        <div className="card">
          <h2 className="text-lg font-semibold border-b border-[#1E293B] pb-3 mb-4" style={{ fontFamily: "Space Grotesk" }}>Trust Score Distribution</h2>
          <div className="space-y-3">
            {MOCK_BUSINESSES.sort((a, b) => b.trust_score - a.trust_score).map((biz) => (
              <div key={biz.id} className="flex items-center gap-3">
                <span className="text-sm text-[#7B8BA5] w-52 truncate shrink-0">{biz.business_name}</span>
                <div className="flex-1 bg-[#141C2B] rounded-full h-3 relative overflow-hidden">
                  <div
                    className={`h-3 rounded-full transition-all duration-1000 ${biz.trust_score >= 80 ? "bg-[#10B981]" : biz.trust_score >= 50 ? "bg-[#F59E0B]" : "bg-[#EF4444]"}`}
                    style={{ width: `${biz.trust_score}%` }}
                  />
                </div>
                <span className="text-sm font-mono w-8 text-right" style={{ color: biz.trust_score >= 80 ? "#10B981" : biz.trust_score >= 50 ? "#F59E0B" : "#EF4444" }}>
                  {biz.trust_score}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Data Completeness */}
        <div className="card">
          <h2 className="text-lg font-semibold border-b border-[#1E293B] pb-3 mb-4" style={{ fontFamily: "Space Grotesk" }}>Field Completeness</h2>
          <div className="space-y-3">
            {[
              { field: "Business Name", pct: 100 },
              { field: "Address", pct: 100 },
              { field: "Phone", pct: 100 },
              { field: "Website", pct: 83 },
              { field: "Email", pct: 83 },
              { field: "Working Hours", pct: 83 },
              { field: "License Info", pct: 67 },
              { field: "Services", pct: 100 },
            ].map((item) => (
              <div key={item.field} className="flex items-center gap-3">
                <span className="text-sm text-[#7B8BA5] w-32 shrink-0">{item.field}</span>
                <div className="flex-1 bg-[#141C2B] rounded-full h-2.5 relative overflow-hidden">
                  <div className="h-2.5 rounded-full bg-[#00D4FF]" style={{ width: `${item.pct}%` }} />
                </div>
                <span className="text-xs font-mono text-[#00D4FF] w-10 text-right">{item.pct}%</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Confidence Breakdown */}
        <div className="card">
          <h2 className="text-lg font-semibold border-b border-[#1E293B] pb-3 mb-4" style={{ fontFamily: "Space Grotesk" }}>Confidence Levels</h2>
          <div className="space-y-4">
            {(["high", "medium", "low", "conflict"] as const).map((level) => {
              const count = MOCK_BUSINESSES.filter((b) => b.confidence === level).length;
              const colors: Record<string, string> = { high: "#10B981", medium: "#00D4FF", low: "#F59E0B", conflict: "#EF4444" };
              return (
                <div key={level} className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <div className="w-3 h-3 rounded-full" style={{ background: colors[level] }} />
                    <span className="text-sm capitalize">{level}</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className="text-lg font-bold font-mono" style={{ color: colors[level] }}>{count}</span>
                    <span className="text-xs text-[#7B8BA5]">/ {total}</span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Source Coverage */}
        <div className="card">
          <h2 className="text-lg font-semibold border-b border-[#1E293B] pb-3 mb-4" style={{ fontFamily: "Space Grotesk" }}>Source Coverage</h2>
          <div className="space-y-3">
            {[
              { source: "Google Business", count: 5, icon: "🌐" },
              { source: "Healthgrades", count: 3, icon: "🏥" },
              { source: "Yelp", count: 2, icon: "⭐" },
              { source: "State Board", count: 1, icon: "📜" },
              { source: "U.S. News", count: 1, icon: "📰" },
              { source: "Yellow Pages", count: 1, icon: "📒" },
            ].map((s) => (
              <div key={s.source} className="flex items-center justify-between py-1">
                <div className="flex items-center gap-2 text-sm">
                  <span>{s.icon}</span>
                  <span className="text-[#7B8BA5]">{s.source}</span>
                </div>
                <span className="text-sm font-mono text-[#F0F4FF]">{s.count} hits</span>
              </div>
            ))}
          </div>
        </div>

        {/* Pipeline Performance */}
        <div className="card">
          <h2 className="text-lg font-semibold border-b border-[#1E293B] pb-3 mb-4" style={{ fontFamily: "Space Grotesk" }}>Pipeline Stats</h2>
          <div className="space-y-4">
            <Stat label="URLs Discovered" value="23" />
            <Stat label="Pages Scraped" value="18" />
            <Stat label="Duplicates Merged" value="12 → 6" />
            <Stat label="Fields Extracted" value="48" />
            <Stat label="Cross-Verifications" value="17" />
            <Stat label="Pipeline Duration" value="4.2s" />
          </div>
        </div>
      </div>
    </div>
  );
}

function KPI({ label, value, color }: { label: string; value: number; color: string }) {
  return (
    <div className="card text-center py-5">
      <div className="text-3xl font-bold font-mono" style={{ color, fontFamily: "Space Grotesk" }}>{value}</div>
      <div className="text-xs text-[#7B8BA5] mt-1 uppercase tracking-wider">{label}</div>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="flex items-center justify-between text-sm">
      <span className="text-[#7B8BA5]">{label}</span>
      <span className="font-mono text-[#F0F4FF]">{value}</span>
    </div>
  );
}
