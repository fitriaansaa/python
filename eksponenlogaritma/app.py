import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Lab Virtual: Eksponen & Logaritma",
    layout="wide"
)

st.title("🔬 Lab Virtual Interaktif: Fungsi Eksponen dan Logaritma")
st.markdown("Eksplorasi visual hubungan antara fungsi eksponen ($f(x) = a^x$) dan fungsi logaritma ($g(x) = \log_a(x)$).")

# Garis pemisah
st.sidebar.header("Pengaturan Parameter")

# --- Pengaturan Parameter Dasar ---
# Basis (a) harus positif dan tidak sama dengan 1
basis = st.sidebar.slider(
    "Pilih Basis (a)",
    min_value=0.1,
    max_value=5.0,
    value=2.0,
    step=0.1,
    help="Basis (a) dari fungsi $f(x) = a^x$ dan $g(x) = \log_a(x)$. Basis harus positif dan tidak sama dengan 1."
)

if basis == 1.0:
    st.sidebar.warning("Basis (a) tidak boleh sama dengan 1.")
    basis = 2.0 # Set default

# Rentang x untuk plot
x_min = -3.0
x_max = 5.0
x_vals = np.linspace(x_min, x_max, 400)

# --- Kolom untuk Tata Letak yang Menarik ---
col1, col2 = st.columns(2)

# ==============================================================================
# 🚀 Bagian 1: Visualisasi Fungsi Eksponen
# ==============================================================================
with col1:
    st.header("1. Fungsi Eksponen ($f(x) = a^x$)")
    
    # --- Input Interaktif Tambahan (Translasi) ---
    k_exp = st.slider("Translasi Vertikal (k): $f(x) = a^x + k$", -5.0, 5.0, 0.0, 0.1)
    h_exp = st.slider("Translasi Horizontal (h): $f(x) = a^{(x-h)}$", -5.0, 5.0, 0.0, 0.1)

    # --- Definisi Fungsi Eksponen ---
    def exponential_function(x, a, h, k):
        return a**(x - h) + k

    y_exp = exponential_function(x_vals, basis, h_exp, k_exp)
    
    # --- Plot Fungsi Eksponen ---
    fig_exp, ax_exp = plt.subplots()
    ax_exp.plot(x_vals, y_exp, label=f'$f(x) = {basis:.1f}^{{(x - {h_exp:.1f})}} + {k_exp:.1f}$', color='blue')
    
    # Asimtot Horizontal
    asymptote_exp = k_exp
    ax_exp.axhline(asymptote_exp, color='red', linestyle='--', label=f'Asimtot: $y = {asymptote_exp:.1f}$')
    
    # Pengaturan Plot
    ax_exp.set_title("Grafik Fungsi Eksponen")
    ax_exp.set_xlabel("x")
    ax_exp.set_ylabel("f(x)")
    ax_exp.grid(True, linestyle=':', alpha=0.6)
    ax_exp.axvline(0, color='gray', linewidth=0.5)
    ax_exp.axhline(0, color='gray', linewidth=0.5)
    ax_exp.set_ylim(-10, 10)
    ax_exp.legend()
    
    st.pyplot(fig_exp)

    st.subheader("💡 Amati:")
    st.write(f"- Jika basis $a > 1$, grafik **meningkat** (fungsi naik).")
    st.write(f"- Jika $0 < a < 1$, grafik **menurun** (fungsi turun).")
    st.write(f"- Grafik selalu melewati titik **(h, 1+k)**, kecuali jika $a$ terdefinisi ulang.")
    st.write(f"- Asimtot horizontal: **$y = {asymptote_exp:.1f}$**.")

