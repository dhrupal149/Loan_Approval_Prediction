import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Loan Approval Prediction")

income = st.number_input("Income", min_value=0, value=3000)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
loan_amount = st.number_input("Loan Amount", min_value=0, value=10000)

if st.button("Predict"):
    result = model.predict([[income, credit_score, loan_amount]])
    status = "Approved" if result[0] == 1 else "Not Approved"
    st.write(f"Loan Status: {status}")