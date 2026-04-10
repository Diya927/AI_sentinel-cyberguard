import streamlit as st
import joblib
import numpy as np

# Load your model
model = joblib.load("cyber_model.pkl")

st.title("AI Cybersecurity Threat Detection System")

# Your 3 inputs
packet_size = st.number_input("Packet Size", step=1)
failed_logins = st.number_input("Failed Logins", step=1)
request_freq = st.number_input("Request Frequency", step=1)

if st.button("Predict"):
    # Create an array of 41 zeros (matching what the model expects)
    full_features = np.zeros((1, 41))
    
    # Place your 3 inputs into the first three slots
    full_features[0, 0] = packet_size
    full_features[0, 1] = failed_logins
    full_features[0, 2] = request_freq
    
    prediction = model.predict(full_features)
    
    if prediction == 1:
        st.error("⚠️ Threat Detected!")
    else:
        st.success("✅ No Threat Detected.")
