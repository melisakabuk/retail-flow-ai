import streamlit as st
import plotly.graph_objects as go

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(page_title="RetailFlow x Decathlon | Business Analytics", layout="wide")

# 2. CSS - SİMETRİ VE TAM OKUNABİLİRLİK (Kutuları ve Yazıları Düzelten Bölüm)
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    
    /* Beyaz Metrik Kutularının Tasarımı ve Sabit Boyutu */
    div[data-testid="stMetric"] {
        background-color: white !important;
        padding: 25px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        border-top: 6px solid #0082C3 !important;
        min-height: 160px !important; /* Tüm kutuları aynı boyuta sabitler */
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    /* Rakamlar - TAM SİYAH */
    [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-size: 30px !important;
        font-weight: 800 !important;
    }

    /* Başlıklar - TAM SİYAH */
    [data-testid="stMetricLabel"] {
        color: #000000 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        margin-bottom: 10px !important;
    }

    /* Grafik Başlığı ve Diğer Metinler */
    h1, h2, h3, p { color: #000000 !important; }
    
    /* Sidebar Yazıları */
    .css-1d391kg, .stSlider label, .stSelectbox label {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST BAŞLIK
st.title("🔵 RetailFlow AI: Decathlon Operasyonel Karar Destek Sistemi")
st.info("Bu prototip, Decathlon iade süreçlerini optimize etmek için tasarlanmış bir İş Analitiği çözümüdür.")

# 4. SIDEBAR
with st.sidebar:
    st.header("🏬 Mağaza Canlı Verileri")
    st.markdown("---")
    kategori = st.selectbox("Odak Spor Kategorisi", ["Outdoor & Kamp", "Fitness & Yoga", "Su Sporları", "Takım Sporları"])
    musteri = st.slider("Mağazadaki Toplam Müşteri", 0, 400, 180)
    personel = st.slider("Aktif Takım Arkadaşı (Staff)", 1, 30, 12)
    iade_kuyrugu = st.slider("Bekleyen İade/Değişim (Kişi)", 0, 100, 30)
    st.markdown("---")
    rfid_active = st.toggle("RFID Otomatik Sayım Sistemi", value=True)

# 5. BUSINESS LOGIC
katsayi = 2.2 if kategori == "Outdoor & Kamp" else 1.3
bekleme_suresi = (iade_kuyrugu * katsayi) / (personel * 0.5)
verimlilik = min(100, int((personel * 18) / (musteri + iade_kuyrugu + 1) * 100))

# 6. ÜST METRİKLER (Kutular artık aynı boyutta!)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Tahmini İade Süresi", f"{int(bekleme_suresi)} dk")
m2.metric("Sistem Sağlığı", f"%{verimlilik}")
m3.metric("Kategori Yoğunluğu", kategori)
m4.metric("RFID Doğruluğu", "%99.6" if rfid_active else "%84.2")

st.markdown("---")

# 7. ANALİZ BÖLÜMÜ
col_left, col_right = st.columns([1.5, 1])

with col_left:
    # Grafik Başlığını Kod İçinde Simsiyah Yapma
    st.markdown("<h3 style='text-align: center; color: black;'>📈 Mağaza Verimlilik Endeksi</h3>", unsafe_allow_html=True)
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = verimlilik,
        gauge = {
            'axis': {'range': [None, 100], 'tickcolor': "black"},
            'bar': {'color': "#0082C3"},
            'steps': [
                {'range': [0, 40], 'color': "#fee2e2"},
                {'range': [40, 75], 'color': "#fef3c7"},
                {'range': [75, 100], 'color': "#dcfce7"}]
        }
    ))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350, margin=dict(t=0, b=0))
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("🤖 Decathlon AI Karar Merkezi")
    if bekleme_suresi > 18:
        st.error(f"**DARBOĞAZ:** {kategori} iadeleri yoğun.")
        st.write("- Welcome Desk personeli iadeye kaydırılmalı.")
    else:
        st.success("**DURUM OPTİMAL:** Kaynak dağılımı verimli.")

    st.markdown("---")
    st.write(f"🔍 **Stratejik Öngörü:** Personel artışı hızı **%20** iyileştirir.")

# 8. ALT BİLGİ
st.caption("RetailFlow x Decathlon Case Study | Melisa | UpSchool Future Talent Program")
