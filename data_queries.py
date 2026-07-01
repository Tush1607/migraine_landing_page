import snowflake.connector
import pandas as pd

# Snowflake connection config
SNOWFLAKE_CONFIG = {
    "warehouse": "VAW_AMER_PROD_WH",
    "database": "VAW_AMER_DESIGN",
    "schema": "USMIGRAINEIISANALYTICSETL",
}

TABLE_NAME = "USMIGRAINEIISANALYTICSETL_SQL_US_MIGRAINE_FINAL_STACK_WEB_APP_VIEWS_SF"


def get_connection(config_override=None):
    """Get Snowflake connection. Override config for DSS or local use."""
    config = {**SNOWFLAKE_CONFIG}
    if config_override:
        config.update(config_override)
    return snowflake.connector.connect(**config)


def fetch_npa_brand_competitive_data(segment="TRx", rx_classification="Overall", channel_type="Overall"):
    """
    Fetch data for NPA Brand Competitive View chart.
    
    Parameters:
        segment: 'TRx', 'NBRx', or 'NRx'
        rx_classification: 'Overall', 'Acute', or 'Preventive'
        channel_type: 'Overall', 'Retail', 'MAIL', 'Long term'
    
    Returns:
        DataFrame with columns: WEEK_ID, BRAND, ACTUALS, STLY, LATEST_GOAL
    """
    query = f"""
    SELECT 
        WEEK_ID,
        BRAND,
        PRESCRIPTION,
        RX_CLASSIFICATION,
        CHANNEL_TYPE,
        ACTUALS,
        STLY,
        LATEST_GOAL
    FROM "{SNOWFLAKE_CONFIG['database']}"."{SNOWFLAKE_CONFIG['schema']}"."{TABLE_NAME}"
    WHERE PRESCRIPTION = %s
      AND RX_CLASSIFICATION = %s
      AND CHANNEL_TYPE = %s
      AND STACK_KEY = 'NPA_TRENDS'
    ORDER BY WEEK_ID, BRAND
    """
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn, params=[segment, rx_classification, channel_type])
    finally:
        conn.close()
    return df


def fetch_npa_channel_data(segment="TRx", rx_classification="Overall", brand="NURTEC"):
    """
    Fetch data for NPA Channel Performance View chart.
    
    Parameters:
        segment: 'TRx', 'NBRx', or 'NRx'
        rx_classification: 'Overall', 'Acute', or 'Preventive'
        brand: 'NURTEC', 'UBRELVY', 'QULIPTA'
    
    Returns:
        DataFrame with columns: WEEK_ID, CHANNEL_TYPE, ACTUALS, STLY, LATEST_GOAL
    """
    query = f"""
    SELECT 
        WEEK_ID,
        BRAND,
        PRESCRIPTION,
        RX_CLASSIFICATION,
        CHANNEL_TYPE,
        ACTUALS,
        STLY,
        LATEST_GOAL
    FROM "{SNOWFLAKE_CONFIG['database']}"."{SNOWFLAKE_CONFIG['schema']}"."{TABLE_NAME}"
    WHERE PRESCRIPTION = %s
      AND RX_CLASSIFICATION = %s
      AND BRAND = %s
      AND CHANNEL_TYPE != 'Overall'
      AND STACK_KEY = 'NPA_TRENDS'
    ORDER BY WEEK_ID, CHANNEL_TYPE
    """
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn, params=[segment, rx_classification, brand])
    finally:
        conn.close()
    return df


def fetch_npa_brand_table_data(segment="TRx", rx_classification="Overall", channel_type="Overall"):
    """
    Fetch summary data for NPA brand tables (Nurtec, Ubrelvy, Qulipta).
    Returns latest week, QTD, and YTD aggregations.
    
    Parameters:
        segment: 'TRx', 'NBRx', or 'NRx'
        rx_classification: 'Overall', 'Acute', or 'Preventive'
        channel_type: 'Overall', 'Retail', 'MAIL', 'Long term'
    
    Returns:
        DataFrame with weekly data for all brands
    """
    query = f"""
    SELECT 
        WEEK_ID,
        BRAND,
        PRESCRIPTION,
        RX_CLASSIFICATION,
        CHANNEL_TYPE,
        ACTUALS,
        STLY,
        LATEST_GOAL
    FROM "{SNOWFLAKE_CONFIG['database']}"."{SNOWFLAKE_CONFIG['schema']}"."{TABLE_NAME}"
    WHERE PRESCRIPTION = %s
      AND RX_CLASSIFICATION = %s
      AND CHANNEL_TYPE = %s
      AND STACK_KEY = 'NPA_TRENDS'
    ORDER BY WEEK_ID, BRAND
    """
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn, params=[segment, rx_classification, channel_type])
    finally:
        conn.close()
    return df


def fetch_all_weeks(segment="TRx", rx_classification="Overall"):
    """
    Fetch all available weeks for the given segment and classification.
    Useful for determining date range for charts.
    """
    query = f"""
    SELECT DISTINCT WEEK_ID
    FROM "{SNOWFLAKE_CONFIG['database']}"."{SNOWFLAKE_CONFIG['schema']}"."{TABLE_NAME}"
    WHERE PRESCRIPTION = %s
      AND RX_CLASSIFICATION = %s
      AND STACK_KEY = 'NPA_TRENDS'
    ORDER BY WEEK_ID
    """
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn, params=[segment, rx_classification])
    finally:
        conn.close()
    return df
