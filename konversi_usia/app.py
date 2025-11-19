import streamlit as st
import datetime

# Ambil tahun sekarang secara dinamis
TAHUN_SEKARANG = datetime.date.today().year

def hitung_usia(tahun_lahir, tahun_sekarang=TAHUN_SEKARANG):
    """Menghitung usia (hanya tahun) berdasarkan tahun lahir."""
    
    # Validasi input
    if tahun_lahir > tahun_sekarang:
        return -1 # Mengembalikan nilai khusus untuk error
    
    usia = tahun_sekarang - tahun_lahir
    return usia

# --- Antarmuka Streamlit ---
st.title("🎂 Kalkulator Usia Sederhana")
st.markdown(f"Aplikasi ini menghitung usia Anda pada tahun **{TAHUN_SEKARANG}**.")

# Input Tahun Lahir (mengganti input())
# Batas minimum diatur cukup jauh ke belakang (misalnya 1900)
tahun_lahir = st.number_input(
    "Masukkan Tahun Lahir Anda (misalnya: 1995):",
    min_value=1900,
    max_value=TAHUN_SEKARANG,
    value=2000, # Nilai default
    step=1,
    format="%d"
)

# Tombol untuk memicu perhitungan
if st.button("Hitung Usia"):
    usia_saat_ini = hitung_usia(tahun_lahir)
    
    # Validasi dan Tampilkan Hasil
    if usia_saat_ini == -1:
        st.error("Tahun lahir tidak boleh melebihi tahun sekarang!")
    else:
        st.balloons() # Efek visual Streamlit
        st.success(
            f"Jika Anda lahir tahun **{tahun_lahir}** dan sekarang adalah tahun **{TAHUN_SEKARANG}**, "
            f"usia Anda adalah: **{usia_saat_ini}** tahun."
        )

st.caption("Dibuat dengan Streamlit dan Python.")
