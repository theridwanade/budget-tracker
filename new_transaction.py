import streamlit as st
import time
import os
import json
import uuid

st.title("Add new transaction")


def add_new_transaction(transaction):
  file_path = "transactions.json"

  if not os.path.exists(file_path):
    with open(file_path, "w") as file:
      json.dump([], file)

  with open(file_path, "r") as file:
    transactions = json.load(file)

  transactions.append(transaction)

  with open(file_path, "w") as file:
    json.dump(transactions, file, indent=2)



with st.form("Enter new transaction"):
  row1 = st.columns([1,1])
  title = row1[0].text_input("Title")
  description = row1[1].text_area("Description")

  row2 = st.columns([1,1])
  date = row2[0].date_input("Date")
  amount = row2[1].number_input("Amount", min_value=0.0, step=0.10)

  row3 = st.columns([1,1])
  category = row3[0].selectbox("Category", ["Food", "Transport", "Entertainment", "Other"])
  transaction_type = row3[1].selectbox("Transaction Type", ["Income", "Expense"])

  submitted = st.form_submit_button('Add new transaction')


if submitted:
  add_new_transaction({
    "id": str(uuid.uuid4())[:8],
    "title": title,
    "description": description,
    "date": date.strftime("%Y-%m-%d"),
    "amount": amount,
    "category": category,
    "transaction_type": transaction_type
  })
  st.success("Transaction added successfully!")
  st.balloons()
  time.sleep(2)
  st.rerun()

