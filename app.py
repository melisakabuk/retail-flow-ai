import streamlit as st
import plotly.graph_objects as go
import numpy as np

# 1. PAGE CONFIG
st.set_page_config(page_title="RetailFlow x Decathlon | Business Analytics", layout="wide")

# 2. CSS
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }

    div[data-testid="stMetric"] {
        background-color: white !important;
        padding: 20px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        border-top: 6px solid #0082C3 !important;
        min-height: 160px !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-size: 32px !important;
        font-weight: 700 !important;
    }

    [data-testid="stMetricLabel"] {
        color: #000000 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    .stSlider label, .stSelectbox label, .stWidget label {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER
st.title("🔵 RetailFlow AI: Decathlon Operasyonel Karar Destek Sistemi")
st.markdown("**Advanced Business Analytics Dashboard | Queue Theory + AI Scoring**")
st.info("Bu sistem, mağaza içi iade süreçlerini Queue Theory ve AI destekli karar mekanizması ile optimize eder.")

# 4. SIDEBAR
with st.sidebar:
    st.header("🏬 Mağaza Canlı Verileri")

    kategori = st.selectbox("Odak Spor Kategorisi",
                            ["Outdoor & Kamp", "Fitness & Yoga", "Su Sporları", "Takım Sporları"])

    # Simülasyon opsiyonu
    sim_mode = st.toggle("📡 Canlı Veri Simülasyonu", value=False)

    if sim_mode:
        musteri = int(np.random.normal(150, 30))
        iade_kuyrugu = int(np.random.normal(30, 10))
    else:
        musteri = st.slider("Toplam Müşteri", 0, 400, 165)
        iade_kuyrugu = st.slider("Bekleyen İade", 0, 100, 35)

    personel = st.slider("Aktif Personel", 1, 30, 12)

    rfid_active = st.toggle("RFID Sistemi", value=True)

# 5. QUEUE THEORY (M/M/1)
arrival_rate = (musteri + iade_kuyrugu) / 60  # λ
service_rate = personel * 1.8  # μ (realistic service capacity)

if service_rate > arrival_rate:
    bekleme_suresi = 1 / (service_rate - arrival_rate)
else:
    bekleme_suresi = 999  # system overload

# 6. KPI CALCULATIONS
throughput = min(arrival_rate, service_rate)
utilization = min(1, arrival_rate / service_rate)
verimlilik = int((1 - utilization) * 100)

# AI Risk Score
risk_score = (bekleme_suresi * 0.6) + ((100 - verimlilik) * 0.4)

# 7. METRICS
m1, m2, m3, m4 = st.columns(4)

m1.metric("Tahmini Bekleme Süresi", f"{int(bekleme_suresi)} dk")
m2.metric("Verimlilik", f"%{verimlilik}")
m3.metric("Utilization", f"%{int(utilization*100)}")
m4.metric("Throughput", f"{round(throughput,2)} kişi/dk")

st.markdown("---")

# 8. GAUGE
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=verimlilik,
    gauge={
        'axis': {'range': [None, 100]},
        'bar': {'color': "#0082C3"},
        'steps': [
            {'range': [0, 40], 'color': "#fee2e2"},
            {'range': [40, 75], 'color': "#fef3c7"},
            {'range': [75, 100], 'color': "#dcfce7"}],
    },
    title={'text': "Operational Efficiency Index"}
))

fig.update_layout(height=400)
st.plotly_chart(fig, use_container_width=True)

# 9. AI DECISION ENGINE
st.subheader("🤖 AI Karar Motoru")

if risk_score > 70:
    st.error("🚨 KRİTİK DURUM: Sistem overload")
    st.write("👉 2 personeli iade hattına yönlendir")
    st.write("👉 RFID Fast Track aktif et")

elif 40 < risk_score <= 70:
    st.warning("⚠️ Yoğunluk artıyor")
    st.write("👉 Personel rotasyonunu optimize et")

else:
    st.success("✅ Sistem stabil çalışıyor")

# 10. TREND SIMULATION
st.markdown("---")
st.subheader("📈 Bekleme Süresi Trend (Simülasyon)")

trend = np.random.normal(bekleme_suresi, 2, 30)
st.line_chart(trend)

# 11. FOOTER
st.markdown("---")
st.caption("RetailFlow x Decathlon Case Study | Melisa Kabuk | UpSchool Future Talent Program")
