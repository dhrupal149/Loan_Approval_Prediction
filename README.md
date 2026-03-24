# Loan Approval Prediction

Predict whether a loan will be approved based on **Income**, **Credit Score**, and **Loan Amount** using a Random Forest model.

---

## Files

- `train_model.py` – Train and save the model (`model.pkl`)  
- `app.py` – Flask API to predict loan approval  
- `app_ui.py` – Streamlit app for interactive predictions  

---

## Usage

1. **Install dependencies**:

```bash
pip install pandas scikit-learn flask streamlit
Train the model:
python train_model.py
Run Flask API:
python app.py
Run Streamlit UI:
streamlit run app_ui.py
