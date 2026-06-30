import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Migraine Intelligence Hub",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important;}
[data-testid="stAppViewBlockContainer"] {padding: 0 !important;}
iframe {height: 100vh !important; min-height: 100vh !important;}
</style>
""", unsafe_allow_html=True)

html_content = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Migraine Intelligence Hub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
    --navy-900: #0A1A3D;
    --navy-800: #102A5C;
    --navy-700: #163990;
    --navy-600: #1C4FC0;
    --navy-500: #3B6FD9;
    --accent: #41B6E6;
    
    --bg: #EEF3FB;
    --bg-2: #E3EBF7;
    --surface: #FFFFFF;
    --surface-2: #F8FAFD;
    --text: #0F172A;
    --text-muted: #64748B;
    --text-soft: #475569;
    --hairline: rgba(15,23,42,0.08);
    --hairline-2: rgba(15,23,42,0.05);
    --up: #10B981;
    --down: #EF4444;
    --flat: #94A3B8;
    --shadow-xs: 0 1px 2px rgba(15,23,42,0.04);
    --shadow-sm: 0 2px 8px rgba(15,23,42,0.05), 0 1px 2px rgba(15,23,42,0.04);
    --shadow-md: 0 6px 16px rgba(15,23,42,0.07), 0 2px 4px rgba(15,23,42,0.04);
    --shadow-lg: 0 18px 40px rgba(15,23,42,0.10), 0 6px 12px rgba(15,23,42,0.06);
    --shadow-panel: 0 8px 24px rgba(15,23,42,0.07), 0 2px 6px rgba(15,23,42,0.04);
    --ease: cubic-bezier(0.4, 0, 0.2, 1);
    --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
    --sidebar-w: 232px;
    --shell-pad: 10px;
    --panel-radius: 18px;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { height: 100%; }

body {
    font-family: 'Inter', system-ui, -apple-system, 'SF Pro Text', 'Segoe UI', Roboto, sans-serif;
    background:
        radial-gradient(ellipse 80% 60% at 0% 0%, rgba(28,79,192,0.08) 0%, transparent 60%),
        radial-gradient(ellipse 70% 50% at 100% 0%, rgba(65,182,230,0.07) 0%, transparent 55%),
        radial-gradient(ellipse 60% 50% at 50% 100%, rgba(124,58,237,0.04) 0%, transparent 60%),
        var(--bg);
    color: var(--text);
    line-height: 1.5;
    font-size: 14px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    overflow: hidden;
}

h1, h2, h3, h4 { font-family: 'Manrope', 'Inter', 'SF Pro Display', system-ui, sans-serif; letter-spacing: -0.015em; }
a { color: inherit; text-decoration: none; }

/* ───── APP SHELL ───── */
.app { height: 100vh; display: grid; grid-template-columns: var(--sidebar-w) 1fr; gap: var(--shell-pad); padding: var(--shell-pad); overflow: hidden; }

/* ───── SIDEBAR ───── */
.sidebar { position: relative; background: rgba(255,255,255,0.62); backdrop-filter: saturate(180%) blur(22px); -webkit-backdrop-filter: saturate(180%) blur(22px); border: 1px solid var(--hairline); border-radius: var(--panel-radius); box-shadow: var(--shadow-panel); display: flex; flex-direction: column; overflow: hidden; z-index: 10; }

.sidebar-brand { padding: 1.4rem 1.2rem 1.2rem; display: flex; flex-direction: column; gap: 0.7rem; }
.sidebar-brand img { height: 28px; align-self: flex-start; }
.sidebar-brand .title { font-family: 'Manrope', sans-serif; font-weight: 800; font-size: 1.22rem; color: var(--navy-900); line-height: 1.18; letter-spacing: -0.025em; }
.sidebar-brand .subtitle { font-size: 0.72rem; color: var(--text-muted); font-weight: 500; }

.sidebar-divider { height: 1px; background: var(--hairline); margin: 0 0.85rem; }

.sidebar-section-label { font-family: 'Manrope', sans-serif; font-size: 0.62rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--text-muted); padding: 0.95rem 1.15rem 0.4rem; }

.nav { padding: 0 0.55rem; }
.nav-item {
    position: relative; display: flex; align-items: center; gap: 0.7rem;
    padding: 0.55rem 0.7rem; margin: 0.08rem 0; border-radius: 8px;
    font-size: 0.84rem; font-weight: 500; color: var(--text-soft);
    cursor: pointer; transition: background 0.18s var(--ease), color 0.18s var(--ease);
    background: transparent; border: none; width: 100%; text-align: left; font-family: inherit;
}
.nav-item .nav-icon { width: 18px; height: 18px; display: flex; align-items: center; justify-content: center; color: var(--text-muted); transition: color 0.18s var(--ease); flex-shrink: 0; }
.nav-item .nav-icon svg { width: 16px; height: 16px; stroke-width: 1.8; fill: none; stroke: currentColor; }
.nav-item .nav-label { flex: 1; min-width: 0; }
.nav-item .nav-count { font-size: 0.66rem; font-weight: 600; color: var(--text-muted); background: rgba(15,23,42,0.06); padding: 0.12rem 0.42rem; border-radius: 5px; font-variant-numeric: tabular-nums; transition: background 0.18s var(--ease), color 0.18s var(--ease); flex-shrink: 0; line-height: 1.3; }
.nav-item:hover { background: rgba(15,23,42,0.04); color: var(--text); }
.nav-item:hover .nav-icon { color: var(--navy-700); }
.nav-item:hover .nav-count { background: rgba(15,23,42,0.09); color: var(--text-soft); }

.nav-item.active { background: linear-gradient(90deg, rgba(28,79,192,0.10) 0%, rgba(28,79,192,0.04) 100%); color: var(--navy-700); font-weight: 600; }
.nav-item.active .nav-icon { color: var(--navy-700); }
.nav-item.active .nav-count { background: rgba(28,79,192,0.14); color: var(--navy-700); }
.nav-item.active::before { content: ''; position: absolute; left: -0.55rem; top: 6px; bottom: 6px; width: 3px; border-radius: 0 3px 3px 0; background: linear-gradient(180deg, var(--navy-600), var(--accent)); box-shadow: 0 0 8px rgba(28,79,192,0.3); }

/* ───── SUB-NAV (indented children) ───── */
.nav-sub {
    display: none;
    flex-direction: column;
    padding: 0.15rem 0 0.15rem 1.8rem;
}
.nav-sub.is-open { display: flex; }
.nav-sub-item {
    position: relative;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.38rem 0.65rem;
    margin: 0.04rem 0;
    border-radius: 6px;
    font-size: 0.76rem;
    font-weight: 500;
    color: var(--text-muted);
    cursor: pointer;
    transition: background 0.18s var(--ease), color 0.18s var(--ease);
    background: transparent;
    border: none;
    width: 100%;
    text-align: left;
    font-family: inherit;
}
.nav-sub-item:hover { background: rgba(15,23,42,0.04); color: var(--text); }
.nav-sub-item.active { background: rgba(28,79,192,0.08); color: var(--navy-700); font-weight: 600; }
.nav-sub-item.external { color: var(--text-muted); font-style: italic; }
.nav-sub-item.external svg { width: 10px; height: 10px; stroke: currentColor; fill: none; stroke-width: 2; flex-shrink: 0; }

.sidebar-spacer { flex: 1; }

.sidebar-meta { padding: 0.85rem 1.15rem 1rem; font-size: 0.7rem; color: var(--text-muted); line-height: 1.55; border-top: 1px solid var(--hairline); background: linear-gradient(180deg, transparent 0%, rgba(28,79,192,0.025) 100%); overflow: hidden; }
.sidebar-meta strong { color: var(--text-soft); font-weight: 600; }
.sidebar-meta a { color: var(--navy-700); white-space: nowrap; font-size: 0.54rem; }
.sidebar-meta a:hover { text-decoration: underline; }
.sidebar-meta .meta-row { margin-bottom: 0.2rem; }

/* ───── MAIN ───── */
.main { background: rgba(255,255,255,0.55); backdrop-filter: saturate(180%) blur(14px); -webkit-backdrop-filter: saturate(180%) blur(14px); border: 1px solid var(--hairline); border-radius: var(--panel-radius); box-shadow: var(--shadow-panel); display: flex; flex-direction: column; overflow: hidden; min-width: 0; }

/* ───── CONTENT ───── */
.content { flex: 1; min-height: 0; overflow-y: auto; padding: 1.4rem; }
.content::-webkit-scrollbar { width: 6px; }
.content::-webkit-scrollbar-track { background: transparent; }
.content::-webkit-scrollbar-thumb { background: rgba(15,23,42,0.14); border-radius: 3px; }
.content::-webkit-scrollbar-thumb:hover { background: rgba(15,23,42,0.24); }

/* ───── DROPDOWN ───── */
.dropdown-wrap { position: relative; }
.icon-btn { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.4rem 0.7rem; border-radius: 7px; background: rgba(255,255,255,0.7); border: 1px solid var(--hairline); color: var(--text-soft); font-size: 0.75rem; font-weight: 500; cursor: pointer; font-family: inherit; transition: all 0.18s var(--ease); }
.icon-btn:hover { background: #fff; color: var(--navy-700); border-color: rgba(28,79,192,0.25); box-shadow: var(--shadow-xs); }
.icon-btn svg { width: 13px; height: 13px; stroke-width: 1.8; fill: none; stroke: currentColor; }
.dropdown { position: absolute; top: calc(100% + 6px); right: 0; background: rgba(255,255,255,0.96); backdrop-filter: saturate(180%) blur(20px); border: 1px solid var(--hairline); border-radius: 12px; box-shadow: var(--shadow-lg); min-width: 240px; padding: 0.45rem 0; opacity: 0; visibility: hidden; transform: translateY(-6px) scale(0.98); transform-origin: top right; transition: opacity 0.2s var(--ease), transform 0.2s var(--ease), visibility 0.2s; z-index: 200; }
.dropdown.show { opacity: 1; visibility: visible; transform: translateY(0) scale(1); }
.dropdown-header { font-size: 0.62rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); padding: 0.5rem 0.95rem 0.35rem; }
.dropdown-item { display: flex; align-items: center; justify-content: space-between; padding: 0.45rem 0.95rem; font-size: 0.78rem; }
.dropdown-item:hover { background: rgba(15,23,42,0.04); }
.dropdown-item .src { font-weight: 500; }
.dropdown-item .date { font-size: 0.7rem; color: var(--text-muted); font-variant-numeric: tabular-nums; }

/* ───── SECTIONS ───── */
.section { display: none; opacity: 0; transform: translateY(4px); transition: opacity 0.22s var(--ease), transform 0.22s var(--ease-out); }
.section.is-active { display: block; }
.section.is-visible { opacity: 1; transform: translateY(0); }

.section-head { margin-bottom: 1rem; }
.section-head-row { display: flex; align-items: center; justify-content: space-between; gap: 1rem; margin-bottom: 0.2rem; }
.section-head h2 { font-size: 1.35rem; font-weight: 700; color: var(--navy-900); letter-spacing: -0.02em; margin-bottom: 0.2rem; }
.section-head p { font-size: 0.84rem; color: var(--text-muted); max-width: 680px; }

.grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }

/* ───── CARDS ───── */
.card { position: relative; display: flex; flex-direction: column; background: var(--surface); border-radius: 14px; padding: 1.15rem 1.2rem; min-height: 148px; overflow: hidden; box-shadow: var(--shadow-sm); transition: transform 0.28s var(--ease-out), box-shadow 0.28s var(--ease); cursor: pointer; }
.card::after { content: ''; position: absolute; inset: 0; border-radius: inherit; background: linear-gradient(135deg, rgba(255,255,255,0) 55%, rgba(65,182,230,0.05) 80%, rgba(28,79,192,0.07) 100%); opacity: 0; transition: opacity 0.28s var(--ease); pointer-events: none; }
.card:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); }
.card:hover::after { opacity: 1; }

.card-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.7rem; }
.icon-chip { width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.icon-chip svg { width: 19px; height: 19px; stroke-width: 1.8; fill: none; }
.chip-s1 { background: linear-gradient(135deg, #DBEAFE, #BFDBFE); } .chip-s1 svg { stroke: #1D4ED8; }
.chip-s2 { background: linear-gradient(135deg, #E0E7FF, #C7D2FE); } .chip-s2 svg { stroke: #4338CA; }
.chip-s3 { background: linear-gradient(135deg, #EDE9FE, #DDD6FE); } .chip-s3 svg { stroke: #6D28D9; }
.chip-s4 { background: linear-gradient(135deg, #CFFAFE, #A5F3FC); } .chip-s4 svg { stroke: #0E7490; }
.chip-s5 { background: linear-gradient(135deg, #DCFCE7, #BBF7D0); } .chip-s5 svg { stroke: #047857; }

.card-title { font-family: 'Manrope', sans-serif; font-size: 1.02rem; font-weight: 700; color: var(--navy-900); line-height: 1.25; margin-bottom: 0.3rem; }
.card-desc { font-size: 0.8rem; color: var(--text-muted); line-height: 1.5; flex: 1; margin-bottom: 0.85rem; }
.dest-pill { display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.7rem; font-weight: 600; color: var(--text-soft); padding: 0.22rem 0.55rem; border-radius: 6px; background: rgba(15,23,42,0.05); align-self: flex-start; }
.dest-tableau .swatch { color: #1F77B4; } .dest-ppt .swatch { color: #D24726; } .dest-xlsx .swatch { color: #107C41; } .dest-agent .swatch { color: #7C3AED; } .dest-doc .swatch { color: #475569; }
.badge { font-size: 0.6rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; padding: 0.2rem 0.5rem; border-radius: 5px; background: rgba(15,23,42,0.05); color: var(--text-muted); }
.badge.weekly { background: rgba(16,185,129,0.12); color: #047857; }
.badge.monthly { background: rgba(59,130,246,0.12); color: #1E40AF; }

/* ───── HERO BANNER ───── */
.hero { position: relative; background: radial-gradient(ellipse 90% 80% at 20% 20%, rgba(28,79,192,0.06) 0%, transparent 50%), radial-gradient(ellipse 60% 70% at 80% 80%, rgba(65,182,230,0.05) 0%, transparent 50%), linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(248,250,253,0.95) 100%); border-radius: 16px; padding: 2rem 2rem 1.6rem; border: 1px solid var(--hairline-2); box-shadow: var(--shadow-sm); overflow: hidden; }
.hero::before { content: ''; position: absolute; top: -1px; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--navy-600), var(--accent), var(--navy-500)); border-radius: 16px 16px 0 0; opacity: 0.7; }
.hero-header { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 1.5rem; }
.hero-title { font-family: 'Manrope', sans-serif; font-size: 1.65rem; font-weight: 800; color: var(--navy-900); letter-spacing: -0.025em; line-height: 1.15; margin-bottom: 0.35rem; }
.hero-subtitle { font-size: 0.82rem; font-weight: 500; color: var(--text-muted); display: flex; align-items: center; gap: 0.5rem; }
.hero-subtitle .dot { width: 4px; height: 4px; border-radius: 50%; background: var(--text-muted); opacity: 0.5; }
.hero-badge { display: inline-flex; align-items: center; gap: 0.4rem; font-size: 0.68rem; font-weight: 600; color: var(--navy-700); background: rgba(28,79,192,0.08); padding: 0.3rem 0.7rem; border-radius: 8px; flex-shrink: 0; margin-top: 0.2rem; }
.hero-badge svg { width: 12px; height: 12px; stroke: currentColor; fill: none; stroke-width: 2; }
.hero-kpis { display: grid; grid-template-columns: repeat(5, 1fr); gap: 0.75rem; }
.hero-kpi { background: rgba(255,255,255,0.75); backdrop-filter: blur(8px); border: 1px solid var(--hairline-2); border-radius: 12px; padding: 0.85rem 1rem 0.8rem; transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease); }
.hero-kpi:hover { transform: translateY(-2px); box-shadow: var(--shadow-md); }
.hero-kpi .kpi-label { font-size: 0.7rem; color: var(--text-muted); font-weight: 500; margin-bottom: 0.25rem; }
.hero-kpi .kpi-value { font-family: 'Manrope', sans-serif; font-size: 1.5rem; font-weight: 700; color: var(--navy-900); line-height: 1.1; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; margin-bottom: 0.3rem; }
.hero-kpi .kpi-delta { display: inline-flex; align-items: center; gap: 0.25rem; font-size: 0.7rem; font-weight: 600; font-variant-numeric: tabular-nums; }
.hero-kpi .kpi-delta.up { color: var(--up); } .hero-kpi .kpi-delta.down { color: var(--down); } .hero-kpi .kpi-delta.flat { color: var(--flat); }
.hero-kpi .kpi-delta .tri { font-size: 0.65rem; line-height: 1; }
.hero-kpi .kpi-delta .vs { color: var(--text-muted); font-weight: 500; }

.workspace-divider { height: 1px; background: var(--hairline); margin: 1.4rem 0; }

/* ───── SUB-PANEL (full content area) ───── */
.sub-panel { display: none; }
.sub-panel.is-active { display: block; }
.sub-panel-title { font-family: 'Manrope', sans-serif; font-size: 1.25rem; font-weight: 700; color: var(--navy-900); margin-bottom: 0.3rem; letter-spacing: -0.02em; }
.sub-panel-desc { font-size: 0.84rem; color: var(--text-muted); margin-bottom: 1.4rem; max-width: 640px; }
.placeholder-chart { border: 2px dashed var(--hairline); border-radius: 12px; padding: 3rem 2rem; display: flex; align-items: center; justify-content: center; color: var(--text-muted); font-size: 0.85rem; font-weight: 500; background: var(--surface-2); margin-bottom: 1.2rem; min-height: 220px; }
.placeholder-table { border: 1px solid var(--hairline); border-radius: 10px; overflow: hidden; }
.placeholder-table-header { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 0.6rem 1rem; background: var(--surface-2); font-size: 0.7rem; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.06em; border-bottom: 1px solid var(--hairline); }
.placeholder-table-row { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 0.55rem 1rem; font-size: 0.8rem; color: var(--text-soft); border-bottom: 1px solid var(--hairline-2); }
.placeholder-table-row:last-child { border-bottom: none; }

/* ───── RESPONSIVE ───── */
@media (max-width: 1180px) { :root { --sidebar-w: 208px; } }
@media (max-width: 980px) { .grid { grid-template-columns: repeat(2, 1fr); } .hero-kpis { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 760px) { :root { --sidebar-w: 60px; } .sidebar-brand .title, .sidebar-brand .subtitle, .sidebar-section-label, .sidebar-meta, .nav-item .nav-label, .nav-item .nav-count, .nav-sub { display: none; } .nav-item { justify-content: center; padding: 0.6rem 0; } .nav { padding: 0 0.3rem; } }
@media (max-width: 560px) { .grid { grid-template-columns: 1fr; } body { overflow: auto; } .app { height: auto; grid-template-columns: 1fr; padding: 0; gap: 0; } .sidebar { display: none; } .main { border-radius: 0; border: none; } .main, .content { overflow: visible; } .hero-kpis { grid-template-columns: repeat(2, 1fr); } .hero-title { font-size: 1.35rem; } .hero { padding: 1.4rem 1.2rem 1.2rem; } .hero-header { flex-direction: column; gap: 0.6rem; } }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }

/* ????? TOOLBAR ????? */
.toolbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.7rem 1.4rem;
    border-bottom: 1px solid var(--hairline);
    flex-shrink: 0;
    z-index: 5;
}
.toolbar-title {
    font-family: 'Manrope', sans-serif;
    font-size: 0.78rem;
    color: var(--text-muted);
    font-weight: 500;
}
.toolbar-title strong { color: var(--text); font-weight: 600; }
.toolbar-actions { display: flex; align-items: center; gap: 0.45rem; }

/* ????? KPI STRIP ????? */
.kpis-head {
    font-family: 'Manrope', sans-serif;
    font-size: 0.62rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: var(--text-muted);
    margin-bottom: 0.55rem;
}
.kpi-row {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 0.85rem;
    margin-bottom: 1.6rem;
}
.kpi {
    background: var(--surface);
    border-radius: 14px;
    padding: 1rem 1.15rem 1.05rem;
    box-shadow: var(--shadow-sm);
    transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease);
    position: relative;
    overflow: hidden;
}
.kpi::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0) 60%, rgba(28,79,192,0.04) 100%);
    opacity: 0;
    transition: opacity 0.25s var(--ease);
    pointer-events: none;
}
.kpi:hover { transform: translateY(-2px); box-shadow: var(--shadow-md); }
.kpi:hover::before { opacity: 1; }
.kpi .kpi-label {
    font-size: 0.74rem;
    color: var(--text-muted);
    font-weight: 500;
    margin-bottom: 0.3rem;
}
.kpi .kpi-value {
    font-family: 'Manrope', sans-serif;
    font-size: 1.7rem;
    font-weight: 700;
    color: var(--navy-900);
    line-height: 1.05;
    letter-spacing: -0.025em;
    font-variant-numeric: tabular-nums;
    margin-bottom: 0.4rem;
}
.kpi .kpi-delta {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.74rem;
    font-weight: 600;
    font-variant-numeric: tabular-nums;
}
.kpi .kpi-delta.up { color: var(--up); }
.kpi .kpi-delta.down { color: var(--down); }
.kpi .kpi-delta.flat { color: var(--flat); }
.kpi .kpi-delta .tri { font-size: 0.7rem; line-height: 1; }
.kpi .kpi-delta .vs { color: var(--text-muted); font-weight: 500; }

/* Card enhancements */
.card:active { transform: translateY(-1px) scale(0.995); transition-duration: 0.08s; }
.card:hover .icon-chip { transform: scale(1.05) rotate(-2deg); }
.card:hover .dest-pill { background: rgba(28,79,192,0.10); color: var(--navy-700); }
.card-updated { font-size: 0.68rem; color: var(--text-muted); font-weight: 500; margin-top: -0.65rem; margin-bottom: 0.7rem; opacity: 0.85; }
</style>
</head>
<body>

<div class="app">

<!-- ═══ SIDEBAR ═══ -->
<aside class="sidebar">
    <div class="sidebar-brand">
        <img src="https://cdn.pfizer.com/pfizercom/2022-10/Pfizer_Logo_Color_CMYK.png" alt="Pfizer">
        <div>
            <div class="title">Migraine<br>Intelligence Hub</div>
            <div class="subtitle">Nurtec&reg; ODT</div>
        </div>
    </div>
    <div class="sidebar-divider"></div>
    <div class="sidebar-section-label">Workspace</div>
    <nav class="nav" id="sidebarNav">
        <button class="nav-item active" data-target="dashboards">
            <span class="nav-icon"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/></svg></span>
            <span class="nav-label">Deep-Dive Dashboards</span>
            <span class="nav-count">6</span>
        </button>
        <button class="nav-item" data-target="newsletter">
            <span class="nav-icon"><svg viewBox="0 0 24 24"><path d="M4 4h16v16H4z"/><path d="M4 9h16M9 4v16"/></svg></span>
            <span class="nav-label">Weekly Newsletter</span>
            <span class="nav-count">6</span>
        </button>
        <!-- Sub-nav items (indented under Weekly Newsletter) -->
        <div class="nav-sub" id="newsletterSub">
            <button class="nav-sub-item active" data-panel="nl-exec">Executive Summary</button>
            <button class="nav-sub-item" data-panel="nl-xponent">Xponent Trends</button>
            <button class="nav-sub-item" data-panel="nl-market">Market Insights</button>
            <button class="nav-sub-item" data-panel="nl-access">Access Changes</button>
            <a class="nav-sub-item external" href="https://dss-amer-design.pfizer.com/webapps/MIGRAINEDOPPLR/zXimTdd/" target="_blank" rel="noopener">DOppLR Alerts <svg viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/></svg></a>
            <button class="nav-sub-item" data-panel="nl-financial">Financial Summary</button>
        </div>
        <button class="nav-item" data-target="agents">
            <span class="nav-icon"><svg viewBox="0 0 24 24"><rect x="6" y="6" width="12" height="10" rx="2"/><path d="M9 16v3M15 16v3M9 6V3M15 6V3M3 11h3M18 11h3"/></svg></span>
            <span class="nav-label">CoWork Agents</span>
            <span class="nav-count">3</span>
        </button>
        <button class="nav-item" data-target="deliverables">
            <span class="nav-icon"><svg viewBox="0 0 24 24"><path d="M14 3v5h5M5 21h14a1 1 0 001-1V8l-5-5H5a1 1 0 00-1 1v16a1 1 0 001 1z"/></svg></span>
            <span class="nav-label">Analytics Deliverables</span>
            <span class="nav-count">3</span>
        </button>
        <button class="nav-item" data-target="docs">
            <span class="nav-icon"><svg viewBox="0 0 24 24"><path d="M5 3h11l3 3v15a1 1 0 01-1 1H5a1 1 0 01-1-1V4a1 1 0 011-1z"/><path d="M9 9h6M9 13h6M9 17h4"/></svg></span>
            <span class="nav-label">Business Rule Docs</span>
            <span class="nav-count">5</span>
        </button>
    </nav>
    <div class="sidebar-spacer"></div>
    <div class="sidebar-meta">
        <div class="meta-row"><strong>IIS Migraine Analytics</strong></div>
        <div class="meta-row"><a href="mailto:Team_ZS_US_Migraine_Analytics@zs.com">Team_ZS_US_Migraine_Analytics@zs.com</a></div>
        <div class="meta-row">Updated Jun 19, 2026</div>
    </div>
</aside>

<!-- ═══ MAIN ═══ -->
<div class="main">
    
    <!-- TOOLBAR -->
    <div class="toolbar">
        <div class="toolbar-title">Workspace &middot; <strong id="toolbarSection">Deep-Dive Dashboards</strong></div>
        <div class="toolbar-actions">
            <button class="icon-btn" title="Help">
                <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 015 0c0 1.5-2.5 2-2.5 4M12 17v.01"/></svg>
                Help
            </button>
        </div>
    </div>

    <main class="content">
        <!-- KPI STRIP -->
        <div class="kpis-head" id="kpisHead">Executive KPIs</div>
        <div class="kpi-row" id="kpiRow">
            <div class="kpi"><div class="kpi-label">Nurtec TRx</div><div class="kpi-value">42.3K</div><div class="kpi-delta up"><span class="tri">&#9650;</span>3.2% <span class="vs">vs PW</span></div></div>
            <div class="kpi"><div class="kpi-label">Nurtec NBRx</div><div class="kpi-value">8.7K</div><div class="kpi-delta up"><span class="tri">&#9650;</span>1.8% <span class="vs">vs PW</span></div></div>
            <div class="kpi"><div class="kpi-label">Market Share (TRx)</div><div class="kpi-value">18.4%</div><div class="kpi-delta up"><span class="tri">&#9650;</span>0.3% <span class="vs">vs PW</span></div></div>
            <div class="kpi"><div class="kpi-label">oCGRP Share</div><div class="kpi-value">34.1%</div><div class="kpi-delta down"><span class="tri">&#9660;</span>0.2% <span class="vs">vs PW</span></div></div>
            <div class="kpi"><div class="kpi-label">NRx-to-TRx Ratio</div><div class="kpi-value">4.9x</div><div class="kpi-delta flat"><span class="tri">&mdash;</span>Flat <span class="vs">vs PW</span></div></div>
        </div>


        <!-- HERO BANNER -->
        <div class="hero">
            <div class="hero-header">
                <div class="hero-text">
                    <h1 class="hero-title">Nurtec Performance YTD</h1>
                    <div class="hero-subtitle"><span>Nurtec&reg; ODT</span><span class="dot"></span><span>IIS Analytics</span></div>
                </div>
                <span class="hero-badge"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 5V3M12 21v-2M16.95 7.05l1.41-1.41M5.64 18.36l1.41-1.41M19 12h2M3 12h2M16.95 16.95l1.41 1.41M5.64 5.64l1.41 1.41"/></svg>Executive KPIs</span>
            </div>
            <div class="hero-kpis">
                <div class="hero-kpi"><div class="kpi-label">Nurtec TRx</div><div class="kpi-value">892K</div><div class="kpi-delta up"><span class="tri">&#9650;</span>+12.4% <span class="vs">vs STLY</span></div></div>
                <div class="hero-kpi"><div class="kpi-label">Nurtec NBRx</div><div class="kpi-value">187K</div><div class="kpi-delta up"><span class="tri">&#9650;</span>+8.6% <span class="vs">vs STLY</span></div></div>
                <div class="hero-kpi"><div class="kpi-label">Nurtec oCGRP Mkt Share</div><div class="kpi-value">34.1%</div><div class="kpi-delta up"><span class="tri">&#9650;</span>+1.8% <span class="vs">vs STLY</span></div></div>
                <div class="hero-kpi"><div class="kpi-label">Acute Nurtec oCGRP Share</div><div class="kpi-value">41.2%</div><div class="kpi-delta up"><span class="tri">&#9650;</span>+2.3% <span class="vs">vs STLY</span></div></div>
                <div class="hero-kpi"><div class="kpi-label">Preventive Nurtec oCGRP Share</div><div class="kpi-value">22.7%</div><div class="kpi-delta down"><span class="tri">&#9660;</span>-0.5% <span class="vs">vs STLY</span></div></div>
            </div>
        </div>

        <div class="workspace-divider"></div>

        <!-- 1. DASHBOARDS -->
        <section class="section is-active is-visible" id="dashboards" data-label="Deep-Dive Dashboards">
            <div class="section-head">
                <div class="section-head-row">
                    <h2>Deep-Dive Dashboards</h2>
                    <div class="dropdown-wrap">
                        <button class="icon-btn" onclick="toggleDropdown('dataDropdown', event)"><svg viewBox="0 0 24 24"><ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v6c0 1.7 3.6 3 8 3s8-1.3 8-3V6"/><path d="M4 12v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/></svg>Data Availability<svg viewBox="0 0 24 24" style="width:11px;height:11px;"><path d="M6 9l6 6 6-6"/></svg></button>
                        <div class="dropdown" id="dataDropdown">
                            <div class="dropdown-header">Last refresh by source</div>
                            <div class="dropdown-item"><span class="src">NPA</span><span class="date">Jun 13, 2026</span></div>
                            <div class="dropdown-item"><span class="src">Weekly LAAD</span><span class="date">Jun 11, 2026</span></div>
                            <div class="dropdown-item"><span class="src">Monthly LAAD</span><span class="date">May 31, 2026</span></div>
                            <div class="dropdown-item"><span class="src">Xponent</span><span class="date">Jun 6, 2026</span></div>
                            <div class="dropdown-item"><span class="src">Forsyth</span><span class="date">Jun 10, 2026</span></div>
                            <div class="dropdown-item"><span class="src">Optum</span><span class="date">Mar 31, 2026</span></div>
                        </div>
                    </div>
                </div>
                <p>Interactive analytics across patient funnel, volume, HCP, payer, and financial performance.</p>
            </div>
            <div class="grid">
                <a class="card" href="https://us-east-1.online.tableau.com/#/site/amerdev/views/USMigraineDashboard/PatientFunnel?:iid=1" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s1"><svg viewBox="0 0 24 24"><path d="M5.5 5h13a1 1 0 011 1v10a1 1 0 01-1 1h-13a1 1 0 01-1-1V6a1 1 0 011-1zM4 20h16M10 5V3M14 5V3"/></svg></span></div><div class="card-title">Patient Funnel</div><div class="card-desc">Eligibility through treatment at claims and patient-level views.</div><span class="dest-pill dest-tableau"><span class="swatch">&#9632;</span>Tableau</span></a>
                <a class="card" href="https://us-east-1.online.tableau.com/#/site/amerdev/views/USMigraineConcurrentUsageTab/ConcurrentUsageTab" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s1"><svg viewBox="0 0 24 24"><circle cx="12" cy="7" r="4"/><path d="M6 21v-2a4 4 0 014-4h4a4 4 0 014 4v2"/></svg></span></div><div class="card-title">Patient Deep Dive</div><div class="card-desc">Concurrent usage, switching patterns, and patient segmentation.</div><span class="dest-pill dest-tableau"><span class="swatch">&#9632;</span>Tableau</span></a>
                <a class="card" href="https://us-east-1.online.tableau.com/#/site/amerdev/views/USMigraineDashboard/VolumeDeepDive" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s1"><svg viewBox="0 0 24 24"><path d="M3 12h4l3-9 4 18 3-9h4"/></svg></span></div><div class="card-title">Volume Deep Dive</div><div class="card-desc">TRx and NBRx volume trends across brands and channels.</div><span class="dest-pill dest-tableau"><span class="swatch">&#9632;</span>Tableau</span></a>
                <a class="card" href="https://us-east-1.online.tableau.com/#/site/amerdev/views/USMigraineDashboard/PrescriptionInsights?:iid=1" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s1"><svg viewBox="0 0 24 24"><path d="M12 4a5 5 0 015 5v3a1 1 0 01-1 1H8a1 1 0 01-1-1V9a5 5 0 015-5z"/><path d="M12 13v7M9 20h6"/></svg></span></div><div class="card-title">HCP Deep Dive</div><div class="card-desc">Prescriber behavior, decile analysis, and targeting insights.</div><span class="dest-pill dest-tableau"><span class="swatch">&#9632;</span>Tableau</span></a>
                <a class="card" href="https://us-east-1.online.tableau.com/#/site/amerdev/views/USMigraineDashboardPayerDeepDive/PayerSummary?:iid=1" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s1"><svg viewBox="0 0 24 24"><path d="M3 21h18M5 21V7l8-4v18M19 21V11l-6-4"/></svg></span></div><div class="card-title">Payer Deep Dive</div><div class="card-desc">Formulary status, payer mix, and access rates.</div><span class="dest-pill dest-tableau"><span class="swatch">&#9632;</span>Tableau</span></a>
                <a class="card" href="https://us-east-1.online.tableau.com/#/site/amerdev/views/USMigraineDashboard/FinancialSummary?:iid=1" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s1"><svg viewBox="0 0 24 24"><path d="M12 2v20M5 9h11a3 3 0 010 6H7a3 3 0 000 6h12"/></svg></span></div><div class="card-title">Financial Summary</div><div class="card-desc">Revenue, cost, and financial KPIs across the portfolio.</div><span class="dest-pill dest-tableau"><span class="swatch">&#9632;</span>Tableau</span></a>
            </div>
        </section>

        <!-- 2. NEWSLETTER -->
        <section class="section" id="newsletter" data-label="Weekly Newsletter">
            <!-- Card grid view (initial state when clicking Weekly Newsletter) -->
            <div id="nl-grid-view">
                <div class="section-head">
                    <h2>Weekly Newsletter Deep-Dive</h2>
                    <p>In-depth weekly analyses covering market momentum, competitive share shifts, and performance trends.</p>
                </div>
                <div class="grid">
                    <div class="card" data-nl-panel="nl-exec"><div class="card-top"><span class="icon-chip chip-s2"><svg viewBox="0 0 24 24"><path d="M4 19h16M4 15l4-6 4 2 4-5 4 4"/></svg></span><span class="badge weekly">Weekly</span></div><div class="card-title">Executive Summary</div><div class="card-desc">High-level performance overview and key takeaways.</div><span class="dest-pill dest-ppt"><span class="swatch">&#9632;</span>PowerPoint</span></div>
                    <div class="card" data-nl-panel="nl-xponent"><div class="card-top"><span class="icon-chip chip-s2"><svg viewBox="0 0 24 24"><path d="M3 17l6-6 4 4 8-8M14 7h7v7"/></svg></span><span class="badge weekly">Weekly</span></div><div class="card-title">Xponent Trends</div><div class="card-desc">Weekly Xponent data trends and brand performance.</div><span class="dest-pill dest-ppt"><span class="swatch">&#9632;</span>PowerPoint</span></div>
                    <div class="card" data-nl-panel="nl-market"><div class="card-top"><span class="icon-chip chip-s2"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg></span><span class="badge weekly">Weekly</span></div><div class="card-title">Market Insights</div><div class="card-desc">Competitive landscape and market share dynamics.</div><span class="dest-pill dest-ppt"><span class="swatch">&#9632;</span>PowerPoint</span></div>
                    <div class="card" data-nl-panel="nl-access"><div class="card-top"><span class="icon-chip chip-s2"><svg viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m5-2a9 9 0 11-4.219-7.619"/></svg></span><span class="badge weekly">Weekly</span></div><div class="card-title">Access Changes</div><div class="card-desc">Payer access updates and formulary change tracking.</div><span class="dest-pill dest-ppt"><span class="swatch">&#9632;</span>PowerPoint</span></div>
                    <a class="card" href="https://dss-amer-design.pfizer.com/webapps/MIGRAINEDOPPLR/zXimTdd/" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s2"><svg viewBox="0 0 24 24"><path d="M10 5a2 2 0 114 0v1a7 7 0 014 6v4l2 2H4l2-2v-4a7 7 0 014-6V5z"/><path d="M9 17v1a3 3 0 006 0v-1"/></svg></span><span class="badge weekly">Weekly</span></div><div class="card-title">DOppLR Alerts</div><div class="card-desc">Predictive alerts for market momentum shifts.</div><span class="dest-pill dest-ppt"><span class="swatch">&#9632;</span>PowerPoint</span></a>
                    <div class="card" data-nl-panel="nl-financial"><div class="card-top"><span class="icon-chip chip-s2"><svg viewBox="0 0 24 24"><path d="M5 21V5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3-7 3z"/></svg></span><span class="badge weekly">Weekly</span></div><div class="card-title">Financial Summary</div><div class="card-desc">Weekly financial metrics and revenue tracking.</div><span class="dest-pill dest-xlsx"><span class="swatch">&#9632;</span>Excel</span></div>
                </div>
            </div>
            <!-- Deep-dive sub-panels (shown when a card is clicked) -->
            <div id="nl-deepdive-view" style="display:none;">
<style>
.nl-content .card { background: white; border: 1px solid #e5e7eb; border-radius: 10px; padding: 20px; margin-bottom: 16px; min-height: auto; box-shadow: none; cursor: default; }
.nl-content .card:hover { transform: none; box-shadow: none; }
.nl-content .card::after { display: none; }
.nl-content .card-title { font-size: 17px; font-weight: 700; margin-bottom: 6px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1a2332; }
.nl-content .card-subtitle { font-size: 12px; color: #4b5563; margin-bottom: 16px; }
.nl-content .row { display: flex; gap: 16px; margin-bottom: 16px; }
.nl-content .row > * { flex: 1; }
.nl-content .stat-tile { background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; padding: 16px; }
.nl-content .stat-tile .label { font-size: 10px; color: #6b7280; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }
.nl-content .stat-tile .value { font-size: 28px; font-weight: 700; color: #1a2332; }
.nl-content .stat-tile .sub { font-size: 11px; color: #6b7280; margin-top: 4px; }
.nl-content table { width: 100%; border-collapse: collapse; font-size: 12px; }
.nl-content th { text-align: left; padding: 10px 12px; border-bottom: 2px solid #e5e7eb; font-size: 10px; text-transform: uppercase; color: #6b7280; letter-spacing: 0.5px; font-weight: 600; }
.nl-content td { padding: 10px 12px; border-bottom: 1px solid #f3f4f6; }
.nl-content tr:last-child td { border-bottom: none; }
.nl-content .pill-group { display: flex; gap: 0; margin-bottom: 16px; }
.nl-content .pill { padding: 8px 16px; border: 1px solid #e5e7eb; cursor: pointer; font-size: 12px; font-weight: 500; background: white; }
.nl-content .pill:first-child { border-radius: 6px 0 0 6px; }
.nl-content .pill:last-child { border-radius: 0 6px 6px 0; }
.nl-content .pill.active { background: #dc2626; color: white; border-color: #dc2626; }
.nl-content .pill-sm { padding: 6px 12px; font-size: 11px; }
.nl-content .chart-container { position: relative; width: 100%; height: 280px; margin: 16px 0; margin-left: -20px; margin-right: -20px; width: calc(100% + 40px); }
.nl-content .chart-container-sm { height: 220px; margin-left: -20px; margin-right: -20px; width: calc(100% + 40px); }
.nl-content svg.chart { width: 100%; height: 100%; }
.nl-content svg.chart text { fill: #4b5563 !important; font-weight: 500 !important; font-size: 10px !important; }
.nl-content .legend { display: flex; gap: 16px; justify-content: center; margin-top: 8px; font-size: 11px; flex-wrap: wrap; }
.nl-content .axis-info { display: flex; justify-content: space-between; font-size: 9px; font-weight: 500; color: #6b7280; margin-top: 4px; margin-bottom: 6px; padding: 0 8px; }
.nl-content .axis-info span { font-style: italic; }
.nl-content .axis-label { font-size: 10px; font-weight: 600; color: #4b5563; text-align: center; margin-top: -8px; margin-bottom: 8px; }
.nl-content .legend-item { display: flex; align-items: center; gap: 6px; }
.nl-content .legend-dot { width: 8px; height: 8px; border-radius: 50%; }
.nl-content .brand-header { padding: 10px 16px; border-radius: 6px; margin-bottom: 12px; color: white; font-size: 12px; font-weight: 600; display: flex; gap: 16px; }
.nl-content .brand-header.brand-a { background: #1e3a5f; }
.nl-content .brand-header.brand-b { background: #6b21a8; }
.nl-content .brand-header.brand-c { background: #0f766e; }
.nl-content .insight-bullet { display: flex; gap: 10px; margin-bottom: 12px; align-items: flex-start; }
.nl-content .insight-dot { width: 8px; height: 8px; border-radius: 50%; background: #f59e0b; margin-top: 4px; flex-shrink: 0; }
.nl-content .alert-item { display: flex; gap: 10px; margin-bottom: 14px; align-items: flex-start; }
.nl-content .alert-icon { width: 20px; height: 20px; flex-shrink: 0; }
.nl-content .alert-signal { font-weight: 600; font-size: 12px; }
.nl-content .alert-anchor { font-size: 11px; color: #6b7280; }
.nl-content .badge { padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: 600; }
.nl-content .badge-gain { background: #dcfce7; color: #166534; }
.nl-content .badge-loss { background: #fee2e2; color: #991b1b; }
.nl-content .badge-restriction { background: #fef3c7; color: #92400e; }
.nl-content .delta-pos { color: #16a34a; }
.nl-content .delta-neg { color: #dc2626; }
.nl-content .card-header-row { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px; }
.nl-content .footnote { font-size: 10px; color: #9ca3af; margin-top: 12px; padding-top: 8px; border-top: 1px solid #f3f4f6; }
.nl-content .split-section { display: flex; gap: 24px; margin-bottom: 16px; }
.nl-content .split-section > .split-col { flex: 1; min-width: 0; }
.nl-content .split-col .section-label { font-size: 13px; font-weight: 700; margin-bottom: 12px; color: #1a2332; text-align: center; }
.nl-content .filter-select { padding: 6px 12px; border: 1px solid #d1d5db; border-radius: 6px; font-size: 11px; background: white; }
.nl-content .sub-signal-table td { padding: 6px 12px; font-size: 11px; }
.nl-content .nl-tab { display: none; }
.nl-content .nl-tab.active { display: block; }
</style>
<div class="nl-content">
<div class="nl-tab active" id="nl-exec-tab">
<div style="padding:8px 32px 24px;">
<div class="section-head"><h2>Executive Summary</h2><p>High-level performance overview and key takeaways for the current reporting week.</p></div>
    <div class="card">
      <div class="card-title">Performance Snapshot</div>
      <div class="card-subtitle">Week ending 06/19/2026 · National</div>
      <table>
        <thead>
          <tr><th>METRIC</th><th style="text-align:right">LATEST WK</th><th style="text-align:right">YTD</th><th style="text-align:right">VS. GOAL</th><th style="text-align:right">VS. STLY</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>Nurtec NBRx</strong></td><td style="text-align:right">48.2K</td><td style="text-align:right">1.21M</td><td style="text-align:right">97.8%</td><td style="text-align:right"><span class="delta-pos">+11.3%</span></td></tr>
          <tr><td><strong>Nurtec NRx</strong></td><td style="text-align:right">112.6K</td><td style="text-align:right">2.85M</td><td style="text-align:right">95.1%</td><td style="text-align:right"><span class="delta-pos">+14.2%</span></td></tr>
          <tr><td><strong>Nurtec TRx</strong></td><td style="text-align:right">612.4K</td><td style="text-align:right">15.9M</td><td style="text-align:right">93.6%</td><td style="text-align:right"><span class="delta-pos">+16.1%</span></td></tr>
          <tr><td><strong>Nurtec NBRx Share</strong></td><td style="text-align:right">21.2%</td><td style="text-align:right">20.9%</td><td style="text-align:right">—</td><td style="text-align:right"><span class="delta-pos">+1.3%</span></td></tr>
          <tr><td><strong>Nurtec NRx Share</strong></td><td style="text-align:right">33.4%</td><td style="text-align:right">33.0%</td><td style="text-align:right">—</td><td style="text-align:right"><span class="delta-pos">+1.1%</span></td></tr>
          <tr><td><strong>Nurtec TRx Share</strong></td><td style="text-align:right">38.7%</td><td style="text-align:right">38.1%</td><td style="text-align:right">—</td><td style="text-align:right"><span class="delta-pos">+1.4%</span></td></tr>
        </tbody>
      </table>
    </div>

    <div class="card">
        <div class="card-title">Weekly Insight Bullets</div>
        <div class="card-subtitle">Key performance highlights for the current reporting week</div>
        <div class="insight-bullet">
          <div class="insight-dot"></div>
          <div><strong>Financial performance:</strong> Gross sales at 101.0% vs. LE2 for P6 PTD and 103.3% vs. LE2 for Q2 QTD.</div>
        </div>
        <div class="insight-bullet">
          <div class="insight-dot"></div>
          <div><strong>As of May 29, Nurtec TRx growth is 16.1% YTD</strong> which is 2.2% higher compared to same time point in 2025.</div>
        </div>
        <div class="insight-bullet">
          <div class="insight-dot"></div>
          <div><strong>oCGRP market TRx YTD growth:</strong> 17.1%</div>
        </div>
        <div class="insight-bullet">
          <div class="insight-dot"></div>
          <div><strong>Competition TRx YTD growth:</strong> Ubrelvy 14.4%; Qulipta 22.5%</div>
        </div>
        <div class="insight-bullet">
          <div class="insight-dot"></div>
          <div><strong>Nurtec market share performance:</strong> TRx YTD: 42.6%; NRx YTD: 42.7%</div>
        </div>
        <div class="insight-bullet">
          <div class="insight-dot"></div>
          <div><strong>vs Budget:</strong> Nurtec TRx is 93.5% YTD; oCGRP TRx is 94.3% YTD</div>
        </div>
        <div class="insight-bullet">
          <div class="insight-dot"></div>
          <div><strong>Weekly channel performance (5/22):</strong> TRx share higher (0.2%) for the week vs same time period last year</div>
        </div>
      </div>

    <div class="row">
      <div class="card">
        <div class="card-title">Access Change Lines</div>
        <div class="card-subtitle">Only appears with material weekly access changes</div>
        <div style="margin-bottom:10px;"><strong>Louisiana Medicaid</strong><br><span style="color:#6b7280">Nurtec removed from PDL · est. -2,200 NRx</span></div>
        <div><strong>UnitedHealth Commercial (IL)</strong><br><span style="color:#6b7280">PA requirement added · 820K covered lives</span></div>
      </div>

      <div class="card">
        <div class="card-title">Weekly Gross Sales</div>
        <div class="card-subtitle">Pending Finance feed alignment (Chris Marino)</div>
        <div style="margin-bottom:4px;font-size:10px;color:#6b7280;">GROSS SALES W/E 06/19</div>
        <div style="font-size:28px;font-weight:700;">$28.4M <span class="badge" style="background:#dcfce7;color:#166534;font-size:11px;vertical-align:middle;">+2.8%</span></div>
        <div style="font-size:11px;color:#6b7280;margin-bottom:16px;">vs. $27.6M prior week</div>
        <hr style="border:none;border-top:1px solid #e5e7eb;margin:12px 0;">
        <div style="font-size:10px;color:#6b7280;">YTD ATTAINMENT VS OP26</div>
        <div style="font-size:24px;font-weight:700;">93.6%</div>
        <div style="font-size:11px;color:#6b7280;">$112K behind pace</div>
      </div>

      
    </div>

    

  </div>
</div>
<div class="nl-tab" id="nl-xponent-tab">
<div style="padding:8px 32px 24px;">
<div class="section-head"><h2>Xponent Trends</h2><p>Weekly Xponent data trends, segment and channel performance analysis.</p></div>
    <div class="card">
      <div class="card-title">Claims MTD & YTD vs. STLY</div>
      <div class="card-subtitle">Nurtec NRx and TRx claim counts</div>
      
    

<div class="row">
        <div class="stat-tile"><div class="label">NRX MTD</div><div class="value">486K</div><div class="sub delta-pos">+15.6%</div></div>
        <div class="stat-tile"><div class="label">NRX YTD</div><div class="value">2.85M</div><div class="sub delta-pos">+16.1%</div></div>
        <div class="stat-tile"><div class="label">TRX MTD</div><div class="value">2.41M</div><div class="sub delta-pos">+16.5%</div></div>
        <div class="stat-tile"><div class="label">TRX YTD</div><div class="value">15.9M</div><div class="sub delta-pos">+16.1%</div></div>
      </div>
    </div>

    <div class="card" style="background:#f8fafd; border:1px solid rgba(15,23,42,0.06); padding:20px 24px;">
      <div class="pill-group" id="xponent-metric-toggle" style="margin-bottom:16px;">
        <div class="pill pill-sm active" id="xp-trx-pill" onclick="switchXponentMetric('trx')">TRx</div>
        <div class="pill pill-sm" id="xp-nrx-pill" onclick="switchXponentMetric('nrx')">NRx</div>
      </div>
      <div class="row" style="margin-bottom:0;">
      
      <div class="card">
        <div class="card-title" data-xp-metric="{XM} Share Trend by Segment">TRx Share Trend by Segment</div>
        <div class="card-subtitle">Commercial / Medicare / Medicaid / Other · weekly</div>
        <div class="chart-container chart-container-sm">
          <svg class="chart" preserveAspectRatio="none" viewBox="0 0 380 200">
            <line x1="40" y1="180" x2="370" y2="180" stroke="#e5e7eb" stroke-width="1"/>
            <line x1="40" y1="140" x2="370" y2="140" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
            <line x1="40" y1="100" x2="370" y2="100" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
            <line x1="40" y1="60" x2="370" y2="60" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
            <text x="35" y="184" text-anchor="end" font-size="9" fill="#9ca3af">0%</text>
            <text x="35" y="144" text-anchor="end" font-size="9" fill="#9ca3af">10%</text>
            <text x="35" y="104" text-anchor="end" font-size="9" fill="#9ca3af">20%</text>
            <text x="35" y="64" text-anchor="end" font-size="9" fill="#9ca3af">30%</text>
            <text x="35" y="24" text-anchor="end" font-size="9" fill="#9ca3af">40%</text>
            <polyline fill="none" stroke="#3b82f6" stroke-width="2" points="50,72 75,70 100,68 125,67 150,66 175,64 200,63 225,62 250,61 275,60 300,59 325,58 350,57"/>
            <polyline fill="none" stroke="#16a34a" stroke-width="2" points="50,95 75,94 100,93 125,92 150,91 175,90 200,89 225,88 250,87 275,87 300,86 325,86 350,85"/>
            <polyline fill="none" stroke="#f59e0b" stroke-width="2" points="50,135 75,134 100,133 125,132 150,132 175,131 200,130 225,130 250,129 275,128 300,128 325,127 350,127"/>
            <polyline fill="none" stroke="#9ca3af" stroke-width="2" points="50,148 75,148 100,147 125,147 150,147 175,146 200,146 225,146 250,145 275,145 300,145 325,144 350,144"/>
            <text x="50" y="196" font-size="8" fill="#9ca3af">Wk 1</text>
            <text x="130" y="196" font-size="8" fill="#9ca3af">Wk 6</text>
            <text x="210" y="196" font-size="8" fill="#9ca3af">Wk 11</text>
            <text x="290" y="196" font-size="8" fill="#9ca3af">Wk 16</text>
            <text x="350" y="196" font-size="8" fill="#9ca3af"></text>
          </svg>
        </div>
        <div class="axis-info"><span>Y-Axis: TRx Share %</span><span>X-Axis: Time Period (Week)</span></div>
        <div class="legend" style="font-size:10px;">
          <div class="legend-item"><div class="legend-dot" style="background:#3b82f6"></div>Commercial</div>
          <div class="legend-item"><div class="legend-dot" style="background:#16a34a"></div>Medicare</div>
          <div class="legend-item"><div class="legend-dot" style="background:#f59e0b"></div>Medicaid</div>
          <div class="legend-item"><div class="legend-dot" style="background:#9ca3af"></div>Other</div>
        </div>
      </div>

      <div class="card">
        <div class="card-title" data-xp-metric="{XM} Share by Channel">TRx Share by Channel</div>
        <div class="card-subtitle">Retail / Mail-Order / LTC · weekly</div>
        <div class="chart-container chart-container-sm">
          <svg class="chart" preserveAspectRatio="none" viewBox="0 0 380 200">
            <line x1="40" y1="180" x2="370" y2="180" stroke="#e5e7eb" stroke-width="1"/>
            <line x1="40" y1="140" x2="370" y2="140" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
            <line x1="40" y1="100" x2="370" y2="100" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
            <line x1="40" y1="60" x2="370" y2="60" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
            <text x="35" y="184" text-anchor="end" font-size="9" fill="#9ca3af">0%</text>
            <text x="35" y="144" text-anchor="end" font-size="9" fill="#9ca3af">20%</text>
            <text x="35" y="104" text-anchor="end" font-size="9" fill="#9ca3af">40%</text>
            <text x="35" y="64" text-anchor="end" font-size="9" fill="#9ca3af">60%</text>
            <text x="35" y="24" text-anchor="end" font-size="9" fill="#9ca3af">80%</text>
            <polyline fill="none" stroke="#0891b2" stroke-width="2" points="50,55 75,54 100,53 125,52 150,51 175,50 200,50 225,49 250,49 275,48 300,48 325,47 350,47"/>
            <polyline fill="none" stroke="#7c3aed" stroke-width="2" points="50,120 75,119 100,118 125,117 150,116 175,115 200,114 225,114 250,113 275,112 300,112 325,111 350,111"/>
            <polyline fill="none" stroke="#9ca3af" stroke-width="2" points="50,145 75,145 100,144 125,144 150,144 175,143 200,143 225,143 250,142 275,142 300,142 325,142 350,141"/>
            <text x="50" y="196" font-size="8" fill="#9ca3af">Wk 1</text>
            <text x="130" y="196" font-size="8" fill="#9ca3af">Wk 6</text>
            <text x="210" y="196" font-size="8" fill="#9ca3af">Wk 11</text>
            <text x="290" y="196" font-size="8" fill="#9ca3af">Wk 16</text>
            <text x="350" y="196" font-size="8" fill="#9ca3af"></text>
          </svg>
        </div>
        <div class="axis-info"><span>Y-Axis: TRx Share %</span><span>X-Axis: Time Period (Week)</span></div>
        <div class="legend" style="font-size:10px;">
          <div class="legend-item"><div class="legend-dot" style="background:#0891b2"></div>Retail</div>
          <div class="legend-item"><div class="legend-dot" style="background:#7c3aed"></div>Mail-Order</div>
          <div class="legend-item"><div class="legend-dot" style="background:#9ca3af"></div>LTC</div>
        </div>
      </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">Payer Performance</div>
      <div class="card-subtitle">NRx & TRx share % · Latest Wk / WoW pp / MTD / vs. STLY / vs. Budget</div>
      <table>
        <thead>
          <tr><th>CUT</th><th style="text-align:right">NRX %</th><th style="text-align:right">WoW %</th><th style="text-align:right">TRX %</th><th style="text-align:right">WoW %</th><th style="text-align:right">MTD TRX</th><th style="text-align:right">VS STLY</th><th style="text-align:right">VS BUDGET</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>National</strong></td><td style="text-align:right">33.4%</td><td style="text-align:right"><span class="delta-pos">+0.2%</span></td><td style="text-align:right">38.7%</td><td style="text-align:right"><span class="delta-pos">+0.1%</span></td><td style="text-align:right">38.5%</td><td style="text-align:right"><span class="delta-pos">+1.4%</span></td><td style="text-align:right"><span class="delta-neg">-1.1%</span></td></tr>
          <tr><td><strong>Commercial</strong></td><td style="text-align:right">36.1%</td><td style="text-align:right"><span class="delta-pos">+0.3%</span></td><td style="text-align:right">41.2%</td><td style="text-align:right"><span class="delta-pos">+0.2%</span></td><td style="text-align:right">41.0%</td><td style="text-align:right"><span class="delta-pos">+1.8%</span></td><td style="text-align:right"><span class="delta-neg">-0.6%</span></td></tr>
          <tr><td><strong>Medicare</strong></td><td style="text-align:right">31.4%</td><td style="text-align:right"><span class="delta-pos">+0.1%</span></td><td style="text-align:right">36.5%</td><td style="text-align:right"><span class="delta-pos">+0.1%</span></td><td style="text-align:right">36.3%</td><td style="text-align:right"><span class="delta-pos">+2.1%</span></td><td style="text-align:right"><span class="delta-neg">-0.4%</span></td></tr>
          <tr><td><strong>Medicaid</strong></td><td style="text-align:right">22.8%</td><td style="text-align:right"><span class="delta-neg">-0.4%</span></td><td style="text-align:right">26.4%</td><td style="text-align:right"><span class="delta-neg">-0.3%</span></td><td style="text-align:right">26.5%</td><td style="text-align:right"><span class="delta-neg">-0.7%</span></td><td style="text-align:right"><span class="delta-neg">-2.4%</span></td></tr>
          <tr><td><strong>Other</strong></td><td style="text-align:right">19.6%</td><td style="text-align:right"><span class="delta-pos">+0.0%</span></td><td style="text-align:right">22.1%</td><td style="text-align:right"><span class="delta-pos">+0.0%</span></td><td style="text-align:right">22.0%</td><td style="text-align:right"><span class="delta-pos">+0.4%</span></td><td style="text-align:right"><span class="delta-neg">-1.2%</span></td></tr>
        </tbody>
      </table>
    </div>

    <div class="card">
      <div class="card-title">Channel Performance</div>
      <div class="card-subtitle">NRx & TRx share % · Latest Wk / WoW pp / MTD / vs. STLY / vs. Budget</div>
      <table>
        <thead>
          <tr><th>CUT</th><th style="text-align:right">NRX %</th><th style="text-align:right">WoW %</th><th style="text-align:right">TRX %</th><th style="text-align:right">WoW %</th><th style="text-align:right">MTD TRX</th><th style="text-align:right">VS STLY</th><th style="text-align:right">VS BUDGET</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>National</strong></td><td style="text-align:right">33.4%</td><td style="text-align:right"><span class="delta-pos">+0.2%</span></td><td style="text-align:right">38.7%</td><td style="text-align:right"><span class="delta-pos">+0.1%</span></td><td style="text-align:right">38.5%</td><td style="text-align:right"><span class="delta-pos">+1.4%</span></td><td style="text-align:right"><span class="delta-neg">-1.1%</span></td></tr>
          <tr><td><strong>Retail</strong></td><td style="text-align:right">34.0%</td><td style="text-align:right"><span class="delta-pos">+0.2%</span></td><td style="text-align:right">39.4%</td><td style="text-align:right"><span class="delta-pos">+0.1%</span></td><td style="text-align:right">39.2%</td><td style="text-align:right"><span class="delta-pos">+1.5%</span></td><td style="text-align:right"><span class="delta-neg">-1.0%</span></td></tr>
          <tr><td><strong>Mail-Order</strong></td><td style="text-align:right">27.6%</td><td style="text-align:right"><span class="delta-pos">+0.4%</span></td><td style="text-align:right">31.8%</td><td style="text-align:right"><span class="delta-pos">+0.3%</span></td><td style="text-align:right">31.6%</td><td style="text-align:right"><span class="delta-pos">+2.3%</span></td><td style="text-align:right"><span class="delta-pos">+0.2%</span></td></tr>
          <tr><td><strong>LTC</strong></td><td style="text-align:right">18.2%</td><td style="text-align:right"><span class="delta-neg">-0.1%</span></td><td style="text-align:right">21.4%</td><td style="text-align:right"><span class="delta-neg">-0.1%</span></td><td style="text-align:right">21.5%</td><td style="text-align:right"><span class="delta-neg">-0.3%</span></td><td style="text-align:right"><span class="delta-neg">-1.6%</span></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
<div class="nl-tab" id="nl-market-tab">
<div style="padding:8px 32px 24px;">
<div class="section-head"><h2>NPA Performance</h2><p>National prescription audit competitive view across Oral CGRP brands.</p></div>
    <div class="pill-group" id="npa-subtabs">
      <div class="pill active" onclick="switchNpaSubtab('retail')">NPA Overall</div>
      <div class="pill" onclick="switchNpaSubtab('acute-prev')">NPA Acute / Preventive Split</div>
    </div>

    <!-- NPA Retail Sub-tab -->
    <div id="npa-retail">
      <div class="pill-group" style="margin-bottom:16px;">
        <div class="pill pill-sm active" id="npa-trx-pill" onclick="toggleNpaMetric('trx')">TRx</div>
        <div class="pill pill-sm" id="npa-nbrx-pill" onclick="toggleNpaMetric('nbrx')">NBRx</div>
      </div>
      <div class="card">
        <div class="card-header-row">
          <div>
            <div class="card-title" data-metric-toggle="Nurtec NPA — Brand Competitive View ({M})">Nurtec NPA — Brand Competitive View (TRx)</div>
            <div class="card-subtitle">National · IQVIA NPA · Actuals 2026 vs Actuals 2025 (Same Time Last Year)</div>
          </div>
          
        </div>
        <div class="chart-container">
          <svg class="chart" preserveAspectRatio="none" viewBox="0 0 800 250">
            <line x1="60" y1="220" x2="780" y2="220" stroke="#e5e7eb" stroke-width="1"/>
            <line x1="60" y1="170" x2="780" y2="170" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
            <line x1="60" y1="120" x2="780" y2="120" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
            <line x1="60" y1="70" x2="780" y2="70" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
            <line x1="60" y1="20" x2="780" y2="20" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
            <text x="50" y="224" text-anchor="end" font-size="10" fill="#9ca3af">0K</text>
            <text x="50" y="174" text-anchor="end" font-size="10" fill="#9ca3af">20K</text>
            <text x="50" y="124" text-anchor="end" font-size="10" fill="#9ca3af">40K</text>
            <text x="50" y="74" text-anchor="end" font-size="10" fill="#9ca3af">60K</text>
            <text x="50" y="24" text-anchor="end" font-size="10" fill="#9ca3af">80K</text>
            <polyline fill="none" stroke="#16a34a" stroke-width="2" points="80,35 108,38 136,36 164,40 192,38 220,42 248,40 276,38 304,36 332,35 360,34 388,33 416,32 444,30 472,28 500,27 528,26 556,25 584,24 612,23 640,22 668,22 696,21 724,20 752,20"/>
            <polyline fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="6" points="80,55 108,58 136,56 164,60 192,58 220,62 248,60 276,58 304,56 332,55 360,54 388,53 416,52 444,52 472,51 500,50 528,50 556,49 584,48 612,48 640,47 668,47 696,46 724,46 752,45"/>
            <polyline fill="none" stroke="#f59e0b" stroke-width="2" points="80,100 108,102 136,100 164,104 192,102 220,105 248,103 276,104 304,102 332,103 360,104 388,103 416,104 444,105 472,104 500,105 528,106 556,105 584,106 612,107 640,106 668,107 696,108 724,108 752,108"/>
            <polyline fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6" points="80,110 108,112 136,110 164,113 192,112 220,114 248,113 276,114 304,113 332,114 360,115 388,115 416,116 444,116 472,117 500,117 528,118 556,118 584,119 612,119 640,120 668,120 696,121 724,121 752,121"/>
            <polyline fill="none" stroke="#3b82f6" stroke-width="2" points="80,145 108,147 136,148 164,150 192,152 220,154 248,155 276,157 304,158 332,160 360,161 388,162 416,163 444,164 472,165 500,166 528,167 556,168 584,169 612,170 640,170 668,171 696,171 724,172 752,172"/>
            <polyline fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="6" points="80,160 108,162 136,163 164,164 192,166 220,167 248,168 276,170 304,171 332,172 360,173 388,174 416,175 444,176 472,177 500,178 528,178 556,179 584,180 612,180 640,181 668,181 696,182 724,182 752,182"/>
            <text x="80" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 1</text>
            <text x="192" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 5</text>
            <text x="304" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 9</text>
            <text x="416" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 13</text>
            <text x="528" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 17</text>
            <text x="640" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 21</text>
            <text x="752" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 26</text>
          
            <!-- Goal line -->
            <polyline fill="none" stroke="#f472b6" stroke-width="2" stroke-dasharray="8,4" points="80,88 108,88 136,87 164,87 192,86 220,86 248,85 276,85 304,84 332,84 360,83 388,83 416,82 444,82 472,81 500,81 528,80 556,80 584,79 612,79 640,78 668,78 696,77 724,77 752,76"/>
          </svg>
        </div>
        <div class="axis-info"><span>Y-Axis: TRx Volume (K)</span><span>X-Axis: Time Period (Week)</span></div>
        <div class="legend">
          <div class="legend-item"><div class="legend-dot" style="background:#16a34a"></div>Nurtec Actuals</div>
          <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#16a34a" stroke-width="2" stroke-dasharray="3"/></svg>Nurtec STLY</div>
          <div class="legend-item"><div class="legend-dot" style="background:#f59e0b"></div>Ubrelvy Actuals</div>
          <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3"/></svg>Ubrelvy STLY</div>
          <div class="legend-item"><div class="legend-dot" style="background:#3b82f6"></div>Qulipta Actuals</div>
          <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#3b82f6" stroke-width="2" stroke-dasharray="3"/></svg>Qulipta STLY</div>
          <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#f472b6" stroke-width="2" stroke-dasharray="4,2"/></svg>Goal</div>
        </div>
        
        <div class="footnote">Time period reference: Actuals 2026 w.e. 06/05/2026 · Same Time Last Year w.e. 06/06/2025</div>
      </div>

      <div class="card">
        <div class="card-header-row">
          <div>
            <div class="card-title" data-metric-toggle="Nurtec NPA — Channel Performance View ({M})">Nurtec NPA — Channel Performance View (TRx)</div>
            <div class="card-subtitle">National · IQVIA NPA · Retail / Mail-Order / LTC · Actuals 2026 vs Actuals 2025 (STLY)</div>
          </div>
          <div class="pill-group" style="margin-bottom:0;">
            <div class="pill pill-sm active" id="channel-nurtec" onclick="switchChannelBrand('nurtec')">Nurtec</div>
            <div class="pill pill-sm" id="channel-ubrelvy" onclick="switchChannelBrand('ubrelvy')">Ubrelvy</div>
            <div class="pill pill-sm" id="channel-qulipta" onclick="switchChannelBrand('qulipta')">Qulipta</div>
          </div>
        
        </div>
        <div class="chart-container">
          <svg class="chart" preserveAspectRatio="none" viewBox="-10 0 810 250">
            <line x1="40" y1="220" x2="790" y2="220" stroke="#e5e7eb" stroke-width="1"/>
            <line x1="40" y1="170" x2="790" y2="170" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
            <line x1="40" y1="120" x2="790" y2="120" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
            <line x1="40" y1="70" x2="790" y2="70" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
            <line x1="40" y1="20" x2="790" y2="20" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
            <text x="30" y="224" text-anchor="end" font-size="10" fill="#9ca3af">0K</text>
            <text x="30" y="174" text-anchor="end" font-size="10" fill="#9ca3af">20K</text>
            <text x="30" y="124" text-anchor="end" font-size="10" fill="#9ca3af">40K</text>
            <text x="30" y="74" text-anchor="end" font-size="10" fill="#9ca3af">60K</text>
            <text x="30" y="24" text-anchor="end" font-size="10" fill="#9ca3af">80K</text>
            <!-- Retail Actuals (solid) -->
            <polyline fill="none" stroke="#0891b2" stroke-width="2" points="60,40 88,42 116,40 144,38 172,36 200,35 228,34 256,33 284,32 312,30 340,29 368,28 396,27 424,26 452,25 480,24 508,23 536,22 564,22 592,21 620,20 648,20 676,19 704,19 732,18"/>
            <!-- Retail STLY (dashed) -->
            <polyline fill="none" stroke="#0891b2" stroke-width="2" stroke-dasharray="6" points="60,55 88,57 116,55 144,53 172,52 200,50 228,49 256,48 284,47 312,46 340,45 368,44 396,43 424,42 452,42 480,41 508,40 536,40 564,39 592,39 620,38 648,38 676,37 704,37 732,36"/>
            <!-- Mail-Order Actuals (solid) -->
            <polyline fill="none" stroke="#7c3aed" stroke-width="2" points="60,130 88,128 116,126 144,125 172,123 200,122 228,120 256,118 284,117 312,115 340,114 368,112 396,111 424,110 452,108 480,107 508,106 536,105 564,104 592,103 620,102 648,101 676,100 704,99 732,98"/>
            <!-- Mail-Order STLY (dashed) -->
            <polyline fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="6" points="60,142 88,140 116,139 144,138 172,136 200,135 228,134 256,133 284,132 312,131 340,130 368,129 396,128 424,128 452,127 480,126 508,126 536,125 564,125 592,124 620,124 648,123 676,123 704,122 732,122"/>
            <!-- LTC Actuals (solid) -->
            <polyline fill="none" stroke="#9ca3af" stroke-width="2" points="60,175 88,176 116,177 144,178 172,178 200,179 228,179 256,180 284,180 312,181 340,181 368,182 396,182 424,183 452,183 480,184 508,184 536,184 564,185 592,185 620,185 648,186 676,186 704,186 732,187"/>
            <!-- LTC STLY (dashed) -->
            <polyline fill="none" stroke="#9ca3af" stroke-width="2" stroke-dasharray="6" points="60,180 88,181 116,181 144,182 172,182 200,183 228,183 256,184 284,184 312,184 340,185 368,185 396,185 424,186 452,186 480,186 508,187 536,187 564,187 592,187 620,188 648,188 676,188 704,188 732,188"/>
            <text x="60" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 1</text>
            <text x="172" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 5</text>
            <text x="284" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 9</text>
            <text x="396" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 13</text>
            <text x="508" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 17</text>
            <text x="620" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 21</text>
            <text x="732" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 26</text>
          
            <!-- Goal line -->
            <polyline fill="none" stroke="#f472b6" stroke-width="2" stroke-dasharray="8,4" points="60,92 88,91 116,90 144,89 172,88 200,87 228,86 256,85 284,84 312,83 340,82 368,81 396,80 424,79 452,78 480,77 508,76 536,75 564,74 592,73 620,72 648,71 676,70 704,69 732,68"/>
          </svg>
        </div>
        <div class="axis-info"><span>Y-Axis: TRx Volume (K)</span><span>X-Axis: Time Period (Week)</span></div>
        <div class="legend">
          <div class="legend-item"><div class="legend-dot" style="background:#0891b2"></div>Retail Actuals</div>
          <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#0891b2" stroke-width="2" stroke-dasharray="3"/></svg>Retail STLY</div>
          <div class="legend-item"><div class="legend-dot" style="background:#7c3aed"></div>Mail-Order Actuals</div>
          <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#7c3aed" stroke-width="2" stroke-dasharray="3"/></svg>Mail-Order STLY</div>
          <div class="legend-item"><div class="legend-dot" style="background:#9ca3af"></div>LTC Actuals</div>
          <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#9ca3af" stroke-width="2" stroke-dasharray="3"/></svg>LTC STLY</div>
          <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#f472b6" stroke-width="2" stroke-dasharray="4,2"/></svg>Goal</div>
        </div>
        <div class="footnote">Time period reference: Actuals 2026 w.e. 06/05/2026 · Same Time Last Year w.e. 06/06/2025</div>
      </div>

      <div class="brand-header brand-a"><span>NURTEC</span><span style="font-weight:400;margin-left:12px;" data-metric-toggle="{M} Volume · Growth (vs STLY) · oCGRP Market Share %">TRx Volume · Growth (vs STLY) · oCGRP Market Share %</span></div>
      <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
        <table>
          <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">QTD %</th><th style="text-align:right">YTD %</th><th style="text-align:right">WK MS</th><th style="text-align:right">QTD MS</th><th style="text-align:right">YTD MS</th></tr></thead>
          <tbody>
            <tr><td>Actuals '26</td><td style="text-align:right">82,914</td><td style="text-align:right">771,205</td><td style="text-align:right">1,718,623</td><td style="text-align:right"><span class="delta-pos">+18.6%</span></td><td style="text-align:right"><span class="delta-pos">+17.9%</span></td><td style="text-align:right"><span class="delta-pos">+17.4%</span></td><td style="text-align:right">44.1%</td><td style="text-align:right">43.8%</td><td style="text-align:right">43.6%</td></tr>
            <tr><td>Actuals '25</td><td style="text-align:right">69,912</td><td style="text-align:right">654,108</td><td style="text-align:right">1,464,331</td><td style="text-align:right"><span class="delta-pos">+13.5%</span></td><td style="text-align:right"><span class="delta-pos">+12.2%</span></td><td style="text-align:right"><span class="delta-pos">+14.3%</span></td><td style="text-align:right">43.6%</td><td style="text-align:right">43.4%</td><td style="text-align:right">43.3%</td></tr>
            <tr><td>Latest Goal OP'26</td><td style="text-align:right">85,326</td><td style="text-align:right">798,471</td><td style="text-align:right">1,832,540</td><td style="text-align:right"><span class="delta-pos">+22.0%</span></td><td style="text-align:right"><span class="delta-pos">+24.2%</span></td><td style="text-align:right"><span class="delta-pos">+25.1%</span></td><td style="text-align:right">—</td><td style="text-align:right">—</td><td style="text-align:right">—</td></tr>
            <tr><td>Goal Attainment '26</td><td style="text-align:right">97.2%</td><td style="text-align:right">96.6%</td><td style="text-align:right">93.8%</td><td style="text-align:right">—</td><td style="text-align:right">—</td><td style="text-align:right">—</td><td style="text-align:right">—</td><td style="text-align:right">—</td><td style="text-align:right">—</td></tr>
          </tbody>
        </table>
      </div>

      <div class="brand-header brand-b" style="margin-top:16px;"><span>UBRELVY</span><span style="font-weight:400;margin-left:12px;" data-metric-toggle="{M} Volume · Growth (vs STLY) · oCGRP Market Share %">TRx Volume · Growth (vs STLY) · oCGRP Market Share %</span></div>
      <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
        <table>
          <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">QTD %</th><th style="text-align:right">YTD %</th><th style="text-align:right">WK MS</th><th style="text-align:right">QTD MS</th><th style="text-align:right">YTD MS</th></tr></thead>
          <tbody>
            <tr><td>Actuals '26</td><td style="text-align:right">59,082</td><td style="text-align:right">557,914</td><td style="text-align:right">1,272,406</td><td style="text-align:right"><span class="delta-pos">+12.1%</span></td><td style="text-align:right"><span class="delta-pos">+11.8%</span></td><td style="text-align:right"><span class="delta-pos">+14.9%</span></td><td style="text-align:right">31.4%</td><td style="text-align:right">31.6%</td><td style="text-align:right">32.0%</td></tr>
            <tr><td>Actuals '25</td><td style="text-align:right">52,706</td><td style="text-align:right">478,902</td><td style="text-align:right">1,107,452</td><td style="text-align:right"><span class="delta-pos">+18.4%</span></td><td style="text-align:right"><span class="delta-pos">+15.3%</span></td><td style="text-align:right"><span class="delta-pos">+16.5%</span></td><td style="text-align:right">32.9%</td><td style="text-align:right">32.8%</td><td style="text-align:right">32.7%</td></tr>
          </tbody>
        </table>
      </div>

      <div class="brand-header brand-c" style="margin-top:16px;"><span>QULIPTA</span><span style="font-weight:400;margin-left:12px;" data-metric-toggle="{M} Volume · Growth (vs STLY) · oCGRP Market Share %">TRx Volume · Growth (vs STLY) · oCGRP Market Share %</span></div>
      <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
        <table>
          <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">QTD %</th><th style="text-align:right">YTD %</th><th style="text-align:right">WK MS</th><th style="text-align:right">QTD MS</th><th style="text-align:right">YTD MS</th></tr></thead>
          <tbody>
            <tr><td>Actuals '26</td><td style="text-align:right">47,538</td><td style="text-align:right">445,083</td><td style="text-align:right">988,217</td><td style="text-align:right"><span class="delta-pos">+24.1%</span></td><td style="text-align:right"><span class="delta-pos">+23.0%</span></td><td style="text-align:right"><span class="delta-pos">+23.8%</span></td><td style="text-align:right">25.3%</td><td style="text-align:right">25.4%</td><td style="text-align:right">25.2%</td></tr>
            <tr><td>Actuals '25</td><td style="text-align:right">38,302</td><td style="text-align:right">361,820</td><td style="text-align:right">798,154</td><td style="text-align:right"><span class="delta-pos">+32.7%</span></td><td style="text-align:right"><span class="delta-pos">+32.4%</span></td><td style="text-align:right"><span class="delta-pos">+32.9%</span></td><td style="text-align:right">23.5%</td><td style="text-align:right">23.6%</td><td style="text-align:right">23.5%</td></tr>
          </tbody>
        </table>
      </div>

      

      
    </div>

    <!-- NPA Acute / Preventive Split Sub-tab -->
    <div id="npa-acute-prev" style="display:none;">
      <div class="pill-group" id="acute-prev-toggle">
        <div class="pill active" onclick="switchAcutePrev('acute')">Acute</div>
        <div class="pill" onclick="switchAcutePrev('preventive')">Preventive</div>
      </div>

      <!-- ACUTE VIEW -->
      <div id="acute-view">
        <div class="card">
          <div class="card-title">Nurtec Acute — Brand Competitive View</div>
          <div class="card-subtitle">National · IQVIA NPA · Actuals 2026 vs Actuals 2025 (Same Time Last Year)</div>

          <!-- TRx (left) and NBRx (right) charts side by side -->
          <div class="split-section">
            <div class="split-col">
              <div class="section-label">TRx</div>
              <div class="chart-container chart-container-sm">
                <svg class="chart" preserveAspectRatio="none" viewBox="0 0 380 200">
                  <line x1="40" y1="180" x2="370" y2="180" stroke="#e5e7eb" stroke-width="1"/>
                  <line x1="40" y1="140" x2="370" y2="140" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="100" x2="370" y2="100" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="60" x2="370" y2="60" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="20" x2="370" y2="20" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <text x="35" y="184" text-anchor="end" font-size="9" fill="#9ca3af">0K</text>
                  <text x="35" y="104" text-anchor="end" font-size="9" fill="#9ca3af">30K</text>
                  <text x="35" y="24" text-anchor="end" font-size="9" fill="#9ca3af">60K</text>
                  <polyline fill="none" stroke="#16a34a" stroke-width="2" points="50,45 75,48 100,44 125,42 150,40 175,38 200,36 225,35 250,33 275,32 300,30 325,28 350,27"/>
                  <polyline fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="4" points="50,62 75,65 100,60 125,58 150,56 175,55 200,53 225,52 250,51 275,50 300,49 325,48 350,47"/>
                  <polyline fill="none" stroke="#f59e0b" stroke-width="2" points="50,90 75,92 100,88 125,87 150,86 175,85 200,84 225,84 250,83 275,82 300,82 325,81 350,80"/>
                  <polyline fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4" points="50,98 75,100 100,97 125,96 150,95 175,95 200,94 225,94 250,93 275,93 300,92 325,92 350,92"/>
                  <text x="50" y="196" font-size="8" fill="#9ca3af">Wk 1</text>
                  <text x="150" y="196" font-size="8" fill="#9ca3af">Wk 9</text>
                  <text x="250" y="196" font-size="8" fill="#9ca3af">Wk 17</text>
                  <text x="350" y="196" font-size="8" fill="#9ca3af">Wk 26</text>
                </svg>
              </div>
            </div>
            <div class="split-col">
              <div class="section-label">NBRx</div>
              <div class="chart-container chart-container-sm">
                <svg class="chart" preserveAspectRatio="none" viewBox="0 0 380 200">
                  <line x1="40" y1="180" x2="370" y2="180" stroke="#e5e7eb" stroke-width="1"/>
                  <line x1="40" y1="140" x2="370" y2="140" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="100" x2="370" y2="100" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="60" x2="370" y2="60" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="20" x2="370" y2="20" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <text x="35" y="184" text-anchor="end" font-size="9" fill="#9ca3af">0K</text>
                  <text x="35" y="104" text-anchor="end" font-size="9" fill="#9ca3af">15K</text>
                  <text x="35" y="24" text-anchor="end" font-size="9" fill="#9ca3af">30K</text>
                  <polyline fill="none" stroke="#16a34a" stroke-width="2" points="50,55 75,58 100,52 125,50 150,48 175,46 200,44 225,42 250,40 275,38 300,36 325,34 350,32"/>
                  <polyline fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="4" points="50,72 75,74 100,70 125,68 150,66 175,64 200,63 225,62 250,61 275,60 300,59 325,58 350,57"/>
                  <polyline fill="none" stroke="#f59e0b" stroke-width="2" points="50,105 75,107 100,103 125,102 150,100 175,99 200,98 225,97 250,96 275,96 300,95 325,95 350,94"/>
                  <polyline fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4" points="50,115 75,116 100,113 125,112 150,111 175,110 200,110 225,109 250,109 275,108 300,108 325,108 350,107"/>
                  <text x="50" y="196" font-size="8" fill="#9ca3af">Wk 1</text>
                  <text x="150" y="196" font-size="8" fill="#9ca3af">Wk 9</text>
                  <text x="250" y="196" font-size="8" fill="#9ca3af">Wk 17</text>
                  <text x="350" y="196" font-size="8" fill="#9ca3af">Wk 26</text>
                </svg>
              </div>
            </div>
          </div>
          <div class="axis-info"><span>Y-Axis: Volume (K)</span><span>X-Axis: Time Period (Week)</span></div>
        <div class="legend">
            <div class="legend-item"><div class="legend-dot" style="background:#16a34a"></div>Nurtec Acute Actuals</div>
            <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#16a34a" stroke-width="2" stroke-dasharray="3"/></svg>Nurtec Acute STLY</div>
            <div class="legend-item"><div class="legend-dot" style="background:#f59e0b"></div>Ubrelvy Acute Actuals</div>
            <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3"/></svg>Ubrelvy Acute STLY</div>
          </div>
        </div>

        <!-- Brand Tables: TRx left, NBRx right — aligned with charts above -->
        <div class="split-section">
          <div class="split-col">
            <div class="brand-header brand-a"><span>NURTEC ACUTE</span><span style="font-weight:400;margin-left:8px;">TRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">58,241</td><td style="text-align:right">542,108</td><td style="text-align:right">1,205,417</td><td style="text-align:right">19.2%</td><td style="text-align:right">54.1%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">48,912</td><td style="text-align:right">459,302</td><td style="text-align:right">1,024,118</td><td style="text-align:right">14.8%</td><td style="text-align:right">51.9%</td></tr>
                </tbody>
              </table>
            </div>

            <div class="brand-header brand-b" style="margin-top:12px;"><span>UBRELVY ACUTE</span><span style="font-weight:400;margin-left:8px;">TRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">42,318</td><td style="text-align:right">398,521</td><td style="text-align:right">912,604</td><td style="text-align:right">11.4%</td><td style="text-align:right">39.3%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">37,986</td><td style="text-align:right">359,411</td><td style="text-align:right">801,823</td><td style="text-align:right">16.2%</td><td style="text-align:right">40.1%</td></tr>
                </tbody>
              </table>
            </div>
          </div>

          <div class="split-col">
            <div class="brand-header brand-a"><span>NURTEC ACUTE</span><span style="font-weight:400;margin-left:8px;">NBRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">21,408</td><td style="text-align:right">198,412</td><td style="text-align:right">442,106</td><td style="text-align:right">20.1%</td><td style="text-align:right">56.2%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">17,820</td><td style="text-align:right">167,540</td><td style="text-align:right">374,821</td><td style="text-align:right">15.6%</td><td style="text-align:right">54.0%</td></tr>
                </tbody>
              </table>
            </div>

            <div class="brand-header brand-b" style="margin-top:12px;"><span>UBRELVY ACUTE</span><span style="font-weight:400;margin-left:8px;">NBRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">15,612</td><td style="text-align:right">146,808</td><td style="text-align:right">335,417</td><td style="text-align:right">12.8%</td><td style="text-align:right">41.0%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">13,842</td><td style="text-align:right">131,204</td><td style="text-align:right">298,612</td><td style="text-align:right">17.4%</td><td style="text-align:right">42.5%</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- PREVENTIVE VIEW -->
      <div id="preventive-view" style="display:none;">
        <div class="card">
          <div class="card-title">Nurtec Preventive — Brand Competitive View</div>
          <div class="card-subtitle">National · IQVIA NPA · Actuals 2026 vs Actuals 2025 (Same Time Last Year)</div>

          <div class="split-section">
            <div class="split-col">
              <div class="section-label">TRx</div>
              <div class="chart-container chart-container-sm">
                <svg class="chart" preserveAspectRatio="none" viewBox="0 0 380 200">
                  <line x1="40" y1="180" x2="370" y2="180" stroke="#e5e7eb" stroke-width="1"/>
                  <line x1="40" y1="140" x2="370" y2="140" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="100" x2="370" y2="100" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="60" x2="370" y2="60" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="20" x2="370" y2="20" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <text x="35" y="184" text-anchor="end" font-size="9" fill="#9ca3af">0K</text>
                  <text x="35" y="104" text-anchor="end" font-size="9" fill="#9ca3af">25K</text>
                  <text x="35" y="24" text-anchor="end" font-size="9" fill="#9ca3af">50K</text>
                  <polyline fill="none" stroke="#16a34a" stroke-width="2" points="50,120 75,118 100,115 125,112 150,108 175,105 200,100 225,96 250,92 275,88 300,84 325,80 350,76"/>
                  <polyline fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="4" points="50,130 75,128 100,126 125,124 150,122 175,120 200,118 225,116 250,115 275,113 300,112 325,110 350,109"/>
                  <polyline fill="none" stroke="#3b82f6" stroke-width="2" points="50,85 75,82 100,78 125,74 150,70 175,66 200,62 225,58 250,54 275,50 300,46 325,42 350,38"/>
                  <polyline fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4" points="50,100 75,97 100,94 125,90 150,87 175,84 200,80 225,77 250,74 275,71 300,68 325,66 350,63"/>
                  <text x="50" y="196" font-size="8" fill="#9ca3af">Wk 1</text>
                  <text x="150" y="196" font-size="8" fill="#9ca3af">Wk 9</text>
                  <text x="250" y="196" font-size="8" fill="#9ca3af">Wk 17</text>
                  <text x="350" y="196" font-size="8" fill="#9ca3af">Wk 26</text>
                </svg>
              </div>
            </div>
            <div class="split-col">
              <div class="section-label">NBRx</div>
              <div class="chart-container chart-container-sm">
                <svg class="chart" preserveAspectRatio="none" viewBox="0 0 380 200">
                  <line x1="40" y1="180" x2="370" y2="180" stroke="#e5e7eb" stroke-width="1"/>
                  <line x1="40" y1="140" x2="370" y2="140" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="100" x2="370" y2="100" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="60" x2="370" y2="60" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <line x1="40" y1="20" x2="370" y2="20" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="3"/>
                  <text x="35" y="184" text-anchor="end" font-size="9" fill="#9ca3af">0K</text>
                  <text x="35" y="104" text-anchor="end" font-size="9" fill="#9ca3af">12K</text>
                  <text x="35" y="24" text-anchor="end" font-size="9" fill="#9ca3af">24K</text>
                  <polyline fill="none" stroke="#16a34a" stroke-width="2" points="50,125 75,122 100,118 125,115 150,111 175,107 200,103 225,99 250,95 275,91 300,87 325,83 350,80"/>
                  <polyline fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="4" points="50,135 75,133 100,130 125,128 150,126 175,124 200,122 225,120 250,118 275,117 300,115 325,114 350,113"/>
                  <polyline fill="none" stroke="#3b82f6" stroke-width="2" points="50,90 75,86 100,82 125,78 150,74 175,70 200,66 225,62 250,58 275,54 300,50 325,46 350,42"/>
                  <polyline fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4" points="50,105 75,102 100,98 125,95 150,92 175,89 200,86 225,83 250,80 275,77 300,74 325,72 350,70"/>
                  <text x="50" y="196" font-size="8" fill="#9ca3af">Wk 1</text>
                  <text x="150" y="196" font-size="8" fill="#9ca3af">Wk 9</text>
                  <text x="250" y="196" font-size="8" fill="#9ca3af">Wk 17</text>
                  <text x="350" y="196" font-size="8" fill="#9ca3af">Wk 26</text>
                </svg>
              </div>
            </div>
          </div>
          <div class="axis-info"><span>Y-Axis: Volume (K)</span><span>X-Axis: Time Period (Week)</span></div>
        <div class="legend">
            <div class="legend-item"><div class="legend-dot" style="background:#16a34a"></div>Nurtec Prev Actuals</div>
            <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#16a34a" stroke-width="2" stroke-dasharray="3"/></svg>Nurtec Prev STLY</div>
            <div class="legend-item"><div class="legend-dot" style="background:#3b82f6"></div>Qulipta Prev Actuals</div>
            <div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#3b82f6" stroke-width="2" stroke-dasharray="3"/></svg>Qulipta Prev STLY</div>
          </div>
        </div>

        <!-- Preventive tables: TRx left, NBRx right -->
        <div class="split-section">
          <div class="split-col">
            <div class="brand-header brand-a"><span>NURTEC PREVENTIVE</span><span style="font-weight:400;margin-left:8px;">TRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">24,673</td><td style="text-align:right">229,097</td><td style="text-align:right">513,206</td><td style="text-align:right">15.8%</td><td style="text-align:right">21.2%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">21,000</td><td style="text-align:right">194,806</td><td style="text-align:right">440,213</td><td style="text-align:right">18.4%</td><td style="text-align:right">19.9%</td></tr>
                </tbody>
              </table>
            </div>

            <div class="brand-header brand-c" style="margin-top:12px;"><span>QULIPTA PREVENTIVE</span><span style="font-weight:400;margin-left:8px;">TRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">38,412</td><td style="text-align:right">358,920</td><td style="text-align:right">802,814</td><td style="text-align:right">26.3%</td><td style="text-align:right">33.0%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">30,418</td><td style="text-align:right">283,740</td><td style="text-align:right">638,102</td><td style="text-align:right">34.2%</td><td style="text-align:right">30.8%</td></tr>
                </tbody>
              </table>
            </div>
          </div>

          <div class="split-col">
            <div class="brand-header brand-a"><span>NURTEC PREVENTIVE</span><span style="font-weight:400;margin-left:8px;">NBRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">9,214</td><td style="text-align:right">85,621</td><td style="text-align:right">191,408</td><td style="text-align:right">17.2%</td><td style="text-align:right">22.8%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">7,860</td><td style="text-align:right">72,414</td><td style="text-align:right">163,210</td><td style="text-align:right">19.8%</td><td style="text-align:right">21.4%</td></tr>
                </tbody>
              </table>
            </div>

            <div class="brand-header brand-c" style="margin-top:12px;"><span>QULIPTA PREVENTIVE</span><span style="font-weight:400;margin-left:8px;">NBRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">14,508</td><td style="text-align:right">135,214</td><td style="text-align:right">302,618</td><td style="text-align:right">28.6%</td><td style="text-align:right">35.9%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">11,204</td><td style="text-align:right">104,812</td><td style="text-align:right">235,404</td><td style="text-align:right">36.1%</td><td style="text-align:right">33.2%</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="nl-tab" id="nl-access-tab">
<div style="padding:8px 32px 24px;">
<div class="section-head"><h2>Access Summary</h2><p>Payer access changes, formulary tracking, and covered lives analysis.</p></div>
    <div class="card">
      <div class="card-header-row">
        <div>
          <div class="card-title">Rolled-up NRx Share by Access-Change Cohort</div>
          <div class="card-subtitle">Calculated share across all plans grouped by access change since Jan 2025. Plans contribute to their cohort only after their change effective date — pre-change months roll into Control.</div>
        </div>
        <div style="display:flex;align-items:center;gap:8px;font-size:11px;">Start <input type="month" value="2025-01" style="padding:4px 8px;border:1px solid #d1d5db;border-radius:4px;font-size:11px;"></div>
      </div>

      <div class="row">
        <div class="stat-tile">
          <div class="label">ACCESS GAIN PLANS</div>
          <div class="value" style="color:#16a34a;">7</div>
          <div class="sub">gain events since Jan 2025</div>
        </div>
        <div class="stat-tile">
          <div class="label">ACCESS LOSS / RESTRICTION</div>
          <div class="value" style="color:#dc2626;">4</div>
          <div class="sub">loss / restriction events</div>
        </div>
        <div class="stat-tile">
          <div class="label">CONTROL GROUP</div>
          <div class="value">38</div>
          <div class="sub">no change (incl. pre-change months)</div>
        </div>
      </div>

      <div class="chart-container">
        <svg class="chart" preserveAspectRatio="none" viewBox="0 0 800 250">
          <line x1="60" y1="20" x2="60" y2="220" stroke="#f3f4f6" stroke-width="1"/>
          <line x1="60" y1="220" x2="780" y2="220" stroke="#e5e7eb" stroke-width="1"/>
          <line x1="60" y1="170" x2="780" y2="170" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
          <line x1="60" y1="120" x2="780" y2="120" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
          <line x1="60" y1="70" x2="780" y2="70" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
          <text x="50" y="224" text-anchor="end" font-size="10" fill="#9ca3af">28%</text>
          <text x="50" y="174" text-anchor="end" font-size="10" fill="#9ca3af">31%</text>
          <text x="50" y="124" text-anchor="end" font-size="10" fill="#9ca3af">34%</text>
          <text x="50" y="74" text-anchor="end" font-size="10" fill="#9ca3af">37%</text>
          <text x="100" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Jan'25</text>
          <text x="180" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Mar'25</text>
          <text x="260" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">May'25</text>
          <text x="340" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Jul'25</text>
          <text x="420" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Sep'25</text>
          <text x="500" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Nov'25</text>
          <text x="580" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Jan'26</text>
          <text x="660" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Mar'26</text>
          <text x="740" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">May'26</text>
          <line x1="260" y1="20" x2="260" y2="220" stroke="#9ca3af" stroke-width="1" stroke-dasharray="4"/>
          <text x="265" y="35" font-size="9" fill="#6b7280">Gain cohort starts</text>
          <polyline fill="none" stroke="#16a34a" stroke-width="2" points="80,180 120,178 160,175 200,172 240,170 280,165 320,155 360,148 400,140 440,130 480,120 520,108 560,95 600,85 640,72 680,60 720,50 760,42"/>
          <polyline fill="none" stroke="#dc2626" stroke-width="2" points="80,145 120,148 160,150 200,152 240,155 280,160 320,168 360,172 400,178 440,182 480,188 520,192 560,195 600,198 640,200 680,202 720,205 760,208"/>
          <polyline fill="none" stroke="#9ca3af" stroke-width="2" stroke-dasharray="6" points="80,130 120,132 160,130 200,128 240,130 280,128 320,127 360,128 400,126 440,125 480,124 520,123 560,122 600,120 640,119 680,118 720,117 760,115"/>
        </svg>
      </div>
      <div class="axis-info"><span>Y-Axis: NRx Share %</span><span>X-Axis: Time Period (Month)</span></div>
        <div class="legend">
        <div class="legend-item"><div class="legend-dot" style="background:#16a34a"></div>Plans w/ access gain (post-change)</div>
        <div class="legend-item"><div class="legend-dot" style="background:#dc2626"></div>Plans w/ access loss (post-change)</div>
        <div class="legend-item"><div class="legend-dot" style="background:#9ca3af"></div>Control (no change / pre-change)</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">Access Change Details</div>
      <div class="card-subtitle">Includes current share vs. share at time of change (delta is the story)</div>
      <table>
        <thead>
          <tr><th>PLAN</th><th>CHANGE</th><th>EFF. DATE</th><th>PAYER</th><th style="text-align:right">LIVES</th><th style="text-align:right">SHARE @ CHANGE</th><th style="text-align:right">CURRENT SHARE</th><th style="text-align:right">Δ SHARE</th><th style="text-align:right">EST. NRX %</th><th style="text-align:right">EST. TRX %</th></tr>
        </thead>
        <tbody>
          <tr><td>Louisiana Medicaid</td><td><span class="badge badge-loss">Loss</span></td><td>06/15/26</td><td>Medicaid</td><td style="text-align:right">1.4M</td><td style="text-align:right">24.1%</td><td style="text-align:right">21.9%</td><td style="text-align:right"><span class="delta-neg">-2.2%</span></td><td style="text-align:right"><span class="delta-neg">-0.3%</span></td><td style="text-align:right"><span class="delta-neg">-0.2%</span></td></tr>
          <tr><td>UnitedHealth Comm (IL)</td><td><span class="badge badge-restriction">Restriction</span></td><td>06/10/26</td><td>Commercial</td><td style="text-align:right">820K</td><td style="text-align:right">36.4%</td><td style="text-align:right">35.8%</td><td style="text-align:right"><span class="delta-neg">-0.6%</span></td><td style="text-align:right"><span class="delta-neg">-0.1%</span></td><td style="text-align:right"><span class="delta-neg">-0.1%</span></td></tr>
          <tr><td>BCBS Texas Comm</td><td><span class="badge badge-gain">Gain</span></td><td>05/28/26</td><td>Commercial</td><td style="text-align:right">2.1M</td><td style="text-align:right">28.7%</td><td style="text-align:right">32.4%</td><td style="text-align:right"><span class="delta-pos">+3.7%</span></td><td style="text-align:right"><span class="delta-pos">+0.6%</span></td><td style="text-align:right"><span class="delta-pos">+0.4%</span></td></tr>
          <tr><td>CVS Caremark Comm</td><td><span class="badge badge-gain">Gain</span></td><td>05/12/26</td><td>Commercial</td><td style="text-align:right">3.6M</td><td style="text-align:right">30.2%</td><td style="text-align:right">34.9%</td><td style="text-align:right"><span class="delta-pos">+4.7%</span></td><td style="text-align:right"><span class="delta-pos">+0.9%</span></td><td style="text-align:right"><span class="delta-pos">+0.7%</span></td></tr>
          <tr><td>Florida Medicaid</td><td><span class="badge badge-restriction">Restriction</span></td><td>04/22/26</td><td>Medicaid</td><td style="text-align:right">980K</td><td style="text-align:right">26.0%</td><td style="text-align:right">23.5%</td><td style="text-align:right"><span class="delta-neg">-2.5%</span></td><td style="text-align:right"><span class="delta-neg">-0.2%</span></td><td style="text-align:right"><span class="delta-neg">-0.2%</span></td></tr>
        </tbody>
      </table>
    </div>

    <div class="card">
      <div class="card-header-row">
        <div>
          <div class="card-title">Lives Covered by Access Status</div>
          <div class="card-subtitle">Longitudinal · cumulative covered lives (millions) by status, filterable by payer type</div>
        </div>
        <div class="filter-group">
          <span style="font-size:11px;">Payer</span><select class="filter-select"><option>All</option></select>
          <span style="font-size:11px;">Status</span><select class="filter-select"><option>All</option></select>
        </div>
      </div>
      <div class="chart-container">
        <svg class="chart" preserveAspectRatio="none" viewBox="0 0 800 250">
          <line x1="60" y1="220" x2="780" y2="220" stroke="#e5e7eb" stroke-width="1"/>
          <text x="50" y="224" text-anchor="end" font-size="10" fill="#9ca3af">0M</text>
          <text x="50" y="174" text-anchor="end" font-size="10" fill="#9ca3af">35M</text>
          <text x="50" y="124" text-anchor="end" font-size="10" fill="#9ca3af">70M</text>
          <text x="50" y="74" text-anchor="end" font-size="10" fill="#9ca3af">105M</text>
          <text x="50" y="24" text-anchor="end" font-size="10" fill="#9ca3af">140M</text>
          <polygon fill="rgba(156,163,175,0.3)" points="80,220 120,180 200,140 300,100 400,70 500,55 600,45 700,38 760,35 760,220"/>
          <polygon fill="rgba(22,163,74,0.3)" points="80,220 120,205 200,195 300,185 400,175 500,165 600,155 700,148 760,145 760,220"/>
          <polygon fill="rgba(220,38,38,0.2)" points="80,220 120,215 200,213 300,212 400,214 500,215 600,216 700,217 760,217 760,220"/>
          <polyline fill="none" stroke="#16a34a" stroke-width="2" points="80,205 120,195 200,185 300,175 400,165 500,155 600,148 700,142 760,140"/>
          <polyline fill="none" stroke="#dc2626" stroke-width="1.5" points="80,215 120,213 200,212 300,213 400,214 500,215 600,216 700,217 760,217"/>
          <polyline fill="none" stroke="#9ca3af" stroke-width="2" points="80,180 120,140 200,100 300,70 400,55 500,45 600,40 700,36 760,34"/>
        </svg>
      </div>
      <div class="axis-info"><span>Y-Axis: Covered Lives (M)</span><span>X-Axis: Time Period (Month)</span></div>
        <div class="legend">
        <div class="legend-item"><div class="legend-dot" style="background:#16a34a"></div>Gain</div>
        <div class="legend-item"><div class="legend-dot" style="background:#dc2626"></div>Loss</div>
        <div class="legend-item"><div class="legend-dot" style="background:#f59e0b"></div>Restriction</div>
        <div class="legend-item"><div class="legend-dot" style="background:#9ca3af"></div>Control</div>
      </div>
    </div>
  </div>
</div>
<div class="nl-tab" id="nl-financial-tab">
<div style="padding:8px 32px 24px;">
<div class="section-head"><h2>Financial Tracker</h2><p>Weekly gross and net sales performance vs. budget and plan attainment.</p></div>
    <div class="pill-group" id="financial-toggle">
      <div class="pill active" onclick="switchFinancial('gross')">Gross Sales</div>
      <div class="pill" onclick="switchFinancial('net')">Net Sales</div>
    </div>

    <div id="gross-view">
    <div class="row">
      <div class="stat-tile">
        <div class="label">GROSS SALES W/E 06/19</div>
        <div class="value">$28.4M</div>
        <div class="sub"><span class="delta-pos">+2.8%</span>&nbsp;&nbsp;WoW · +$0.8M</div>
      </div>
      <div class="stat-tile">
        <div class="label">MTD ATTAINMENT VS OP26</div>
        <div class="value">94.4%</div>
        <div class="sub">$1.6M behind MTD plan</div>
      </div>
      <div class="stat-tile">
        <div class="label">YTD ATTAINMENT VS OP26</div>
        <div class="value">93.6%</div>
        <div class="sub">$112K behind YTD plan</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">Weekly Gross Sales vs Budget</div>
      <div class="card-subtitle">Last 14 weeks · $M</div>
      <div class="chart-container">
        <svg class="chart" preserveAspectRatio="none" viewBox="0 0 800 260">
          <line x1="60" y1="230" x2="780" y2="230" stroke="#e5e7eb" stroke-width="1"/>
          <line x1="60" y1="180" x2="780" y2="180" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
          <line x1="60" y1="130" x2="780" y2="130" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
          <line x1="60" y1="80" x2="780" y2="80" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
          <line x1="60" y1="30" x2="780" y2="30" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
          <text x="50" y="234" text-anchor="end" font-size="10" fill="#9ca3af">$0M</text>
          <text x="50" y="184" text-anchor="end" font-size="10" fill="#9ca3af">$8M</text>
          <text x="50" y="134" text-anchor="end" font-size="10" fill="#9ca3af">$16M</text>
          <text x="50" y="84" text-anchor="end" font-size="10" fill="#9ca3af">$24M</text>
          <text x="50" y="34" text-anchor="end" font-size="10" fill="#9ca3af">$32M</text>
          <rect x="72" y="120" width="18" height="110" fill="#1e3a5f" rx="2"/>
          <rect x="92" y="100" width="18" height="130" fill="#d1d5db" rx="2"/>
          <rect x="122" y="110" width="18" height="120" fill="#1e3a5f" rx="2"/>
          <rect x="142" y="100" width="18" height="130" fill="#d1d5db" rx="2"/>
          <rect x="172" y="105" width="18" height="125" fill="#1e3a5f" rx="2"/>
          <rect x="192" y="100" width="18" height="130" fill="#d1d5db" rx="2"/>
          <rect x="222" y="95" width="18" height="135" fill="#1e3a5f" rx="2"/>
          <rect x="242" y="100" width="18" height="130" fill="#d1d5db" rx="2"/>
          <rect x="272" y="90" width="18" height="140" fill="#1e3a5f" rx="2"/>
          <rect x="292" y="95" width="18" height="135" fill="#d1d5db" rx="2"/>
          <rect x="322" y="85" width="18" height="145" fill="#1e3a5f" rx="2"/>
          <rect x="342" y="90" width="18" height="140" fill="#d1d5db" rx="2"/>
          <rect x="372" y="68" width="18" height="162" fill="#1e3a5f" rx="2"/>
          <rect x="392" y="75" width="18" height="155" fill="#d1d5db" rx="2"/>
          <rect x="422" y="72" width="18" height="158" fill="#1e3a5f" rx="2"/>
          <rect x="442" y="75" width="18" height="155" fill="#d1d5db" rx="2"/>
          <rect x="472" y="65" width="18" height="165" fill="#1e3a5f" rx="2"/>
          <rect x="492" y="70" width="18" height="160" fill="#d1d5db" rx="2"/>
          <rect x="522" y="58" width="18" height="172" fill="#1e3a5f" rx="2"/>
          <rect x="542" y="65" width="18" height="165" fill="#d1d5db" rx="2"/>
          <rect x="572" y="55" width="18" height="175" fill="#1e3a5f" rx="2"/>
          <rect x="592" y="60" width="18" height="170" fill="#d1d5db" rx="2"/>
          <rect x="622" y="50" width="18" height="180" fill="#1e3a5f" rx="2"/>
          <rect x="642" y="55" width="18" height="175" fill="#d1d5db" rx="2"/>
          <rect x="672" y="45" width="18" height="185" fill="#1e3a5f" rx="2"/>
          <rect x="692" y="50" width="18" height="180" fill="#d1d5db" rx="2"/>
          <rect x="722" y="42" width="18" height="188" fill="#1e3a5f" rx="2"/>
          <rect x="742" y="48" width="18" height="182" fill="#d1d5db" rx="2"/>
          <text x="88" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 1</text>
          <text x="138" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 2</text>
          <text x="188" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 3</text>
          <text x="238" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 4</text>
          <text x="288" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 5</text>
          <text x="338" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 6</text>
          <text x="388" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 7</text>
          <text x="438" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 8</text>
          <text x="488" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 9</text>
          <text x="538" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 10</text>
          <text x="588" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 11</text>
          <text x="638" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 12</text>
          <text x="688" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 13</text>
          <text x="738" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 14</text>
        </svg>
      </div>
      <div class="axis-info"><span>Y-Axis: Gross Sales ($M)</span><span>X-Axis: Time Period (Week)</span></div>
        <div class="legend">
        <div class="legend-item"><div class="legend-dot" style="background:#1e3a5f;border-radius:2px;width:12px;"></div>Actual</div>
        <div class="legend-item"><div class="legend-dot" style="background:#d1d5db;border-radius:2px;width:12px;"></div>Budget</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">Script vs Budget — MTD & YTD growth</div>
      <div class="card-subtitle">Δ '25-'26 · Nurtec & oiCGRP</div>
      <table>
        <thead>
          <tr><th>BRAND</th><th style="text-align:right">SCRIPT Δ MTD</th><th style="text-align:right">SCRIPT Δ YTD</th><th style="text-align:right">BUDGET ATTN MTD</th><th style="text-align:right">BUDGET ATTN YTD</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>Nurtec NBRx</strong></td><td style="text-align:right"><span class="delta-pos">+15.6%</span></td><td style="text-align:right"><span class="delta-pos">+11.3%</span></td><td style="text-align:right">100.5%</td><td style="text-align:right">98.3%</td></tr>
          <tr><td><strong>oiCGRP NBRx</strong></td><td style="text-align:right"><span class="delta-pos">+12.1%</span></td><td style="text-align:right"><span class="delta-pos">+10.1%</span></td><td style="text-align:right">—</td><td style="text-align:right">—</td></tr>
          <tr><td><strong>Nurtec TRx</strong></td><td style="text-align:right"><span class="delta-pos">+16.5%</span></td><td style="text-align:right"><span class="delta-pos">+16.1%</span></td><td style="text-align:right">94.4%</td><td style="text-align:right">93.5%</td></tr>
          <tr><td><strong>oiCGRP TRx</strong></td><td style="text-align:right"><span class="delta-pos">+15.8%</span></td><td style="text-align:right"><span class="delta-pos">+17.1%</span></td><td style="text-align:right">95.8%</td><td style="text-align:right">94.3%</td></tr>
        </tbody>
      </table>
    </div>
    </div>

    <div id="net-view" style="display:none;">
    <div class="row">
      <div class="stat-tile">
        <div class="label">NET SALES W/E 06/19</div>
        <div class="value">$18.6M</div>
        <div class="sub"><span class="delta-pos">+3.1%</span>&nbsp;&nbsp;WoW · +$0.8M</div>
      </div>
      <div class="stat-tile">
        <div class="label">NET MTD ATTAINMENT VS OP26</div>
        <div class="value">92.1%</div>
        <div class="sub">$2.1M behind MTD plan</div>
      </div>
      <div class="stat-tile">
        <div class="label">NET YTD ATTAINMENT VS OP26</div>
        <div class="value">91.8%</div>
        <div class="sub">$186K behind YTD plan</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">Weekly Net Sales vs Budget</div>
      <div class="card-subtitle">Last 14 weeks · $M</div>
      <div class="chart-container">
        <svg class="chart" preserveAspectRatio="none" viewBox="0 0 800 260">
          <line x1="60" y1="230" x2="780" y2="230" stroke="#e5e7eb" stroke-width="1"/>
          <line x1="60" y1="180" x2="780" y2="180" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
          <line x1="60" y1="130" x2="780" y2="130" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
          <line x1="60" y1="80" x2="780" y2="80" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
          <line x1="60" y1="30" x2="780" y2="30" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>
          <text x="50" y="234" text-anchor="end" font-size="10" fill="#9ca3af">$0M</text>
          <text x="50" y="184" text-anchor="end" font-size="10" fill="#9ca3af">$8M</text>
          <text x="50" y="134" text-anchor="end" font-size="10" fill="#9ca3af">$16M</text>
          <text x="50" y="84" text-anchor="end" font-size="10" fill="#9ca3af">$24M</text>
          <text x="50" y="34" text-anchor="end" font-size="10" fill="#9ca3af">$32M</text>
          <rect x="72" y="120" width="18" height="110" fill="#1e3a5f" rx="2"/>
          <rect x="92" y="100" width="18" height="130" fill="#d1d5db" rx="2"/>
          <rect x="122" y="110" width="18" height="120" fill="#1e3a5f" rx="2"/>
          <rect x="142" y="100" width="18" height="130" fill="#d1d5db" rx="2"/>
          <rect x="172" y="105" width="18" height="125" fill="#1e3a5f" rx="2"/>
          <rect x="192" y="100" width="18" height="130" fill="#d1d5db" rx="2"/>
          <rect x="222" y="95" width="18" height="135" fill="#1e3a5f" rx="2"/>
          <rect x="242" y="100" width="18" height="130" fill="#d1d5db" rx="2"/>
          <rect x="272" y="90" width="18" height="140" fill="#1e3a5f" rx="2"/>
          <rect x="292" y="95" width="18" height="135" fill="#d1d5db" rx="2"/>
          <rect x="322" y="85" width="18" height="145" fill="#1e3a5f" rx="2"/>
          <rect x="342" y="90" width="18" height="140" fill="#d1d5db" rx="2"/>
          <rect x="372" y="68" width="18" height="162" fill="#1e3a5f" rx="2"/>
          <rect x="392" y="75" width="18" height="155" fill="#d1d5db" rx="2"/>
          <rect x="422" y="72" width="18" height="158" fill="#1e3a5f" rx="2"/>
          <rect x="442" y="75" width="18" height="155" fill="#d1d5db" rx="2"/>
          <rect x="472" y="65" width="18" height="165" fill="#1e3a5f" rx="2"/>
          <rect x="492" y="70" width="18" height="160" fill="#d1d5db" rx="2"/>
          <rect x="522" y="58" width="18" height="172" fill="#1e3a5f" rx="2"/>
          <rect x="542" y="65" width="18" height="165" fill="#d1d5db" rx="2"/>
          <rect x="572" y="55" width="18" height="175" fill="#1e3a5f" rx="2"/>
          <rect x="592" y="60" width="18" height="170" fill="#d1d5db" rx="2"/>
          <rect x="622" y="50" width="18" height="180" fill="#1e3a5f" rx="2"/>
          <rect x="642" y="55" width="18" height="175" fill="#d1d5db" rx="2"/>
          <rect x="672" y="45" width="18" height="185" fill="#1e3a5f" rx="2"/>
          <rect x="692" y="50" width="18" height="180" fill="#d1d5db" rx="2"/>
          <rect x="722" y="42" width="18" height="188" fill="#1e3a5f" rx="2"/>
          <rect x="742" y="48" width="18" height="182" fill="#d1d5db" rx="2"/>
          <text x="88" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 1</text>
          <text x="138" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 2</text>
          <text x="188" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 3</text>
          <text x="238" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 4</text>
          <text x="288" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 5</text>
          <text x="338" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 6</text>
          <text x="388" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 7</text>
          <text x="438" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 8</text>
          <text x="488" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 9</text>
          <text x="538" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 10</text>
          <text x="588" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 11</text>
          <text x="638" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 12</text>
          <text x="688" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 13</text>
          <text x="738" y="248" text-anchor="middle" font-size="9" fill="#9ca3af">Wk 14</text>
        </svg>
      </div>
      <div class="axis-info"><span>Y-Axis: Net Sales ($M)</span><span>X-Axis: Time Period (Week)</span></div>
        <div class="legend">
        <div class="legend-item"><div class="legend-dot" style="background:#1e3a5f;border-radius:2px;width:12px;"></div>Actual</div>
        <div class="legend-item"><div class="legend-dot" style="background:#d1d5db;border-radius:2px;width:12px;"></div>Budget</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">Net Revenue vs Budget — MTD & YTD growth</div>
      <div class="card-subtitle">Δ '25-'26 · Nurtec & oiCGRP</div>
      <table>
        <thead>
          <tr><th>BRAND</th><th style="text-align:right">SCRIPT Δ MTD</th><th style="text-align:right">SCRIPT Δ YTD</th><th style="text-align:right">BUDGET ATTN MTD</th><th style="text-align:right">BUDGET ATTN YTD</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>Nurtec NBRx</strong></td><td style="text-align:right"><span class="delta-pos">+15.6%</span></td><td style="text-align:right"><span class="delta-pos">+11.3%</span></td><td style="text-align:right">100.5%</td><td style="text-align:right">98.3%</td></tr>
          <tr><td><strong>oiCGRP NBRx</strong></td><td style="text-align:right"><span class="delta-pos">+12.1%</span></td><td style="text-align:right"><span class="delta-pos">+10.1%</span></td><td style="text-align:right">—</td><td style="text-align:right">—</td></tr>
          <tr><td><strong>Nurtec TRx</strong></td><td style="text-align:right"><span class="delta-pos">+16.5%</span></td><td style="text-align:right"><span class="delta-pos">+16.1%</span></td><td style="text-align:right">92.1%</td><td style="text-align:right">93.5%</td></tr>
          <tr><td><strong>oiCGRP TRx</strong></td><td style="text-align:right"><span class="delta-pos">+15.8%</span></td><td style="text-align:right"><span class="delta-pos">+17.1%</span></td><td style="text-align:right">95.8%</td><td style="text-align:right">94.3%</td></tr>
        </tbody>
      </table>
    </div>
</div>
</div>
</div>
</div>
            </div>
        </section>

        <!-- 3. AGENTS -->
        <section class="section" id="agents" data-label="CoWork Agents">
            <div class="section-head"><h2>Snowflake CoWork Agents</h2><p>AI-powered analytical agents for automated insights and conversational data exploration.</p></div>
            <div class="grid">
                <a class="card" href="https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s3"><svg viewBox="0 0 24 24"><rect x="6" y="4" width="12" height="7" rx="2"/><path d="M9 11v4M15 11v4M8 18h8M12 15v3M7 4V2M17 4V2"/></svg></span></div><div class="card-title">Migraine NPA Agent</div><div class="card-desc">Conversational NPA data querying and automated insight generation.</div><span class="dest-pill dest-agent"><span class="swatch">&#9632;</span>Cortex Agent</span></a>
                <a class="card" href="https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s3"><svg viewBox="0 0 24 24"><rect x="6" y="4" width="12" height="7" rx="2"/><path d="M9 11v4M15 11v4M8 18h8M12 15v3M7 4V2M17 4V2"/></svg></span><span class="badge weekly">Weekly</span></div><div class="card-title">LAAD Weekly Agent</div><div class="card-desc">Weekly LAAD data processing and trend surfacing.</div><span class="dest-pill dest-agent"><span class="swatch">&#9632;</span>Cortex Agent</span></a>
                <a class="card" href="https://app.us-east-1.privatelink.snowflakecomputing.com/pfe/amerprod01/#/ai" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s3"><svg viewBox="0 0 24 24"><rect x="6" y="4" width="12" height="7" rx="2"/><path d="M9 11v4M15 11v4M8 18h8M12 15v3M7 4V2M17 4V2"/></svg></span><span class="badge monthly">Monthly</span></div><div class="card-title">eLAAD Monthly Agent</div><div class="card-desc">Monthly eLAAD aggregation and reporting automation.</div><span class="dest-pill dest-agent"><span class="swatch">&#9632;</span>Cortex Agent</span></a>
            </div>
        </section>

        <!-- 4. DELIVERABLES -->
        <section class="section" id="deliverables" data-label="Analytics Deliverables">
            <div class="section-head"><h2>Analytics Deliverables</h2><p>PowerPoint and Excel deliverables for leadership and cross-functional stakeholders.</p></div>
            <div class="grid">
                <a class="card" href="https://pfizer.sharepoint.com/:p:/s/MigraineAnalytics/IQA7CzbiZxm9SYbErQAXLG5kASpgzKHmNLmQz8yBenX6kNc?e=KgQ7yz" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s4"><svg viewBox="0 0 24 24"><path d="M4 4h16a1 1 0 011 1v14a1 1 0 01-1 1H4a1 1 0 01-1-1V5a1 1 0 011-1z"/><path d="M8 9h8M8 13h6M8 17h4"/></svg></span></div><div class="card-title">Nurtec Offsite Deck</div><div class="card-desc">Strategic offsite presentation with market overview.</div><div class="card-updated">Updated Feb 24, 2026</div><span class="dest-pill dest-ppt"><span class="swatch">&#9632;</span>PowerPoint</span></a>
                <a class="card" href="https://pfizer.sharepoint.com/:p:/s/MigraineAnalytics/IQBvAxCrDDmeTbpe9RH14ha6AeG6J09GqT4ft1vRBHtmTk8?e=qFF3D9" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s4"><svg viewBox="0 0 24 24"><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/><circle cx="12" cy="6" r="2"/><path d="M6 16V8l6-2M18 16V8l-6-2"/></svg></span></div><div class="card-title">oCGRP Market Dynamics</div><div class="card-desc">Competitive dynamics and market share analysis.</div><div class="card-updated">Updated Feb 4, 2026</div><span class="dest-pill dest-ppt"><span class="swatch">&#9632;</span>PPT &middot; Excel</span></a>
                <a class="card" href="#" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s4"><svg viewBox="0 0 24 24"><path d="M14 3v4a1 1 0 001 1h4"/><path d="M17 21H7a2 2 0 01-2-2V5a2 2 0 012-2h7l5 5v11a2 2 0 01-2 2z"/><path d="M9 17v-6M12 17v-1M15 17v-4"/></svg></span></div><div class="card-title">Nurtec Deep-Dives</div><div class="card-desc">Detailed deep-dive analyses across key metrics.</div><span class="dest-pill dest-ppt"><span class="swatch">&#9632;</span>PowerPoint</span></a>
            </div>
        </section>

        <!-- 5. DOCS -->
        <section class="section" id="docs" data-label="Business Rule Docs">
            <div class="section-head"><h2>Business Rule Documentation</h2><p>Data definitions, metric calculations, business logic, and reporting standards.</p></div>
            <div class="grid">
                <a class="card" href="https://pfizer.sharepoint.com/:p:/s/MigraineAnalytics/IQBdBFg1vxdFR6HZvdxtKVPZAUdmK-vTwF4Trvm4JdEBru4?e=TG0guS" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s5"><svg viewBox="0 0 24 24"><path d="M3 19a9 9 0 019-9 9 9 0 019 9"/><path d="M3 19h18M12 10V3"/><path d="M7.8 4.8L12 3l4.2 1.8"/></svg></span></div><div class="card-title">Migraine Market Overview</div><div class="card-desc">Market landscape and key therapeutic area definitions.</div><div class="card-updated">Updated Dec 23, 2025</div><span class="dest-pill dest-doc"><span class="swatch">&#9632;</span>Doc</span></a>
                <a class="card" href="#" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s5"><svg viewBox="0 0 24 24"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2"/><rect x="9" y="3" width="6" height="4" rx="1"/><path d="M9 12l2 2 4-4"/></svg></span></div><div class="card-title">BR Alignment</div><div class="card-desc">Cross-functional business rule alignment documentation.</div><span class="dest-pill dest-doc"><span class="swatch">&#9632;</span>Doc</span></a>
                <a class="card" href="https://pfizer.sharepoint.com/:p:/s/MigraineAnalytics/IQA9ft3L-N9VT4YQzW36UFsXAQU2ZNBXbO3UjFvDwa6NV5E?e=8ytpZI" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s5"><svg viewBox="0 0 24 24"><path d="M12 4L4 8l8 4 8-4-8-4zM4 12l8 4 8-4M4 16l8 4 8-4"/></svg></span></div><div class="card-title">IIS BR Master Deck</div><div class="card-desc">Master business rules deck for IIS analytics.</div><div class="card-updated">Updated Jan 1, 2026</div><span class="dest-pill dest-ppt"><span class="swatch">&#9632;</span>PowerPoint</span></a>
                <a class="card" href="https://pfizer.sharepoint.com/:p:/s/MigraineAnalytics/IQBOAt2MOv_OTqhwLardlsHPAZdTa2hsvBq5pUuZfNbVWTM?e=tDWmaa" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s5"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><circle cx="12" cy="4" r="1.5"/><circle cx="12" cy="20" r="1.5"/><circle cx="4" cy="12" r="1.5"/><circle cx="20" cy="12" r="1.5"/><path d="M12 7v2M12 15v2M7 12h2M15 12h2"/></svg></span></div><div class="card-title">IIS Migraine Data Ecosystem</div><div class="card-desc">Data sources, flows, and ecosystem mapping.</div><div class="card-updated">Updated Jan 1, 2026</div><span class="dest-pill dest-doc"><span class="swatch">&#9632;</span>Doc</span></a>
                <a class="card" href="https://pfizer.sharepoint.com/:p:/s/MigraineAnalytics/IQADCiim_iD7QbxZE7Fm3F89Ab8O10p4xzPmog3z4X7KQ2g?e=jA6LCi" target="_blank" rel="noopener"><div class="card-top"><span class="icon-chip chip-s5"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 5V3M12 21v-2M16.95 7.05l1.41-1.41M5.64 18.36l1.41-1.41M19 12h2M3 12h2M16.95 16.95l1.41 1.41M5.64 5.64l1.41 1.41"/></svg></span></div><div class="card-title">Migraine Dashboard BR</div><div class="card-desc">Dashboard-specific metric logic and standards.</div><div class="card-updated">Updated Feb 1, 2026</div><span class="dest-pill dest-doc"><span class="swatch">&#9632;</span>Doc</span></a>
            </div>
        </section>

    </main>
</div>
</div>

<script>
(function() {
    'use strict';

    // Dropdown
    window.toggleDropdown = function(id, ev) {
        ev.stopPropagation();
        document.querySelectorAll('.dropdown.show').forEach(function(d) { if (d.id !== id) d.classList.remove('show'); });
        document.getElementById(id).classList.toggle('show');
    };
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.dropdown-wrap')) {
            document.querySelectorAll('.dropdown.show').forEach(function(d) { d.classList.remove('show'); });
        }
    });

    // Sidebar main navigation
    var nav = document.getElementById('sidebarNav');
    var items = nav.querySelectorAll('.nav-item');
    var sections = {};
    items.forEach(function(it) { sections[it.dataset.target] = document.getElementById(it.dataset.target); });
    var toolbarSection = document.getElementById('toolbarSection');
    var newsletterSub = document.getElementById('newsletterSub');
    var nlGridView = document.getElementById('nl-grid-view');
    var nlDeepdiveView = document.getElementById('nl-deepdive-view');
    var heroEl = document.querySelector('.hero');
    var dividerEl = document.querySelector('.workspace-divider');
    var inDeepdive = false;

    function setActive(item) {
        items.forEach(function(i) { i.classList.remove('active'); });
        item.classList.add('active');
    }

    function exitDeepdive() {
        inDeepdive = false;
        nlGridView.style.display = '';
        nlDeepdiveView.style.display = 'none';
        newsletterSub.classList.remove('is-open');
        heroEl.style.display = '';
        dividerEl.style.display = '';
        var kpisHead = document.getElementById('kpisHead');
        var kpiRow = document.getElementById('kpiRow');
        if (kpisHead) kpisHead.style.display = '';
        if (kpiRow) kpiRow.style.display = '';
        newsletterSub.querySelectorAll('.nav-sub-item').forEach(function(s) { s.classList.remove('active'); });
    }

    function enterDeepdive(panelId) {
        inDeepdive = true;
        nlGridView.style.display = 'none';
        nlDeepdiveView.style.display = '';
        newsletterSub.classList.add('is-open');
        heroEl.style.display = 'none';
        dividerEl.style.display = 'none';
        var kpisHead = document.getElementById('kpisHead');
        var kpiRow = document.getElementById('kpiRow');
        if (kpisHead) kpisHead.style.display = 'none';
        if (kpiRow) kpiRow.style.display = 'none';
        // Activate the correct nl-tab
        nlDeepdiveView.querySelectorAll('.nl-tab').forEach(function(p) { p.classList.remove('active'); });
        var target = document.getElementById(panelId + '-tab');
        if (target) target.classList.add('active');
        // Activate the correct sub-nav item
        newsletterSub.querySelectorAll('.nav-sub-item').forEach(function(s) { s.classList.remove('active'); });
        var matchingSub = newsletterSub.querySelector('[data-panel="' + panelId + '"]');
        if (matchingSub) matchingSub.classList.add('active');
    }

    var switching = false;
    function showSection(id, label) {
        if (switching) return;
        var current = document.querySelector('.section.is-active');
        var next = sections[id];
        if (!next || next === current) return;
        switching = true;
        if (current) current.classList.remove('is-visible');
        setTimeout(function() {
            if (current) current.classList.remove('is-active');
            var content = document.querySelector('.content');
            if (content) content.scrollTop = 0;
            next.classList.add('is-active');
            void next.offsetWidth;
            next.classList.add('is-visible');
            if (toolbarSection && label) toolbarSection.textContent = label;
            switching = false;
        }, 220);
    }

    items.forEach(function(item) {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            setActive(item);
            var label = sections[item.dataset.target] ? sections[item.dataset.target].dataset.label : '';
            showSection(item.dataset.target, label);

            // When clicking Newsletter from nav, show card grid (reset deepdive)
            if (item.dataset.target === 'newsletter') {
                exitDeepdive();
            } else {
                newsletterSub.classList.remove('is-open');
                if (inDeepdive) exitDeepdive();
            }

            // Restore hero for non-deepdive views
            if (item.dataset.target !== 'newsletter' || !inDeepdive) {
                heroEl.style.display = '';
                dividerEl.style.display = '';
            }
        });
    });

    // Newsletter card clicks → enter deepdive
    var nlCards = document.querySelectorAll('#nl-grid-view .card[data-nl-panel]');
    nlCards.forEach(function(card) {
        card.addEventListener('click', function(e) {
            e.preventDefault();
            var panelId = card.dataset.nlPanel;
            if (panelId) enterDeepdive(panelId);
        });
    });

    // Newsletter sub-nav items (sidebar) → switch panels
    var subItems = newsletterSub.querySelectorAll('.nav-sub-item[data-panel]');
    subItems.forEach(function(subItem) {
        subItem.addEventListener('click', function(e) {
            e.preventDefault();
            newsletterSub.querySelectorAll('.nav-sub-item').forEach(function(s) { s.classList.remove('active'); });
            subItem.classList.add('active');
            nlDeepdiveView.querySelectorAll('.nl-tab').forEach(function(p) { p.classList.remove('active'); });
            var target = document.getElementById(subItem.dataset.panel + '-tab');
            if (target) target.classList.add('active');
        });
    });

    // Newsletter sub-tab functions
    window.switchNpaSubtab = function(subtab) {
        document.querySelectorAll('#npa-subtabs .pill').forEach(function(el) { el.classList.remove('active'); });
        event.currentTarget.classList.add('active');
        if (subtab === 'retail') {
            document.getElementById('npa-retail').style.display = 'block';
            document.getElementById('npa-acute-prev').style.display = 'none';
        } else {
            document.getElementById('npa-retail').style.display = 'none';
            document.getElementById('npa-acute-prev').style.display = 'block';
        }
    };
    window.switchAcutePrev = function(view) {
        document.querySelectorAll('#acute-prev-toggle .pill').forEach(function(el) { el.classList.remove('active'); });
        event.currentTarget.classList.add('active');
        if (view === 'acute') {
            document.getElementById('acute-view').style.display = 'block';
            document.getElementById('preventive-view').style.display = 'none';
        } else {
            document.getElementById('acute-view').style.display = 'none';
            document.getElementById('preventive-view').style.display = 'block';
        }
    };
    
    window.switchFinancial = function(view) {
        document.querySelectorAll('#financial-toggle .pill').forEach(function(el) { el.classList.remove('active'); });
        event.currentTarget.classList.add('active');
        if (view === 'gross') {
            document.getElementById('gross-view').style.display = 'block';
            document.getElementById('net-view').style.display = 'none';
        } else {
            document.getElementById('gross-view').style.display = 'none';
            document.getElementById('net-view').style.display = 'block';
        }
    };
    
    
    window.switchXponentMetric = function(metric) {
        document.getElementById('xp-trx-pill').classList.toggle('active', metric === 'trx');
        document.getElementById('xp-nrx-pill').classList.toggle('active', metric === 'nrx');
        var label = metric === 'trx' ? 'TRx' : 'NRx';
        document.querySelectorAll('[data-xp-metric]').forEach(function(el) {
            var template = el.getAttribute('data-xp-metric');
            el.textContent = template.replace('{XM}', label);
        });
    };
    window.switchChannelBrand = function(brand) {
        document.getElementById('channel-nurtec').classList.toggle('active', brand === 'nurtec');
        document.getElementById('channel-ubrelvy').classList.toggle('active', brand === 'ubrelvy');
        document.getElementById('channel-qulipta').classList.toggle('active', brand === 'qulipta');
    };
    window.toggleNpaMetric = function(metric) {
        document.getElementById('npa-trx-pill').classList.toggle('active', metric === 'trx');
        document.getElementById('npa-nbrx-pill').classList.toggle('active', metric === 'nbrx');
        // Update all elements with data-metric-toggle attribute
        var label = metric === 'trx' ? 'TRx' : 'NBRx';
        document.querySelectorAll('[data-metric-toggle]').forEach(function(el) {
            var template = el.getAttribute('data-metric-toggle');
            el.textContent = template.replace('{M}', label);
        });
    };
})();
</script>
</body>
</html>
"""

components.html(html_content, height=920, scrolling=False)
