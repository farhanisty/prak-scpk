import streamlit as st
import numpy as np
import pandas as pd

st.title("Pemilihan Smartphone Terbaik dengan Metode SAW")

# Data Alternatif dan Kriteria
alternatives = ["Kapasitas Baterai", "Kualitas Kamera", "Harga", "Berat", "Skor Benchmark"]
criteria = ["Smartphone A", "Smartphone B", "Smartphone C", "Smartphone D", "Smartphone E"]

data = np.array([
        [4500, 8, 6, 180, 300000],
        [5000, 7, 5, 190, 280000],
        [4200, 9, 7, 175, 310000],
        [4700, 8, 6, 185, 290000],
        [4800, 9, 5, 178, 320000]
])

attribute = np.array([1, 1, 0, 0, 1])

weights = np.array([.3,.2,.2,.1,.2])

df = pd.DataFrame(data, index=alternatives, columns=criteria)

#================ NORMALISASI MATRIX==============#
m, n = data.shape
normalized_matrix = np.zeros((m, n))

#normalisasi
for i in range(n):
    if attribute[i] == 1:
        normalized_matrix[:, i] = data[:, i] / np.max(data[:, i])
    else:
        normalized_matrix[:, i] = np.min(data[:, i]) / data[:, i]

normalized_df = pd.DataFrame(normalized_matrix, index=alternatives, columns=criteria)

#============== MENGHITUNG NILAI PREFERENSI DENGAN BOBOT KRITERIA ======================#
preference_value = np.dot(normalized_matrix, weights)
rangking = pd.DataFrame(preference_value, index=criteria, columns=["Nilai Preferensi"])
rangking_sorted = rangking.sort_values(by="Nilai Preferensi", ascending=False)

st.header("Pemilihan Smartphone Terbaik dengan Metode SAW")

st.subheader("Matriks Keputusan Awal")
st.dataframe(df)

st.subheader("Matriks Ternormalisasi")
st.dataframe(normalized_df)

st.subheader("Hasil Perangkingan")
st.dataframe(rangking_sorted)

st.subheader("Visualisasi Rangking (Bar Plot)")
st.bar_chart(rangking_sorted)

st.success(f"Alternatif terbaik adalah: {rangking_sorted.index[0]}")
