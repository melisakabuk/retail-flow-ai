import streamlit as st
import plotly.graph_objects as go
import random

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(page_title="RetailFlow Pro | AI & Analytics", layout="wide")

# 2. CSS - MODERN LACİVERT & GRİ TONLARI (Simsiyah değil, premium görünüm)
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    div[data-testid="stMetric"] {
        background-color: white !important; padding: 25px !important;
        border-radius: 12px !important; box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        border-top: 6px solid #0082C3 !important; min-height: 160px !important;
        display: flex; flex-direction: column; justify-content: center;
    }
    [data-testid="stMetricValue"] { color: #1e3a8a !important; font-size: 30px !important; font-weight: 800 !important; }
    [data-testid="stMetricLabel"] { color: #4b5563 !important; font-size: 16px !important; font-weight: 700 !important; }
    h1, h2, h3, p { color: #1f2937 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST BAŞLIK
st.title("🔵 RetailFlow AI: Decathlon Operasyonel Karar Destek Sistemi")
st.info("Bu sistem, RFID verilerini ve AI destekli karar mekanizmasını kullanarak mağaza verimliliğini optimize eder.")

# 4. SIDEBAR - CANLI VERİ GİRİŞİ
with st.sidebar:
    st.header("🏬 Mağaza Canlı Verileri")
    st.markdown("---")
    kategori = st.selectbox("Odak Spor Kategorisi", ["Outdoor & Kamp", "Fitness & Yoga", "Su Sporları", "Takım Sporları"])
    
    # AI Simülasyonu için rastgele veri butonu
    if st.button("🚀 AI Senaryosu Oluştur"):
        m_val, p_val, i_val = random.randint(100, 350), random.randint(5, 15), random.randint(10, 60)
    else:
        m_val, p_val, i_val = 165, 12, 35

    musteri = st.slider("Anlık Müşteri Sayısı", 0, 400, m_val)
    personel = st.slider("Aktif Takım Arkadaşı", 1, 30, p_val)
    iade_kuyrugu = st.slider("Bekleyen İade/Değişim", 0, 100, i_val)
    
    st.markdown("---")
    rfid_active = st.toggle("RFID Otomatik Sayım Aktif", value=True)

# 5. BUSINESS LOGIC & AI SCORING (İş Analisti Mantığı)
katsayi = 2.2 if kategori == "Outdoor & Kamp" else 1.3
bekleme_suresi = (iade_kuyrugu * katsayi) / (personel * 0.5)
verimlilik = min(100, int((personel * 18) / (musteri + iade_kuyrugu + 1) * 100))

# AI Risk Skoru Hesaplama (0-100)
ai_risk_score = min(100, int((bekleme_suresi * 3) + (100 - verimlilik)))

# 6. ÜST METRİKLER (KPIs)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Tahmini Bekleme", f"{int(bekleme_suresi)} dk")
m2.metric("Sistem Sağlığı", f"%{verimlilik}")
m3.metric("AI Risk Skoru", f"{ai_risk_score}/100", delta="Yüksek" if ai_risk_score > 60 else "Düşük", delta_color="inverse")
m4.metric("RFID Doğruluğu", "%99.6" if rfid_active else "%84.2")

st.divider()

# 7. ANALİZ VE AI STRATEJİ MERKEZİ
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.markdown("<h3 style='text-align: center;'>📈 Mağaza Verimlilik Endeksi</h3>", unsafe_allow_html=True)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number", value = verimlilik,
        gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': "#0082C3"},
                 'steps': [{'range': [0, 40], 'color': "#fee2e2"}, 
                           {'range': [40, 75], 'color': "#fef3c7"},
                           {'range': [75, 100], 'color': "#dcfce7"}]}))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', height=380)
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("🤖 AI Strateji Merkezi")
    
    # Dinamik AI Analiz Metni Üretimi
    if ai_risk_score > 65:
        st.error(f"**KRİTİK ANALİZ:** {kategori} kategorisindeki yığılma operasyonel riski artırıyor.")
        ai_advice = f"Müşteri/Personel yükü optimal sınırın %{ai_risk_score - 50} üzerinde. Acil personel kaydırma önerilir."
    elif 35 <= ai_risk_score <= 65:
        st.warning(f"**DİKKAT:** Bekleme süresi artış trendinde.")
        ai_advice = "RFID Fast-Track kanalını aktif ederek küçük ürün iadelerini hızlandırın."
    else:
        st.success("**DURUM OPTİMAL:** Sistem verimli çalışıyor.")
        ai_advice = "Mevcut kaynak dağılımı talebi karşılamak için yeterli."

    st.write(f"🔍 **AI Yorumu:** {ai_advice}")

    # 8. RAPOR ÇIKTISI (Dinamik Raporlama)
    st.markdown("---")
    report_data = f"RETAILFLOW ANALİZ RAPORU\nKategori: {kategori}\nVerimlilik: %{verimlilik}\nRisk Skoru: {ai_risk_score}\nAI Tavsiyesi: {ai_advice}"
    st.download_button(label="📄 Analiz Raporunu İndir (TXT)", data=report_data, file_name="retailflow_analiz.txt")

# 9. ALT BİLGİ
st.caption("RetailFlow x Decathlon Pro | Melisa Kabuk | UpSchool AI Future Talent Program")
