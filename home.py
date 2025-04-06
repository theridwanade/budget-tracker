import streamlit as st
import os
import json
import pandas as pd

st.title("Transaction Book")

if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to_new_transaction():
    st.session_state.page = "new_transaction"
    st.rerun() 


df = pd.read_json("transactions.json")
df.reset_index(drop=True, inplace=True)
st.table(df)

st.button("Add new transaction", on_click=go_to_new_transaction)