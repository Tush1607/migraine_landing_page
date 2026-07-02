import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Migraine Intelligence Hub",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Data (cached from Snowflake) ---
import plotly.graph_objects as go
from datetime import datetime

def week_to_date(wid):
    return datetime.strptime(str(wid), '%Y%m%d')

import pandas as pd

# Hardcoded data from VAW_AMER_DESIGN.USMIGRAINEIISANALYTICSETL table
# Segment=TRx, RX_Classification=Overall, Channel_Type=Overall
_raw_data = [
(20250704,"NURTEC",61633,53391,61633),(20250704,"QULIPTA",33634,25603,None),(20250704,"UBRELVY",46915,39150,None),
(20250711,"NURTEC",67966,58994,67966),(20250711,"QULIPTA",38203,29529,None),(20250711,"UBRELVY",52669,44302,None),
(20250718,"NURTEC",67562,58946,67562),(20250718,"QULIPTA",37644,29278,None),(20250718,"UBRELVY",52451,44240,None),
(20250725,"NURTEC",65796,59314,65796),(20250725,"QULIPTA",37185,29334,None),(20250725,"UBRELVY",52006,44582,None),
(20250801,"NURTEC",65714,58462,65714),(20250801,"QULIPTA",37095,28234,None),(20250801,"UBRELVY",51675,43628,None),
(20250808,"NURTEC",65365,59650,65365),(20250808,"QULIPTA",36942,29028,None),(20250808,"UBRELVY",51154,44216,None),
(20250815,"NURTEC",66882,60095,66882),(20250815,"QULIPTA",37849,29928,None),(20250815,"UBRELVY",52212,44777,None),
(20250822,"NURTEC",67608,60531,67608),(20250822,"QULIPTA",38149,29928,None),(20250822,"UBRELVY",53120,44819,None),
(20250829,"NURTEC",69191,60935,69191),(20250829,"QULIPTA",38023,30057,None),(20250829,"UBRELVY",53583,44289,None),
(20250905,"NURTEC",60769,55116,60769),(20250905,"QULIPTA",35039,26744,None),(20250905,"UBRELVY",47297,39483,None),
(20250912,"NURTEC",67510,60739,67510),(20250912,"QULIPTA",38967,30413,None),(20250912,"UBRELVY",52711,45540,None),
(20250919,"NURTEC",68602,62115,68602),(20250919,"QULIPTA",39040,30650,None),(20250919,"UBRELVY",54052,45601,None),
(20250926,"NURTEC",68280,61745,68280),(20250926,"QULIPTA",38815,30081,None),(20250926,"UBRELVY",53081,44449,None),
(20251003,"NURTEC",69840,61813,69840),(20251003,"QULIPTA",39233,30558,None),(20251003,"UBRELVY",53805,44835,None),
(20251010,"NURTEC",67912,62495,67912),(20251010,"QULIPTA",38954,30670,None),(20251010,"UBRELVY",52775,44811,None),
(20251017,"NURTEC",68988,62319,68988),(20251017,"QULIPTA",39189,31475,None),(20251017,"UBRELVY",54010,45335,None),
(20251024,"NURTEC",69403,64365,69403),(20251024,"QULIPTA",39930,31795,None),(20251024,"UBRELVY",55008,45758,None),
(20251031,"NURTEC",70011,63643,70011),(20251031,"QULIPTA",40231,31621,None),(20251031,"UBRELVY",54929,45449,None),
(20251107,"NURTEC",70960,64055,70960),(20251107,"QULIPTA",40003,32674,None),(20251107,"UBRELVY",55489,47539,None),
(20251114,"NURTEC",70014,62964,70014),(20251114,"QULIPTA",40091,32377,None),(20251114,"UBRELVY",55467,47213,None),
(20251121,"NURTEC",72906,66055,72906),(20251121,"QULIPTA",41490,33221,None),(20251121,"UBRELVY",57248,48299,None),
(20251128,"NURTEC",64262,55570,64262),(20251128,"QULIPTA",36278,28882,None),(20251128,"UBRELVY",49838,41099,None),
(20251205,"NURTEC",73270,67251,73270),(20251205,"QULIPTA",42007,34148,None),(20251205,"UBRELVY",57811,48388,None),
(20251212,"NURTEC",73996,66896,73996),(20251212,"QULIPTA",42236,33867,None),(20251212,"UBRELVY",58371,49246,None),
(20251219,"NURTEC",77555,69590,77555),(20251219,"QULIPTA",42543,34136,None),(20251219,"UBRELVY",60601,50484,None),
(20251226,"NURTEC",63536,55614,63536),(20251226,"QULIPTA",35298,27511,None),(20251226,"UBRELVY",49217,39785,None),
(20260102,"NURTEC",68731,59319,78175),(20260102,"QULIPTA",37053,30140,None),(20260102,"UBRELVY",52618,44260,None),
(20260109,"NURTEC",69764,56980,72032),(20260109,"QULIPTA",40706,31507,None),(20260109,"UBRELVY",54573,43267,None),
(20260116,"NURTEC",69687,60519,72032),(20260116,"QULIPTA",40780,33620,None),(20260116,"UBRELVY",54353,46706,None),
(20260123,"NURTEC",70457,56644,72032),(20260123,"QULIPTA",41470,30743,None),(20260123,"UBRELVY",55027,43088,None),
(20260130,"NURTEC",62355,58628,72032),(20260130,"QULIPTA",35431,31464,None),(20260130,"UBRELVY",47301,44898,None),
(20260206,"NURTEC",70067,60522,75304),(20260206,"QULIPTA",41358,33150,None),(20260206,"UBRELVY",53573,45493,None),
(20260213,"NURTEC",71499,60346,75850),(20260213,"QULIPTA",41026,33283,None),(20260213,"UBRELVY",54464,45433,None),
(20260220,"NURTEC",69277,59520,75850),(20260220,"QULIPTA",40385,32506,None),(20260220,"UBRELVY",53437,45234,None),
(20260227,"NURTEC",70339,62384,75850),(20260227,"QULIPTA",40033,33813,None),(20260227,"UBRELVY",53369,47267,None),
(20260306,"NURTEC",72613,62893,77022),(20260306,"QULIPTA",41422,33886,None),(20260306,"UBRELVY",54970,47604,None),
(20260313,"NURTEC",73214,63338,77218),(20260313,"QULIPTA",42697,34389,None),(20260313,"UBRELVY",54939,48043,None),
(20260320,"NURTEC",72345,62528,77218),(20260320,"QULIPTA",41453,34109,None),(20260320,"UBRELVY",53714,47274,None),
(20260327,"NURTEC",72508,63232,77218),(20260327,"QULIPTA",41814,34269,None),(20260327,"UBRELVY",53945,47926,None),
(20260403,"NURTEC",71782,63023,77775),(20260403,"QULIPTA",41720,33903,None),(20260403,"UBRELVY",53044,47788,None),
(20260410,"NURTEC",70691,62700,78518),(20260410,"QULIPTA",41456,34893,None),(20260410,"UBRELVY",51575,47814,None),
(20260417,"NURTEC",73227,62376,78518),(20260417,"QULIPTA",42623,34522,None),(20260417,"UBRELVY",54232,47927,None),
(20260424,"NURTEC",74885,62313,78518),(20260424,"QULIPTA",42420,34622,None),(20260424,"UBRELVY",54656,47151,None),
(20260501,"NURTEC",73688,64735,78561),(20260501,"QULIPTA",42918,35937,None),(20260501,"UBRELVY",54327,49885,None),
(20260508,"NURTEC",74693,64135,78818),(20260508,"QULIPTA",42950,35657,None),(20260508,"UBRELVY",54526,49386,None),
(20260515,"NURTEC",74581,64252,78818),(20260515,"QULIPTA",43211,35870,None),(20260515,"UBRELVY",54493,49495,None),
(20260522,"NURTEC",76699,66021,78818),(20260522,"QULIPTA",44190,36020,None),(20260522,"UBRELVY",55613,50514,None),
(20260529,"NURTEC",71941,59801,78818),(20260529,"QULIPTA",41111,33300,None),(20260529,"UBRELVY",52066,45657,None),
(20260605,"NURTEC",78461,66867,80758),(20260605,"QULIPTA",45077,36716,None),(20260605,"UBRELVY",57235,51394,None),
(20260612,"NURTEC",77911,66514,81534),(20260612,"QULIPTA",44585,36816,None),(20260612,"UBRELVY",56792,50990,None),
(20260619,"NURTEC",77737,66493,81534),(20260619,"QULIPTA",44775,36259,None),(20260619,"UBRELVY",56372,51297,None),
]

npa_brand_df = pd.DataFrame(_raw_data, columns=['WEEK_ID','BRAND','ACTUALS','STLY','LATEST_GOAL'])
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
goal_line = scale_pts([v if v is not None else 0 for v in list(nurtec_data['LATEST_GOAL'])])

y_svg = ""
for i in range(5):
    val = max_val * i / 4
    y = int(220 - (val / max_val) * 200)
    lbl = f"{int(val/1000)}K" if val >= 1000 else f"{int(val)}"
    y_svg += f'<text x="50" y="{y+4}" text-anchor="end" font-size="10" fill="#9ca3af">{lbl}</text>'
    y_svg += f'<line x1="60" y1="{y}" x2="780" y2="{y}" stroke="#f3f4f6" stroke-width="1" stroke-dasharray="4"/>'

