import streamlit as st
import plotly.graph_objects as go
import random

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(page_title="RetailFlow x Decathlon | AI Analytics", layout="wide")

# 2. CSS - RENK DENGESİ VE SİMETRİ (Yazıları simsiyahlıktan kurtarıp premium yaptık)
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    
    /* Beyaz Metrik Kutuları */
    div[data-testid="stMetric"] {
        background-color: white !important;
        padding: 20px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08) !important;
        border-top: 6px solid #0082C3 !important; /* Decathlon Mavisi */
        min-height: 160px !important;
        display: flex; flex-direction: column; justify-content: center;
    }

    /* Rakamlar - Koyu Lacivert */
    [data-testid="stMetricValue"] {
        color: #1e3a8a !important; 
        font-size: 32px !important;
        font-weight: 700 !important;
    }

    /* Başlıklar - Koyu Gri */
    [data-testid="stMetricLabel"] {
        color: #4b5563 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    /* Sidebar Etiketleri */
    .stSlider label, .stSelectbox label, .stWidget label {
        color: #1f2937 !important;
        font-weight: 600 !important;
    }
    /* Sidebar'daki Selectbox (Kategori) etiketini beyaz yapar */
    [data-testid="stWidgetLabel"] p {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST BAŞLIK VE BRANDING
st.title("🔵 RetailFlow AI: Decathlon Operasyonel Karar Destek Sistemi")
st.markdown("**Business Analytics Dashboard** | RFID & Queue Theory Optimization")
st.info("Bu sistem, mağaza içi iade süreçlerini gerçek zamanlı verilerle optimize etmek için tasarlanmıştır.")

# 4. SIDEBAR: PARAMETRELER
with st.sidebar:
    st.header("🏬 Mağaza Canlı Verileri")
    st.markdown("---")
    kategori = st.selectbox("Odak Spor Kategorisi", 
                            ["Outdoor & Kamp", "Fitness & Yoga", "Su Sporları", "Takım Sporları"])
    
    # Küçük bir creative dokunuş: Simülasyon butonu
    if st.button("🔄 Verileri Rastgele Güncelle"):
        musteri_val = random.randint(50, 350)
        iade_val = random.randint(5, 60)
    else:
        musteri_val = 165
        iade_val = 35

    musteri = st.slider("Mağazadaki Toplam Müşteri", 0, 400, musteri_val)
    personel = st.slider("Aktif Takım Arkadaşı (Staff)", 1, 30, 12)
    iade_kuyrugu = st.slider("Bekleyen İade/Değişim (Kişi)", 0, 100, iade_val)
    
    st.markdown("---")
    rfid_active = st.toggle("RFID Otomatik Sayım Sistemi", value=True)
    st.caption("💡 Veriler RFID gate sistemlerinden anlık beslenmektedir.")

# 5. BUSINESS LOGIC
katsayi = 2.1 if kategori == "Outdoor & Kamp" else 1.3
bekleme_suresi = (iade_kuyrugu * katsayi) / (personel * 0.5)
verimlilik = min(100, int((personel * 18) / (musteri + iade_kuyrugu + 1) * 100))

# 6. ÜST METRİKLER
m1, m2, m3, m4 = st.columns(4)
m1.metric("Tahmini İade Süresi", f"{int(bekleme_suresi)} dk", delta="Gecikme!" if bekleme_suresi > 20 else None)
m2.metric("Sistem Sağlığı", f"%{verimlilik}")
m3.metric("Kategori Yoğunluğu", kategori)
m4.metric("RFID Doğruluğu", "%99.6" if rfid_active else "%84.2")

st.markdown("---")

# 7. ANALİZ VE AI TAVSİYELERİ
col_left, col_right = st.columns([1.5, 1])

with col_left:
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = verimlilik,
        gauge = {
            'axis': {'range': [None, 100], 'tickcolor': "#4b5563"},
            'bar': {'color': "#0082C3"},
            'bgcolor': "white",
            'steps': [
                {'range': [0, 40], 'color': "#fee2e2"},
                {'range': [40, 75], 'color': "#fef3c7"},
                {'range': [75, 100], 'color': "#dcfce7"}]
        },
        title = {'text': "Mağaza Verimlilik Endeksi", 'font': {'size': 20, 'color': 'white'}}
    ))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', height=400)
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("🤖 Decathlon AI Karar Merkezi")
    if bekleme_suresi > 20:
        st.error(f"**DARBOĞAZ TESPİT EDİLDİ:** {kategori} yoğunlaştı.")
        öneri = "Welcome Desk'ten 2 kişiyi iade masasına kaydırın."
        st.write(f"👉 **Aksiyon:** {öneri}")
    else:
        st.success("**DURUM OPTİMAL:** Kaynak dağılımı verimli.")
        öneri = "Mevcut kaynak dağılımı şu an optimal seviyede."

    st.markdown("---")
    st.write(f"🔍 **Stratejik Öngörü:** Personel sayısını 1 kişi artırmak hızı **%22** iyileştirir.")
    
    # 📄 RAPOR İNDİRME BUTONU (BA Farkı)
    report_text = f"""DECATHLON OPERASYON RAPORU
---------------------------
Kategori: {kategori}
Müşteri Sayısı: {musteri}
Verimlilik: %{verimlilik}
Bekleme Süresi: {int(bekleme_suresi)} dk
AI Önerisi: {öneri}
---------------------------
RetailFlow AI Analiz Sistemi"""
    
    st.download_button(
        label="📄 Analiz Raporunu İndir (TXT)",
        data=report_text,
        file_name="mağaza_analiz_raporu.txt",
        mime="text/plain"
    )

# 8. ALT BİLGİ
st.caption("RetailFlow x Decathlon Case Study | Melisa Kabuk | UpSchool Future Talent Program")
