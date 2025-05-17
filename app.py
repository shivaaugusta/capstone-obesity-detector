import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("Prediksi Tingkat Obesitas")

age = st.slider("Umur", 10, 100, 25)
height = st.number_input("Tinggi (m)", 1.0, 2.5, 1.70)
weight = st.number_input("Berat (kg)", 30.0, 200.0, 70.0)

# Tambahkan input lain sesuai fitur training-mu

if st.button("Prediksi"):
    features = np.array([[age, height, weight]])
    pred = model.predict(features)
    st.success(f"Hasil prediksi: {pred[0]}")
