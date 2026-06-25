import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "BIRA — AI Business Research Agent",
  description: "Discover, verify, and analyze businesses with autonomous AI agents.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
      </head>
      <body>
        <div className="flex h-screen overflow-hidden">
          {/* Sidebar */}
          <aside className="w-60 border-r border-[#1E293B] bg-[#080C14] flex flex-col py-6 px-4 shrink-0 hidden md:flex">
            <div className="flex items-center gap-3 mb-10 px-2">
              <div className="w-9 h-9 rounded-lg bg-[#00D4FF] flex items-center justify-center font-bold text-[#080C14] text-lg shadow-[0_0_16px_rgba(0,212,255,0.4)]">B</div>
              <div>
                <div className="text-lg font-bold tracking-tight" style={{fontFamily:'Space Grotesk'}}>BIRA</div>
                <div className="text-[10px] text-[#7B8BA5] uppercase tracking-widest">Research Agent</div>
              </div>
            </div>

            <nav className="flex flex-col gap-1 flex-1">
              <NavLink href="/" icon={<SearchIcon />} label="Search" />
              <NavLink href="/results?q=Cardiologists+in+Birmingham" icon={<ListIcon />} label="Results" />
              <NavLink href="/dashboard" icon={<ChartIcon />} label="Dashboard" />
            </nav>

            <div className="mt-auto px-2">
              <div className="text-[10px] text-[#7B8BA5] uppercase tracking-widest mb-1">Pipeline</div>
              <div className="flex items-center gap-2">
                <span className="relative flex h-2 w-2">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#10B981] opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-[#10B981]"></span>
                </span>
                <span className="text-xs text-[#10B981]">All agents online</span>
              </div>
            </div>
          </aside>

          {/* Main */}
          <main className="flex-1 overflow-auto bg-[#080C14]">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}

/* ── Icon Components ── */
function SearchIcon() {
  return <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>;
}
function ListIcon() {
  return <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>;
}
function ChartIcon() {
  return <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>;
}

function NavLink({ href, icon, label }: { href: string; icon: React.ReactNode; label: string }) {
  return (
    <a href={href} className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-[#7B8BA5] hover:text-[#F0F4FF] hover:bg-[#0E1420] transition-colors">
      {icon}
      {label}
    </a>
  );
}
