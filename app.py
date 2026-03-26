import streamlit as st
import pandas as pd
import joblib

# 1. Load Otak AI
model = joblib.load('model_startup.pkl')

# 2. Setup Tema Warna & Konfigurasi Premium
st.set_page_config(page_title="Startup Success Predictor", page_icon="🚀", layout="wide")

# ADVANCED CSS INJECTION (Mantra Rahasia Wow)
# - Import Google Fonts (Poppins)
# - Custom styling buat seluruh app, sidebar, judul, tabel, dan tombol
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Poppins', sans-serif !important;
        background-color: #0d1117;
        color: #ffffff;
    }

    [data-testid="stSidebar"] {
        background-color: #161b22;
        padding-top: 2rem;
    }

    /* Warna Judul Utama & Subjudul */
    h1, h2, h3 {
        color: #00e5ff !important; /* Rich Toska */
        font-weight: 700 !important;
    }

    /* Menghilangkan Embos pada Dataframe */
    .stTable {
        background-color: transparent !important;
        border-collapse: collapse !important;
        width: 100% !important;
        border: none !important;
    }

    /* Customisasi Tabel st.table */
    .stTable th {
        background-color: #00e5ff;
        color: black !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 8px 8px 0 0 !important;
    }

    .stTable td {
        background-color: #1c2128 !important;
        color: white !important;
        border: none !important;
        font-size: 1.1rem !important;
    }
    
    .stTable tr:last-child td:first-child {
        border-radius: 0 0 0 8px !important;
    }
    .stTable tr:last-child td:last-child {
        border-radius: 0 0 8px 0 !important;
    }

    /* Tombol Analisis Premium */
    .stButton>button {
        background-color: #00e5ff;
        color: black;
        border-radius: 12px;
        border: none;
        padding: 15px 30px;
        font-size: 1.2rem;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #00b8d4;
        color: black;
        transform: scale(1.05);
    }

    /* Customisasi Kotak Hasil Prediksi (Pop-up modern) */
    .stAlert {
        border-radius: 16px;
        padding: 20px;
        margin-top: 1rem;
    }

</style>
""", unsafe_allow_html=True)

# 3. Tampilan Utama Web
st.title("🚀 Startup Success Predictor")
st.markdown("Analisis probabilitas kesuksesan startup berdasarkan parameter historis.")

# 4. Inputan di Sidebar (Rapi dan Jelas)
st.sidebar.markdown("## 🛠️ Parameter Startup")
def user_input_features():
    funding = st.sidebar.number_input("Total Pendanaan (USD)", min_value=0, value=1000000, step=100000)
    rounds = st.sidebar.slider("Jumlah Ronde Pendanaan", 1, 10, 1)
    age = st.sidebar.slider("Umur Startup (Tahun)", 0, 20, 3)
    
    # Rapiin datanya
    data = {
        'funding_total_usd': funding,
        'funding_rounds': rounds,
        'umur_startup_tahun': age
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# 5. Area Utama (Layouting)
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("### 📋 Input Data")
    # PENGGUNAAN st.table() UNTUK TABEL STATIS PENUH
    # Gak ada lagi scrollbar untuk satu baris data!
    # Panggil fungsi style.hide() buat nebas nomor index-nya
    st.table(input_df.style.hide(axis="index"))
    predict_btn = st.button("Analisis Nasib! ✨")

with col2:
    st.markdown("### 🔍 Hasil Analisis")
    if predict_btn:
        prediction = model.predict(input_df)
        
        # Pembeda visual yang lebih wow
        if prediction[0] == 0:
            st.error("💀 STATUS: CLOSED")
            st.warning("⚠️ **Peringatan Tinggi:** Startup terdeteksi berisiko bangkrut. Evaluasi strategi bisnis dan efisiensi operasional sangat disarankan.")
        elif prediction[0] == 1:
            st.success("💰 STATUS: ACQUIRED")
            st.balloons()
            st.info("🎉 **Potensi Kesuksesan Besar:** Startup memiliki parameter kuat untuk akuisisi atau exit yang menguntungkan.")
        else:
            st.info("🏢 STATUS: OPERATING")
            st.write("✅ Startup stabil dan memiliki parameter operasional yang sehat untuk jangka panjang.")
    else:
        st.write("Tekan tombol **'Analisis Nasib!'** untuk melihat hasil analisis data.")

st.markdown("---")
st.markdown("""
### 🧠 Catatan Analis (Data Scientist Note):
Model AI ini dilatih menggunakan dataset historis dari Crunchbase. Namun, terdapat fenomena **Imbalanced Dataset** dan **Kekurangan Fitur (Feature Starvation)**:
1.  **Mayoritas Data:** Lebih dari 85% data historis berstatus 'Operating'. Hal ini membuat model memiliki kecenderungan bias untuk memprediksi startup akan terus beroperasi.
2.  **Konteks Bisnis:** Prediksi ini hanya menggunakan 3 variabel sederhana (Pendanaan, Ronde, Umur). Di dunia nyata, kesuksesan startup sangat bergantung pada faktor kualitatif seperti model bisnis, kompetensi *founder*, dan kondisi pasar ekonomi makro yang tidak tertangkap oleh model ini.
""")

st.caption("Created by Aqilla")