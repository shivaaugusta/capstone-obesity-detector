import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("Prediksi Tingkat Obesitas")

st.markdown("Masukkan data gaya hidup dan kondisi fisik Anda:")

# --- INPUT FORM SESUAI FITUR TRAINING ---
age = st.slider("Umur", 10, 100, 25)
gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
height = st.number_input("Tinggi Badan (meter)", 1.0, 2.5, 1.70)
weight = st.number_input("Berat Badan (kg)", 30.0, 200.0, 65.0)
calc = st.selectbox("Konsumsi alkohol", ["no", "Sometimes", "Frequently", "Always"])
favc = st.selectbox("Sering makan tinggi kalori?", ["yes", "no"])
fcvc = st.slider("Konsumsi sayur (1: jarang, 3: sering)", 1, 3, 2)
ncp = st.slider("Jumlah makan besar per hari", 1, 4, 3)
scc = st.selectbox("Pantau asupan kalori?", ["yes", "no"])
smoke = st.selectbox("Merokok?", ["yes", "no"])
ch2o = st.slider("Konsumsi air (liter per hari)", 1, 3, 2)
family_history = st.selectbox("Riwayat keluarga kelebihan berat badan?", ["yes", "no"])
faf = st.slider("Aktivitas fisik (jam per minggu)", 0, 5, 1)
tue = st.slider("Waktu dengan perangkat (jam per hari)", 0, 5, 2)
caec = st.selectbox("Ngemil di antara waktu makan?", ["no", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox("Transportasi utama", [
    "Walking", "Automobile", "Motorbike", "Bike", "Public_Transportation"])

# --- ENCODING MANUAL SESUAI TRAINING ---
def encode(val, mapping):
    return mapping.get(val, 0)

gender_map = {"Male": 1, "Female": 0}
yesno_map = {"yes": 1, "no": 0}
calc_map = {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}
caec_map = {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}
mtrans_map = {
    "Walking": 0, "Automobile": 1, "Motorbike": 2,
    "Bike": 3, "Public_Transportation": 4
}

# Susun array fitur sesuai urutan saat training
features = np.array([[
    age,
    encode(gender, gender_map),
    height,
    weight,
    encode(calc, calc_map),
    encode(favc, yesno_map),
    fcvc,
    ncp,
    encode(scc, yesno_map),
    encode(smoke, yesno_map),
    ch2o,
    encode(family_history, yesno_map),
    faf,
    tue,
    encode(caec, caec_map),
    encode(mtrans, mtrans_map)
]])

# --- PREDIKSI ---
if st.button("Prediksi"):
    pred = model.predict(features)
    st.success(f"Tingkat Obesitas: {pred[0]}")
