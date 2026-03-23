import streamlit as st
import plotly.graph_objects as go

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(page_title="RetailFlow x Decathlon | Business Analytics", layout="wide")

# 2. CSS - SADECE KUTU BOYUTLARI VE SİYAH METİN DÜZELTMESİ
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    
    /* Beyaz Metrik Kutularının Tasarımı ve Boyut Sabitleme */
    div[data-testid="stMetric"] {
        background-color: white !important;
        padding: 20px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        border-top: 6px solid #0082C3 !important; /* Decathlon Mavisi */
        min-height: 160px !important; /* Tüm kutuları aynı boyuta sabitler */
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    /* Rakamlar - TAM SİYAH VE NET */
    [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-size: 32px !important;
        font-weight: 700 !important;
    }

    /* Başlıklar - TAM SİYAH VE NET */
    [data-testid="stMetricLabel"] {
        color: #000000 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    /* Sidebar Yazılarını Belirginleştirme */
    .stSlider label, .stSelectbox label, .stWidget label {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST BAŞLIK VE BRANDING
st.title("🔵 RetailFlow AI: Decathlon Operasyonel Karar Destek Sistemi")
st.markdown("**İş Analizi Portfolyo Projesi** | RFID ve Kuyruk Teorisi Entegrasyonu")
st.info("Bu prototip, Decathlon mağaza içi iade süreçlerindeki darboğazları gerçek zamanlı verilerle optimize etmek için tasarlanmıştır.")

# 4. SIDEBAR: PARAMETRELER
with st.sidebar:
    st.header("🏬 Mağaza Canlı Verileri")
    st.markdown("---")
    kategori = st.selectbox("Odak Spor Kategorisi", 
                            ["Outdoor & Kamp", "Fitness & Yoga", "Su Sporları", "Takım Sporları"])
    
    musteri = st.slider("Mağazadaki Toplam Müşteri", 0, 400, 165)
    personel = st.slider("Aktif Takım Arkadaşı (Staff)", 1, 30, 12)
    iade_kuyrugu = st.slider("Bekleyen İade/Değişim (Kişi)", 0, 100, 35)
    
    st.markdown("---")
    rfid_active = st.toggle("RFID Otomatik Sayım Sistemi", value=True)
    st.caption("💡 Bu veriler mağaza içi sensörlerden ve RFID gate sistemlerinden anlık beslenmektedir.")

# 5. BUSINESS LOGIC
katsayi = 2.1 if kategori == "Outdoor & Kamp" else 1.3
bekleme_suresi = (iade_kuyrugu * katsayi) / (personel * 0.5)
verimlilik = min(100, int((personel * 18) / (musteri + iade_kuyrugu + 1) * 100))

# 6. ÜST METRİKLER (Artık hepsi aynı boyutta ve simsiyah)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Tahmini İade Süresi", f"{int(bekleme_suresi)} dk", delta="Kritik" if bekleme_suresi > 20 else "Normal")
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
            'axis': {'range': [None, 100], 'tickcolor': "black"},
            'bar': {'color': "#0082C3"},
            'bgcolor': "white",
            'steps': [
                {'range': [0, 40], 'color': "#fee2e2"},
                {'range': [40, 75], 'color': "#fef3c7"},
                {'range': [75, 100], 'color': "#dcfce7"}],
            'threshold': {'line': {'color': "black", 'width': 4}, 'value': verimlilik}
        },
        title = {'text': "Mağaza Verimlilik Endeksi", 'font': {'size': 20, 'color': 'black'}}
    ))
    # Grafik Başlığını Beyaz, Arka Planı Şeffaf Yapma
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)', 
        height=400,
        font={'color': "white"} # Grafik içindeki tüm yazıların rengini beyaz yapar
    )
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("🤖 Decathlon AI Karar Merkezi")
    if bekleme_suresi > 20:
        st.error(f"**DARBOĞAZ TESPİT EDİLDİ:** {kategori} iade işlemleri yavaşladı.")
        st.write("👉 **Aksiyon:** Welcome Desk'ten 2 kişiyi acil iade masasına kaydırın.")
        st.write("👉 **Aksiyon:** RFID hızlı kontrol kanalını (Fast Track) devreye alın.")
    elif 40 <= verimlilik < 75:
        st.warning("**DİKKAT:** Yoğunluk artış trendinde. Personel rotasyonunu beklemeye alın.")
    else:
        st.success("**DURUM OPTİMAL:** Kaynak dağılımı verimli.")

    st.markdown("---")
    st.write(f"🔍 **Stratejik Öngörü:** Personel sayısını 1 kişi artırmak hızı **%22** iyileştirir.")

# 8. ALT BİLGİ
st.markdown("---")
st.caption("RetailFlow x Decathlon Case Study | Melisa | UpSchool Future Talent Program")
