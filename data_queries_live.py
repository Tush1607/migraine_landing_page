import pandas as pd

# For DSS deployment - uses dataiku managed connection
# No credentials needed - DSS handles authentication

WAREHOUSE = "VAW_AMER_PROD_WH"
DATABASE = "VAW_AMER_DESIGN"
SCHEMA = "USMIGRAINEIISANALYTICSETL"
TABLE = "USMIGRAINEIISANALYTICSETL_SQL_US_MIGRAINE_FINAL_STACK_WEB_APP_VIEWS_SF"
FULL_TABLE = f'"{DATABASE}"."{SCHEMA}"."{TABLE}"'


def get_connection():
    """Get Snowflake connection via DSS managed connection."""
    import dataiku
    client = dataiku.api_client()
    conn = dataiku.get_connection("SNOWFLAKE_AMERPROD01")
    return conn.get_snowflake_connector()


def get_snowflake_connection_direct():
    """Direct Snowflake connection (for non-DSS environments)."""
    import snowflake.connector
    conn = snowflake.connector.connect(
        warehouse=WAREHOUSE,
        database=DATABASE,
        schema=SCHEMA,
        authenticator="externalbrowser",
        account="pfe-amerprod01.us-east-1",
    )
    return conn


def fetch_brand_data(segment="TRx", rx_classification="Overall", channel_type="Overall"):
    """
    Fetch NPA Brand Competitive data.
    Returns DataFrame with: WEEK_ID, BRAND, ACTUALS, STLY, LATEST_GOAL
    """
    query = f"""
    SELECT WEEK_ID, BRAND, ACTUALS, STLY, LATEST_GOAL
    FROM {FULL_TABLE}
    WHERE SEGMENT = '{segment}'
      AND RX_CLASSIFICATION = '{rx_classification}'
      AND CHANNEL_TYPE = '{channel_type}'
      AND STACK_KEY = 'NPA_BRANDS_BY_CHANNEL'
    ORDER BY WEEK_ID, BRAND
    """
    try:
        import dataiku
        dataset = dataiku.Dataset("USMIGRAINEIISANALYTICSETL_SQL_US_MIGRAINE_FINAL_STACK_WEB_APP_VIEWS_SF")
        df = dataset.get_dataframe()
        df = df[(df['SEGMENT'] == segment) & (df['RX_CLASSIFICATION'] == rx_classification) & (df['CHANNEL_TYPE'] == channel_type) & (df['STACK_KEY'] == 'NPA_BRANDS_BY_CHANNEL')]
        df = df[['WEEK_ID','BRAND','ACTUALS','STLY','LATEST_GOAL']].sort_values(['WEEK_ID','BRAND'])
        return df
    except:
        conn = get_snowflake_connection_direct()
        try:
            df = pd.read_sql(query, conn)
        finally:
            conn.close()
        return df


def fetch_channel_data(segment="TRx", rx_classification="Overall", brand="NURTEC"):
    """
    Fetch NPA Channel Performance data for a specific brand.
    Returns DataFrame with: WEEK_ID, CHANNEL_TYPE, ACTUALS, STLY, LATEST_GOAL
    """
    query = f"""
    SELECT WEEK_ID, BRAND, CHANNEL_TYPE, ACTUALS, STLY, LATEST_GOAL
    FROM {FULL_TABLE}
    WHERE SEGMENT = '{segment}'
      AND RX_CLASSIFICATION = '{rx_classification}'
      AND BRAND = '{brand}'
      AND CHANNEL_TYPE != 'Overall'
      AND STACK_KEY = 'NPA_BRANDS_BY_CHANNEL'
    ORDER BY WEEK_ID, CHANNEL_TYPE
    """
    try:
        import dataiku
        dataset = dataiku.Dataset("USMIGRAINEIISANALYTICSETL_SQL_US_MIGRAINE_FINAL_STACK_WEB_APP_VIEWS_SF")
        df = dataset.get_dataframe()
        df = df[(df['SEGMENT'] == segment) & (df['RX_CLASSIFICATION'] == rx_classification) & (df['BRAND'] == brand) & (df['CHANNEL_TYPE'] != 'Overall') & (df['STACK_KEY'] == 'NPA_BRANDS_BY_CHANNEL')]
        df = df[['WEEK_ID','BRAND','CHANNEL_TYPE','ACTUALS','STLY','LATEST_GOAL']].sort_values(['WEEK_ID','CHANNEL_TYPE'])
        return df
    except:
        conn = get_snowflake_connection_direct()
        try:
            df = pd.read_sql(query, conn)
        finally:
            conn.close()
        return df
