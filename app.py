import streamlit as st
import plotly.graph_objects as go
import random

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(page_title="RetailFlow x Decathlon | AI Analytics", layout="wide")

# 2. CSS - MODERN TASARIM VE RENK DENGESİ
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    
    /* Beyaz Metrik Kutuları */
    div[data-testid="stMetric"] {
        background-color: white !important;
        padding: 20px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08) !important;
        border-top: 6px solid #0082C3 !important;
        min-height: 160px !important;
        display: flex; flex-direction: column; justify-content: center;
    }

    /* Rakamlar - Lacivert */
    [data-testid="stMetricValue"] {
        color: #1e3a8a !important; 
        font-size: 32px !important;
        font-weight: 700 !important;
    }

    /* Başlıklar - Gri */
    [data-testid="stMetricLabel"] {
        color: #4b5563 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    /* Sidebar Yazı Düzenlemeleri */
    .stSlider label, .stWidget label {
        color: #1f2937 !important;
        font-weight: 600 !important;
    }
    [data-testid="stWidgetLabel"] p {
        color: white !important; /* Odak Spor Kategorisi Yazısı */
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST BAŞLIK VE BRANDING
st.title("🔵 RetailFlow AI: Decathlon Operasyonel Karar Destek Sistemi")
st.markdown("**Business Analytics Dashboard** | RFID & AI-Powered Queue Optimization")
st.info("Bu sistem, RFID verilerini ve yapay zeka destekli tahminleme modellerini kullanarak iade süreçlerini optimize eder.")

# 4. SIDEBAR: PARAMETRELER
with st.sidebar:
    st.header("🏬 Mağaza Canlı Verileri")
    st.markdown("---")
    
    kategori = st.selectbox("Odak Spor Kategorisi", 
                            ["Outdoor & Kamp", "Fitness & Yoga", "Su Sporları", "Takım Sporları"])
    
    # 🔄 Verileri Rastgele Güncelleme Mantığı (AI Senaryo Simülasyonu)
    if st.button("🔄 AI Senaryosunu Güncelle"):
        musteri_val = random.randint(50, 380)
        iade_val = random.randint(5, 75)
        personel_val = random.randint(4, 28)
    else:
        musteri_val, iade_val, personel_val = 165, 35, 12

    musteri = st.slider("Mağazadaki Toplam Müşteri", 0, 400, musteri_val)
    personel = st.slider("Aktif Takım Arkadaşı (Staff)", 1, 30, personel_val)
    iade_kuyrugu = st.slider("Bekleyen İade/Değişim (Kişi)", 0, 100, iade_val)
    
    st.markdown("---")
    rfid_active = st.toggle("RFID Otomatik Sayım Sistemi", value=True)
    st.caption("💡 AI Modeli: 'Kuyruk Teorisi v2.1' aktif.")

# 5. BUSINESS LOGIC & AI SCORING (İş Analitiği Zekası)
katsayi = 2.3 if kategori == "Outdoor & Kamp" else 1.4
bekleme_suresi = (iade_kuyrugu * katsayi) / (personel * 0.5)
verimlilik = min(100, int((personel * 18) / (musteri + iade_kuyrugu + 1) * 100))

# AI Tahmin Skoru (0-100) - Sistemin ne kadar riskli olduğunu hesaplar
ai_risk_score = min(100, int((bekleme_suresi * 2.5) + (100 - verimlilik)))

# 6. ÜST METRİKLER (KPIs)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Tahmini İade Süresi", f"{int(bekleme_suresi)} dk", delta="Gecikme!" if bekleme_suresi > 18 else None)
m2.metric("Sistem Sağlığı", f"%{verimlilik}")
m3.metric("AI Risk Skoru", f"{ai_risk_score}/100", delta="Yüksek" if ai_risk_score > 65 else "Normal", delta_color="inverse")
m4.metric("RFID Doğruluğu", "%99.6" if rfid_active else "%82.4")

st.markdown("---")

# 7. ANALİZ VE AI STRATEJİ MERKEZİ
col_left, col_right = st.columns([1.4, 1])

with col_left:
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = verimlilik,
        gauge = {
            'axis': {'range': [None, 100], 'tickcolor': "#4b5563"},
            'bar': {'color': "#0082C3"},
            'steps': [
                {'range': [0, 40], 'color': "#fee2e2"},
                {'range': [40, 75], 'color': "#fef3c7"},
                {'range': [75, 100], 'color': "#dcfce7"}]
        },
        title = {'text': "Operasyonel Verimlilik Endeksi", 'font': {'size': 20, 'color': 'white'}}
    ))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', height=400)
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("🤖 AI Strateji Merkezi")
    
    # Dinamik AI Yorumlama Mantığı (Gerçek AI hissi veren bölüm)
    if ai_risk_score > 70:
        st.error(f"**KRİTİK UYARI:** {kategori} iadeleri operasyonu kilitliyor.")
        ai_tavsiye = f"AI Analizi: Müşteri/Personel yükü optimal sınırın %{ai_risk_score - 50} üzerinde. Welcome Desk personeli derhal iade masasına kaydırılmalıdır."
    elif 40 <= ai_risk_score <= 70:
        st.warning(f"**DİKKAT:** Bekleme süresi artış trendinde.")
        ai_tavsiye = "AI Öngörüsü: Mevcut ivme devam ederse 15 dk içinde darboğaz yaşanabilir. RFID Fast-Track kanalını sadece iadeler için önceliklendirin."
    else:
        st.success("**STABİL:** Kaynak kullanımı verimli.")
        ai_tavsiye = "AI Modeli: Mevcut kapasite talebi karşılamak için yeterli. NPS (Müşteri Memnuniyeti) anketlerine odaklanılabilir."

    st.write(f"🔍 **AI Tavsiyesi:** {ai_tavsiye}")

    st.markdown("---")
    
    # 📄 RAPOR İNDİRME BUTONU
    report_text = f"""RETAILFLOW AI ANALİZ RAPORU
---------------------------
Kategori: {kategori}
Verimlilik: %{verimlilik}
AI Risk Skoru: {ai_risk_score}/100
Bekleme Süresi: {int(bekleme_suresi)} dk
---------------------------
STRATEJİK TAVSİYE:
{ai_tavsiye}
---------------------------
Oluşturan: Melisa Kabuk | RetailFlow AI"""
    
    st.download_button(
        label="📄 Operasyon Raporunu İndir (TXT)",
        data=report_text,
        file_name="retailflow_analiz.txt",
        mime="text/plain"
    )

# 8. ALT BİLGİ
st.caption("RetailFlow x Decathlon Projesi | Melisa Kabuk | UpSchool Future Talent Program")
