import streamlit as st
import plotly.graph_objects as go
import random
import time

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(page_title="RetailFlow Pro | AI & Analytics", layout="wide")

# 2. CSS - TAM SİYAH OKUNABİLİR METİNLER VE SİMETRİ
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    div[data-testid="stMetric"] {
        background-color: white !important; padding: 25px !important;
        border-radius: 12px !important; box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        border-top: 6px solid #0082C3 !important; min-height: 160px !important;
        display: flex; flex-direction: column; justify-content: center;
    }
    [data-testid="stMetricValue"] { color: #000000 !important; font-size: 30px !important; font-weight: 800 !important; }
    [data-testid="stMetricLabel"] { color: #000000 !important; font-size: 16px !important; font-weight: 700 !important; }
    h1, h2, h3, p { color: #000000 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST BAŞLIK
st.title("🔵 RetailFlow AI: Decathlon Operasyonel Karar Destek Sistemi")
st.info("Bu sistem, RFID verilerini ve Kuyruk Teorisi algoritmalarını kullanarak mağaza verimliliğini AI ile optimize eder.")

# 4. SIDEBAR - CANLI VERİ GİRİŞİ
with st.sidebar:
    st.header("🏬 Mağaza Canlı Verileri")
    st.markdown("---")
    kategori = st.selectbox("Odak Spor Kategorisi", ["Outdoor & Kamp", "Fitness & Yoga", "Su Sporları", "Takım Sporları"])
    
    # Simülasyon için session state (Dinamik özellik 1)
    if 'musteri_sim' not in st.session_state: st.session_state.musteri_sim = 150
    musteri = st.slider("Anlık Müşteri Sayısı", 0, 400, st.session_state.musteri_sim)
    personel = st.slider("Aktif Takım Arkadaşı", 1, 30, 10)
    iade_kuyrugu = st.slider("Bekleyen İade/Değişim", 0, 100, 25)
    
    st.markdown("---")
    if st.button("🚀 Canlı Trafiği Simüle Et"):
        st.session_state.musteri_sim = random.randint(50, 350)
        st.toast("Mağaza sensör verileri güncelleniyor...", icon='📈')
        time.sleep(0.5)
        st.rerun()

# 5. BUSINESS LOGIC (AI ALGORİTMASI)
katsayi = 2.2 if kategori == "Outdoor & Kamp" else 1.3
bekleme_suresi = (iade_kuyrugu * katsayi) / (personel * 0.5)
verimlilik = min(100, int((personel * 18) / (musteri + iade_kuyrugu + 1) * 100))

# 6. ÜST METRİKLER
m1, m2, m3, m4 = st.columns(4)
m1.metric("Tahmini İade Süresi", f"{int(bekleme_suresi)} dk")
m2.metric("Sistem Sağlığı", f"%{verimlilik}")
m3.metric("Kategori Yoğunluğu", kategori)
m4.metric("Beklenen Müşteri Yükü", f"{round(musteri/personel, 1)} Müş/Per")

st.divider()

# 7. ANALİZ VE AI STRATEJİ MERKEZİ
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.markdown("<h3 style='text-align: center;'>📈 Mağaza Verimlilik Endeksi</h3>", unsafe_allow_html=True)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number", value = verimlilik,
        gauge = {'axis': {'range': [None, 100], 'tickcolor': "black"},
                 'bar': {'color': "#0082C3"},
                 'steps': [{'range': [0, 40], 'color': "#fee2e2"}, 
                           {'range': [40, 75], 'color': "#fef3c7"},
                           {'range': [75, 100], 'color': "#dcfce7"}]}))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=380)
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("🤖 AI Strateji Merkezi (Dinamik Analiz)")
    
    # Burası artık sadece statik değil, veriye göre cümle kuran bir "Analitik Zeka" gibi davranıyor.
    if verimlilik < 45:
        st.error(f"**KRİTİK DURUM TESPİTİ:** {kategori} iadeleri operasyonu yavaşlatıyor.")
        ai_output = f"""
        1. **Acil Kaynak:** Welcome Desk'ten 2 kişiyi iadeye kaydırın.
        2. **Darboğaz:** Müşteri/Personel oranı ({round(musteri/personel, 1)}) hedef değerin üzerinde.
        3. **Aksiyon:** Fast-Track RFID kanalını sadece {kategori} için önceliklendirin.
        """
    else:
        st.success(f"**OPTİMAL DURUM:** {kategori} kategorisinde süreçler verimli.")
        ai_output = """
        1. **Müşteri Deneyimi:** Bekleme süresi ideal. NPS anketlerini başlatın.
        2. **Verimlilik:** Mevcut personel dağılımı talebi karşılıyor.
        3. **Öneri:** Takım arkadaşları için 15 dk mikro-mola planlayabilirsiniz.
        """
    st.write(ai_output)

    # 8. RAPOR ÇIKTISI (Dinamik özellik 2)
    st.markdown("---")
    report = f"RETAILFLOW ANALİZ RAPORU\nKategori: {kategori}\nVerimlilik: %{verimlilik}\nBekleme: {int(bekleme_suresi)} dk\nÖneriler: {ai_output}"
    st.download_button(label="📄 Operasyon Raporunu İndir (TXT)", data=report, file_name="retailflow_rapor.txt")

# 9. ALT BİLGİ
st.caption("RetailFlow x Decathlon Pro | Melisa | UpSchool AI Future Talent Program")
