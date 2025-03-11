import streamlit as st
import pandas as pd

tab1, tab2, tab3, tab4 = st.tabs(['Identitas', 'world', 'haii', 'hoii'])

datasets = pd.read_csv("weather_data_extended.csv")

with tab1:
    st.title("Latihan Kuis")
    st.text("Nama : Farhannivta Ramadhana")
    st.text("NIM : 123230139")
    st.text("Kelas : IF-D")

with tab2:
    temperatureDatasets = datasets.groupby('Location', as_index=False)['Temperature (°C)'].mean().sort_values(by="Location").head(5)
    st.dataframe(temperatureDatasets)
