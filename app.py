from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        input_features = [
            float(request.form['Customer_Age']),
            float(request.form['Dependent_count']),
            float(request.form['Months_on_book']),
            float(request.form['Total_Relationship_Count']),
            float(request.form['Months_Inactive_12_mon']),
            float(request.form['Contacts_Count_12_mon']),
            float(request.form['Credit_Limit']),
            float(request.form['Total_Revolving_Bal']),
            float(request.form['Avg_Open_To_Buy']),
            float(request.form['Total_Amt_Chng_Q4_Q1']),
            float(request.form['Total_Trans_Amt']),
            float(request.form['Total_Trans_Ct']),
            float(request.form['Total_Ct_Chng_Q4_Q1']),
            float(request.form['Avg_Utilization_Ratio']),
            int(request.form['Gender']),
            int(request.form['Education_Level']),
            int(request.form['Marital_Status']),
            int(request.form['Income_Category']),
            int(request.form['Card_Category'])
        ]

        # Convert to numpy array and predict
        features = np.array([input_features])
        prediction = model.predict(features)
        result = "Churn" if prediction[0] == 1 else "No Churn"

        return render_template('predict.html', prediction=result)

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
