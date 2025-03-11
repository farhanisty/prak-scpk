import streamlit as st
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

st.title("Aplikasi Pertama Saya")

st.header("Ini adalah header")

st.subheader("Ini adalah subheader")

st.text("ini adalah text biasa")

st.write("*lorem ipsum dolor sit amet*")

df = pd.DataFrame({
    "Nama": ['farhannivta', 'ramadhana', 'garry'],
    "Usia": [20, 21, 19],
    "Kota": ['bantul', 'bantul', 'sleman'],
})

st.dataframe(df)

if st.button("klik saya"):
    st.write("Tombol telah diklik")

nilai = st.slider(label="Pilih nilai", min_value=50, max_value=150, value=70)
st.write(f'nilai yang kupilih adalah: {nilai}')

kota = st.selectbox("Pilih Opsi", ['Bantul', 'Yogyakarta', 'Banten'])
st.write(f'Kota yang kupilih adalah: {kota}')

st.text_input("Masukkan text", "ini adalah value default", placeholder='Input text woi')

st.text_area("Deskripsi")

col1, col2 = st.columns(2)

with col1:
    st.write("ini di kolom satu")

with col2:
    st.write("ini di kolom kedua")


with st.expander('selengkapnya'):
    st.write("cukurukuk")

tab1, tab2 = st.tabs(['Data', 'Informasi'])

with tab1:
    st.write("ini konten untuk tab data")

with tab2:
    st.write("ini konten untuk tab informasi")
# Input angka
angka1 = st.number_input("Masukkan Angka 1", min_value=0, value=0)
angka2 = st.number_input("Masukkan Angka 2", min_value=0, value=0)
# Tombol untuk operasi
if st.button("Kali"):
    hasil = angka1 * angka2
    st.success(f"Hasil perkalian: {hasil}")
if st.button("Bagi"):
    if angka2 != 0:
        hasil = angka1 / angka2
        st.success(f"Hasil pembagian: {hasil}")
else:
    st.error("Angka 2 tidak boleh 0 untuk pembagian!")

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

st.write("Dataset iris")
st.dataframe(df)

st.text(df.isnull().sum())
st.write(df.describe())

df['target'] = iris.target

# visualisasi data
figure, axis = plt.subplots(figsize=(10, 6))

for species in df['target'].unique():
    subset = df[df['target'] == species]
    axis.plot(subset.index, subset['sepal length (cm)'], marker= 'o', label = f'species {species}')

axis.set_xlabel("Index")
axis.set_ylabel("Sepal Length")
axis.set_title("Index")
axis.legend(title="Species")
st.pyplot(figure)
