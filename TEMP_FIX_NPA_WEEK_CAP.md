# Temporary Fix: NPA Week Cap to NBRx Max

## Why
NBRx data was 1 week behind TRx (50 vs 51 weeks), causing `ValueError: Length of values does not match length of index` across multiple Excel download and chart functions.

## When to revert
Once the latest NBRx file is available and both TRx and NBRx have the same number of weeks.

## How to find all changes
Search for `TEMP FIX` in `landing_page_with_data_live.py`. All temp lines are tagged with:
```
# TEMP FIX: cap ... (revert when NBRx catches up)
```

## All locations changed (6 total)

### 1. NPA Brand Data (lines ~184-190)
After `nbrx_brand_df = load_brand_data("NBRx")`, added:
```python
_nbrx_max_wk = nbrx_brand_df['WEEK_ID'].max()
npa_brand_df = npa_brand_df[npa_brand_df['WEEK_ID'] <= _nbrx_max_wk]
weeks = sorted(npa_brand_df['WEEK_ID'].unique())
nurtec_data = npa_brand_df[npa_brand_df['BRAND'] == 'NURTEC'].sort_values('WEEK_ID')
ubrelvy_data = npa_brand_df[npa_brand_df['BRAND'] == 'UBRELVY'].sort_values('WEEK_ID')
qulipta_data = npa_brand_df[npa_brand_df['BRAND'] == 'QULIPTA'].sort_values('WEEK_ID')
```
**Revert:** Remove these 7 lines (including comment). Keep only:
```python
nbrx_brand_df = load_brand_data("NBRx")
nbrx_nurtec = ...
```

### 2. get_channel_dict() (line ~200-201)
Added inside function after `ch_df = load_channel_data(...)`:
```python
ch_df = ch_df[ch_df['WEEK_ID'] <= _nbrx_max_wk]
```
**Revert:** Remove this line and the comment above it.

### 3. Acute/Preventive Brand Data (lines ~220-224)
After loading all 4 dataframes, added:
```python
_acute_trx_df = _acute_trx_df[_acute_trx_df['WEEK_ID'] <= _nbrx_max_wk]
_acute_nbrx_df = _acute_nbrx_df[_acute_nbrx_df['WEEK_ID'] <= _nbrx_max_wk]
_prev_trx_df = _prev_trx_df[_prev_trx_df['WEEK_ID'] <= _nbrx_max_wk]
_prev_nbrx_df = _prev_nbrx_df[_prev_nbrx_df['WEEK_ID'] <= _nbrx_max_wk]
```
**Revert:** Remove these 5 lines (including comment).

### 4. _build_ap_channel_excel() (line ~317-318)
Added inside function after `ch_df = load_acute_prev_channel_data(...)`:
```python
ch_df = ch_df[ch_df['WEEK_ID'] <= _nbrx_max_wk]
```
**Revert:** Remove this line and the comment above it.

### 5. build_ap_channel_chart_live() (line ~558-559)
Added inside function after `ch_df = load_acute_prev_channel_data(...)`:
```python
ch_df = ch_df[ch_df['WEEK_ID'] <= _nbrx_max_wk]
```
**Revert:** Remove this line and the comment above it.

## Quick revert command
Search and delete all lines matching `TEMP FIX` and the filter line immediately after each comment. Also remove the `_nbrx_max_wk` variable and the re-assignments of `npa_brand_df`, `weeks`, `nurtec_data`, `ubrelvy_data`, `qulipta_data` at location #1.
