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
        (df['SEGMENT'] == segment) &
        (df['RX_CLASSIFICATION'] == rx_classification) &
        (df['CHANNEL_TYPE'] == channel_type) &
        (df['STACK_KEY'] == 'NPA_BRANDS_BY_CHANNEL')
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
        (df['SEGMENT'] == segment) &
        (df['RX_CLASSIFICATION'] == rx_classification) &
        (df['BRAND'] == brand) &
        (df['CHANNEL_TYPE'] != 'Overall') &
        (df['STACK_KEY'] == 'NPA_BRANDS_BY_CHANNEL')
    ]
    df = df[['WEEK_ID', 'BRAND', 'CHANNEL_TYPE', 'ACTUALS', 'STLY', 'LATEST_GOAL']].sort_values(['WEEK_ID', 'CHANNEL_TYPE']).reset_index(drop=True)
    return df
