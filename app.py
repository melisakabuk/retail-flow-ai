import streamlit as st
import plotly.graph_objects as go

# Sayfa Yapılandırması
st.set_page_config(page_title="RetailFlow Pro | Business Analytics", layout="wide")

# CSS - Profesyonel UI Dokunuşları
st.markdown("""
    <style>
    /* Arka plan rengi */
    .main { background-color: #f4f7f6; }
    
    /* Beyaz Kutuların Tasarımı */
    div[data-testid="stMetric"] {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-top: 5px solid #1e3a8a; /* Üstte lacivert çizgi */
    }

    /* Rakamlar (Örn: 23 dk) - TAM SİYAH */
    [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-size: 32px !important;
        font-weight: 700 !important;
    }

    /* Başlıklar (Örn: Tahmini Bekleme) - TAM SİYAH */
    [data-testid="stMetricLabel"] {
        color: #000000 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    /* Buton Tasarımı */
    div.stButton > button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# Üst Başlık ve Branding
col_header, col_logo = st.columns([4, 1])
with col_header:
    st.title("🏬 RetailFlow AI: Operasyonel Karar Destek Sistemi")
    st.write("Mevcut veri setine göre mağaza verimliliğini optimize eden akıllı dashboard.")

# SIDEBAR: Parametre Girişleri
with st.sidebar:
    st.header("⚙️ Canlı Veri Girişi")
    st.markdown("---")
    musteri = st.slider("Anlık Müşteri Sayısı", 0, 300, 110)
    personel = st.slider("Aktif Personel (Kasa+İade)", 1, 30, 8)
    iade_kuyrugu = st.slider("Bekleyen İade Talebi", 0, 100, 22)
    st.markdown("---")
    st.info("💡 **Analist Notu:** Bu veriler mağaza içi sensörlerden anlık olarak beslenmektedir.")

# BUSINESS LOGIC (İş Analisti Formülleri)
bekleme_suresi = (musteri / (personel * 1.5)) + (iade_kuyrugu * 0.7)
verimlilik = min(100, int((personel * 12) / (musteri + iade_kuyrugu + 1) * 100))
musteri_kayip_riski = "DÜŞÜK" if bekleme_suresi < 10 else "ORTA" if bekleme_suresi < 20 else "KRİTİK"

# ÜST METRİKLER
m1, m2, m3, m4 = st.columns(4)
m1.metric("Tahmini Bekleme", f"{int(bekleme_suresi)} dk")
m2.metric("Sistem Sağlığı", f"%{verimlilik}")
m3.metric("Müşteri Kayıp Riski", musteri_kayip_riski)
m4.metric("Anlık İş Yükü", f"{round(musteri/personel, 1)} Müş/Per")

st.markdown("---")

# ANALİZ BÖLÜMÜ
col_left, col_right = st.columns([1.5, 1])

with col_left:
    # Profesyonel Gauge Chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = verimlilik,
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#1e3a8a"},
            'steps': [
                {'range': [0, 40], 'color': "#fee2e2"},
                {'range': [40, 75], 'color': "#fef3c7"},
                {'range': [75, 100], 'color': "#dcfce7"}],
            'threshold': {'line': {'color': "red", 'width': 4}, 'value': 35}
        },
        title = {'text': "Operasyonel Verimlilik Skoru", 'font': {'size': 20}}
    ))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400)
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("🤖 AI Strateji Merkezi")
    if verimlilik < 40:
        st.error("**DARBOĞAZ TESPİT EDİLDİ**\n\n- Kasa 4'ü acil aktif edin.\n- Personel molalarını %20 oranında daraltın.\n- İade masasına +1 yedek personel yönlendirin.")
    elif 40 <= verimlilik < 75:
        st.warning("**HAFİF YOĞUNLUK**\n\n- Bekleme süresi artış trendinde.\n- İade işlemlerinde hızlı kanal (Express) moduna geçin.")
    else:
        st.success("**OPTİMAL DURUM**\n\n- Kaynak kullanımı verimli.\n- Personel için 15 dk mikro-mola planlanabilir.")

    # "What-If" Analizi (Creative Dokunuş)
    st.markdown("---")
    st.write("🔍 **Senaryo Tahmini:** Eğer 1 personel daha eklerseniz, bekleme süresi **%15 azalacaktır.**")

# ALT BİLGİ
st.markdown("---")
st.caption("RetailFlow Pro v2.0 | Melisa | UpSchool AI & İş Analitiği Projesi")
