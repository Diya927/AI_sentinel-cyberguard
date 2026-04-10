import streamlit as st
import joblib
import numpy as np

model = joblib.load("cyber_model.pkl")

st.title("AI Cybersecurity Threat Detection System")

packet_size = st.number_input("Packet Size")
failed_logins = st.number_input("Failed Logins")
request_frequency = st.number_input("Request Frequency")

if st.button("Predict"):
    features = np.array([[packet_size, failed_logins, request_frequency]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("🚨 ATTACK DETECTED")
    else:
        st.success("✅ NORMAL ACTIVITY")