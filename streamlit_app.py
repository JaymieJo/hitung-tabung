import streamlit as st

st.title("Menghitung :blue[volume tabung] :rocket:")

r = st.number_input("masukan Jari-Jari (cm): ",0)
t = st.number_input("masukan Tinggi (cm): ",0)

if st.button("Hitung Volume", type="primary"):
  v = math.pi*(r**2)*t
  st.success(f'Volume tabung adalah {v}:.2f')
