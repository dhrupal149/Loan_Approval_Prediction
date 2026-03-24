# Loan Approval Prediction

A simple machine learning project to predict whether a loan will be approved based on **Income**, **Credit Score**, and **Loan Amount**.  

---

## Features

- **Income** – Applicant's monthly income  
- **Credit Score** – Applicant's credit rating (300–850)  
- **Loan Amount** – Requested loan amount  

## Target

- **Approved** – Loan status: 1 = Approved, 0 = Not Approved  

---

## Files

- `train_model.py` – Trains a `RandomForestClassifier` on example data and saves the model (`model.pkl`).  
- `app.py` – Flask API to predict loan approval via POST requests.  
- `app_ui.py` – Streamlit app for interactive predictions.  

---

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
Install dependencies:
pip install pandas scikit-learn flask streamlit
Train the model:
python train_model.py
Usage
Run Flask API
python app.py
Access API at http://127.0.0.1:5000/
POST JSON example:
{
  "Income": 4000,
  "Credit_Score": 700,
  "Loan_Amount": 15000
}
Run Streamlit App
streamlit run app_ui.py
Enter values for Income, Credit Score, and Loan Amount.
Click Predict to see loan status.
