# SOP: Pushing Changes from Testing to Live Version
## Migraine Intelligence Hub - Landing Page

---

### Overview
- **Testing file (local):** `landing_page_with_data.py` (hardcoded data, no Snowflake needed)
- **Live file (DSS):** `landing_page_with_data_live.py` (uses `dataiku.Dataset` for live data)
- **Live queries:** `data_queries_live.py` (DSS data fetching functions)
- **Git repo:** https://github.com/Tush1607/migraine_landing_page.git

---

### Step-by-Step Process

#### Step 1: Complete Testing Locally
- Make all UI/chart changes in `landing_page_with_data.py`
- Test locally using: `& "C:\Program Files\Python311\Scripts\streamlit.exe" run "C:\Users\T15\OneDrive - Pfizer\EOW\landing_page_with_data.py"`
- Verify all toggles, formatting, and data display work correctly

#### Step 2: Identify What Changed
Determine what was added/modified:
1. **New hardcoded data** (e.g., new `_raw_data` arrays)
2. **New Plotly chart generation** (e.g., `fig_xxx = go.Figure()...`)
3. **New HTML placeholders** (e.g., `XXX_PLACEHOLDER`)
4. **New JS toggle functions** (e.g., `window.switchXxx`)
5. **New HTML injection code** (e.g., `html_content.replace(...)`)

#### Step 3: Update `data_queries_live.py`
If new data views were added:
1. Add a new function to `data_queries_live.py` following this pattern:
```python
def fetch_new_view_data(segment="TRx", rx_classification="Overall", ...):
    df = _get_full_dataset()
    df = df[
        (df['SEGMENT'] == segment) &
        (df['RX_CLASSIFICATION'] == rx_classification) &
        # ... additional filters
    ]
    df = df[['WEEK_ID', 'BRAND', 'ACTUALS', 'STLY', 'LATEST_GOAL']].sort_values([...]).reset_index(drop=True)
    return df
```

**Key rules:**
- Always use `_get_full_dataset()` (calls `dataiku.Dataset`)
- Never import `snowflake.connector`
- Filter in pandas, not SQL
- Dataset name: `SQL_US_MIGRAINE_FINAL_STACK_WEB_APP_VIEWS_SF`

#### Step 4: Update `landing_page_with_data_live.py`
Replace hardcoded data with live queries:

1. **Replace hardcoded data arrays** with live fetch calls:
```python
# TESTING (hardcoded):
_raw_data = [(20250704,"NURTEC",61633,53391,61633), ...]
npa_brand_df = pd.DataFrame(_raw_data, columns=[...])

# LIVE (replace with):
from data_queries_live import fetch_brand_data
npa_brand_df = load_brand_data("TRx")  # uses @st.cache_data
```

2. **Keep all Plotly chart generation code identical** - same `go.Figure()`, same layout, same colors

3. **Keep all HTML template and JS code identical** - same placeholders, same injection logic

4. **Ensure all variables referenced in injection code are defined:**
   - `brand_chart_svg` (TRx brand chart HTML)
   - `nbrx_chart_svg` (NBRx brand chart HTML)
   - `ch_nurtec_trx`, `ch_nurtec_nbrx` (channel charts)
   - `ch_ubrelvy_trx`, `ch_ubrelvy_nbrx`
   - `ch_qulipta_trx`, `ch_qulipta_nbrx`
   - Any new chart variables for new views

#### Step 5: Verify Live File Syntax
```powershell
py -c "import ast; ast.parse(open(r'path\to\landing_page_with_data_live.py', encoding='utf-8').read()); print('Syntax OK')"
```

#### Step 6: Commit and Push
```powershell
cd "C:\Users\T15\OneDrive - Pfizer\EOW"
git add data_queries_live.py landing_page_with_data_live.py
git commit -m "Description of changes"
git push --force origin main
```

#### Step 7: Pull in DSS
Pull the updated repo in DSS project libs and restart the Streamlit webapp backend.

---

### Architecture Summary

```
landing_page_with_data.py (TESTING - LOCAL)
  |-- Hardcoded data arrays (_raw_data, _nbrx_data, _channel_trx_data)
  |-- Plotly chart generation (go.Figure, fig.to_html)
  |-- HTML template (r""" ... """) with placeholders
  |-- Injection logic (html_content.replace)
  |-- components.html() rendering

landing_page_with_data_live.py (PRODUCTION - DSS)
  |-- data_queries_live.py (dataiku.Dataset calls)
  |-- @st.cache_data(ttl=3600) for hourly refresh
  |-- Same Plotly chart generation
  |-- Same HTML template
  |-- Same injection logic
  |-- components.html() rendering

data_queries_live.py (DATA LAYER - DSS)
  |-- _get_full_dataset() -> dataiku.Dataset("SQL_US_MIGRAINE_FINAL_STACK_WEB_APP_VIEWS_SF")
  |-- fetch_brand_data(segment, rx_classification, channel_type)
  |-- fetch_channel_data(segment, rx_classification, brand)
```

---

### Common Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `NameError: name 'xxx' is not defined` | Chart variable not generated in live file | Add the Plotly figure generation code before the injection |
| `ModuleNotFoundError: No module named 'snowflake'` | Using snowflake.connector in DSS | Use `dataiku.Dataset()` instead |
| `KeyError: 'COLUMN_NAME'` | Column case mismatch | Add `df.columns = [col.upper() for col in df.columns]` |
| Blank page on load | Plotly chart rendered in hidden div | Add `window.dispatchEvent(new Event('resize'))` in JS |
| Chart not filling width | Missing responsive config | Add `'responsive': True` and `width:100%` to chart div |

---

### Checklist Before Going Live

- [ ] All chart variables defined (no NameError)
- [ ] No `snowflake.connector` imports
- [ ] `data_queries_live.py` uses correct dataset name
- [ ] `@st.cache_data(ttl=3600)` on all data fetch functions
- [ ] Syntax check passes
- [ ] All toggles (TRx/NBRx, Brand) update both charts
- [ ] JS resize triggers present for Plotly charts
- [ ] HTML template has all required placeholders
- [ ] Git pushed and pulled in DSS