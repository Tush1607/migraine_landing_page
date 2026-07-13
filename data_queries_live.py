import pandas as pd

# DSS Dataset name (same as Snowflake table)
DATASET_NAME = "SQL_US_MIGRAINE_FINAL_STACK_WEB_APP_VIEWS_SF"


def _get_full_dataset():
    """Load the full dataset via DSS dataiku.Dataset."""
    import dataiku
    df = dataiku.Dataset(DATASET_NAME).get_dataframe()
    # Normalize column names to uppercase
    df.columns = [col.upper() for col in df.columns]
    return df


def fetch_brand_data(segment="TRx", rx_classification="Overall", channel_type="Overall"):
    """
    Fetch NPA Brand Competitive data.
    Returns DataFrame with: WEEK_ID, BRAND, ACTUALS, STLY, LATEST_GOAL
    """
    df = _get_full_dataset()
    df = df[
        (df['PRESCRIPTION'] == segment) &
        (df['RX_CLASSIFICATION'] == rx_classification) &
        (df['CHANNEL_TYPE'] == channel_type) &
        (df['STACK_KEY'] == 'NPA_TRENDS')
    ]
    df = df[['WEEK_ID', 'BRAND', 'ACTUALS', 'STLY', 'LATEST_GOAL']].sort_values(['WEEK_ID', 'BRAND']).reset_index(drop=True)
    return df


def fetch_channel_data(segment="TRx", rx_classification="Overall", brand="NURTEC"):
    """
    Fetch NPA Channel Performance data for a specific brand.
    Returns DataFrame with: WEEK_ID, BRAND, CHANNEL_TYPE, ACTUALS, STLY, LATEST_GOAL
    """
    df = _get_full_dataset()
    df = df[
        (df['PRESCRIPTION'] == segment) &
        (df['RX_CLASSIFICATION'] == rx_classification) &
        (df['BRAND'] == brand) &
        (df['CHANNEL_TYPE'] != 'Overall') &
        (df['STACK_KEY'] == 'NPA_TRENDS')
    ]
    df = df[['WEEK_ID', 'BRAND', 'CHANNEL_TYPE', 'ACTUALS', 'STLY', 'LATEST_GOAL']].sort_values(['WEEK_ID', 'CHANNEL_TYPE']).reset_index(drop=True)
    return df


def fetch_npa_stacked(stack_key='NPA_BRANDS_OVERALL'):
    """
    Fetch NPA stacked metrics (KPI table data).
    Returns DataFrame with all columns for the given stack key.
    """
    df = _get_full_dataset()
    df = df[df['STACK_KEY'] == stack_key]
    return df


def fetch_xponent_trends():
    """
    Fetch Xponent Trends data (weekly share by Payer/Channel).
    Returns DataFrame with: WEEK_ID, PRESCRIPTION, CUT_TYPE, CUT_VALUE, SHARE_PCT
    """
    df = _get_full_dataset()
    df = df[
        (df['STACK_KEY'] == 'XPONENT_TRENDS') &
        (df['SHARE_PCT'].notna())
    ]
    df = df[['WEEK_ID', 'PRESCRIPTION', 'CUT_TYPE', 'CUT_VALUE', 'SHARE_PCT']].sort_values(['CUT_TYPE', 'CUT_VALUE', 'PRESCRIPTION', 'WEEK_ID']).reset_index(drop=True)
    return df


def fetch_xponent_stacked():
    """
    Fetch Xponent Stacked Matrices (KPI summary values).
    Returns DataFrame with share and volume columns by CUT_TYPE/CUT_VALUE.
    """
    df = _get_full_dataset()
    df = df[df['STACK_KEY'] == 'XPT_STACKED_MATRICES']
    return df


def fetch_finance_trends():
    """
    Fetch Finance Trends data (weekly gross / monthly net).
    Returns DataFrame with: SECTION_NAME, PERIOD_LABEL, DATE_PARSED, ACTUAL_VALUE, BUDGET_VALUE, PRIOR_YEAR_VALUE
    """
    df = _get_full_dataset()
    df = df[df['STACK_KEY'] == 'FINANCE_TRENDS']
    df = df[['SECTION_NAME', 'PERIOD_LABEL', 'DATE_PARSED', 'ACTUAL_VALUE', 'BUDGET_VALUE', 'PRIOR_YEAR_VALUE']].sort_values(['SECTION_NAME', 'DATE_PARSED']).reset_index(drop=True)
    return df


def fetch_finance_stacked():
    """
    Fetch Finance Stacked Metrics (KPI summary values).
    Returns DataFrame with: SECTION_NAME, KPI_TITLE, ACTUAL_VALUE, BUDGET_VALUE, PRIOR_YEAR_VALUE, BUDGET_ATT, VARIANCE_TO_PY_PCT, DATA_AS_OF_DATE
    """
    df = _get_full_dataset()
    df = df[df['STACK_KEY'] == 'FINANCE_STACKED_METRICES']
    return df


def fetch_data_refresh():
    """
    Fetch Data Availability refresh dates by source.
    Returns DataFrame with: DATA_SOURCE, REFRESH_DATE
    """
    import dataiku
    df = dataiku.Dataset("LANDING_PAGE_DATA_REFRESH_SF").get_dataframe()
    df.columns = [col.upper() for col in df.columns]
    # Clean quoted date strings
    df['REFRESH_DATE'] = df['REFRESH_DATE'].astype(str).str.strip('"')
    return df[['DATA_SOURCE', 'REFRESH_DATE']].reset_index(drop=True)
