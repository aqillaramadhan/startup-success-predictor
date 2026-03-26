import streamlit as st
import pandas as pd
import joblib

# 1. Load Otak AI
model = joblib.load('model_startup.pkl')

# 2. Setup Tema & Visual Premium
st.set_page_config(page_title="Startup Success Predictor", page_icon="🚀", layout="wide")

# Custom CSS buat Visual "WOW" (Nggak Ngeberatin Web!)
st.markdown("""
<style>
    /* Import Google Fonts (Poppins) */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    /* Terapkan font ke seluruh aplikasi */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Poppins', sans-serif;
        background-color: #0e1117; /* Charcoal gelap yang elegan */
        color: white;
    }
    
    /* Warna Judul Utama */
    h1 {
        color: #00c8b5; /* Rich Turquoise yang lu minta */
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Ganti Judul di Sidebar */
    .stHeader h1 {
        color: white !important;
        font-weight: 600 !important;
    }

    /* Hias Kotak Area Input & Output (Shadow & Rounded) */
    [data-testid="stVerticalBlock"] > div:has(div.element-container) {
        border-radius: 12px;
        background-color: #1a1c24; /* Sedikit lebih terang dari background */
        padding: 1rem;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3); /* Shadow halus */
    }

    /* Tombol Prediksi Mahal (Turquoise) */
    .stButton>button {
        background-color: #00c8b5;
        color: black;
        border-radius: 10px;
        border: none;
        padding: 15px 30px;
        font-size: 1.2rem;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #00e0cb;
        color: black;
        transform: scale(1.05); /* Sedikit membesar saat dihover */
    }
    
    /* Warna Slider */
    .stSlider [data-testid="stThumb"] {
        background-color: #00c8b5;
    }
    
    /* Warna Input Nomor */
    .stNumberInput input {
        color: #00c8b5;
    }
</style>
""", unsafe_allow_html=True)

# 3. Tampilan Utama Web
st.title("🚀 Startup Success Predictor")
st.markdown("Aplikasi berbasis Data Science untuk menganalisis probabilitas nasib startup lu.")

# 4. Inputan di Sidebar (Dibuat lebih simpel)
st.sidebar.markdown("## 🛠️ Input Parameter")
def user_input_features():
    funding = st.sidebar.number_input("Total Pendanaan (USD)", min_value=0, value=1000000, step=100000)
    rounds = st.sidebar.slider("Jumlah Ronde Pendanaan", 1, 10, 1)
    age = st.sidebar.slider("Umur Startup (Tahun)", 0, 20, 3)
    
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
    st.markdown("### 📋 Data Input")
    st.write(input_df)
    predict_btn = st.button("Analisis Nasib! ✨")

with col2:
    st.markdown("### 🔍 Hasil Analisis")
    if predict_btn:
        prediction = model.predict(input_df)
        
        # Area Hasil dengan Pembeda Visual Wow
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
        st.write("Silakan klik tombol **'Analisis Nasib!'** untuk melihat hasil analisis data.")

st.markdown("---")
st.markdown("""
### 🧠 Catatan Analis (Data Scientist Note):
Model AI ini dilatih menggunakan dataset historis dari Crunchbase. Namun, terdapat fenomena **Imbalanced Dataset** dan **Kekurangan Fitur (Feature Starvation)**:
1.  **Mayoritas Data:** Lebih dari 85% data historis berstatus 'Operating'. Hal ini membuat model memiliki kecenderungan bias untuk memprediksi startup akan terus beroperasi.
2.  **Konteks Bisnis:** Prediksi ini hanya menggunakan 3 variabel sederhana (Pendanaan, Ronde, Umur). Di dunia nyata, kesuksesan startup sangat bergantung pada faktor kualitatif seperti model bisnis, kompetensi *founder*, dan kondisi pasar ekonomi makro yang tidak tertangkap oleh model ini.
""")
st.caption("Created by Aqilla")