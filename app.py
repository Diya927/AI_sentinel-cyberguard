from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Load model and encoders
model = joblib.load("cyber_model.pkl")
encoders = joblib.load("encoders.pkl")

app = Flask(__name__)

# Categorical columns
cat_cols = ["protocol_type", "service", "flag"]

@app.route("/")
def home():
    return "Cybersecurity Threat Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Convert input into DataFrame
    df = pd.DataFrame([data])

    # Encode categorical features
    for col in cat_cols:
        if col in df:
            df[col] = encoders[col].transform(df[col])

    # Ensure correct order (same as training)
    df = df.reindex(columns=model.feature_names_in_, fill_value=0)

    # Prediction
    prediction = model.predict(df)[0]

    result = "Attack" if prediction == 1 else "Normal"

    return jsonify({
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)