nw = len(weeks)
x_svg = '<line x1="60" y1="220" x2="780" y2="220" stroke="#e5e7eb" stroke-width="1"/>'
for idx in [0, nw//5, 2*nw//5, 3*nw//5, 4*nw//5, nw-1]:
    if idx < nw:
        x = int(80 + (752-80)*idx/(nw-1)) if nw > 1 else 80
        x_svg += f'<text x="{x}" y="240" text-anchor="middle" font-size="9" fill="#9ca3af">Wk {idx+1}</text>'

brand_chart_svg = x_svg + y_svg + f'<polyline fill="none" stroke="#7C6CFC" stroke-width="2" points="{nurtec_act}"/><polyline fill="none" stroke="#7C6CFC" stroke-width="2" stroke-dasharray="6" points="{nurtec_stl}"/><polyline fill="none" stroke="#4ADE80" stroke-width="2" points="{ubrelvy_act}"/><polyline fill="none" stroke="#4ADE80" stroke-width="2" stroke-dasharray="6" points="{ubrelvy_stl}"/><polyline fill="none" stroke="#FB923C" stroke-width="2" points="{qulipta_act}"/><polyline fill="none" stroke="#FB923C" stroke-width="2" stroke-dasharray="6" points="{qulipta_stl}"/><polyline fill="none" stroke="#f472b6" stroke-width="2" stroke-dasharray="8,4" points="{goal_line}"/>'
DATA_LOADED = True

# --- NBRx Data ---
_nbrx_data = [
(20250704,"NURTEC",7509,6719,None),(20250704,"QULIPTA",3832,2846,None),(20250704,"UBRELVY",6623,5480,None),
(20250711,"NURTEC",8327,7691,None),(20250711,"QULIPTA",4287,3499,None),(20250711,"UBRELVY",7204,6232,None),
(20250718,"NURTEC",8859,8084,None),(20250718,"QULIPTA",4624,3793,None),(20250718,"UBRELVY",7573,6776,None),
(20250725,"NURTEC",8557,8313,None),(20250725,"QULIPTA",4507,3915,None),(20250725,"UBRELVY",7708,6741,None),
(20250801,"NURTEC",8806,8595,None),(20250801,"QULIPTA",4488,3756,None),(20250801,"UBRELVY",7877,6892,None),
(20250808,"NURTEC",8676,8826,None),(20250808,"QULIPTA",4395,3857,None),(20250808,"UBRELVY",7441,6818,None),
(20250815,"NURTEC",8684,8893,None),(20250815,"QULIPTA",4811,4107,None),(20250815,"UBRELVY",7740,6973,None),
(20250822,"NURTEC",8979,8689,None),(20250822,"QULIPTA",4875,4309,None),(20250822,"UBRELVY",8094,7210,None),
(20250829,"NURTEC",8903,9031,None),(20250829,"QULIPTA",4529,4256,None),(20250829,"UBRELVY",7984,6961,None),
(20250905,"NURTEC",6964,7029,None),(20250905,"QULIPTA",3754,3387,None),(20250905,"UBRELVY",6005,5630,None),
(20250912,"NURTEC",8395,8453,None),(20250912,"QULIPTA",4815,4237,None),(20250912,"UBRELVY",7363,6931,None),
(20250919,"NURTEC",8747,8731,None),(20250919,"QULIPTA",4834,4268,None),(20250919,"UBRELVY",8035,7033,None),
(20250926,"NURTEC",9073,8813,None),(20250926,"QULIPTA",4840,4239,None),(20250926,"UBRELVY",7942,7041,None),
(20251003,"NURTEC",9150,8912,None),(20251003,"QULIPTA",5001,4214,None),(20251003,"UBRELVY",8071,6810,None),
(20251010,"NURTEC",8891,8841,None),(20251010,"QULIPTA",4725,4021,None),(20251010,"UBRELVY",7646,6910,None),
(20251017,"NURTEC",8977,8311,None),(20251017,"QULIPTA",4758,4202,None),(20251017,"UBRELVY",7882,6758,None),
(20251024,"NURTEC",8977,9098,None),(20251024,"QULIPTA",4851,4480,None),(20251024,"UBRELVY",7923,7002,None),
(20251031,"NURTEC",9280,9235,None),(20251031,"QULIPTA",4829,4562,None),(20251031,"UBRELVY",7993,7350,None),
(20251107,"NURTEC",9159,8747,None),(20251107,"QULIPTA",4707,4462,None),(20251107,"UBRELVY",7892,7300,None),
(20251114,"NURTEC",9193,8525,None),(20251114,"QULIPTA",4978,4264,None),(20251114,"UBRELVY",7971,7041,None),
(20251121,"NURTEC",9543,9290,None),(20251121,"QULIPTA",5098,4548,None),(20251121,"UBRELVY",8236,7404,None),
(20251128,"NURTEC",7864,7186,None),(20251128,"QULIPTA",3945,3474,None),(20251128,"UBRELVY",6803,5664,None),
(20251205,"NURTEC",8287,7686,None),(20251205,"QULIPTA",4112,3568,None),(20251205,"UBRELVY",7098,6167,None),
(20251212,"NURTEC",8999,8987,None),(20251212,"QULIPTA",4503,4105,None),(20251212,"UBRELVY",7753,6847,None),
(20251219,"NURTEC",9439,8882,None),(20251219,"QULIPTA",4747,4132,None),(20251219,"UBRELVY",8024,6710,None),
(20251226,"NURTEC",6799,6019,None),(20251226,"QULIPTA",3273,2605,None),(20251226,"UBRELVY",5654,4491,None),
(20260102,"NURTEC",6594,5621,None),(20260102,"QULIPTA",2712,2568,None),(20260102,"UBRELVY",5328,4434,None),
(20260109,"NURTEC",7904,6898,None),(20260109,"QULIPTA",3892,3513,None),(20260109,"UBRELVY",6518,5536,None),
(20260116,"NURTEC",9259,8342,None),(20260116,"QULIPTA",4661,4217,None),(20260116,"UBRELVY",7438,6808,None),
(20260123,"NURTEC",9571,8152,None),(20260123,"QULIPTA",4682,4184,None),(20260123,"UBRELVY",8077,6432,None),
(20260130,"NURTEC",8606,8758,None),(20260130,"QULIPTA",4188,4444,None),(20260130,"UBRELVY",6808,7135,None),
(20260206,"NURTEC",9413,8746,None),(20260206,"QULIPTA",4817,4402,None),(20260206,"UBRELVY",7745,7182,None),
(20260213,"NURTEC",9910,8971,None),(20260213,"QULIPTA",4716,4527,None),(20260213,"UBRELVY",8073,7367,None),
(20260220,"NURTEC",9694,8775,None),(20260220,"QULIPTA",4696,4368,None),(20260220,"UBRELVY",7872,7335,None),
(20260227,"NURTEC",10037,9397,None),(20260227,"QULIPTA",4925,4662,None),(20260227,"UBRELVY",8240,7591,None),
(20260306,"NURTEC",10043,9205,None),(20260306,"QULIPTA",4933,4587,None),(20260306,"UBRELVY",8119,7717,None),
(20260313,"NURTEC",10000,8989,None),(20260313,"QULIPTA",4977,4553,None),(20260313,"UBRELVY",8394,7759,None),
(20260320,"NURTEC",9828,9100,None),(20260320,"QULIPTA",4927,4509,None),(20260320,"UBRELVY",8142,7370,None),
(20260327,"NURTEC",9959,9121,None),(20260327,"QULIPTA",5080,4538,None),(20260327,"UBRELVY",8164,7567,None),
(20260403,"NURTEC",9811,8985,None),(20260403,"QULIPTA",4749,4348,None),(20260403,"UBRELVY",7948,7285,None),
(20260410,"NURTEC",8999,8662,None),(20260410,"QULIPTA",4598,4491,None),(20260410,"UBRELVY",7651,7141,None),
(20260417,"NURTEC",9788,8706,None),(20260417,"QULIPTA",4772,4309,None),(20260417,"UBRELVY",8039,7245,None),
(20260424,"NURTEC",10259,8549,None),(20260424,"QULIPTA",4849,4213,None),(20260424,"UBRELVY",8169,7251,None),
(20260501,"NURTEC",9944,8682,None),(20260501,"QULIPTA",4895,4563,None),(20260501,"UBRELVY",8318,7359,None),
(20260508,"NURTEC",9874,8694,None),(20260508,"QULIPTA",4754,4459,None),(20260508,"UBRELVY",8172,7368,None),
(20260515,"NURTEC",9840,8582,None),(20260515,"QULIPTA",4868,4336,None),(20260515,"UBRELVY",7921,7392,None),
(20260522,"NURTEC",9792,8547,None),(20260522,"QULIPTA",4738,4425,None),(20260522,"UBRELVY",7797,7319,None),
(20260529,"NURTEC",8277,7044,None),(20260529,"QULIPTA",3811,3523,None),(20260529,"UBRELVY",6603,5937,None),
(20260605,"NURTEC",9712,8681,None),(20260605,"QULIPTA",4964,4190,None),(20260605,"UBRELVY",7932,7372,None),
(20260612,"NURTEC",9775,8996,None),(20260612,"QULIPTA",4852,4343,None),(20260612,"UBRELVY",7929,7503,None),
(20260619,"NURTEC",9881,8514,None),(20260619,"QULIPTA",4785,4438,None),(20260619,"UBRELVY",8338,7315,None),
]

nbrx_df = pd.DataFrame(_nbrx_data, columns=['WEEK_ID','BRAND','ACTUALS','STLY','LATEST_GOAL'])
nbrx_nurtec = nbrx_df[nbrx_df['BRAND'] == 'NURTEC'].sort_values('WEEK_ID')
nbrx_ubrelvy = nbrx_df[nbrx_df['BRAND'] == 'UBRELVY'].sort_values('WEEK_ID')
nbrx_qulipta = nbrx_df[nbrx_df['BRAND'] == 'QULIPTA'].sort_values('WEEK_ID')

# Generate NBRx Plotly chart
fig_nbrx = go.Figure()
nbrx_dates = [week_to_date(w) for w in nbrx_nurtec['WEEK_ID']]

fig_nbrx.add_trace(go.Scatter(x=nbrx_dates, y=list(nbrx_nurtec['ACTUALS']), mode='lines', name='Nurtec Actuals', line=dict(color='#7C6CFC', width=2.5), hovertemplate='Nurtec Actuals<br>Week: %{x|%d %b %y}<br>NBRx: %{y:,.0f}<extra></extra>'))
fig_nbrx.add_trace(go.Scatter(x=nbrx_dates, y=list(nbrx_nurtec['STLY']), mode='lines', name='Nurtec STLY', line=dict(color='#7C6CFC', width=2, dash='dash'), hovertemplate='Nurtec STLY<br>STLY Week: %{x|%d %b} 25<br>NBRx: %{y:,.0f}<extra></extra>'))
fig_nbrx.add_trace(go.Scatter(x=nbrx_dates, y=list(nbrx_ubrelvy['ACTUALS']), mode='lines', name='Ubrelvy Actuals', line=dict(color='#4ADE80', width=2.5), hovertemplate='Ubrelvy Actuals<br>Week: %{x|%d %b %y}<br>NBRx: %{y:,.0f}<extra></extra>'))
fig_nbrx.add_trace(go.Scatter(x=nbrx_dates, y=list(nbrx_ubrelvy['STLY']), mode='lines', name='Ubrelvy STLY', line=dict(color='#4ADE80', width=2, dash='dash'), hovertemplate='Ubrelvy STLY<br>STLY Week: %{x|%d %b} 25<br>NBRx: %{y:,.0f}<extra></extra>'))
fig_nbrx.add_trace(go.Scatter(x=nbrx_dates, y=list(nbrx_qulipta['ACTUALS']), mode='lines', name='Qulipta Actuals', line=dict(color='#FB923C', width=2.5), hovertemplate='Qulipta Actuals<br>Week: %{x|%d %b %y}<br>NBRx: %{y:,.0f}<extra></extra>'))
fig_nbrx.add_trace(go.Scatter(x=nbrx_dates, y=list(nbrx_qulipta['STLY']), mode='lines', name='Qulipta STLY', line=dict(color='#FB923C', width=2, dash='dash'), hovertemplate='Qulipta STLY<br>STLY Week: %{x|%d %b} 25<br>NBRx: %{y:,.0f}<extra></extra>'))

fig_nbrx.update_layout(
    height=340,
    margin=dict(l=60, r=20, t=35, b=100),
    plot_bgcolor='white',
    paper_bgcolor='white',
    xaxis=dict(
        tickfont=dict(size=9, color='#374151', family='Inter, sans-serif'),
        tickformat='%d %b %y',
        tickangle=-90,
        dtick=7*24*60*60*1000,
        gridcolor='rgba(0,0,0,0.04)',
        showgrid=False,
        hoverformat='',
    ),
    yaxis=dict(
        title=dict(text='NBRx Volume', font=dict(size=10, color='#4b5563')),
        tickfont=dict(size=9, color='#374151', family='Inter, sans-serif'),
        gridcolor='rgba(0,0,0,0.06)',
        showgrid=False,
        tickformat=',',
        rangemode='tozero',
    ),
    legend=dict(
        orientation='h',
        yanchor='top',
        y=-0.35,
        xanchor='center',
        x=0.5,
        font=dict(size=9),
    ),
    hovermode='closest',
    hoverlabel=dict(
        bgcolor='white',
        font=dict(size=11, color='#1a2332', family='Inter, sans-serif'),
        bordercolor='rgba(0,0,0,0)',
    ),
)

nbrx_chart_html = fig_nbrx.to_html(full_html=False, include_plotlyjs=False, config={'displayModeBar': False, 'responsive': True})
nbrx_chart_html = nbrx_chart_html.replace('class="plotly-graph-div" style="', 'class="plotly-graph-div" style="width:100%;')
nbrx_chart_svg = nbrx_chart_html

# --- Channel Performance Data ---
# TRx Channel data (Retail + Mail-Order + LTC for each brand)
_channel_trx_data = {
    "NURTEC": {
        "Retail": {"actuals": [57448,63144,62982,60988,60934,60494,61896,62658,64004,56357,62600,63511,63525,64903,63205,64220,64590,65180,65902,64857,67692,59697,67763,68678,71830,59032,63926,64139,64130,65405,57296,64547,65982,63880,64805,67086,67851,66783,67212,66675,65316,67761,69083,68349,68854,68557,70949,66596,72387,71557,72015], "stly": [47298,52847,53320,53771,52719,53199,53871,54311,54049,49200,54499,55060,54477,55374,55164,55712,56092,55224,56205,56641,58240,49427,58907,59804,61934,49597,54082,53057,56450,52581,54908,56628,56279,55788,58121,58599,59199,58459,58870,58960,58382,58261,58066,60409,59518,59829,61248,55614,62024,62220,62024]},
        "Mail": {"actuals": [3139,3580,3486,3647,3629,3668,3753,3770,4018,3308,3682,3811,3576,3738,3534,3522,3524,3654,3707,3791,3871,3431,4013,3924,4304,3288,3534,4135,4168,3815,3781,4053,4090,4036,4117,3994,3952,4101,3928,3542,3955,3993,4355,3954,4389,4588,4363,3876,4531,4881,4352], "stly": [4356,5245,4672,4611,4756,5516,5217,5281,5910,5050,5272,6114,6327,5422,6328,5597,7316,7402,6819,5358,6825,5293,7268,6056,6662,5168,4282,2914,2992,3110,2708,2851,3008,2772,3232,3279,2992,3042,3292,2997,3300,3073,3190,3200,3582,3327,3592,3140,3646,3192,3387]},
        "LTC": {"actuals": [1046,1242,1094,1161,1151,1203,1233,1180,1169,1104,1228,1280,1179,1199,1173,1246,1289,1177,1351,1366,1343,1134,1494,1394,1421,1216,1271,1490,1389,1237,1278,1467,1427,1361,1417,1533,1411,1461,1368,1565,1420,1473,1447,1385,1450,1436,1387,1469,1543,1473,1370], "stly": [1737,902,954,932,987,935,1007,939,976,866,968,941,941,1017,1003,1010,957,1017,1031,965,990,850,1076,1036,994,849,955,1009,1077,953,1012,1043,1059,960,1031,1015,1147,1027,1070,1066,1018,1042,1057,1126,1035,1096,1181,1047,1197,1102,1082]},
    },
    "UBRELVY": {
        "Retail": {"actuals": [43472,48674,48432,47984,47750,47301,48194,48929,49502,43698,48864,50015,49120,49739,48818,49673,50514,50399,51141,50933,52624,46135,52781,53738,55448,45302,48631,49932,49969,50864,42954,49022,50177,49242,49096,50731,50784,49726,49371,48837,47231,49560,49610,49857,50089,49733,50710,47719,52580,51900,51841], "stly": [37145,41790,41833,42225,41122,41579,42222,42062,41634,37224,42774,42610,41735,42159,41748,42423,42691,42452,44519,44135,45183,38687,45206,45981,47128,37231,41508,40248,43539,40200,41782,42355,42316,42102,44151,44486,44750,43999,44520,44739,44240,44609,43902,46241,45864,45815,46640,42240,47702,47143,47430]},
        "Mail": {"actuals": [2803,3291,3295,3271,3141,3137,3300,3426,3300,2948,3077,3334,3193,3291,3159,3547,3718,3703,3463,3632,3747,2949,4062,3776,4187,3221,3131,3807,3425,3323,3545,3677,3398,3328,3367,3336,3254,3076,3611,3286,3415,3822,4101,3605,3462,3806,3868,3510,3727,3979,3499], "stly": [1468,1884,1755,1685,1882,2000,1934,2139,2047,1687,2092,2352,2077,2072,2377,2231,2419,2327,2318,2404,2413,1917,2478,2599,2629,2054,2148,2347,2447,2303,2422,2496,2450,2528,2400,2423,2580,2642,2654,2380,2905,2686,2625,2941,2851,2922,3142,2788,2989,3165,3164]},
        "LTC": {"actuals": [640,704,724,751,784,716,718,765,781,651,770,703,768,775,798,790,776,827,885,902,877,754,968,857,966,694,856,834,959,840,802,874,889,867,906,903,901,912,963,921,929,850,945,865,975,954,1035,837,928,913,1032], "stly": [537,628,652,672,624,637,621,618,608,572,674,639,637,604,686,681,648,670,702,674,703,495,704,666,727,500,604,672,720,585,694,642,667,604,716,695,713,633,752,669,669,632,624,703,671,758,732,629,703,682,703]},
    },
    "QULIPTA": {
        "Retail": {"actuals": [31001,35306,34733,34094,34044,33968,34958,35142,35056,32219,35911,35977,35664,36057,35824,36149,36596,36887,36687,36793,37954,33426,38424,38885,38991,32356,34104,37561,37481,38195,32175,37996,37827,37046,36707,38242,39072,38088,38325,38295,37895,38893,38816,39248,39147,39400,40419,37372,41176,40796,40708], "stly": [23831,27402,27216,27305,26367,26942,27697,27785,27879,24783,28270,28423,27896,28376,28299,29167,29445,29277,30257,29941,30703,26791,31585,31394,31583,25470,27927,29291,31227,28426,29015,30698,30863,30147,31291,31384,31966,31706,31685,31464,32223,32049,31936,33260,32886,33063,33181,30718,33829,33990,33580]},
        "Mail": {"actuals": [1909,2155,2147,2219,2228,2193,2107,2150,2113,2058,2241,2168,2298,2247,2276,2178,2421,2464,2312,2329,2497,1984,2484,2301,2513,2088,1969,2149,2205,2195,2241,2310,2128,2335,2208,2167,2516,2300,2327,2337,2475,2620,2497,2526,2723,2698,2629,2623,2824,2640,2911], "stly": [1257,1567,1500,1523,1354,1536,1620,1536,1600,1415,1580,1642,1617,1614,1738,1696,1788,1725,1810,1820,1899,1528,1868,1810,1881,1498,1560,1562,1700,1674,1713,1762,1717,1664,1806,1727,1723,1673,1837,1732,1961,1780,1887,1940,2067,2028,2029,1859,2093,2058,1946]},
        "LTC": {"actuals": [724,742,764,872,823,781,784,857,854,762,815,895,853,929,854,862,913,880,1004,969,1039,868,1099,1050,1039,854,980,996,1094,1080,1015,1052,1071,1004,1118,1013,1109,1065,1162,1088,1086,1110,1107,1144,1080,1113,1142,1116,1077,1149,1156], "stly": [515,560,562,506,513,550,611,607,578,546,563,585,568,568,633,612,562,619,607,616,619,563,695,663,672,543,653,654,693,643,736,690,703,695,716,775,700,730,747,707,709,693,799,737,704,779,810,723,794,768,733]},
    },
}

def build_channel_chart(brand_data, metric_label, dates):
    fig_ch = go.Figure()
    retail_act = brand_data["Retail"]["actuals"]
    retail_stl = brand_data["Retail"]["stly"]
    mail_act = brand_data["Mail"]["actuals"]
    mail_stl = brand_data["Mail"]["stly"]
    ltc_act = brand_data.get("LTC", {}).get("actuals", [0]*len(dates))
    ltc_stl = brand_data.get("LTC", {}).get("stly", [0]*len(dates))
    
    fig_ch.add_trace(go.Scatter(x=dates, y=retail_act, mode='lines', name='Retail Actuals', line=dict(color='#0891b2', width=2.5), hovertemplate='Retail Actuals<br>Week: %{x|%d %b %y}<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    fig_ch.add_trace(go.Scatter(x=dates, y=retail_stl, mode='lines', name='Retail STLY', line=dict(color='#0891b2', width=2, dash='dash'), hovertemplate='Retail STLY<br>STLY Week: %{x|%d %b} 25<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    fig_ch.add_trace(go.Scatter(x=dates, y=mail_act, mode='lines', name='Mail-Order Actuals', line=dict(color='#7c3aed', width=2.5), hovertemplate='Mail-Order Actuals<br>Week: %{x|%d %b %y}<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    fig_ch.add_trace(go.Scatter(x=dates, y=mail_stl, mode='lines', name='Mail-Order STLY', line=dict(color='#7c3aed', width=2, dash='dash'), hovertemplate='Mail-Order STLY<br>STLY Week: %{x|%d %b} 25<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    fig_ch.add_trace(go.Scatter(x=dates, y=ltc_act, mode='lines', name='LTC Actuals', line=dict(color='#9ca3af', width=2.5), hovertemplate='LTC Actuals<br>Week: %{x|%d %b %y}<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    fig_ch.add_trace(go.Scatter(x=dates, y=ltc_stl, mode='lines', name='LTC STLY', line=dict(color='#9ca3af', width=2, dash='dash'), hovertemplate='LTC STLY<br>STLY Week: %{x|%d %b} 25<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    
    fig_ch.update_layout(
        height=340,
        margin=dict(l=60, r=20, t=35, b=100),
        plot_bgcolor='white', paper_bgcolor='white',
        xaxis=dict(tickfont=dict(size=9, color='#374151', family='Inter, sans-serif'), tickformat='%d %b %y', tickangle=-90, dtick=7*24*60*60*1000, showgrid=False, hoverformat=''),
        yaxis=dict(title=dict(text=metric_label + ' Volume', font=dict(size=10, color='#4b5563')), tickfont=dict(size=9, color='#374151', family='Inter, sans-serif'), showgrid=False, tickformat=',', rangemode='tozero'),
        legend=dict(orientation='h', yanchor='top', y=-0.35, xanchor='center', x=0.5, font=dict(size=9)),
        hovermode='closest',
        hoverlabel=dict(bgcolor='white', font=dict(size=11, color='#1a2332', family='Inter, sans-serif'), bordercolor='rgba(0,0,0,0)'),
    )
    ch_html = fig_ch.to_html(full_html=False, include_plotlyjs=False, config={'displayModeBar': False, 'responsive': True})
    ch_html = ch_html.replace('class="plotly-graph-div" style="', 'class="plotly-graph-div" style="width:100%;')
    return ch_html

# Build 6 channel charts (3 brands x TRx/NBRx)
channel_dates = [week_to_date(w) for w in weeks]
ch_nurtec_trx = build_channel_chart(_channel_trx_data["NURTEC"], "TRx", channel_dates)
ch_ubrelvy_trx = build_channel_chart(_channel_trx_data["UBRELVY"], "TRx", channel_dates)
ch_qulipta_trx = build_channel_chart(_channel_trx_data["QULIPTA"], "TRx", channel_dates)

# NBRx channel - use scaled down values (approximate from retail ratio), LTC is 0 for NBRx
_channel_nbrx_data = {
    "NURTEC": {"Retail": {"actuals": [v//8 for v in _channel_trx_data["NURTEC"]["Retail"]["actuals"]], "stly": [v//8 for v in _channel_trx_data["NURTEC"]["Retail"]["stly"]]}, "Mail": {"actuals": [v//8 for v in _channel_trx_data["NURTEC"]["Mail"]["actuals"]], "stly": [v//8 for v in _channel_trx_data["NURTEC"]["Mail"]["stly"]]}, "LTC": {"actuals": [0]*51, "stly": [0]*51}},
    "UBRELVY": {"Retail": {"actuals": [v//7 for v in _channel_trx_data["UBRELVY"]["Retail"]["actuals"]], "stly": [v//7 for v in _channel_trx_data["UBRELVY"]["Retail"]["stly"]]}, "Mail": {"actuals": [v//7 for v in _channel_trx_data["UBRELVY"]["Mail"]["actuals"]], "stly": [v//7 for v in _channel_trx_data["UBRELVY"]["Mail"]["stly"]]}, "LTC": {"actuals": [0]*51, "stly": [0]*51}},
    "QULIPTA": {"Retail": {"actuals": [v//8 for v in _channel_trx_data["QULIPTA"]["Retail"]["actuals"]], "stly": [v//8 for v in _channel_trx_data["QULIPTA"]["Retail"]["stly"]]}, "Mail": {"actuals": [v//8 for v in _channel_trx_data["QULIPTA"]["Mail"]["actuals"]], "stly": [v//8 for v in _channel_trx_data["QULIPTA"]["Mail"]["stly"]]}, "LTC": {"actuals": [0]*51, "stly": [0]*51}},
}
ch_nurtec_nbrx = build_channel_chart(_channel_nbrx_data["NURTEC"], "NBRx", channel_dates)
ch_ubrelvy_nbrx = build_channel_chart(_channel_nbrx_data["UBRELVY"], "NBRx", channel_dates)
ch_qulipta_nbrx = build_channel_chart(_channel_nbrx_data["QULIPTA"], "NBRx", channel_dates)

# --- Acute/Preventive Brand Competitive View Data ---
_acute_trx_nurtec = [42069,46424,46491,44768,44867,44762,45629,46139,47127,40900,45892,46744,46279,47539,46154,46625,47249,47226,47556,46606,48564,42536,49107,50197,52476,42882,46424,46950,46929,47261,41853,46881,47739,45971,47033,48683,49414,48725,49002,47944,46846,49506,50627,49696,50373,50298,51726,48767,53186,52813,52695]
_acute_trx_nurtec_stly = [36449,40280,40280,40478,40109,40818,40965,41422,41898,37689,41451,42183,42095,42273,42493,42451,43890,43500,43666,43012,45158,37881,46394,47046,49016,39092,41249,39273,41577,38866,40321,41255,41338,40502,42610,42913,43374,42948,43494,43133,42848,42490,42561,44096,43592,43858,45181,40532,45569,45479,45461]
_acute_trx_ubrelvy = [46915,52669,52451,52006,51675,51154,52212,53120,53583,47297,52711,54052,53081,53805,52775,54010,55008,54929,55489,55467,57248,49838,57811,58371,60601,49217,52618,54573,54353,55027,47301,53573,54464,53437,53369,54970,54939,53714,53945,53044,51575,54232,54656,54327,54526,54493,55613,52066,57235,56792,56372]
_acute_trx_ubrelvy_stly = [39150,44302,44240,44582,43628,44216,44777,44819,44289,39483,45540,45601,44449,44835,44811,45335,45758,45449,47539,47213,48299,41099,48388,49246,50484,39785,44260,43267,46706,43088,44898,45493,45433,45234,47267,47604,48043,47274,47926,47788,47814,47927,47151,49885,49386,49495,50514,45657,51394,50990,51297]
_acute_nbrx_nurtec = [5937,6509,6884,6603,6872,6823,6853,7067,6906,5450,6529,6851,7059,7156,6956,7019,6973,7210,7172,7071,7367,6071,6463,7014,7267,5285,5106,6128,7180,7351,6651,7309,7559,7408,7738,7811,7804,7623,7738,7528,6881,7671,8050,7824,7766,7746,7697,6418,7338,7599,7682]
_acute_nbrx_nurtec_stly = [5218,5946,6208,6361,6601,6868,6902,6742,7149,5487,6620,6773,6828,7016,6921,6522,7129,7138,6817,6674,7213,5672,6053,7096,6967,4770,4472,5432,6473,6339,6892,6853,7010,6866,7307,7204,6999,7215,7147,7094,6843,6799,6675,6767,6817,6776,6684,5565,6804,7016,6654]
_acute_nbrx_ubrelvy = [6625,7206,7574,7702,7881,7435,7747,8090,7994,6001,7367,8031,7945,8067,7643,7885,7925,7996,7891,7974,8234,6799,7105,7750,8037,5657,5329,6533,7434,8083,6810,7753,8070,7885,8234,8118,8399,8139,8148,7953,7647,8024,8179,8326,8173,7915,7817,6597,7814,7929,8338]
_acute_nbrx_ubrelvy_stly = [5480,6234,6778,6739,6886,6811,6972,7224,6968,5637,6924,7035,7043,6811,6908,6755,6991,7352,7301,7034,7410,5669,6174,6846,6709,4494,4432,5540,6800,6437,7137,7178,7382,7343,7580,7719,7759,7370,7564,7286,7141,7243,7257,7362,7367,7392,7317,5937,7372,7503,7315]
_prev_trx_nurtec = [19564,21542,21071,21028,20847,20603,21253,21469,22064,19869,21618,21858,22001,22301,21758,22363,22154,22785,23404,23408,24342,21726,24163,23799,25079,20654,22307,22814,22758,23196,20502,23186,23760,23306,23306,23930,23800,23620,23506,23838,23845,23721,24258,23992,24320,24283,24973,23174,25275,25098,25042]
_prev_trx_nurtec_stly = [16942,18714,18666,18836,18353,18832,19130,19109,19037,17427,19288,19932,19650,19540,20002,19868,20475,20143,20389,19952,20897,17689,20857,19850,20574,16522,18070,17707,18942,17778,18307,19267,19008,19018,19774,19980,19964,19580,19738,19890,19852,19886,19752,20639,20543,20394,20840,19269,21298,21035,21032]
_prev_trx_qulipta = [33634,38203,37644,37185,37095,36942,37849,38149,38023,35039,38967,39040,38815,39233,38954,39189,39930,40231,40003,40091,41490,36278,42007,42236,42543,35298,37053,40706,40780,41470,35431,41358,41026,40385,40033,41422,42697,41453,41814,41720,41456,42623,42420,42918,42950,43211,44190,41111,45077,44585,44775]
_prev_trx_qulipta_stly = [25603,29529,29278,29334,28234,29028,29928,29928,30057,26744,30413,30650,30081,30558,30670,31475,31795,31621,32674,32377,33221,28882,34148,33867,34136,27511,30140,31507,33620,30743,31464,33150,33283,32506,33813,33886,34389,34109,34269,33903,34893,34522,34622,35937,35657,35870,36020,33300,36716,36816,36259]
_prev_nbrx_nurtec = [1569,1816,1970,1953,1938,1853,1832,1908,1998,1516,1857,1899,2024,2000,1935,1965,1992,2070,1995,2125,2178,1789,1831,1991,2178,1521,1486,1775,2078,2214,1953,2099,2358,2292,2289,2244,2201,2208,2219,2282,2128,2118,2222,2123,2108,2103,2089,1837,2101,2176,2199]
_prev_nbrx_nurtec_stly = [1503,1745,1879,1959,1998,1959,1997,1942,1878,1537,1835,1963,1986,1908,1924,1794,1968,2098,1945,1849,2077,1524,1645,1891,1914,1255,1153,1475,1876,1815,1863,1909,1966,1910,2071,2001,1981,1884,1977,1876,1829,1910,1882,1918,1880,1813,1869,1471,1882,1980,1860]
_prev_nbrx_qulipta = [3835,4289,4634,4500,4488,4394,4811,4875,4537,3758,4813,4833,4844,5006,4728,4759,4854,4820,4708,4982,5094,3944,4111,4503,4744,3275,2713,3902,4666,4680,4189,4820,4722,4706,4926,4938,4975,4935,5076,4751,4595,4769,4847,4890,4731,4847,4741,3793,4841,4852,4785]
_prev_nbrx_qulipta_stly = [2850,3501,3794,3908,3754,3857,4104,4299,4260,3389,4237,4271,4239,4213,4021,4202,4475,4565,4462,4266,4549,3476,3574,4102,4126,2608,2567,3519,4212,4192,4440,4407,4532,4367,4665,4588,4553,4505,4531,4349,4499,4311,4205,4564,4466,4334,4429,3525,4190,4343,4438]

def build_acute_prev_chart(brand1_act, brand1_stly, brand2_act, brand2_stly, brand1_name, brand2_name, brand1_color, brand2_color, metric_label, dates):
    fig_ap = go.Figure()
    fig_ap.add_trace(go.Scatter(x=dates, y=brand1_act, mode='lines', name=f'{brand1_name} Actuals', line=dict(color=brand1_color, width=2.5), hovertemplate=f'{brand1_name} Actuals<br>Week: %{{x|%d %b %y}}<br>{metric_label}: %{{y:,.0f}}<extra></extra>'))
    fig_ap.add_trace(go.Scatter(x=dates, y=brand1_stly, mode='lines', name=f'{brand1_name} STLY', line=dict(color=brand1_color, width=2, dash='dash'), hovertemplate=f'{brand1_name} STLY<br>Week: %{{x|%d %b}} 25<br>{metric_label}: %{{y:,.0f}}<extra></extra>'))
    fig_ap.add_trace(go.Scatter(x=dates, y=brand2_act, mode='lines', name=f'{brand2_name} Actuals', line=dict(color=brand2_color, width=2.5), hovertemplate=f'{brand2_name} Actuals<br>Week: %{{x|%d %b %y}}<br>{metric_label}: %{{y:,.0f}}<extra></extra>'))
    fig_ap.add_trace(go.Scatter(x=dates, y=brand2_stly, mode='lines', name=f'{brand2_name} STLY', line=dict(color=brand2_color, width=2, dash='dash'), hovertemplate=f'{brand2_name} STLY<br>Week: %{{x|%d %b}} 25<br>{metric_label}: %{{y:,.0f}}<extra></extra>'))
    fig_ap.update_layout(
        height=300, margin=dict(l=50, r=10, t=10, b=80),
        plot_bgcolor='white', paper_bgcolor='white',
        xaxis=dict(tickfont=dict(size=8, color='#374151', family='Inter, sans-serif'), tickformat='%d %b %y', tickangle=-90, dtick=14*24*60*60*1000, showgrid=False, hoverformat=''),
        yaxis=dict(tickfont=dict(size=8, color='#374151', family='Inter, sans-serif'), showgrid=False, tickformat=',.0f', rangemode='tozero'),
        legend=dict(orientation='h', yanchor='top', y=-0.32, xanchor='center', x=0.5, font=dict(size=8)),
        hovermode='closest',
        hoverlabel=dict(bgcolor='white', font=dict(size=11, color='#1a2332', family='Inter, sans-serif'), bordercolor='rgba(0,0,0,0)'),
        showlegend=False,
    )
    ap_html = fig_ap.to_html(full_html=False, include_plotlyjs=False, config={'displayModeBar': False, 'responsive': True})
    ap_html = ap_html.replace('class="plotly-graph-div" style="', 'class="plotly-graph-div" style="width:100%;')
    return ap_html

ap_dates = [week_to_date(w) for w in weeks]
# Build 4 Acute/Preventive charts
acute_trx_chart = build_acute_prev_chart(_acute_trx_nurtec, _acute_trx_nurtec_stly, _acute_trx_ubrelvy, _acute_trx_ubrelvy_stly, 'Nurtec Acute', 'Ubrelvy Acute', '#7C6CFC', '#4ADE80', 'TRx', ap_dates)
acute_nbrx_chart = build_acute_prev_chart(_acute_nbrx_nurtec, _acute_nbrx_nurtec_stly, _acute_nbrx_ubrelvy, _acute_nbrx_ubrelvy_stly, 'Nurtec Acute', 'Ubrelvy Acute', '#7C6CFC', '#4ADE80', 'NBRx', ap_dates)
prev_trx_chart = build_acute_prev_chart(_prev_trx_nurtec, _prev_trx_nurtec_stly, _prev_trx_qulipta, _prev_trx_qulipta_stly, 'Nurtec Prev', 'Qulipta Prev', '#7C6CFC', '#FB923C', 'TRx', ap_dates)
prev_nbrx_chart = build_acute_prev_chart(_prev_nbrx_nurtec, _prev_nbrx_nurtec_stly, _prev_nbrx_qulipta, _prev_nbrx_qulipta_stly, 'Nurtec Prev', 'Qulipta Prev', '#7C6CFC', '#FB923C', 'NBRx', ap_dates)

# --- Acute/Preventive Channel Data ---
# Nurtec Acute TRx channels
_nurtec_acute_trx_retail = [39213,43131,43340,41496,41603,41426,42228,42760,43594,37931,42554,43275,43056,44178,42955,43403,43972,43967,44166,43174,45091,39515,45416,46590,48602,39842,43178,43164,43187,43872,38458,43188,44055,42389,43332,44977,45794,44978,45423,44533,43284,45811,46705,46095,46435,46235,47848,45143,49069,48506,48817]
_nurtec_acute_trx_retail_stly = [32289,36083,36436,36695,36169,36404,36723,37165,37163,33644,37193,37392,37140,37869,37508,37950,38249,37746,38315,38693,39815,33693,40638,42059,43623,34863,37607,36569,38782,36078,37762,38601,38552,37962,39698,39983,40539,40154,40494,40352,39898,39687,39660,41149,40454,40839,41915,37694,42268,42543,42406]
_nurtec_acute_trx_mail = [2143,2445,2399,2481,2478,2512,2560,2573,2737,2226,2503,2597,2424,2544,2402,2380,2399,2465,2484,2524,2579,2271,2690,2662,2912,2219,2387,2783,2807,2559,2538,2712,2731,2678,2753,2678,2667,2762,2655,2366,2621,2700,2944,2667,2960,3094,2942,2627,3071,3309,2950]
_nurtec_acute_trx_mail_stly = [2974,3581,3193,3147,3263,3775,3556,3614,4064,3453,3598,4152,4313,3708,4303,3813,4989,5059,4648,3660,4666,3608,5014,4259,4692,3633,2978,2008,2056,2134,1862,1943,2061,1886,2208,2237,2049,2089,2264,2051,2255,2093,2179,2180,2435,2271,2458,2128,2485,2183,2316]
# Nurtec Acute NBRx channels
_nurtec_acute_nbrx_retail = [5698,6126,6559,6225,6488,6520,6573,6740,6589,5284,6266,6617,6792,6861,6710,6750,6695,6947,6918,6773,7093,5817,6201,6736,6958,5082,4928,5819,6777,7022,6347,6977,7242,7074,7379,7447,7447,7272,7340,7202,6518,7285,7627,7365,7320,7278,7247,6093,6976,7164,7287]
_nurtec_acute_nbrx_retail_stly = [4882,5543,5790,5991,6201,6314,6283,6198,6299,5077,6068,6126,6309,6506,6339,6125,6515,6385,6294,6292,6602,5240,5650,6574,6395,4488,4320,5205,6198,6101,6623,6560,6716,6588,6998,6923,6762,6924,6898,6838,6609,6531,6466,6514,6479,6524,6401,5354,6540,6786,6384]
_nurtec_acute_nbrx_mail = [240,383,325,377,385,304,279,327,317,167,262,233,267,295,246,270,278,263,254,298,274,254,262,278,309,203,177,309,402,329,304,332,318,335,359,364,356,351,398,326,363,386,422,459,446,469,450,324,362,435,395]
_nurtec_acute_nbrx_mail_stly = [336,403,418,370,400,554,619,544,850,410,552,647,519,509,581,398,614,753,523,382,612,431,403,522,572,283,153,227,275,238,269,293,294,278,309,282,237,291,249,256,234,269,209,253,338,252,283,211,264,229,270]
# Ubrelvy Acute TRx channels
_ubrelvy_acute_trx_retail = [43472,48674,48432,47984,47750,47301,48194,48929,49502,43698,48864,50015,49120,49739,48818,49673,50514,50399,51141,50933,52624,46135,52781,53738,55448,45302,48631,49932,49969,50864,42954,49022,50177,49242,49096,50731,50784,49726,49371,48837,47231,49560,49610,49857,50089,49733,50710,47719,52580,51900,51841]
_ubrelvy_acute_trx_retail_stly = [37145,41790,41833,42225,41122,41579,42222,42062,41634,37224,42774,42610,41735,42159,41748,42423,42691,42452,44519,44135,45183,38687,45206,45981,47128,37231,41508,40248,43539,40200,41782,42355,42316,42102,44151,44486,44750,43999,44520,44739,44240,44609,43902,46241,45864,45815,46640,42240,47702,47143,47430]
_ubrelvy_acute_trx_mail = [2803,3291,3295,3271,3141,3137,3300,3426,3300,2948,3077,3334,3193,3291,3159,3547,3718,3703,3463,3632,3747,2949,4062,3776,4187,3221,3131,3807,3425,3323,3545,3677,3398,3328,3367,3336,3254,3076,3611,3286,3415,3822,4101,3605,3462,3806,3868,3510,3727,3979,3499]
_ubrelvy_acute_trx_mail_stly = [1468,1884,1755,1685,1882,2000,1934,2139,2047,1687,2092,2352,2077,2072,2377,2231,2419,2327,2318,2404,2413,1917,2478,2599,2629,2054,2148,2347,2447,2303,2422,2496,2450,2528,2400,2423,2580,2642,2654,2380,2905,2686,2625,2941,2851,2922,3142,2788,2989,3165,3164]
# Ubrelvy Acute NBRx channels
_ubrelvy_acute_nbrx_retail = [6298,6738,7022,7207,7432,7153,7375,7657,7521,5722,7055,7709,7603,7619,7268,7425,7518,7535,7534,7603,7873,6469,6633,7290,7599,5364,5046,6157,7133,7620,6389,7387,7647,7487,7776,7774,7945,7686,7593,7553,7207,7589,7684,7893,7773,7541,7301,6218,7485,7492,7918]
_ubrelvy_acute_nbrx_retail_stly = [5272,5953,6499,6506,6618,6504,6712,6937,6654,5408,6638,6694,6695,6547,6596,6489,6695,7030,7059,6725,7134,5430,5951,6529,6420,4284,4240,5246,6504,6213,6770,6812,7054,6873,7277,7301,7318,7039,7119,6965,6757,6897,6900,7006,6957,6987,6932,5635,7051,7083,6937]
_ubrelvy_acute_nbrx_mail = [327,468,552,495,449,282,372,433,473,279,312,322,342,448,375,460,407,461,357,371,361,330,472,460,438,293,283,376,301,463,421,366,423,398,458,344,454,453,555,400,440,435,495,433,400,374,516,379,329,437,420]
_ubrelvy_acute_nbrx_mail_stly = [208,281,279,233,268,307,260,287,314,229,286,341,348,264,312,266,296,322,242,309,276,239,223,317,289,210,192,294,296,224,367,366,328,470,303,418,441,331,445,321,384,346,357,356,410,405,385,302,321,420,378]
# Nurtec Preventive TRx channels
_nurtec_prev_trx_retail = [18235,20013,19642,19492,19331,19068,19668,19898,20410,18426,20046,20236,20469,20725,20250,20817,20618,21213,21736,21683,22601,20182,22347,22088,23228,19190,20748,20975,20943,21533,18838,21359,21927,21491,21473,22109,22057,21805,21789,22142,22032,21950,22378,22254,22419,22322,23101,21453,23318,23051,23198]
_nurtec_prev_trx_retail_stly = [15009,16764,16884,17076,16550,16795,17148,17146,16886,15556,17306,17668,17337,17505,17656,17762,17843,17478,17890,17948,18425,15734,18269,17745,18311,14734,16475,16488,17668,16503,17146,18027,17727,17826,18423,18616,18660,18305,18376,18608,18484,18574,18406,19260,19064,18990,19333,17920,19756,19677,19618]
_nurtec_prev_trx_mail = [996,1135,1087,1166,1151,1156,1193,1197,1281,1082,1179,1214,1152,1194,1132,1142,1125,1189,1223,1267,1292,1160,1323,1262,1392,1069,1147,1352,1361,1256,1243,1341,1359,1358,1364,1316,1285,1339,1273,1176,1334,1293,1411,1287,1429,1494,1421,1249,1460,1572,1402]
_nurtec_prev_trx_mail_stly = [1382,1664,1479,1464,1493,1741,1661,1667,1846,1597,1674,1962,2014,1714,2025,1784,2327,2343,2171,1698,2159,1685,2254,1797,1970,1535,1304,906,936,976,846,908,947,886,1024,1042,943,953,1028,946,1045,980,1011,1020,1147,1056,1134,1012,1161,1009,1071]
# Nurtec Preventive NBRx channels
_nurtec_prev_nbrx_retail = [1505,1709,1877,1842,1829,1770,1758,1820,1906,1469,1783,1835,1948,1918,1867,1889,1912,1994,1924,2035,2097,1714,1757,1912,2085,1462,1435,1685,1962,2115,1864,2004,2258,2188,2183,2139,2101,2106,2105,2183,2016,2011,2106,1999,1987,1975,1967,1745,1997,2051,2086]
_nurtec_prev_nbrx_retail_stly = [1406,1627,1752,1845,1877,1801,1818,1785,1655,1422,1682,1776,1835,1770,1763,1684,1798,1877,1796,1743,1900,1409,1535,1752,1757,1180,1113,1413,1796,1747,1790,1828,1883,1833,1984,1922,1914,1808,1908,1808,1766,1834,1823,1846,1787,1746,1790,1415,1809,1916,1785]
_nurtec_prev_nbrx_mail = [63,107,93,112,108,82,75,88,92,46,75,65,76,82,68,75,80,76,71,90,81,75,74,79,93,59,52,90,117,99,89,95,99,103,106,105,101,102,114,99,112,107,117,124,121,127,122,93,104,125,113]
_nurtec_prev_nbrx_mail_stly = [97,118,127,114,121,158,179,157,223,115,153,187,151,139,162,109,170,221,149,106,176,116,110,139,157,74,39,62,80,68,73,81,83,77,87,78,67,76,69,68,63,75,59,72,93,67,79,56,73,65,75]
# Qulipta Preventive TRx channels
_qulipta_prev_trx_retail = [31001,35306,34733,34094,34044,33968,34958,35142,35056,32219,35911,35977,35664,36057,35824,36149,36596,36887,36687,36793,37954,33426,38424,38885,38991,32356,34104,37561,37481,38195,32175,37996,37827,37046,36707,38242,39072,38088,38325,38295,37895,38893,38816,39248,39147,39400,40419,37372,41176,40796,40708]
_qulipta_prev_trx_retail_stly = [23831,27402,27216,27305,26367,26942,27697,27785,27879,24783,28270,28423,27896,28376,28299,29167,29445,29277,30257,29941,30703,26791,31585,31394,31583,25470,27927,29291,31227,28426,29015,30698,30863,30147,31291,31384,31966,31706,31685,31464,32223,32049,31936,33260,32886,33063,33181,30718,33829,33990,33580]
_qulipta_prev_trx_mail = [1909,2155,2147,2219,2228,2193,2107,2150,2113,2058,2241,2168,2298,2247,2276,2178,2421,2464,2312,2329,2497,1984,2484,2301,2513,2088,1969,2149,2205,2195,2241,2310,2128,2335,2208,2167,2516,2300,2327,2337,2475,2620,2497,2526,2723,2698,2629,2623,2824,2640,2911]
_qulipta_prev_trx_mail_stly = [1257,1567,1500,1523,1354,1536,1620,1536,1600,1415,1580,1642,1617,1614,1738,1696,1788,1725,1810,1820,1899,1528,1868,1810,1881,1498,1560,1562,1700,1674,1713,1762,1717,1664,1806,1727,1723,1673,1837,1732,1961,1780,1887,1940,2067,2028,2029,1859,2093,2058,1946]
# Qulipta Preventive NBRx channels
_qulipta_prev_nbrx_retail = [3644,4037,4317,4238,4273,4174,4597,4685,4327,3606,4626,4641,4596,4783,4519,4547,4627,4577,4492,4716,4825,3786,3886,4295,4510,3138,2605,3730,4448,4464,3963,4572,4505,4492,4633,4722,4707,4682,4832,4520,4317,4513,4595,4657,4500,4602,4519,3545,4605,4641,4520]
_qulipta_prev_nbrx_retail_stly = [2686,3332,3629,3732,3616,3679,3936,4092,4090,3214,4062,4041,4040,4032,3801,3981,4301,4368,4236,4081,4322,3371,3390,3939,3921,2480,2442,3387,3994,3966,4206,4172,4303,4160,4418,4375,4341,4321,4281,4158,4257,4114,4006,4330,4197,4125,4194,3341,4013,4156,4274]
_qulipta_prev_nbrx_mail = [191,252,317,262,215,220,214,190,210,152,187,192,248,223,209,212,227,243,216,266,269,158,225,208,234,137,108,172,218,216,226,248,217,214,293,216,268,253,244,231,278,256,252,233,231,245,222,248,236,211,265]
_qulipta_prev_nbrx_mail_stly = [164,169,165,176,138,178,168,207,170,175,175,230,199,181,220,221,174,197,226,185,227,105,184,163,205,128,125,132,218,226,234,235,229,207,247,213,212,184,250,191,242,197,199,234,269,209,235,184,177,187,164]
# LTC channel data for Acute/Preventive (TRx only - NBRx is 0)
_nurtec_acute_trx_ltc = [714,848,753,790,786,824,841,805,796,743,835,872,799,816,797,842,878,794,905,909,895,751,1001,946,961,821,858,1003,935,830,858,982,953,903,947,1028,952,984,925,1045,941,996,978,934,978,968,935,996,1046,998,929]
_nurtec_acute_trx_ltc_stly = [1186,616,652,636,677,640,686,643,671,592,661,639,642,696,682,688,653,695,703,659,677,579,742,729,700,597,664,695,740,654,696,711,725,653,704,693,785,705,736,730,696,710,722,767,703,748,808,710,816,753,740]
_ubrelvy_acute_trx_ltc = [640,704,724,751,784,716,718,765,781,651,770,703,768,775,798,790,776,827,885,902,877,754,968,857,966,694,856,834,959,840,802,874,889,867,906,903,901,912,963,921,929,850,945,865,975,954,1035,837,928,913,1032]
_ubrelvy_acute_trx_ltc_stly = [537,628,652,672,624,637,621,618,608,572,674,639,637,604,686,681,648,670,702,674,703,495,704,666,727,500,604,672,720,585,694,642,667,604,716,695,713,633,752,669,669,632,624,703,671,758,732,629,703,682,703]
_nurtec_prev_trx_ltc = [332,394,341,371,365,379,392,375,373,361,393,408,380,383,376,404,411,383,446,457,448,383,493,448,460,395,413,487,454,407,420,485,474,458,470,505,459,477,443,520,479,477,469,451,472,468,452,473,497,475,441]
_nurtec_prev_trx_ltc_stly = [551,286,302,296,310,295,321,296,305,274,307,302,299,321,321,322,304,322,328,306,313,271,334,307,294,252,291,314,337,299,316,332,334,307,327,322,362,322,334,336,322,332,335,359,332,348,373,337,381,349,342]
_qulipta_prev_trx_ltc = [724,742,764,872,823,781,784,857,854,762,815,895,853,929,854,862,913,880,1004,969,1039,868,1099,1050,1039,854,980,996,1094,1080,1015,1052,1071,1004,1118,1013,1109,1065,1162,1088,1086,1110,1107,1144,1080,1113,1142,1116,1077,1149,1156]
_qulipta_prev_trx_ltc_stly = [515,560,562,506,513,550,611,607,578,546,563,585,568,568,633,612,562,619,607,616,619,563,695,663,672,543,653,654,693,643,736,690,703,695,716,775,700,730,747,707,709,693,799,737,704,779,810,723,794,768,733]

def build_ap_channel_chart(retail_act, retail_stly, mail_act, mail_stly, metric_label, dates, ltc_act=None, ltc_stly=None):
    if ltc_act is None:
        ltc_act = [0]*len(dates)
    if ltc_stly is None:
        ltc_stly = [0]*len(dates)
    fig_ch = go.Figure()
    fig_ch.add_trace(go.Scatter(x=dates, y=retail_act, mode='lines', name='Retail Actuals', line=dict(color='#0891b2', width=2.5), hovertemplate='Retail Actuals<br>Week: %{x|%d %b %y}<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    fig_ch.add_trace(go.Scatter(x=dates, y=retail_stly, mode='lines', name='Retail STLY', line=dict(color='#0891b2', width=2, dash='dash'), hovertemplate='Retail STLY<br>Week: %{x|%d %b %y}<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    fig_ch.add_trace(go.Scatter(x=dates, y=mail_act, mode='lines', name='Mail-Order Actuals', line=dict(color='#7c3aed', width=2.5), hovertemplate='Mail-Order Actuals<br>Week: %{x|%d %b %y}<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    fig_ch.add_trace(go.Scatter(x=dates, y=mail_stly, mode='lines', name='Mail-Order STLY', line=dict(color='#7c3aed', width=2, dash='dash'), hovertemplate='Mail-Order STLY<br>Week: %{x|%d %b %y}<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    fig_ch.add_trace(go.Scatter(x=dates, y=ltc_act, mode='lines', name='LTC Actuals', line=dict(color='#9ca3af', width=2.5), hovertemplate='LTC Actuals<br>Week: %{x|%d %b %y}<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    fig_ch.add_trace(go.Scatter(x=dates, y=ltc_stly, mode='lines', name='LTC STLY', line=dict(color='#9ca3af', width=2, dash='dash'), hovertemplate='LTC STLY<br>Week: %{x|%d %b %y}<br>' + metric_label + ': %{y:,.0f}<extra></extra>'))
    fig_ch.update_layout(
        height=300, margin=dict(l=50, r=10, t=10, b=80),
        plot_bgcolor='white', paper_bgcolor='white',
        xaxis=dict(tickfont=dict(size=8, color='#374151', family='Inter, sans-serif'), tickformat='%d %b %y', tickangle=-90, dtick=14*24*60*60*1000, showgrid=False, hoverformat=''),
        yaxis=dict(tickfont=dict(size=8, color='#374151', family='Inter, sans-serif'), showgrid=False, tickformat=',.0f', rangemode='tozero'),
        hovermode='closest',
        hoverlabel=dict(bgcolor='white', font=dict(size=11, color='#1a2332', family='Inter, sans-serif'), bordercolor='rgba(0,0,0,0)'),
        showlegend=False,
    )
    ch_html = fig_ch.to_html(full_html=False, include_plotlyjs=False, config={'displayModeBar': False, 'responsive': True})
    ch_html = ch_html.replace('class="plotly-graph-div" style="', 'class="plotly-graph-div" style="width:100%;')
    return ch_html

# Build 8 Acute/Preventive channel charts (4 brands x 2 metrics, side by side TRx|NBRx)
ap_ch_nurtec_acute_trx = build_ap_channel_chart(_nurtec_acute_trx_retail, _nurtec_acute_trx_retail_stly, _nurtec_acute_trx_mail, _nurtec_acute_trx_mail_stly, 'TRx', ap_dates, _nurtec_acute_trx_ltc, _nurtec_acute_trx_ltc_stly)
ap_ch_nurtec_acute_nbrx = build_ap_channel_chart(_nurtec_acute_nbrx_retail, _nurtec_acute_nbrx_retail_stly, _nurtec_acute_nbrx_mail, _nurtec_acute_nbrx_mail_stly, 'NBRx', ap_dates)
ap_ch_ubrelvy_acute_trx = build_ap_channel_chart(_ubrelvy_acute_trx_retail, _ubrelvy_acute_trx_retail_stly, _ubrelvy_acute_trx_mail, _ubrelvy_acute_trx_mail_stly, 'TRx', ap_dates, _ubrelvy_acute_trx_ltc, _ubrelvy_acute_trx_ltc_stly)
ap_ch_ubrelvy_acute_nbrx = build_ap_channel_chart(_ubrelvy_acute_nbrx_retail, _ubrelvy_acute_nbrx_retail_stly, _ubrelvy_acute_nbrx_mail, _ubrelvy_acute_nbrx_mail_stly, 'NBRx', ap_dates)
ap_ch_nurtec_prev_trx = build_ap_channel_chart(_nurtec_prev_trx_retail, _nurtec_prev_trx_retail_stly, _nurtec_prev_trx_mail, _nurtec_prev_trx_mail_stly, 'TRx', ap_dates, _nurtec_prev_trx_ltc, _nurtec_prev_trx_ltc_stly)
ap_ch_nurtec_prev_nbrx = build_ap_channel_chart(_nurtec_prev_nbrx_retail, _nurtec_prev_nbrx_retail_stly, _nurtec_prev_nbrx_mail, _nurtec_prev_nbrx_mail_stly, 'NBRx', ap_dates)
ap_ch_qulipta_prev_trx = build_ap_channel_chart(_qulipta_prev_trx_retail, _qulipta_prev_trx_retail_stly, _qulipta_prev_trx_mail, _qulipta_prev_trx_mail_stly, 'TRx', ap_dates, _qulipta_prev_trx_ltc, _qulipta_prev_trx_ltc_stly)
ap_ch_qulipta_prev_nbrx = build_ap_channel_chart(_qulipta_prev_nbrx_retail, _qulipta_prev_nbrx_retail_stly, _qulipta_prev_nbrx_mail, _qulipta_prev_nbrx_mail_stly, 'NBRx', ap_dates)





# --- Generate Interactive Chart with Plotly ---

nurtec_dates = [week_to_date(w) for w in nurtec_data['WEEK_ID']]
ubrelvy_dates = [week_to_date(w) for w in ubrelvy_data['WEEK_ID']]
qulipta_dates = [week_to_date(w) for w in qulipta_data['WEEK_ID']]

fig = go.Figure()

# Nurtec Actuals
fig.add_trace(go.Scatter(x=nurtec_dates, y=list(nurtec_data['ACTUALS']),
    mode='lines', name='Nurtec Actuals', line=dict(color='#7C6CFC', width=2.5),
    hovertemplate='Nurtec Actuals<br>Week: %{x|%d %b %y}<br>TRx: %{y:,.0f}<extra></extra>'))
# Nurtec STLY
fig.add_trace(go.Scatter(x=nurtec_dates, y=list(nurtec_data['STLY']),
    mode='lines', name='Nurtec STLY', line=dict(color='#7C6CFC', width=2, dash='dash'),
    hovertemplate='Nurtec STLY<br>STLY Week: %{x|%d %b} 25<br>TRx: %{y:,.0f}<extra></extra>'))
# Ubrelvy Actuals
fig.add_trace(go.Scatter(x=ubrelvy_dates, y=list(ubrelvy_data['ACTUALS']),
    mode='lines', name='Ubrelvy Actuals', line=dict(color='#4ADE80', width=2.5),
    hovertemplate='Ubrelvy Actuals<br>Week: %{x|%d %b %y}<br>TRx: %{y:,.0f}<extra></extra>'))
# Ubrelvy STLY
fig.add_trace(go.Scatter(x=ubrelvy_dates, y=list(ubrelvy_data['STLY']),
    mode='lines', name='Ubrelvy STLY', line=dict(color='#4ADE80', width=2, dash='dash'),
    hovertemplate='Ubrelvy STLY<br>STLY Week: %{x|%d %b} 25<br>TRx: %{y:,.0f}<extra></extra>'))
# Qulipta Actuals
fig.add_trace(go.Scatter(x=qulipta_dates, y=list(qulipta_data['ACTUALS']),
    mode='lines', name='Qulipta Actuals', line=dict(color='#FB923C', width=2.5),
    hovertemplate='Qulipta Actuals<br>Week: %{x|%d %b %y}<br>TRx: %{y:,.0f}<extra></extra>'))
# Qulipta STLY
fig.add_trace(go.Scatter(x=qulipta_dates, y=list(qulipta_data['STLY']),
    mode='lines', name='Qulipta STLY', line=dict(color='#FB923C', width=2, dash='dash'),
    hovertemplate='Qulipta STLY<br>STLY Week: %{x|%d %b} 25<br>TRx: %{y:,.0f}<extra></extra>'))
# Goal
goal_vals = [v if v is not None and v > 0 else None for v in list(nurtec_data['LATEST_GOAL'])]
fig.add_trace(go.Scatter(x=nurtec_dates, y=goal_vals,
    mode='lines', name='Goal', line=dict(color='#f472b6', width=2, dash='dashdot'),
    hovertemplate='Goal<br>Week: %{x|%d %b %y}<br>TRx: %{y:,.0f}<extra></extra>'))

fig.update_layout(
    height=340,
    margin=dict(l=60, r=20, t=35, b=100),
    plot_bgcolor='white',
    paper_bgcolor='white',
    xaxis=dict(
        tickfont=dict(size=9, color='#374151', family='Inter, sans-serif'),
        tickformat='%d %b %y',
        tickangle=-90,
        dtick=7*24*60*60*1000,
        gridcolor='rgba(0,0,0,0.04)',
        showgrid=False,
        hoverformat='',
    ),
    yaxis=dict(
        title=dict(text='TRx Volume', font=dict(size=10, color='#4b5563')),
        tickfont=dict(size=9, color='#374151', family='Inter, sans-serif'),
        gridcolor='rgba(0,0,0,0.06)',
        showgrid=False,
        tickformat=',',
        rangemode='tozero',
    ),
    legend=dict(
        orientation='h',
        yanchor='top',
        y=-0.35,
        xanchor='center',
        x=0.5,
        font=dict(size=9),
    ),
    hovermode='closest',
    hoverlabel=dict(
        bgcolor='white',
        font=dict(size=11, color='#1a2332', family='Inter, sans-serif'),
        bordercolor='rgba(0,0,0,0)',
    ),
)

# Export to HTML div (self-contained with plotly.js CDN)
chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn', config={'displayModeBar': False, 'responsive': True})
# Make chart div fill container width
chart_html = chart_html.replace('class="plotly-graph-div" style="', 'class="plotly-graph-div" style="width:100%;')
brand_chart_svg = chart_html





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
<style>
:root {
    --navy-900: #0000C9;
    --navy-800: #0000C9;
    --navy-700: #0000C9;
    --navy-600: #0000C9;
    --navy-500: #0000C9;
    --accent: #0EA5E9;
    
    --bg: #F0F4FA;
    --bg-2: #EFF6FF;
    --surface: #FFFFFF;
    --surface-2: #F8FAFD;
    --text: #1A1A1A;
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
    font-family: 'Pfizer Diatype Office', Arial, Helvetica, sans-serif;
    background: linear-gradient(160deg, #EFF6FF 0%, #F0F4FA 50%, #EEF2FF 100%);
    color: var(--text);
    line-height: 1.5;
    font-size: 14px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    overflow: hidden;
}

h1, h2, h3, h4 { font-family: 'Pfizer Diatype Office', Arial, Helvetica, sans-serif; font-weight: 800; letter-spacing: -0.015em; }
a { color: inherit; text-decoration: none; }

/* ───── APP SHELL ───── */
.app { height: 100vh; display: grid; grid-template-columns: var(--sidebar-w) 1fr; gap: var(--shell-pad); padding: var(--shell-pad); overflow: hidden; }

/* ───── SIDEBAR ───── */
.sidebar { position: relative; background: rgba(255,255,255,0.62); backdrop-filter: saturate(180%) blur(22px); -webkit-backdrop-filter: saturate(180%) blur(22px); border: 1px solid var(--hairline); border-radius: var(--panel-radius); box-shadow: var(--shadow-panel); display: flex; flex-direction: column; overflow: hidden; z-index: 10; }

.sidebar-brand { padding: 1.4rem 1.2rem 1.2rem; display: flex; flex-direction: column; gap: 0.7rem; }
.sidebar-brand img { height: 28px; align-self: flex-start; }
.sidebar-brand .title { font-family: 'Pfizer Diatype Office', Arial, Helvetica, sans-serif; font-weight: 800; font-size: 1.22rem; color: var(--navy-900); line-height: 1.18; letter-spacing: -0.025em; }
.sidebar-brand .subtitle { font-size: 0.72rem; color: var(--text-muted); font-weight: 500; }

.sidebar-divider { height: 1px; background: var(--hairline); margin: 0 0.85rem; }

.sidebar-section-label { font-family: 'Pfizer Diatype Office', Arial, Helvetica, sans-serif; font-size: 0.62rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--text-muted); padding: 0.95rem 1.15rem 0.4rem; }

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

.card-title { font-family: 'Pfizer Diatype Office', Arial, Helvetica, sans-serif; font-size: 1.02rem; font-weight: 700; color: var(--navy-900); line-height: 1.25; margin-bottom: 0.3rem; }
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
.hero-title { font-family: 'Pfizer Diatype Office', Arial, Helvetica, sans-serif; font-size: 1.65rem; font-weight: 800; color: var(--navy-900); letter-spacing: -0.025em; line-height: 1.15; margin-bottom: 0.35rem; }
.hero-subtitle { font-size: 0.82rem; font-weight: 500; color: var(--text-muted); display: flex; align-items: center; gap: 0.5rem; }
.hero-subtitle .dot { width: 4px; height: 4px; border-radius: 50%; background: var(--text-muted); opacity: 0.5; }
.hero-badge { display: inline-flex; align-items: center; gap: 0.4rem; font-size: 0.68rem; font-weight: 600; color: var(--navy-700); background: rgba(28,79,192,0.08); padding: 0.3rem 0.7rem; border-radius: 8px; flex-shrink: 0; margin-top: 0.2rem; }
.hero-badge svg { width: 12px; height: 12px; stroke: currentColor; fill: none; stroke-width: 2; }
.hero-kpis { display: grid; grid-template-columns: repeat(5, 1fr); gap: 0.75rem; }
.hero-kpi { background: #EEF5FB; border: 1px solid var(--hairline-2); border-radius: 12px; padding: 0.85rem 1rem 0.8rem; transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease); }
.hero-kpi:hover { transform: translateY(-2px); box-shadow: var(--shadow-md); }
.hero-kpi .kpi-label { font-size: 0.7rem; color: var(--text-muted); font-weight: 500; margin-bottom: 0.25rem; }
.hero-kpi .kpi-value { font-family: 'Pfizer Diatype Office', Arial, Helvetica, sans-serif; font-size: 1.5rem; font-weight: 700; color: var(--navy-900); line-height: 1.1; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; margin-bottom: 0.3rem; }
.hero-kpi .kpi-delta { display: inline-flex; align-items: center; gap: 0.25rem; font-size: 0.7rem; font-weight: 600; font-variant-numeric: tabular-nums; }
.hero-kpi .kpi-delta.up { color: var(--up); } .hero-kpi .kpi-delta.down { color: var(--down); } .hero-kpi .kpi-delta.flat { color: var(--flat); }
.hero-kpi .kpi-delta .tri { font-size: 0.65rem; line-height: 1; }
.hero-kpi .kpi-delta .vs { color: var(--text-muted); font-weight: 500; }

.workspace-divider { height: 1px; background: var(--hairline); margin: 1.4rem 0; }

/* ───── SUB-PANEL (full content area) ───── */
.sub-panel { display: none; }
.sub-panel.is-active { display: block; }
.sub-panel-title { font-family: 'Pfizer Diatype Office', Arial, Helvetica, sans-serif; font-size: 1.25rem; font-weight: 700; color: var(--navy-900); margin-bottom: 0.3rem; letter-spacing: -0.02em; }
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
    font-family: 'Pfizer Diatype Office', Arial, Helvetica, sans-serif;
    font-size: 0.78rem;
    color: var(--navy-700);
    font-weight: 500;
}
.toolbar-title strong { color: var(--navy-900); font-weight: 600; }
.toolbar-actions { display: flex; align-items: center; gap: 0.45rem; }

/* ????? KPI STRIP ????? */
.kpis-head {
    font-family: 'Pfizer Diatype Office', Arial, Helvetica, sans-serif;
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
    font-family: 'Pfizer Diatype Office', Arial, Helvetica, sans-serif;
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
                <div class="hero-kpi"><div class="kpi-label">Nurtec TRx</div><div class="kpi-value">1.81M</div><div class="kpi-delta up"><span class="tri">&#9650;</span>+16.3% <span class="vs">vs STLY</span></div></div>
                <div class="hero-kpi"><div class="kpi-label">Nurtec NBRx</div><div class="kpi-value">237K</div><div class="kpi-delta up"><span class="tri">&#9650;</span>+11.2% <span class="vs">vs STLY</span></div></div>
                <div class="hero-kpi"><div class="kpi-label">Nurtec oCGRP Mkt Share</div><div class="kpi-value">43.0%</div><div class="kpi-delta up"><span class="tri">&#9650;</span>+0.1pp <span class="vs">vs STLY</span></div></div>
                <div class="hero-kpi"><div class="kpi-label">Acute Nurtec oCGRP Share</div><div class="kpi-value">47.4%</div><div class="kpi-delta up"><span class="tri">&#9650;</span>+0.6pp <span class="vs">vs STLY</span></div></div>
                <div class="hero-kpi"><div class="kpi-label">Preventive Nurtec oCGRP Share</div><div class="kpi-value">36.2%</div><div class="kpi-delta down"><span class="tri">&#9660;</span>-0.3pp <span class="vs">vs STLY</span></div></div>
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
.nl-content .stat-tile .label { font-size: 13px; color: #374151; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; font-weight: 700; }
.nl-content .label { font-size: 13px; color: #374151; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; font-weight: 700; }
.nl-content .stat-tile .value { font-size: 28px; font-weight: 700; color: #1a2332; }
.nl-content .stat-tile .sub { font-size: 10px; color: #9ca3af; margin-top: 4px; }
.nl-content .sub { font-size: 10px; color: #9ca3af; margin-top: 4px; }
.nl-content .value { font-size: 28px; font-weight: 700; color: #1a2332; }
.nl-content table { width: 100%; border-collapse: collapse; font-size: 12px; table-layout: fixed; }
.nl-content th { text-align: left; padding: 10px 12px; border-bottom: 2px solid #e5e7eb; font-size: 10px; text-transform: uppercase; color: #6b7280; letter-spacing: 0.5px; font-weight: 600; }
.nl-content td { padding: 10px 12px; border-bottom: 1px solid #f3f4f6; }
.nl-content tr:last-child td { border-bottom: none; }
.nl-content table th:first-child, .nl-content table td:first-child { width: 18%; }
.nl-content table th:nth-child(2), .nl-content table td:nth-child(2) { width: 10%; }
.nl-content table th:nth-child(3), .nl-content table td:nth-child(3) { width: 10%; }
.nl-content table th:nth-child(4), .nl-content table td:nth-child(4) { width: 11%; }
.nl-content table th:nth-child(5), .nl-content table td:nth-child(5) { width: 9%; }
.nl-content table th:nth-child(6), .nl-content table td:nth-child(6) { width: 9%; }
.nl-content table th:nth-child(7), .nl-content table td:nth-child(7) { width: 9%; }
.nl-content table th:nth-child(8), .nl-content table td:nth-child(8) { width: 8%; }
.nl-content table th:nth-child(9), .nl-content table td:nth-child(9) { width: 8%; }
.nl-content table th:nth-child(10), .nl-content table td:nth-child(10) { width: 8%; }
.nl-content .pill-group { display: inline-flex; gap: 0; margin-bottom: 16px; border: 2px solid #0000C9; border-radius: 50px; overflow: hidden; }
.nl-content .pill { padding: 8px 20px; border: none; cursor: pointer; font-size: 12px; font-weight: 600; background: white; color: #0000C9; }
.nl-content .pill:first-child { border-radius: 50px 0 0 50px; }
.nl-content .pill:last-child { border-radius: 0 50px 50px 0; }
.nl-content .pill.active { background: #0000C9; color: white; }
.nl-content .pill-sm { padding: 6px 14px; font-size: 11px; }
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

    <!-- KPI CARDS ROW -->
    <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:16px;margin-bottom:32px;">
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);cursor:default;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div style="font-size:28px;font-weight:800;color:#0000C9;margin-bottom:6px;">48.2K</div>
        <div style="font-size:12px;font-weight:600;color:#374151;margin-bottom:2px;">Nurtec NBRx</div>
        <div style="font-size:11px;color:#16a34a;font-weight:600;">+3.1% WoW</div>
        <div style="font-size:10px;color:#9ca3af;margin-top:4px;">W/E Jun 19, 2026</div>
      </div>
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);cursor:default;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div style="font-size:28px;font-weight:800;color:#0000C9;margin-bottom:6px;">612.4K</div>
        <div style="font-size:12px;font-weight:600;color:#374151;margin-bottom:2px;">Nurtec TRx</div>
        <div style="font-size:11px;color:#16a34a;font-weight:600;">+2.4% WoW</div>
        <div style="font-size:10px;color:#9ca3af;margin-top:4px;">W/E Jun 19, 2026</div>
      </div>
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);cursor:default;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div style="font-size:28px;font-weight:800;color:#0000C9;margin-bottom:6px;">38.7%</div>
        <div style="font-size:12px;font-weight:600;color:#374151;margin-bottom:2px;">oCGRP TRx Share</div>
        <div style="font-size:11px;color:#16a34a;font-weight:600;">+0.2pp WoW</div>
        <div style="font-size:10px;color:#9ca3af;margin-top:4px;">National &middot; All Segments</div>
      </div>
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);cursor:default;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div style="font-size:28px;font-weight:800;color:#0000C9;margin-bottom:6px;">$28.4M</div>
        <div style="font-size:12px;font-weight:600;color:#374151;margin-bottom:2px;">Gross Sales W/E</div>
        <div style="font-size:11px;color:#16a34a;font-weight:600;">+2.8% WoW</div>
        <div style="font-size:10px;color:#9ca3af;margin-top:4px;">vs. $27.6M prior week</div>
      </div>
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);cursor:default;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div style="font-size:28px;font-weight:800;color:#0000C9;margin-bottom:6px;">93.6%</div>
        <div style="font-size:12px;font-weight:600;color:#374151;margin-bottom:2px;">YTD Goal Attainment</div>
        <div style="font-size:11px;color:#d97706;font-weight:600;">$112K behind pace</div>
        <div style="font-size:10px;color:#9ca3af;margin-top:4px;">TRx vs OP26</div>
      </div>
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);cursor:default;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div style="font-size:28px;font-weight:800;color:#0000C9;margin-bottom:6px;">128M</div>
        <div style="font-size:12px;font-weight:600;color:#374151;margin-bottom:2px;">Covered Lives w/ Access</div>
        <div style="font-size:11px;color:#16a34a;font-weight:600;">+1.2M vs prior month</div>
        <div style="font-size:10px;color:#9ca3af;margin-top:4px;">As of Jun 2026</div>
      </div>
    </div>

    <!-- PERFORMANCE INSIGHTS -->
    <div style="background:#ffffff;border:1px solid #e8ecf0;border-left:4px solid #0000C9;border-radius:8px;padding:24px 28px;margin-bottom:24px;">
      <div style="font-size:18px;font-weight:700;color:#1a2332;margin-bottom:6px;">Performance Insights</div>
      <div style="font-size:12px;color:#6b7280;margin-bottom:20px;">Key observations for week ending 06/19/2026 &middot; Numbers in bold update weekly</div>

      <div style="font-size:14px;font-weight:700;color:#1a2332;margin-bottom:4px;text-decoration:underline;">Weekly Insights</div>
      <div style="font-size:11px;color:#6b7280;margin-bottom:12px;">Week-over-week changes and weekly-level observations</div>
      <ul style="list-style-type:disc;padding-left:20px;margin-bottom:16px;color:#0000C9;">
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">Nurtec NBRx volume this week was <strong style="color:#0000C9;">48.2K</strong>, up <strong style="color:#0000C9;">+3.1%</strong> vs. prior week (46.7K) and <strong style="color:#0000C9;">+5.8%</strong> vs. same week last year.</span></li>
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">Nurtec TRx volume came in at <strong style="color:#0000C9;">612.4K</strong>, an increase of <strong style="color:#0000C9;">+2.4%</strong> WoW, with retail channel contributing <strong style="color:#0000C9;">+0.2pp</strong> share gain vs. same week last year.</span></li>
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">Nurtec oCGRP TRx market share moved to <strong style="color:#0000C9;">38.7%</strong> this week, up <strong style="color:#0000C9;">+0.2pp</strong> WoW. Ubrelvy flat at <strong style="color:#0000C9;">31.4%</strong>; Qulipta gained <strong style="color:#0000C9;">+0.1pp</strong> to <strong style="color:#0000C9;">24.8%</strong>.</span></li>
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">Acute oCGRP share for Nurtec at <strong style="color:#0000C9;">54.1%</strong> (<strong style="color:#0000C9;">+0.3pp</strong> WoW); Preventive share at <strong style="color:#0000C9;">21.2%</strong> (<strong style="color:#0000C9;">-0.1pp</strong> WoW).</span></li>
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">Gross sales for the week were <strong style="color:#0000C9;">$28.4M</strong>, up <strong style="color:#0000C9;">+2.8%</strong> vs. prior week ($27.6M). MTD attainment at <strong style="color:#0000C9;">94.4%</strong> vs. OP26.</span></li>
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">Preventive segment: Qulipta weekly volume grew <strong style="color:#0000C9;">+4.2%</strong> WoW vs. Nurtec Preventive at <strong style="color:#0000C9;">+1.1%</strong> WoW &#8212; gap widening by <strong style="color:#0000C9;">3.1pp</strong> this week.</span></li>
      </ul>

      <hr style="border:none;border-top:1px solid #e8ecf0;margin:24px 0;">

      <div style="font-size:14px;font-weight:700;color:#1a2332;margin-bottom:4px;text-decoration:underline;">Year to Date Insights</div>
      <div style="font-size:11px;color:#6b7280;margin-bottom:12px;">Cumulative performance statements as of week ending 06/19/2026</div>
      <ul style="list-style-type:disc;padding-left:20px;margin-bottom:16px;color:#0000C9;">
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">As of <strong style="color:#0000C9;">June 19, 2026</strong>, the oral CGRP TRx market is growing at <strong style="color:#0000C9;">17.0% YTD</strong> vs. same time last year, which is <strong style="color:#0000C9;">1.5%</strong> lower growth than the same time period in 2025 vs. 2024 (18.5%).</span></li>
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">Nurtec TRx is growing at <strong style="color:#0000C9;">16.3% YTD</strong>, which is <strong style="color:#0000C9;">2.7%</strong> higher than Nurtec's growth in 2025 by this point in the year (13.5%).</span></li>
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">Comparatively, Ubrelvy's YTD growth is <strong style="color:#0000C9;">14.0%</strong> (3.0% lower than in 2025), and Qulipta's is <strong style="color:#0000C9;">22.5%</strong> (9.0% lower than in 2025).</span></li>
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">Nurtec remains the market leader in Oral CGRP with <strong style="color:#0000C9;">43.0% TRx share YTD</strong> and <strong style="color:#0000C9;">43.3% NBRx share YTD</strong> (-0.3% TRx share and +0.5% NBRx share vs. same period last year).</span></li>
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">Ubrelvy has <strong style="color:#0000C9;">32.1%</strong> TRx share YTD and <strong style="color:#0000C9;">35.5%</strong> NBRx share YTD (-0.9% and -0.1% respectively vs. same time last year).</span></li>
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">Qulipta has <strong style="color:#0000C9;">24.8%</strong> TRx share YTD and <strong style="color:#0000C9;">21.2%</strong> NBRx share YTD (+1.1% and -0.3% respectively vs. same time last year).</span></li>
        <li style="margin-bottom:8px;font-size:13px;line-height:1.7;"><span style="color:#374151;">vs Budget: Nurtec TRx attainment is <strong style="color:#0000C9;">93.5% YTD</strong>; oCGRP TRx attainment is <strong style="color:#0000C9;">94.3% YTD</strong>.</span></li>
      </ul>
    </div>

    <!-- PERFORMANCE SNAPSHOT + ACCESS CHANGES -->
    <div style="display:flex;gap:20px;margin-bottom:24px;">
      <div style="flex:2;background:#ffffff;border:1px solid #e8ecf0;border-left:4px solid #0000C9;border-radius:8px;padding:24px 28px;">
        <div style="font-size:16px;font-weight:700;margin-bottom:4px;">Performance Snapshot</div>
        <div style="font-size:11px;color:#6b7280;margin-bottom:16px;">Week ending 06/19/2026 &middot; National</div>
        <table>
          <thead>
            <tr><th>METRIC</th><th style="text-align:right">LATEST WK</th><th style="text-align:right">R4W AVG</th><th style="text-align:right">YTD</th><th style="text-align:right">VS. GOAL</th><th style="text-align:right">VS. STLY</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Nurtec NBRx</strong></td><td style="text-align:right">48.2K</td><td style="text-align:right">46.8K</td><td style="text-align:right">1.21M</td><td style="text-align:right">97.8%</td><td style="text-align:right"><span class="delta-pos">+11.3%</span></td></tr>
            <tr><td><strong>Nurtec NRx</strong></td><td style="text-align:right">112.6K</td><td style="text-align:right">110.4K</td><td style="text-align:right">2.85M</td><td style="text-align:right">95.1%</td><td style="text-align:right"><span class="delta-pos">+14.2%</span></td></tr>
            <tr><td><strong>Nurtec TRx</strong></td><td style="text-align:right">612.4K</td><td style="text-align:right">601.8K</td><td style="text-align:right">15.9M</td><td style="text-align:right">93.6%</td><td style="text-align:right"><span class="delta-pos">+16.1%</span></td></tr>
            <tr><td><strong>Nurtec NBRx Share</strong></td><td style="text-align:right">21.2%</td><td style="text-align:right">21.0%</td><td style="text-align:right">20.9%</td><td style="text-align:right">—</td><td style="text-align:right"><span class="delta-pos">+1.3%</span></td></tr>
            <tr><td><strong>Nurtec NRx Share</strong></td><td style="text-align:right">33.4%</td><td style="text-align:right">33.2%</td><td style="text-align:right">33.0%</td><td style="text-align:right">—</td><td style="text-align:right"><span class="delta-pos">+1.1%</span></td></tr>
            <tr><td><strong>Nurtec TRx Share</strong></td><td style="text-align:right">38.7%</td><td style="text-align:right">38.5%</td><td style="text-align:right">38.1%</td><td style="text-align:right">—</td><td style="text-align:right"><span class="delta-pos">+1.4%</span></td></tr>
          </tbody>
        </table>
      </div>

      <div style="flex:1;background:#ffffff;border:1px solid #e8ecf0;border-left:4px solid #0000C9;border-radius:8px;padding:20px 24px;">
        <div style="font-size:16px;font-weight:700;margin-bottom:4px;">Access Change Lines</div>
        <div style="font-size:11px;color:#6b7280;margin-bottom:16px;">Only appears with material weekly access changes</div>
        <div style="margin-bottom:14px;">
          <div><strong>Louisiana Medicaid</strong></div>
          <div style="color:#6b7280;font-size:12px;">Nurtec removed from PDL &middot; est. <strong style="color:#0000C9;">-2,200 NRx</strong></div>
        </div>
        <div>
          <div><strong>UnitedHealth Commercial (IL)</strong></div>
          <div style="color:#6b7280;font-size:12px;">PA requirement added &middot; <strong style="color:#0000C9;">820K</strong> covered lives</div>
        </div>
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
        <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''"><div class="label">NRX MTD</div><div class="value" style="color:#0000C9;">486K</div><div class="sub delta-pos">+15.6%</div></div>
        <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''"><div class="label">NRX YTD</div><div class="value" style="color:#0000C9;">2.85M</div><div class="sub delta-pos">+16.1%</div></div>
        <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''"><div class="label">TRX MTD</div><div class="value" style="color:#0000C9;">2.41M</div><div class="sub delta-pos">+16.5%</div></div>
        <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''"><div class="label">TRX YTD</div><div class="value" style="color:#0000C9;">15.9M</div><div class="sub delta-pos">+16.1%</div></div>
      </div>
    </div>

    <div class="pill-group" id="xponent-metric-toggle" style="margin-bottom:16px;">
        <div class="pill pill-sm active" id="xp-trx-pill" onclick="switchXponentMetric('trx')">TRx</div>
        <div class="pill pill-sm" id="xp-nrx-pill" onclick="switchXponentMetric('nrx')">NRx</div>
      </div>
      <div class="row" style="margin-bottom:0;">
      
      <div class="card">
        <div class="card-title" data-xp-metric="{XM} Share Trend by Payer">TRx Share Trend by Payer</div>
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

    <div class="row">
      <div class="card">
      <div class="card-title">Payer Performance</div>
      <div class="card-subtitle">Share % · Latest Wk / WoW % / MTD / vs. STLY</div>
      <table>
        <thead>
          <tr><th>CUT</th><th style="text-align:right" data-xp-metric="WoW Mkt Share ({XM})">WoW Mkt Share (TRx)</th><th style="text-align:right" data-xp-metric="WoW Growth ({XM})">WoW Growth (TRx)</th><th style="text-align:right" data-xp-metric="MTD Mkt Share ({XM})">MTD Mkt Share (TRx)</th><th style="text-align:right" data-xp-metric="MTD Growth vs STLY ({XM})">MTD Growth vs STLY (TRx)</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>National</strong></td><td style="text-align:right">38.7%</td><td style="text-align:right"><span class="delta-pos">+0.1%</span></td><td style="text-align:right">38.5%</td><td style="text-align:right"><span class="delta-pos">+1.4%</span></td></tr>
          <tr><td><strong>Commercial</strong></td><td style="text-align:right">41.2%</td><td style="text-align:right"><span class="delta-pos">+0.2%</span></td><td style="text-align:right">41.0%</td><td style="text-align:right"><span class="delta-pos">+1.8%</span></td></tr>
          <tr><td><strong>Medicare</strong></td><td style="text-align:right">36.5%</td><td style="text-align:right"><span class="delta-pos">+0.1%</span></td><td style="text-align:right">36.3%</td><td style="text-align:right"><span class="delta-pos">+2.1%</span></td></tr>
          <tr><td><strong>Medicaid</strong></td><td style="text-align:right">26.4%</td><td style="text-align:right"><span class="delta-neg">-0.3%</span></td><td style="text-align:right">26.5%</td><td style="text-align:right"><span class="delta-neg">-0.7%</span></td></tr>
          <tr><td><strong>Other</strong></td><td style="text-align:right">22.1%</td><td style="text-align:right"><span class="delta-pos">+0.0%</span></td><td style="text-align:right">22.0%</td><td style="text-align:right"><span class="delta-pos">+0.4%</span></td></tr>
        </tbody>
      </table>
    </div>
      <div class="card">
      <div class="card-title">Channel Performance</div>
      <div class="card-subtitle">Share % · Latest Wk / WoW % / MTD / vs. STLY</div>
      <table>
        <thead>
          <tr><th>CUT</th><th style="text-align:right" data-xp-metric="WoW Mkt Share ({XM})">WoW Mkt Share (TRx)</th><th style="text-align:right" data-xp-metric="WoW Growth ({XM})">WoW Growth (TRx)</th><th style="text-align:right" data-xp-metric="MTD Mkt Share ({XM})">MTD Mkt Share (TRx)</th><th style="text-align:right" data-xp-metric="MTD Growth vs STLY ({XM})">MTD Growth vs STLY (TRx)</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>National</strong></td><td style="text-align:right">38.7%</td><td style="text-align:right"><span class="delta-pos">+0.1%</span></td><td style="text-align:right">38.5%</td><td style="text-align:right"><span class="delta-pos">+1.4%</span></td></tr>
          <tr><td><strong>Retail</strong></td><td style="text-align:right">39.4%</td><td style="text-align:right"><span class="delta-pos">+0.1%</span></td><td style="text-align:right">39.2%</td><td style="text-align:right"><span class="delta-pos">+1.5%</span></td></tr>
          <tr><td><strong>Mail-Order</strong></td><td style="text-align:right">31.8%</td><td style="text-align:right"><span class="delta-pos">+0.3%</span></td><td style="text-align:right">31.6%</td><td style="text-align:right"><span class="delta-pos">+2.3%</span></td></tr>
          <tr><td><strong>LTC</strong></td><td style="text-align:right">21.4%</td><td style="text-align:right"><span class="delta-neg">-0.1%</span></td><td style="text-align:right">21.5%</td><td style="text-align:right"><span class="delta-neg">-0.3%</span></td></tr>
        </tbody>
      </table>
    </div>
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
BRAND_CHART_DATA_PLACEHOLDER
          </svg>
        </div>
        
        
        
        <div class="footnote">Time period reference: Actuals 2026 w.e. 06/05/2026 · Same Time Last Year w.e. 06/06/2025</div>
      </div>

      <div class="card">
        <div class="card-header-row">
          <div>
            <div class="card-title" id="overall-ch-title" data-metric-toggle="Nurtec NPA — Channel Performance View ({M})">Nurtec NPA — Channel Performance View (TRx)</div>
            <div class="card-subtitle">National · IQVIA NPA · Retail / Mail-Order / LTC · Actuals 2026 vs Actuals 2025 (STLY)</div>
          </div>
          <div class="pill-group" style="margin-bottom:0;">
            <div class="pill pill-sm active" id="channel-nurtec" onclick="switchChannelBrand('nurtec')">Nurtec</div>
            <div class="pill pill-sm" id="channel-ubrelvy" onclick="switchChannelBrand('ubrelvy')">Ubrelvy</div>
            <div class="pill pill-sm" id="channel-qulipta" onclick="switchChannelBrand('qulipta')">Qulipta</div>
          </div>
        
        </div>
        CHANNEL_CHART_PLACEHOLDER
        
        
        <div class="footnote">Time period reference: Actuals 2026 w.e. 06/05/2026 · Same Time Last Year w.e. 06/06/2025</div>
      </div>

      <div class="brand-header brand-a"><span>NURTEC</span><span style="font-weight:400;margin-left:12px;" data-metric-toggle="{M} Volume · Growth (vs STLY) · oCGRP Market Share %">TRx Volume · Growth (vs STLY) · oCGRP Market Share %</span></div>
      <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
        <table>
          <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">QTD %</th><th style="text-align:right">YTD %</th><th style="text-align:right">WK MS</th><th style="text-align:right">QTD MS</th><th style="text-align:right">YTD MS</th></tr></thead>
          <tbody class="npa-table-trx">
            <tr><td>Actuals '26</td><td style="text-align:right">77,737</td><td style="text-align:right">896,296</td><td style="text-align:right">1,809,152</td><td style="text-align:right"><span class="delta-pos">+16.9%</span></td><td style="text-align:right"><span class="delta-pos">+16.5%</span></td><td style="text-align:right"><span class="delta-pos">+16.3%</span></td><td style="text-align:right">43.5%</td><td style="text-align:right">43.3%</td><td style="text-align:right">43.0%</td></tr>
            <tr><td>Actuals '25</td><td style="text-align:right">66,493</td><td style="text-align:right">835,126</td><td style="text-align:right">3,397,510</td><td style="text-align:right"><span class="delta-pos">+11.2%</span></td><td style="text-align:right"><span class="delta-pos">+11.4%</span></td><td style="text-align:right"><span class="delta-pos">+12.4%</span></td><td style="text-align:right">43.2%</td><td style="text-align:right">43.1%</td><td style="text-align:right">42.9%</td></tr>
            <tr><td>Latest Goal OP'26</td><td style="text-align:right">81,534</td><td style="text-align:right">685,559</td><td style="text-align:right">1,649,919</td><td style="text-align:right"><span class="delta-pos">+22.6%</span></td><td style="text-align:right"><span class="delta-neg">-10.9%</span></td><td style="text-align:right"><span class="delta-pos">+6.0%</span></td><td style="text-align:right">—</td><td style="text-align:right">—</td><td style="text-align:right">—</td></tr>
            <tr><td>Goal Attainment '26</td><td style="text-align:right">95.3%</td><td style="text-align:right">130.7%</td><td style="text-align:right">109.7%</td><td style="text-align:right">—</td><td style="text-align:right">—</td><td style="text-align:right">—</td><td style="text-align:right">—</td><td style="text-align:right">—</td><td style="text-align:right">—</td></tr>
          </tbody>
          <tbody class="npa-table-nbrx" style="display:none;">
            <tr><td>Actuals '26</td><td style="text-align:right">9,881</td><td style="text-align:right">115,686</td><td style="text-align:right">236,508</td><td style="text-align:right"><span class="delta-pos">+16.1%</span></td><td style="text-align:right"><span class="delta-pos">+12.7%</span></td><td style="text-align:right"><span class="delta-pos">+11.2%</span></td><td style="text-align:right">43.0%</td><td style="text-align:right">43.4%</td><td style="text-align:right">43.3%</td></tr>
            <tr><td>Actuals '25</td><td style="text-align:right">8,514</td><td style="text-align:right">111,462</td><td style="text-align:right">446,622</td><td style="text-align:right"><span class="delta-pos">+1.5%</span></td><td style="text-align:right"><span class="delta-pos">+3.9%</span></td><td style="text-align:right"><span class="delta-pos">+4.7%</span></td><td style="text-align:right">42.0%</td><td style="text-align:right">42.7%</td><td style="text-align:right">42.3%</td></tr>
          </tbody>
        </table>
      </div>

      <div class="brand-header brand-b" style="margin-top:16px;"><span>UBRELVY</span><span style="font-weight:400;margin-left:12px;" data-metric-toggle="{M} Volume · Growth (vs STLY) · oCGRP Market Share %">TRx Volume · Growth (vs STLY) · oCGRP Market Share %</span></div>
      <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
        <table>
          <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">QTD %</th><th style="text-align:right">YTD %</th><th style="text-align:right">WK MS</th><th style="text-align:right">QTD MS</th><th style="text-align:right">YTD MS</th></tr></thead>
          <tbody class="npa-table-trx">
            <tr><td>Actuals '26</td><td style="text-align:right">56,372</td><td style="text-align:right">654,931</td><td style="text-align:right">1,351,214</td><td style="text-align:right"><span class="delta-pos">+9.9%</span></td><td style="text-align:right"><span class="delta-pos">+11.1%</span></td><td style="text-align:right"><span class="delta-pos">+14.0%</span></td><td style="text-align:right">31.5%</td><td style="text-align:right">31.7%</td><td style="text-align:right">32.1%</td></tr>
            <tr><td>Actuals '25</td><td style="text-align:right">51,297</td><td style="text-align:right">640,379</td><td style="text-align:right">2,624,367</td><td style="text-align:right"><span class="delta-pos">+16.5%</span></td><td style="text-align:right"><span class="delta-pos">+16.0%</span></td><td style="text-align:right"><span class="delta-pos">+17.9%</span></td><td style="text-align:right">33.3%</td><td style="text-align:right">33.1%</td><td style="text-align:right">33.2%</td></tr>
          </tbody>
          <tbody class="npa-table-nbrx" style="display:none;">
            <tr><td>Actuals '26</td><td style="text-align:right">8,338</td><td style="text-align:right">94,712</td><td style="text-align:right">193,647</td><td style="text-align:right"><span class="delta-pos">+14.0%</span></td><td style="text-align:right"><span class="delta-pos">+9.5%</span></td><td style="text-align:right"><span class="delta-pos">+9.6%</span></td><td style="text-align:right">36.2%</td><td style="text-align:right">35.5%</td><td style="text-align:right">35.5%</td></tr>
            <tr><td>Actuals '25</td><td style="text-align:right">7,315</td><td style="text-align:right">93,778</td><td style="text-align:right">380,580</td><td style="text-align:right"><span class="delta-pos">+9.2%</span></td><td style="text-align:right"><span class="delta-pos">+7.9%</span></td><td style="text-align:right"><span class="delta-pos">+10.4%</span></td><td style="text-align:right">36.1%</td><td style="text-align:right">35.9%</td><td style="text-align:right">36.0%</td></tr>
          </tbody>
        </table>
      </div>

      <div class="brand-header brand-c" style="margin-top:16px;"><span>QULIPTA</span><span style="font-weight:400;margin-left:12px;" data-metric-toggle="{M} Volume · Growth (vs STLY) · oCGRP Market Share %">TRx Volume · Growth (vs STLY) · oCGRP Market Share %</span></div>
      <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
        <table>
          <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">QTD %</th><th style="text-align:right">YTD %</th><th style="text-align:right">WK MS</th><th style="text-align:right">QTD MS</th><th style="text-align:right">YTD MS</th></tr></thead>
          <tbody class="npa-table-trx">
            <tr><td>Actuals '26</td><td style="text-align:right">44,775</td><td style="text-align:right">517,036</td><td style="text-align:right">1,042,664</td><td style="text-align:right"><span class="delta-pos">+23.5%</span></td><td style="text-align:right"><span class="delta-pos">+21.8%</span></td><td style="text-align:right"><span class="delta-pos">+22.5%</span></td><td style="text-align:right">25.0%</td><td style="text-align:right">25.0%</td><td style="text-align:right">24.8%</td></tr>
            <tr><td>Actuals '25</td><td style="text-align:right">36,259</td><td style="text-align:right">460,078</td><td style="text-align:right">1,891,025</td><td style="text-align:right"><span class="delta-pos">+28.9%</span></td><td style="text-align:right"><span class="delta-pos">+30.6%</span></td><td style="text-align:right"><span class="delta-pos">+28.9%</span></td><td style="text-align:right">23.5%</td><td style="text-align:right">23.8%</td><td style="text-align:right">23.9%</td></tr>
          </tbody>
          <tbody class="npa-table-nbrx" style="display:none;">
            <tr><td>Actuals '26</td><td style="text-align:right">4,785</td><td style="text-align:right">56,442</td><td style="text-align:right">115,690</td><td style="text-align:right"><span class="delta-pos">+7.8%</span></td><td style="text-align:right"><span class="delta-pos">+9.3%</span></td><td style="text-align:right"><span class="delta-pos">+8.4%</span></td><td style="text-align:right">20.8%</td><td style="text-align:right">21.2%</td><td style="text-align:right">21.2%</td></tr>
            <tr><td>Actuals '25</td><td style="text-align:right">4,438</td><td style="text-align:right">56,087</td><td style="text-align:right">229,304</td><td style="text-align:right"><span class="delta-pos">+14.8%</span></td><td style="text-align:right"><span class="delta-pos">+14.1%</span></td><td style="text-align:right"><span class="delta-pos">+14.0%</span></td><td style="text-align:right">21.9%</td><td style="text-align:right">21.5%</td><td style="text-align:right">21.7%</td></tr>
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
          ACUTE_BRAND_CHART_PLACEHOLDER
        </div>

        <hr style="border:none;border-top:1.5px dashed rgba(0,0,201,0.25);margin:20px 0;">
        
        <div class="card">
          <div class="card-header-row">
            <div>
              <div class="card-title" id="acute-ch-title">Nurtec Acute &#8212; Channel Performance View</div>
              <div class="card-subtitle">National &middot; IQVIA NPA &middot; Retail / Mail-Order / LTC &middot; Actuals 2026 vs STLY</div>
            </div>
            <div class="pill-group" style="margin-bottom:0;">
              <div class="pill pill-sm active" id="acute-ch-nurtec" onclick="switchAcuteChannel('nurtec')">Nurtec</div>
              <div class="pill pill-sm" id="acute-ch-ubrelvy" onclick="switchAcuteChannel('ubrelvy')">Ubrelvy</div>
            </div>
          </div>
          ACUTE_CHANNEL_CHART_PLACEHOLDER
        </div>

        <hr style="border:none;border-top:1.5px dashed rgba(0,0,201,0.25);margin:20px 0;">

        <!-- Brand Tables: TRx left, NBRx right — aligned with charts above -->
        <div class="split-section">
          <div class="split-col">
            <div class="brand-header brand-a"><span>NURTEC ACUTE</span><span style="font-weight:400;margin-left:8px;">TRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">52,695</td><td style="text-align:right">604,478</td><td style="text-align:right">1,217,341</td><td style="text-align:right"><span class="delta-pos">+15.9%</span></td><td style="text-align:right">48.3%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">45,461</td><td style="text-align:right">570,048</td><td style="text-align:right">2,312,576</td><td style="text-align:right"><span class="delta-pos">+10.5%</span></td><td style="text-align:right">47.0%</td></tr>
                </tbody>
              </table>
            </div>

            <div class="brand-header brand-b" style="margin-top:12px;"><span>UBRELVY ACUTE</span><span style="font-weight:400;margin-left:8px;">TRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">56,372</td><td style="text-align:right">654,931</td><td style="text-align:right">1,351,214</td><td style="text-align:right"><span class="delta-pos">+9.9%</span></td><td style="text-align:right">51.7%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">51,297</td><td style="text-align:right">640,379</td><td style="text-align:right">2,624,367</td><td style="text-align:right"><span class="delta-pos">+16.5%</span></td><td style="text-align:right">53.0%</td></tr>
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
                  <tr><td>Actuals '26</td><td style="text-align:right">7,682</td><td style="text-align:right">90,200</td><td style="text-align:right">183,606</td><td style="text-align:right"><span class="delta-pos">+15.4%</span></td><td style="text-align:right">48.0%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">6,654</td><td style="text-align:right">87,392</td><td style="text-align:right">348,969</td><td style="text-align:right"><span class="delta-pos">+6.6%</span></td><td style="text-align:right">47.6%</td></tr>
                </tbody>
              </table>
            </div>

            <div class="brand-header brand-b" style="margin-top:12px;"><span>UBRELVY ACUTE</span><span style="font-weight:400;margin-left:8px;">NBRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">8,338</td><td style="text-align:right">94,712</td><td style="text-align:right">193,647</td><td style="text-align:right"><span class="delta-pos">+14.0%</span></td><td style="text-align:right">52.0%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">7,315</td><td style="text-align:right">93,778</td><td style="text-align:right">380,580</td><td style="text-align:right"><span class="delta-pos">+9.2%</span></td><td style="text-align:right">52.4%</td></tr>
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

          PREV_BRAND_CHART_PLACEHOLDER
        </div>

        
        <div class="card">
          <div class="card-header-row">
            <div>
              <div class="card-title" id="prev-ch-title">Nurtec Preventive &#8212; Channel Performance View</div>
              <div class="card-subtitle">National &middot; IQVIA NPA &middot; Retail / Mail-Order / LTC &middot; Actuals 2026 vs STLY</div>
            </div>
            <div class="pill-group" style="margin-bottom:0;">
              <div class="pill pill-sm active" id="prev-ch-nurtec" onclick="switchPrevChannel('nurtec')">Nurtec</div>
              <div class="pill pill-sm" id="prev-ch-qulipta" onclick="switchPrevChannel('qulipta')">Qulipta</div>
            </div>
          </div>
          PREV_CHANNEL_CHART_PLACEHOLDER
        </div>

        <!-- Preventive tables: TRx left, NBRx right -->
        <div class="split-section">
          <div class="split-col">
            <div class="brand-header brand-a"><span>NURTEC PREVENTIVE</span><span style="font-weight:400;margin-left:8px;">TRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">25,042</td><td style="text-align:right">291,818</td><td style="text-align:right">591,811</td><td style="text-align:right"><span class="delta-pos">+19.1%</span></td><td style="text-align:right">35.9%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">21,032</td><td style="text-align:right">265,078</td><td style="text-align:right">1,084,934</td><td style="text-align:right"><span class="delta-pos">+12.5%</span></td><td style="text-align:right">36.7%</td></tr>
                </tbody>
              </table>
            </div>

            <div class="brand-header brand-c" style="margin-top:12px;"><span>QULIPTA PREVENTIVE</span><span style="font-weight:400;margin-left:8px;">TRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">44,775</td><td style="text-align:right">517,036</td><td style="text-align:right">1,042,664</td><td style="text-align:right"><span class="delta-pos">+23.5%</span></td><td style="text-align:right">64.1%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">36,259</td><td style="text-align:right">460,078</td><td style="text-align:right">1,891,025</td><td style="text-align:right"><span class="delta-pos">+28.9%</span></td><td style="text-align:right">63.3%</td></tr>
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
                  <tr><td>Actuals '26</td><td style="text-align:right">2,199</td><td style="text-align:right">25,486</td><td style="text-align:right">52,902</td><td style="text-align:right"><span class="delta-pos">+18.2%</span></td><td style="text-align:right">31.5%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">1,860</td><td style="text-align:right">24,070</td><td style="text-align:right">97,653</td><td style="text-align:right"><span class="delta-neg">-13.2%</span></td><td style="text-align:right">29.5%</td></tr>
                </tbody>
              </table>
            </div>

            <div class="brand-header brand-c" style="margin-top:12px;"><span>QULIPTA PREVENTIVE</span><span style="font-weight:400;margin-left:8px;">NBRx Volume · Growth · MS</span></div>
            <div class="card" style="border-top-left-radius:0;border-top-right-radius:0;margin-top:-1px;">
              <table>
                <thead><tr><th></th><th style="text-align:right">LATEST WK</th><th style="text-align:right">QTD</th><th style="text-align:right">YTD</th><th style="text-align:right">WK %</th><th style="text-align:right">WK MS</th></tr></thead>
                <tbody>
                  <tr><td>Actuals '26</td><td style="text-align:right">4,785</td><td style="text-align:right">56,442</td><td style="text-align:right">115,690</td><td style="text-align:right"><span class="delta-pos">+7.8%</span></td><td style="text-align:right">68.5%</td></tr>
                  <tr><td>Actuals '25</td><td style="text-align:right">4,438</td><td style="text-align:right">56,087</td><td style="text-align:right">229,304</td><td style="text-align:right"><span class="delta-pos">+14.8%</span></td><td style="text-align:right">70.5%</td></tr>
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
        <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
          <div class="label">ACCESS GAIN PLANS</div>
          <div class="value" style="color:#16a34a;">7</div>
          <div class="sub">gain events since Jan 2025</div>
        </div>
        <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
          <div class="label">ACCESS LOSS / RESTRICTION</div>
          <div class="value" style="color:#dc2626;">4</div>
          <div class="sub">loss / restriction events</div>
        </div>
        <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
          <div class="label">CONTROL GROUP</div>
          <div class="value" style="color:#0000C9;">38</div>
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
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div class="label">GROSS SALES W/E 06/19</div>
        <div class="value" style="color:#0000C9;">$28.4M</div>
        <div class="sub"><span class="delta-pos">+2.8%</span>&nbsp;&nbsp;WoW · +$0.8M</div>
      </div>
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div class="label">MTD ATTAINMENT VS OP26</div>
        <div class="value" style="color:#0000C9;">94.4%</div>
        <div class="sub">$1.6M behind MTD plan</div>
      </div>
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div class="label">YTD ATTAINMENT VS OP26</div>
        <div class="value" style="color:#0000C9;">93.6%</div>
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
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div class="label">NET SALES W/E 06/19</div>
        <div class="value" style="color:#0000C9;">$18.6M</div>
        <div class="sub"><span class="delta-pos">+3.1%</span>&nbsp;&nbsp;WoW · +$0.8M</div>
      </div>
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div class="label">NET MTD ATTAINMENT VS OP26</div>
        <div class="value" style="color:#0000C9;">92.1%</div>
        <div class="sub">$2.1M behind MTD plan</div>
      </div>
      <div style="background:#EEF5FB;border-radius:12px;padding:14px 16px;text-align:left;border:1px solid rgba(15,23,42,0.05);transition:transform 0.25s cubic-bezier(0.16,1,0.3,1),box-shadow 0.25s cubic-bezier(0.4,0,0.2,1);flex:1;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(15,23,42,0.07),0 2px 4px rgba(15,23,42,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div class="label">NET YTD ATTAINMENT VS OP26</div>
        <div class="value" style="color:#0000C9;">91.8%</div>
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
        
        newsletterSub.querySelectorAll('.nav-sub-item').forEach(function(s) { s.classList.remove('active'); });
    }

    function enterDeepdive(panelId) {
        inDeepdive = true;
        nlGridView.style.display = 'none';
        nlDeepdiveView.style.display = '';
        newsletterSub.classList.add('is-open');
        heroEl.style.display = 'none';
        dividerEl.style.display = 'none';
        
        // Activate the correct nl-tab
        nlDeepdiveView.querySelectorAll('.nl-tab').forEach(function(p) { p.classList.remove('active'); });
        var target = document.getElementById(panelId + '-tab');
        if (target) target.classList.add('active');
        // Activate the correct sub-nav item
        newsletterSub.querySelectorAll('.nav-sub-item').forEach(function(s) { s.classList.remove('active'); });
        var matchingSub = newsletterSub.querySelector('[data-panel="' + panelId + '"]');
        if (matchingSub) matchingSub.classList.add('active');
        // Trigger resize for Plotly charts
        setTimeout(function() { window.dispatchEvent(new Event('resize')); }, 100);
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
            // Trigger resize for Plotly charts
            window.dispatchEvent(new Event('resize'));
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
        var pills = document.querySelectorAll('#npa-subtabs .pill');
        pills.forEach(function(el) { el.classList.remove('active'); });
        if (subtab === 'retail') {
            pills[0].classList.add('active');
            document.getElementById('npa-retail').style.display = 'block';
            document.getElementById('npa-acute-prev').style.display = 'none';
        } else {
            pills[1].classList.add('active');
            document.getElementById('npa-retail').style.display = 'none';
            document.getElementById('npa-acute-prev').style.display = 'block';
            window.dispatchEvent(new Event('resize'));
            setTimeout(function(){ window.dispatchEvent(new Event('resize')); }, 300);
        }
    };
    window.switchAcutePrev = function(view) {
        var pills = document.querySelectorAll('#acute-prev-toggle .pill');
        pills.forEach(function(el) { el.classList.remove('active'); });
        if (view === 'acute') {
            pills[0].classList.add('active');
            document.getElementById('acute-view').style.display = 'block';
            document.getElementById('preventive-view').style.display = 'none';
        } else {
            pills[1].classList.add('active');
            document.getElementById('acute-view').style.display = 'none';
            document.getElementById('preventive-view').style.display = 'block';
        }
        window.dispatchEvent(new Event('resize'));
        setTimeout(function(){ window.dispatchEvent(new Event('resize')); }, 300);
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
    
    window.switchAcuteChannel = function(brand) {
        document.getElementById('acute-ch-nurtec').classList.toggle('active', brand === 'nurtec');
        document.getElementById('acute-ch-ubrelvy').classList.toggle('active', brand === 'ubrelvy');
        var label = brand === 'nurtec' ? 'Nurtec' : 'Ubrelvy';
        document.getElementById('acute-ch-title').innerHTML = label + ' Acute &#8212; Channel Performance View';
        document.getElementById('ap-ch-nurtec-acute').style.display = brand === 'nurtec' ? 'block' : 'none';
        document.getElementById('ap-ch-ubrelvy-acute').style.display = brand === 'ubrelvy' ? 'block' : 'none';
        window.dispatchEvent(new Event('resize'));
    };
    window.switchPrevChannel = function(brand) {
        document.getElementById('prev-ch-nurtec').classList.toggle('active', brand === 'nurtec');
        document.getElementById('prev-ch-qulipta').classList.toggle('active', brand === 'qulipta');
        var label = brand === 'nurtec' ? 'Nurtec' : 'Qulipta';
        document.getElementById('prev-ch-title').innerHTML = label + ' Preventive &#8212; Channel Performance View';
        document.getElementById('ap-ch-nurtec-prev').style.display = brand === 'nurtec' ? 'block' : 'none';
        document.getElementById('ap-ch-qulipta-prev').style.display = brand === 'qulipta' ? 'block' : 'none';
        window.dispatchEvent(new Event('resize'));
    };
    window.switchChannelBrand = function(brand) {
        document.getElementById('channel-nurtec').classList.toggle('active', brand === 'nurtec');
        document.getElementById('channel-ubrelvy').classList.toggle('active', brand === 'ubrelvy');
        document.getElementById('channel-qulipta').classList.toggle('active', brand === 'qulipta');
        var labels = {'nurtec':'Nurtec','ubrelvy':'Ubrelvy','qulipta':'Qulipta'};
        var el = document.getElementById('overall-ch-title');
        var metric = document.getElementById('npa-trx-pill').classList.contains('active') ? 'TRx' : 'NBRx';
        if (el) {
            el.innerHTML = labels[brand] + ' NPA &#8212; Channel Performance View (' + metric + ')';
            el.setAttribute('data-metric-toggle', labels[brand] + ' NPA &#8212; Channel Performance View ({M})');
        }
        // Switch channel chart based on brand + current metric
        var metric = document.getElementById('npa-trx-pill').classList.contains('active') ? 'trx' : 'nbrx';
        var brands = ['nurtec','ubrelvy','qulipta'];
        brands.forEach(function(b) {
            var trxEl = document.getElementById('ch-' + b + '-trx');
            var nbrxEl = document.getElementById('ch-' + b + '-nbrx');
            if (trxEl) trxEl.style.display = (b === brand && metric === 'trx') ? 'block' : 'none';
            if (nbrxEl) nbrxEl.style.display = (b === brand && metric === 'nbrx') ? 'block' : 'none';
        });
        window.dispatchEvent(new Event('resize'));
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
        // Toggle TRx/NBRx charts
        var trxChart = document.getElementById('trx-brand-chart');
        var nbrxChart = document.getElementById('nbrx-brand-chart');
        if (trxChart && nbrxChart) {
            trxChart.style.display = metric === 'trx' ? 'block' : 'none';
            nbrxChart.style.display = metric === 'nbrx' ? 'block' : 'none';
        }
        // Toggle channel charts based on metric + current brand
        var brands = ['nurtec','ubrelvy','qulipta'];
        var activeBrand = 'nurtec';
        var chNurtec = document.getElementById('channel-nurtec');
        var chUbrelvy = document.getElementById('channel-ubrelvy');
        var chQulipta = document.getElementById('channel-qulipta');
        if (chNurtec && chNurtec.classList.contains('active')) activeBrand = 'nurtec';
        if (chUbrelvy && chUbrelvy.classList.contains('active')) activeBrand = 'ubrelvy';
        if (chQulipta && chQulipta.classList.contains('active')) activeBrand = 'qulipta';
        brands.forEach(function(b) {
            var trxEl = document.getElementById('ch-' + b + '-trx');
            var nbrxEl = document.getElementById('ch-' + b + '-nbrx');
            if (trxEl) trxEl.style.display = (b === activeBrand && metric === 'trx') ? 'block' : 'none';
            if (nbrxEl) nbrxEl.style.display = (b === activeBrand && metric === 'nbrx') ? 'block' : 'none';
        });
        // Toggle NPA table tbody (TRx/NBRx)
        document.querySelectorAll('.npa-table-trx').forEach(function(el) {
            el.style.display = metric === 'trx' ? '' : 'none';
        });
        document.querySelectorAll('.npa-table-nbrx').forEach(function(el) {
            el.style.display = metric === 'nbrx' ? '' : 'none';
        });
        window.dispatchEvent(new Event('resize'));
    };
    // Initial resize trigger for Plotly - staggered to ensure charts fill width on first load
    function resizeAllPlotly() {
        window.dispatchEvent(new Event('resize'));
        document.querySelectorAll('.plotly-graph-div').forEach(function(gd) {
            if (gd && gd.data && typeof Plotly !== 'undefined') { Plotly.Plots.resize(gd); }
        });
    }
    setTimeout(resizeAllPlotly, 300);
    setTimeout(resizeAllPlotly, 800);
    setTimeout(resizeAllPlotly, 1500);
})();
</script>
</body>
</html>
"""

# Inject live Plotly chart - replace the entire chart container
trx_nbrx_html = '<div id="trx-brand-chart" style="width:100%;overflow:hidden;">' + brand_chart_svg + '</div><div id="nbrx-brand-chart" style="width:100%;overflow:hidden;display:none;">' + nbrx_chart_svg + '</div>'
html_content = html_content.replace('<div class="chart-container">\n          <svg class="chart" preserveAspectRatio="none" viewBox="0 0 800 250">\nBRAND_CHART_DATA_PLACEHOLDER\n          </svg>\n        </div>', trx_nbrx_html)

# Channel chart injection (6 divs: 3 brands x 2 metrics, only nurtec-trx visible initially)
channel_html = '<div id="ch-nurtec-trx" style="width:100%;overflow:hidden;">' + ch_nurtec_trx + '</div>'
channel_html += '<div id="ch-nurtec-nbrx" style="width:100%;overflow:hidden;display:none;">' + ch_nurtec_nbrx + '</div>'
channel_html += '<div id="ch-ubrelvy-trx" style="width:100%;overflow:hidden;display:none;">' + ch_ubrelvy_trx + '</div>'
channel_html += '<div id="ch-ubrelvy-nbrx" style="width:100%;overflow:hidden;display:none;">' + ch_ubrelvy_nbrx + '</div>'
channel_html += '<div id="ch-qulipta-trx" style="width:100%;overflow:hidden;display:none;">' + ch_qulipta_trx + '</div>'
channel_html += '<div id="ch-qulipta-nbrx" style="width:100%;overflow:hidden;display:none;">' + ch_qulipta_nbrx + '</div>'
# Acute Channel chart injection (brand toggle: nurtec/ubrelvy, side by side TRx|NBRx)
acute_ch_legend = '<div class="legend" style="margin-top:8px;justify-content:center;"><div class="legend-item"><div class="legend-dot" style="background:#0891b2"></div>Retail Actuals</div><div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#0891b2" stroke-width="2" stroke-dasharray="3"/></svg>Retail STLY</div><div class="legend-item"><div class="legend-dot" style="background:#7c3aed"></div>Mail-Order Actuals</div><div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#7c3aed" stroke-width="2" stroke-dasharray="3"/></svg>Mail-Order STLY</div><div class="legend-item"><div class="legend-dot" style="background:#9ca3af"></div>LTC Actuals</div><div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#9ca3af" stroke-width="2" stroke-dasharray="3"/></svg>LTC STLY</div></div>'
acute_ch_html = '<div id="ap-ch-nurtec-acute" style="width:100%;"><div class="split-section"><div class="split-col"><div class="section-label">TRx</div>' + ap_ch_nurtec_acute_trx + '</div><div class="split-col"><div class="section-label">NBRx</div>' + ap_ch_nurtec_acute_nbrx + '</div></div></div>'
acute_ch_html += '<div id="ap-ch-ubrelvy-acute" style="width:100%;display:none;"><div class="split-section"><div class="split-col"><div class="section-label">TRx</div>' + ap_ch_ubrelvy_acute_trx + '</div><div class="split-col"><div class="section-label">NBRx</div>' + ap_ch_ubrelvy_acute_nbrx + '</div></div></div>'
acute_ch_html += acute_ch_legend
html_content = html_content.replace('ACUTE_CHANNEL_CHART_PLACEHOLDER', acute_ch_html)

# Preventive Channel chart injection (brand toggle: nurtec/qulipta, side by side TRx|NBRx)
prev_ch_legend = '<div class="legend" style="margin-top:8px;justify-content:center;"><div class="legend-item"><div class="legend-dot" style="background:#0891b2"></div>Retail Actuals</div><div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#0891b2" stroke-width="2" stroke-dasharray="3"/></svg>Retail STLY</div><div class="legend-item"><div class="legend-dot" style="background:#7c3aed"></div>Mail-Order Actuals</div><div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#7c3aed" stroke-width="2" stroke-dasharray="3"/></svg>Mail-Order STLY</div><div class="legend-item"><div class="legend-dot" style="background:#9ca3af"></div>LTC Actuals</div><div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#9ca3af" stroke-width="2" stroke-dasharray="3"/></svg>LTC STLY</div></div>'
prev_ch_html = '<div id="ap-ch-nurtec-prev" style="width:100%;"><div class="split-section"><div class="split-col"><div class="section-label">TRx</div>' + ap_ch_nurtec_prev_trx + '</div><div class="split-col"><div class="section-label">NBRx</div>' + ap_ch_nurtec_prev_nbrx + '</div></div></div>'
prev_ch_html += '<div id="ap-ch-qulipta-prev" style="width:100%;display:none;"><div class="split-section"><div class="split-col"><div class="section-label">TRx</div>' + ap_ch_qulipta_prev_trx + '</div><div class="split-col"><div class="section-label">NBRx</div>' + ap_ch_qulipta_prev_nbrx + '</div></div></div>'
prev_ch_html += prev_ch_legend
html_content = html_content.replace('PREV_CHANNEL_CHART_PLACEHOLDER', prev_ch_html)

# NPA Overall channel chart injection (must come AFTER acute/prev channel replacements)
html_content = html_content.replace('CHANNEL_CHART_PLACEHOLDER', channel_html)

# Acute/Preventive chart injection - side by side TRx | NBRx
acute_legend = '<div class="legend" style="margin-top:8px;justify-content:center;"><div class="legend-item"><div class="legend-dot" style="background:#7C6CFC"></div>Nurtec Acute Actuals</div><div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#7C6CFC" stroke-width="2" stroke-dasharray="3"/></svg>Nurtec Acute STLY</div><div class="legend-item"><div class="legend-dot" style="background:#4ADE80"></div>Ubrelvy Acute Actuals</div><div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#4ADE80" stroke-width="2" stroke-dasharray="3"/></svg>Ubrelvy Acute STLY</div></div>'
acute_html = '<div class="split-section"><div class="split-col"><div class="section-label">TRx</div>' + acute_trx_chart + '</div><div class="split-col"><div class="section-label">NBRx</div>' + acute_nbrx_chart + '</div></div>' + acute_legend
html_content = html_content.replace('ACUTE_BRAND_CHART_PLACEHOLDER', acute_html)

prev_legend = '<div class="legend" style="margin-top:8px;justify-content:center;"><div class="legend-item"><div class="legend-dot" style="background:#7C6CFC"></div>Nurtec Prev Actuals</div><div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#7C6CFC" stroke-width="2" stroke-dasharray="3"/></svg>Nurtec Prev STLY</div><div class="legend-item"><div class="legend-dot" style="background:#FB923C"></div>Qulipta Prev Actuals</div><div class="legend-item"><svg width="20" height="2" style="margin-right:4px"><line x1="0" y1="1" x2="20" y2="1" stroke="#FB923C" stroke-width="2" stroke-dasharray="3"/></svg>Qulipta Prev STLY</div></div>'
prev_html = '<div class="split-section"><div class="split-col"><div class="section-label">TRx</div>' + prev_trx_chart + '</div><div class="split-col"><div class="section-label">NBRx</div>' + prev_nbrx_chart + '</div></div>' + prev_legend
html_content = html_content.replace('PREV_BRAND_CHART_PLACEHOLDER', prev_html)

components.html(html_content, height=920, scrolling=False)
