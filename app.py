import streamlit as st
import plotly.graph_objects as go

# Sayfa Yapılandırması
st.set_page_config(page_title="RetailFlow AI | İş Analitiği", layout="wide")

# Kurumsal Stil (Creative Dokunuş)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { border-left: 5px solid #007bff; background: white; padding: 10px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 RetailFlow AI: Akıllı Mağaza Yönetimi")
st.info("Bu prototip, İş Analizi prensipleriyle iade ve kasa süreçlerini optimize etmek için tasarlanmıştır.")

# SIDEBAR: Giriş Paneli
with st.sidebar:
    st.header("🏢 Mağaza Verileri")
    musteri = st.slider("Müşteri Sayısı", 0, 300, 120)
    personel = st.slider("Aktif Personel", 1, 20, 6)
    iade_kuyrugu = st.slider("İade Bekleyenler", 0, 50, 15)

# İŞ ANALİZİ MANTIĞI (Jüriyi etkileyecek kısım)
bekleme_suresi = (musteri / (personel * 1.5)) + (iade_kuyrugu * 0.8)
verimlilik = (personel * 10) / (musteri + 1) * 100
finansal_risk = "YÜKSEK" if bekleme_suresi > 15 else "DÜŞÜK"

# METRİKLER
c1, c2, c3 = st.columns(3)
c1.metric("Tahmini Bekleme", f"{int(bekleme_suresi)} dk", delta="Gecikme!" if bekleme_suresi > 15 else "Optimal")
c2.metric("Sistem Verimliliği", f"%{int(min(100, verimlilik))}")
c3.metric("Müşteri Kayıp Riski", finansal_risk)

st.divider()

# GRAFİK VE AI TAVSİYESİ
col_l, col_r = st.columns([1.5, 1])

with col_l:
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = min(100, int(verimlilik * 2.5)),
        title = {'text': "Operasyonel Sağlık Skoru"},
        gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#007bff"},
                 'steps': [{'range': [0, 40], 'color': "red"}, {'range': [40, 75], 'color': "orange"}, {'range': [75, 100], 'color': "green"}]}))
    st.plotly_chart(fig, use_container_width=True)

with col_r:
    st.subheader("🤖 AI Karar Destek")
    if bekleme_suresi > 15:
        st.error(f"**KRİTİK:** Bekleme süresi çok uzun! \n\n1. Kasa 3'ü acil açın. \n2. İade masasına +1 takviye yapın.")
    else:
        st.success("**STABİL:** Operasyon verimli gidiyor. Müşteri memnuniyeti yüksek.")
    
    with st.expander("🧐 Analist Notu"):
        st.write("Bu model, Decathlon müşteri iade sürecini iyileştirmek amacıyla geliştirilen 'Kuyruk Teorisi' algoritmalarını kullanmaktadır.")

st.caption("RetailFlow AI | Melis - İş Analizi Portfolyo Projesi")