# ==============================================================================
# 🌳 Bagian 2: Visualisasi Fungsi Logaritma
# ==============================================================================
with col2:
    st.header("2. Fungsi Logaritma ($g(x) = \log_a(x)$)")

    # --- Input Interaktif Tambahan (Translasi) ---
    k_log = st.slider("Translasi Vertikal (k): $g(x) = \log_a(x) + k$", -5.0, 5.0, 0.0, 0.1)
    h_log = st.slider("Translasi Horizontal (h): $g(x) = \log_a(x - h)$", -5.0, 5.0, 0.0, 0.1)
    
    # --- Definisi Fungsi Logaritma ---
    # Logaritma alami (np.log) dibagi dengan log alami basis (ln(x)/ln(a))
    def logarithmic_function(x, a, h, k):
        # Hindari logaritma dari bilangan non-positif
        x_shifted = x - h
        mask = x_shifted > 0.001 
        y = np.full_like(x_shifted, np.nan)
        y[mask] = np.log(x_shifted[mask]) / np.log(a) + k
        return y

    y_log = logarithmic_function(x_vals, basis, h_log, k_log)
    
    # --- Plot Fungsi Logaritma ---
    fig_log, ax_log = plt.subplots()
    ax_log.plot(x_vals, y_log, label=f'$g(x) = \log_{{{basis:.1f}}}(x - {h_log:.1f}) + {k_log:.1f}$', color='green')

    # Asimtot Vertikal
    asymptote_log = h_log
    ax_log.axvline(asymptote_log, color='red', linestyle='--', label=f'Asimtot: $x = {asymptote_log:.1f}$')
    
    # Pengaturan Plot
    ax_log.set_title("Grafik Fungsi Logaritma")
    ax_log.set_xlabel("x")
    ax_log.set_ylabel("g(x)")
    ax_log.grid(True, linestyle=':', alpha=0.6)
    ax_log.axvline(0, color='gray', linewidth=0.5)
    ax_log.axhline(0, color='gray', linewidth=0.5)
    ax_log.set_ylim(-10, 10)
    ax_log.legend()

    st.pyplot(fig_log)
    
    st.subheader("💡 Amati:")
    st.write(f"- Domain fungsi: **$x > {asymptote_log:.1f}$**.")
    st.write(f"- Range fungsi: **Semua bilangan real**.")
    st.write(f"- Asimtot vertikal: **$x = {asymptote_log:.1f}$**.")

# ==============================================================================
# 🤝 Bagian 3: Hubungan Invers (Opsional)
# ==============================================================================

st.subheader("3. Hubungan Invers: Eksponen dan Logaritma")
st.markdown("Kedua fungsi adalah **invers** satu sama lain *jika* memiliki **basis** yang sama dan **transformasi** yang sama (misalnya, $h_{exp}=k_{log}$ dan $k_{exp}=h_{log}$ dengan basis yang sama).")

# Plot gabungan untuk melihat pencerminan (hanya untuk fungsi dasar: h=0, k=0)
if st.checkbox("Tampilkan Fungsi Dasar Invers (Basis yang Sama, Tanpa Translasi)", value=True):
    
    x_inv = np.linspace(0.01, x_max, 400) # Domain log > 0
    y_exp_inv = exponential_function(x_vals, basis, 0, 0)
    y_log_inv = logarithmic_function(x_inv, basis, 0, 0)
    
    fig_inv, ax_inv = plt.subplots()
    ax_inv.plot(x_vals, y_exp_inv, label=f'$f(x) = {basis:.1f}^x$', color='darkblue')
    ax_inv.plot(x_inv, y_log_inv, label=f'$g(x) = \log_{{{basis:.1f}}}(x)$', color='darkgreen')
    
    # Garis y = x (cermin)
    mirror_line = np.linspace(min(x_min, -10), max(x_max, 10), 100)
    ax_inv.plot(mirror_line, mirror_line, 'k--', label='$y = x$ (Garis Cermin)', alpha=0.5)
    
    # Pengaturan Plot
    ax_inv.set_title(f"Fungsi Eksponen dan Logaritma (Basis a={basis:.1f})")
    ax_inv.set_xlabel("x")
    ax_inv.set_ylabel("y")
    ax_inv.grid(True, linestyle=':', alpha=0.6)
    ax_inv.axvline(0, color='gray', linewidth=0.5)
    ax_inv.axhline(0, color='gray', linewidth=0.5)
    ax_inv.set_xlim(-5, 5)
    ax_inv.set_ylim(-5, 5)
    ax_inv.legend()
    ax_inv.set_aspect('equal', adjustable='box') # Penting untuk melihat pencerminan yang benar

    st.pyplot(fig_inv)

    st.info("Kedua fungsi tersebut adalah **refleksi (pencerminan)** satu sama lain terhadap garis **$y=x$**.")
