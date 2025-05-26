import streamlit as st
import numpy as np
import pandas as pd

benefit = 1
cost = 0

st.title("Pemilihan Smartphone Terbaik dengan Metode WP")

criteria = ["Kapasitas Baterai", "Kualitas Kamera", "Harga", "Berat", "Skor Benchmark"]
alternatives = ["Smartphone A", "Smartphone B", "Smartphone C", "Smartphone D", "Smartphone E"]

data = np.array([
        [4500, 8, 6, 180, 300000],
        [5000, 7, 5, 190, 280000],
        [4200, 9, 7, 175, 310000],
        [4700, 8, 6, 185, 290000],
        [4800, 9, 5, 178, 320000]
])

weights = np.array([.3,.2,.2,.1,.2])

df = pd.DataFrame(data, index=alternatives, columns=criteria)

attribute = [benefit, benefit, cost, cost, benefit]

st.header("Data Smartphone")
st.dataframe(df)

st.header("1. Normalisasi Bobot")
st.write("Bobot yang digunakan (normalisasi otomatis)")
df_weights = pd.DataFrame([weights], columns=criteria)
st.dataframe(df_weights)

#============== MENGHITUNG VEKTOR S ================#
m, n = data.shape
s = []
for i in range(m):
    s_value = 1
    for j in range(n):
        s_value = data[i][j] ** (attribute[j] * weights[j])
    s.append(s_value)


s_df = pd.DataFrame(s, index=alternatives, columns=["Vektor S"])
st.header("2. Perhitungan Vektor S")
st.dataframe(s_df)

#=============== MENGHITUNG VEKTOR V ==============#
sumS = sum(s)
v = [s_value / sumS for s_value in s]
v_df = pd.DataFrame(v, index=alternatives, columns=["Vektor V"])
st.header("3. Perhitungan Vektor V")
st.dataframe(v_df)

#============= RANGKING ALTERNATIVE ==============#
ra_df = pd.DataFrame(np.array([s, v]).T, index=alternatives, columns=["Vektor S", "Vektor V"])
ra_sorted_df = ra_df.sort_values(by="Vektor V", ascending=False)
st.header("4. Rangking Alternatif")
st.write("Rangking alternatif berdasarkan vektor v")
st.dataframe(ra_sorted_df)

#============ VISUALISASI HASIL ==================#
st.header("5. Visualisasi Hasil")
st.bar_chart(ra_sorted_df)

#============ PRINT HASIL ================#
st.header("Smartphone Terbaik")
st.success(ra_sorted_df.index[0])
