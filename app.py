import streamlit as st
import plotly.graph_objects as go
import numpy as np

# 1. PAGE CONFIG
st.set_page_config(page_title="RetailFlow AI", layout="wide")

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
}

[data-testid="stMetricValue"] {
    color: #000 !important;
    font-size: 32px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricLabel"] {
    color: #000 !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

# 3. HEADER
st.title("🔵 RetailFlow AI: Operational Dashboard")
st.markdown("Queue Theory + AI Decision Engine")

# 4. SIDEBAR
with st.sidebar:
    st.header("Mağaza Verileri")

    sim_mode = st.toggle("📡 Simülasyon", True)

    if sim_mode:
        musteri = int(np.random.normal(150, 25))
        iade_kuyrugu = int(np.random.normal(30, 8))
    else:
        musteri = st.slider("Müşteri", 0, 400, 150)
        iade_kuyrugu = st.slider("İade Kuyruğu", 0, 100, 30)

    personel = st.slider("Personel", 1, 30, 10)

# 5. QUEUE THEORY (STABLE VERSION)
arrival_rate = max((musteri + iade_kuyrugu) / 60, 0.1)  # λ
service_rate = max(personel * 1.8, 0.1)                 # μ

epsilon = 0.1
diff = service_rate - arrival_rate

if diff <= 0:
    bekleme_suresi = 60  # sistem overload (max cap)
    system_status = "overload"
else:
    bekleme_suresi = (1 / max(diff, epsilon)) * 10
    bekleme_suresi = min(bekleme_suresi, 60)
    system_status = "stable"

# 6. KPI
utilization = min(arrival_rate / service_rate, 1)
throughput = min(arrival_rate, service_rate)
verimlilik = int((1 - utilization) * 100)

# AI Risk Score (normalized)
risk_score = (bekleme_suresi * 0.5) + ((1 - utilization) * 50)

# 7. METRICS
c1, c2, c3, c4 = st.columns(4)

c1.metric("Bekleme Süresi", f"{int(bekleme_suresi)} dk")
c2.metric("Verimlilik", f"%{verimlilik}")
c3.metric("Utilization", f"%{int(utilization*100)}")
c4.metric("Throughput", f"{round(throughput,2)} /dk")

st.markdown("---")

# 8. GAUGE
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=verimlilik,
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "#0082C3"},
        'steps': [
            {'range': [0, 40], 'color': "#fee2e2"},
            {'range': [40, 75], 'color': "#fef3c7"},
            {'range': [75, 100], 'color': "#dcfce7"}],
    },
    title={'text': "Efficiency Index"}
))
fig.update_layout(height=350)
st.plotly_chart(fig, use_container_width=True)

# 9. AI DECISION ENGINE
st.subheader("🤖 AI Karar Merkezi")

if system_status == "overload" or risk_score > 70:
    st.error("🚨 Kritik yoğunluk!")
    st.write("👉 2 personeli iade hattına kaydır")
    st.write("👉 Fast-track sürecini başlat")

elif risk_score > 40:
    st.warning("⚠️ Yoğunluk artıyor")
    st.write("👉 Personel dağılımını optimize et")

else:
    st.success("✅ Sistem stabil")

# 10. TREND
st.markdown("---")
st.subheader("📈 Bekleme Süresi Trend")

trend = np.random.normal(bekleme_suresi, 2, 30)
trend = [max(0, min(x, 60)) for x in trend]

st.line_chart(trend)

# 11. FOOTER
st.markdown("---")
st.caption(f"RetailFlow x Decathlon | {kategori} Analizi | Melisa Kabuk | UpSchool Future Talent")
