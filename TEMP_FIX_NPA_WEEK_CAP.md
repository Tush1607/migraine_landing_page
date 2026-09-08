# Temporary Fix: NPA TRx Week Cap to NBRx Max

## What was changed
**File:** `landing_page_with_data_live.py`  
**Location:** Lines 184-190 (after `nbrx_brand_df = load_brand_data("NBRx")`)

### Added lines (to revert):
```python
# TEMP FIX: cap TRx weeks to NBRx max so lengths match (revert when NBRx catches up)
_nbrx_max_wk = nbrx_brand_df['WEEK_ID'].max()
npa_brand_df = npa_brand_df[npa_brand_df['WEEK_ID'] <= _nbrx_max_wk]
weeks = sorted(npa_brand_df['WEEK_ID'].unique())
nurtec_data = npa_brand_df[npa_brand_df['BRAND'] == 'NURTEC'].sort_values('WEEK_ID')
ubrelvy_data = npa_brand_df[npa_brand_df['BRAND'] == 'UBRELVY'].sort_values('WEEK_ID')
qulipta_data = npa_brand_df[npa_brand_df['BRAND'] == 'QULIPTA'].sort_values('WEEK_ID')
```

### To revert, replace lines 183-191 with:
```python
nbrx_brand_df = load_brand_data("NBRx")
nbrx_nurtec = nbrx_brand_df[nbrx_brand_df['BRAND'] == 'NURTEC'].sort_values('WEEK_ID')
```

The original `weeks`, `nurtec_data`, `ubrelvy_data`, `qulipta_data` assignments at lines 178-181 will then be the only ones (no re-assignment needed since they already exist above).

## Why
NBRx data was 1 week behind TRx (50 vs 51 weeks), causing a `ValueError: Length of values (50) does not match length of index (51)` in `_build_npa_brand_excel` and `_build_xpt_excel`.

## When to revert
Once the latest NBRx file is available and both TRx and NBRx have the same number of weeks.
