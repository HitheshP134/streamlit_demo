import streamlit as st

# Connection
try:
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    import toml
    from snowflake.snowpark.session import Session

    snowflake_connection_cfg = toml.load('connection.toml')['snowflake']
    session = Session.builder.configs(snowflake_connection_cfg).create()

# Contents
st.title("Harato Page")

query = "SELECT id as test FROM D_HARATO_DB.DEV.NEW_TABLE"
data = session.sql(query).collect()
st.dataframe(data)