import streamlit as st
import numpy as np
import pandas as pd

# Fungsi AHP
def normalize_comparation(M):
    return M / M.sum(axis=0)

def weight(M):
    return np.mean(M, axis=1)

def validity_check(M, W):
    n = len(M)
    RI_table = {
        1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12,
        6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.51,
        11: 1.53, 12: 1.54, 13: 1.56, 14: 1.57
    }
    CV = M @ W / W
    eigen = np.mean(CV)
    CI = (eigen - n) / (n - 1)
    RI = RI_table.get(n, 1.59)
    CR = CI / RI if RI != 0 else 0
    return CV, eigen, CI, RI, CR

def final_weight(W_alt, W_crit):
    return W_alt.T @ W_crit

# Data
alternatif = ["Yamaha", "Honda", "Suzuki", "Kawasaki"]
kriteria = ["Gaya", "Keandalan", "Keekonomisan BBM"]

st.title("📊 AHP: Pemilihan Motor Terbaik dengan Penjelasan Lengkap")

st.markdown("""
Metode AHP digunakan untuk menentukan **alternatif terbaik** berdasarkan beberapa kriteria.
Langkah-langkah:
1. Menyusun **matriks perbandingan berpasangan** antar kriteria dan alternatif.
2. **Normalisasi** matriks dan menghitung **bobot prioritas**.
3. Menghitung **konsistensi**: CV, eigen, CI, RI, CR.
4. Melakukan **perankingan akhir** berdasarkan hasil bobot.

---

""")

# Fungsi untuk tampilkan info perhitungan dan penjelasan
def tampil_validasi(nama, M, bobot, index=None):
    CV, eigen, CI, RI, CR = validity_check(M, bobot)
    st.markdown(f"### 🔍 Validasi Konsistensi – {nama}")
    st.markdown("""
**Langkah menghitung:**
- **CV (Consistency Vector)**: (M × W) ÷ W
- **Eigen (λ max)**: Rata-rata dari CV
- **CI (Consistency Index)**: (λ max − n) / (n − 1)
- **RI (Random Index)**: Nilai acuan tergantung ukuran matriks
- **CR (Consistency Ratio)**: CI / RI → nilai ideal **≤ 0.1**
""")
    st.write(f"CV: {np.round(CV, 4)}")
    st.write(f"Eigen (λ max): {eigen:.4f}")
    st.write(f"CI: {CI:.4f}")
    st.write(f"RI: {RI:.4f}")
    st.write(f"CR: {CR:.4f} → {'✅ Valid' if CR <= 0.1 else '❌ Tidak Valid'}")

    if index is not None:
        st.dataframe(pd.DataFrame({"Alternatif": index, "CV": CV}))

# === KRITERIA ===
st.header("1️⃣ Matriks Perbandingan Kriteria")
MPBk = np.array([
    [1,   1/2, 3],
    [2,   1,   4],
    [1/3, 1/4, 1]
])
MPBk_df = pd.DataFrame(MPBk, index=kriteria, columns=kriteria)
st.subheader("📋 Matriks Kriteria")
st.dataframe(MPBk_df.style.format("{:.2f}"))

norm_k = normalize_comparation(MPBk)
Wk = weight(norm_k)
norm_df = pd.DataFrame(norm_k, index=kriteria, columns=kriteria)
norm_df["Bobot"] = Wk
st.subheader("📈 Normalisasi & Bobot Kriteria")
st.dataframe(norm_df.style.format("{:.3f}"))

tampil_validasi("Kriteria", MPBk, Wk, index=kriteria)

# === GAYA ===
st.header("2️⃣ Matriks Perbandingan Alternatif Berdasarkan Gaya")
MPBg = np.array([
    [1,   1/2, 2,   1/3],
    [2,   1,   3,   1/2],
    [1/2, 1/3, 1,   1/4],
    [3,   2,   4,   1]
])
MPBg_df = pd.DataFrame(MPBg, index=alternatif, columns=alternatif)
st.subheader("📋 Matriks Gaya")
st.dataframe(MPBg_df.style.format("{:.2f}"))

norm_g = normalize_comparation(MPBg)
Wg = weight(norm_g)
norm_df = pd.DataFrame(norm_g, index=alternatif, columns=alternatif)
norm_df["Bobot"] = Wg
st.subheader("📈 Normalisasi & Bobot Gaya")
st.dataframe(norm_df.style.format("{:.3f}"))

tampil_validasi("Gaya", MPBg, Wg, index=alternatif)

# === KEANDALAN ===
st.header("3️⃣ Matriks Perbandingan Alternatif Berdasarkan Keandalan")
MPBa = np.array([
    [1,   1/2, 3,   2],
    [2,   1,   4,   3],
    [1/3, 1/4, 1,   1/2],
    [1/2, 1/3, 2,   1]
])
MPBa_df = pd.DataFrame(MPBa, index=alternatif, columns=alternatif)
st.subheader("📋 Matriks Keandalan")
st.dataframe(MPBa_df.style.format("{:.2f}"))

norm_a = normalize_comparation(MPBa)
Wa = weight(norm_a)
norm_df = pd.DataFrame(norm_a, index=alternatif, columns=alternatif)
norm_df["Bobot"] = Wa
st.subheader("📈 Normalisasi & Bobot Keandalan")
st.dataframe(norm_df.style.format("{:.3f}"))

tampil_validasi("Keandalan", MPBa, Wa, index=alternatif)

# === KEEKONOMISAN ===
st.header("4️⃣ Matriks Perbandingan Alternatif Berdasarkan Keekonomisan BBM")
MPBe = np.array([
    [1,     60/80, 1,     60/80],
    [80/60, 1,     80/60, 1],
    [1,     60/80, 1,     60/80],
    [80/60, 1,     80/60, 1]
])
MPBe_df = pd.DataFrame(MPBe, index=alternatif, columns=alternatif)
st.subheader("📋 Matriks Keekonomisan BBM")
st.dataframe(MPBe_df.style.format("{:.2f}"))

norm_e = normalize_comparation(MPBe)
We = weight(norm_e)
norm_df = pd.DataFrame(norm_e, index=alternatif, columns=alternatif)
norm_df["Bobot"] = We
st.subheader("📈 Normalisasi & Bobot Keekonomisan")
st.dataframe(norm_df.style.format("{:.3f}"))

tampil_validasi("Keekonomisan", MPBe, We, index=alternatif)

# === HASIL AKHIR ===
st.header("5️⃣ Perhitungan Akhir & Perankingan")
W_total = np.array([Wg, Wa, We])  # (kriteria x alternatif)
W_final = final_weight(W_total, Wk)  # (alternatif)
final_df = pd.DataFrame({
    "Alternatif": alternatif,
    "Skor Akhir": W_final
}).sort_values(by="Skor Akhir", ascending=False).reset_index(drop=True)

st.subheader("📌 Penjelasan Perankingan:")
st.markdown("""
Bobot akhir dihitung dengan mengalikan:
- Bobot **kriteria** × bobot **alternatif** pada tiap kriteria.
Contoh:
> Bobot Total = (Bobot_Gaya × Wg) + (Bobot_Keandalan × Wa) + (Bobot_Keekonomisan × We)

Alternatif dengan **nilai tertinggi adalah yang terbaik.**
""")
st.dataframe(final_df.style.format({"Skor Akhir": "{:.4f}"}))

st.success(f"✅ Alternatif terbaik adalah **{final_df.iloc[0]['Alternatif']}** dengan skor {final_df.iloc[0]['Skor Akhir']:.4f}")

