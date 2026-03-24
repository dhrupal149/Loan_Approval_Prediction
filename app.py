from flask import Flask, request, jsonify
import pickle 

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    income = data['Income']
    credit_score = data['Credit_Score']
    loan_amount = data['Loan_Amount']
    
    result = model.predict([[income, credit_score, loan_amount]])
    
    return jsonify({
        "Approved": int(result[0])
    })

if __name__ == "__main__":
    app.run(debug=True)
    
    
