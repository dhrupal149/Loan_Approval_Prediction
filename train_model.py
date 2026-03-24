import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    "Income": [2500, 4000, 3000, 6000, 2000],
    "Credit_Score": [650, 700, 620, 720, 600],
    "Loan_Amount": [10000, 15000, 12000, 20000, 8000],
    "Approved": [0, 1, 0, 1, 0]  
}

df = pd.DataFrame(data)

X = df[['Income', 'Credit_Score', 'Loan_Amount']]
y = df['Approved']

# Train classifier
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))
print("Loan approval model trained & saved!")