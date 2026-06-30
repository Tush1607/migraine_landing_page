import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Migraine Intelligence Hub",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Data Fetching for Live Charts ---
import pandas as pd

DATA_LOADED = False
brand_chart_svg = ""

try:
    import snowflake.connector
    
    @st.cache_data(ttl=3600)
    def fetch_npa_brand_data():
        conn = snowflake.connector.connect(
            warehouse="VAW_AMER_PROD_WH",
            database="VAW_AMER_DESIGN",
            schema="USMIGRAINEIISANALYTICSETL",
        )
        query = """SELECT WEEK_ID, BRAND, ACTUALS, STLY, LATEST_GOAL
        FROM "VAW_AMER_DESIGN"."USMIGRAINEIISANALYTICSETL"."USMIGRAINEIISANALYTICSETL_SQL_US_MIGRAINE_FINAL_STACK_WEB_APP_VIEWS_SF"
        WHERE SEGMENT = 'TRx' AND RX_CLASSIFICATION = 'Overall' AND CHANNEL_TYPE = 'Overall' AND STACK_KEY = 'NPA_BRANDS_BY_CHANNEL'
        ORDER BY WEEK_ID, BRAND"""
        try:
            df = pd.read_sql(query, conn)
        finally:
            conn.close()
        return df

    npa_brand_df = fetch_npa_brand_data()
    weeks = sorted(npa_brand_df['WEEK_ID'].unique())
    nurtec_data = npa_brand_df[npa_brand_df['BRAND'] == 'NURTEC'].sort_values('WEEK_ID')
    ubrelvy_data = npa_brand_df[npa_brand_df['BRAND'] == 'UBRELVY'].sort_values('WEEK_ID')
    qulipta_data = npa_brand_df[npa_brand_df['BRAND'] == 'QULIPTA'].sort_values('WEEK_ID')
    
    all_vals = [v for v in list(nurtec_data['ACTUALS']) + list(ubrelvy_data['ACTUALS']) + list(qulipta_data['ACTUALS']) + list(nurtec_data['STLY']) + list(ubrelvy_data['STLY']) + list(qulipta_data['STLY']) if v is not None and v > 0]
    max_val = max(all_vals) if all_vals else 80000
    
    def scale_pts(vals, mx=None):
        if mx is None: mx = max_val
        pts = []
        n = len(vals)
        for i, v in enumerate(vals):
            if v is None or v <= 0: v = 0
            x = 80 + (752 - 80) * i / (n - 1) if n > 1 else 80
            y = 220 - (v / mx) * 200 if mx > 0 else 120
            pts.append(f"{int(x)},{int(y)}")
        return " ".join(pts)
    
    nurtec_act = scale_pts(list(nurtec_data['ACTUALS']))
    nurtec_stl = scale_pts(list(nurtec_data['STLY']))
    ubrelvy_act = scale_pts(list(ubrelvy_data['ACTUALS']))
    ubrelvy_stl = scale_pts(list(ubrelvy_data['STLY']))
    qulipta_act = scale_pts(list(qulipta_data['ACTUALS']))
    qulipta_stl = scale_pts(list(qulipta_data['STLY']))
    goal_line = scale_pts(list(nurtec_data['LATEST_GOAL']))
    
    # Y-axis
    y_svg = ""
    for i in range(5):
        val = max_val * i / 4
        y = int(220 - (val / max_val) * 200)
        lbl = f"{int(val/1000)}K" if val >= 1000 else f"{int(val)}"
        y_svg += f'<text x="50" y="{y+4}" text-anchor="end" font-size="10" fill="#9ca3af">{lbl}</text>'
        y_svg += f'<line x1="60" y1="{y}" x2="780" y2="{y}" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>'
    
    # X-axis
    nw = len(weeks)
    x_svg = '<line x1="60" y1="220" x2="780" y2="220" stroke="#e5e7eb" stroke-width="1"/>'
    for idx in [0, nw//5, 2*nw//5, 3*nw//5, 4*nw//5, nw-1]:
        if idx < nw:
            x = int(80 + (752 - 80) * idx / (nw - 1)) if nw > 1 else 80
            x_svg += f'<text x="{x}" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk {idx+1}</text>'
    
    brand_chart_svg = f"""{x_svg}
            {y_svg}
            <polyline fill="none" stroke="#16a34a" stroke-width="2" points="{nurtec_act}"/>
            <polyline fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="6" points="{nurtec_stl}"/>
            <polyline fill="none" stroke="#f59e0b" stroke-width="2" points="{ubrelvy_act}"/>
            <polyline fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6" points="{ubrelvy_stl}"/>
            <polyline fill="none" stroke="#3b82f6" stroke-width="2" points="{qulipta_act}"/>
            <polyline fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="6" points="{qulipta_stl}"/>
            <polyline fill="none" stroke="#f472b6" stroke-width="2" stroke-dasharray="8,4" points="{goal_line}"/>"""
    DATA_LOADED = True
except Exception as e:
    brand_chart_svg = ""
    DATA_LOADED = False



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
<meBRAND_CHART_DATA_PLACEHOLDER
"""

# Inject live data
if DATA_LOADED:
    html_content = html_content.replace('BRAND_CHART_DATA_PLACEHOLDER', brand_chart_svg)

components.html(html_content, height=920, scrolling=False)
