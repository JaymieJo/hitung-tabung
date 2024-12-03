import streamlit as st
import pandas as pd

# Judul halaman
st.title("Toko Baju Online")

st.write("Selamat datang di toko baju online kami! Di sini Anda dapat menemukan berbagai macam baju dengan harga terjangkau.")

with st.sidebar:
    
    kategori = st.selectbox("Kategori", ["Semua", "Kaos", "Kemeja", "Celana", "Rok"])

    harga_min, harga_max = st.slider("Rentang Harga", 0, 100, (0, 100))

    ukuran = st.multiselect("Ukuran", ["S", "M", "L", "XL", "XXL"])

    warna = st.multiselect("Warna", ["Merah", "Biru", "Hijau", "Kuning", "Hitam", "Putih"])

    urutan = st.selectbox("Urutkan Berdasarkan", ["Harga (Terendah ke Tertinggi)", "Harga (Tertinggi ke Terendah)", "Nama (A-Z)", "Nama (Z-A)"])

data = pd.read_csv("baju.csv")

if kategori != "Semua":
    data = data[data["Kategori"] == kategori]
if harga_min > 0 or harga_max < 100:
    data = data[(data["Harga"] >= harga_min) & (data["Harga"] <= harga_max)]
if len(ukuran) > 0:
    data = data[data["Ukuran"].isin(ukuran)]
if len(warna) > 0:
    data = data[data["Warna"].isin(warna)]

if urutan == "Harga (Terendah ke Tertinggi)":
    data = data.sort_values("Harga")
elif urutan == "Harga (Tertinggi ke Terendah)":
    data = data.sort_values("Harga", ascending=False)
elif urutan == "Nama (A-Z)":
    data = data.sort_values("Nama")
elif urutan == "Nama (Z-A)":
    data = data.sort_values("Nama", ascending=False)

st.table(data)
