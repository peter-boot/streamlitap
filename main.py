import streamlit as st
import pandas as pd

from supabase import create_client, Client

# Initialize connection to db


# @st.cache_resource
# def init_connection():
#     url: str = st.secrets['supabase_url']
#     key: str = st.secrets['supabase_key']

#     client: Client = create_client(url, key)

#     return client


# supabase = init_connection()

# # Query the db


# @st.cache_data(ttl=600)  # cache clears after 10 minutes
# def run_query():
#     # Return all data
#     return supabase.table('car_parts_monthly_sales').select("*").execute()

#     # Filter data
#     # return supabase.table('car_parts_monthly_sales').select("*").eq("parts_id", 2674).execute()


st.title("Query a database")

st.title("App Title")

st.header("Main Header")
st.subheader("This is a subheader")

df = pd.read_csv("data/sample.csv", dtype="int")
st.dataframe(df)

st.table(df)

st.dataframe(df)


# st.header("")
st.markdown("This is markdown **text**")
st.markdown("#Header 1")
st.markdown("##Header 2")
st.markdown("###Header 3")

st.caption("This is a caption")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.text("Some text")

st.latex("x = 2^2")

st.text("Text above divider")
st.divider()
st.text("Text above divider")