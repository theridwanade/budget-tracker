import streamlit as st

pg = st.navigation([
    st.Page("home.py", title="Home", icon="🏠"),
    st.Page("new_transaction.py", title="Add new Transaction", icon="🔥"),
])
pg.run()