# 🔵 RetailFlow AI: Decathlon Operational Decision Support System

This project is a **Data-Driven Decision Support System (DSS)** prototype developed as part of the **UpSchool & YGA Future Talent Program**, aiming to enhance operational efficiency and customer experience at Decathlon.

---

## 🏟️ Why Decathlon? (Business Case & Analytics)
The system was designed considering Decathlon's unique operational dynamics and its leadership in retail technology:

* **RFID & Data Integration:** Decathlon is a global leader in utilizing RFID technology. This dashboard processes real-time data from RFID gate systems into actionable operational insights for store managers.
* **Product Complexity (Category-Based Analysis):** A return process for an "Outdoor & Camping" item (e.g., tent inspection) takes significantly longer than a "Fitness" item. My algorithm accounts for this **operational complexity** using category-specific coefficients.
* **Workshop & Technical Integration:** Returns of technical equipment (bikes, tents, etc.) require coordination with the **Workshop (Atölye)** team. This DSS simulates the need for technical staff shifting during peak return hours.
* **Bulky Goods Management:** The system predicts potential storage bottlenecks for large-scale equipment returns, suggesting pre-emptive space allocation in the **Bulky Goods Area**.

---

## 🚀 Technical Features
* **Dynamic AI Analysis Engine:** Analyzes real-time customer/staff balance to generate an **AI Risk Score (0-100)** for immediate action.
* **Queue Theory (M/M/1 Model):** Mathematically models waiting times and system throughput for optimal resource allocation.
* **Live Scenario Simulation:** Features an "Update AI Scenario" button to simulate various store traffic conditions (e.g., Weekend Rush or Seasonal Peaks).
* **Professional Reporting:** Generates downloadable operational reports in `.txt` format for management review.

---

## 🛠️ Tech Stack
* **Python:** Data processing and algorithmic logic.
* **Streamlit:** Interactive dashboard interface and cloud deployment.
* **Plotly:** Visualization of operational efficiency indices.
* **Markdown & CSS:** User-centric and professional UI design.

---

## 👩‍💻 Developer
**Melisa Kabuk**
*UpSchool AI & Data Science Future Talent Program Candidate*

---

# 🔵 RetailFlow AI: Decathlon Operasyonel Karar Destek Sistemi

Bu proje, perakende sektöründeki operasyonel verimliliği artırmayı hedefleyen veri odaklı bir **Karar Destek Sistemi (Decision Support System)** prototipidir.

---

## 🏟️ Neden Decathlon? (Sektörel Bağlam ve İş Analizi)
Proje, Decathlon'un operasyonel DNA'sı ve teknolojik liderliği temel alınarak tasarlanmıştır:

* **RFID ve Veri Entegrasyonu:** Decathlon'un dünyaca ünlü RFID altyapısından gelen anlık verileri işleyerek, mağaza müdürleri için anlamlı birer operasyonel aksiyona dönüştürür.
* **Ürün Kompleksitesi (Kategori Bazlı Analiz):** Bir "Outdoor & Kamp" iadesi (örn: çadır kontrolü) ile bir "Fitness" iadesi aynı sürede tamamlanmaz. Algoritmam, bu farklılıkları **kategori bazlı katsayılar** ile hesaba katar.
* **Workshop (Atölye) Koordinasyonu:** Teknik ekipman iadelerinde (bisiklet, kamp ekipmanı vb.) **Workshop** ekibinin onayı kritiktir. Sistem, yoğunluk anlarında teknik personelin iade masasına koordinasyonunu simüle eder.
* **Bulky Goods (Büyük Hacimli Ürün) Yönetimi:** Hacimli ürünlerin iadesinde oluşabilecek alan daralmasını öngörür ve depolama alanı optimizasyonu için stratejik uyarılar üretir.

---

## 🚀 Projenin Teknik Özellikleri
* **Dinamik AI Analiz Motoru:** Anlık müşteri/personel dengesini analiz ederek **0-100 arası bir AI Risk Skoru** üretir.
* **Kuyruk Teorisi:** Bekleme sürelerini ve sistem verimliliğini matematiksel modellerle hesaplar.
* **Canlı Senaryo Simülasyonu:** "AI Senaryosunu Güncelle" özelliği ile hafta sonu yoğunluğu veya kamp sezonu açılışı gibi farklı trafik durumlarını simüle eder.
* **Profesyonel Raporlama:** Analiz sonuçlarını tek tıkla `.txt` formatında indirerek üst yönetime sunulabilir operasyonel raporlar oluşturur.

---

## 🛠️ Kullanılan Teknolojiler
* **Python, Streamlit, Plotly, CSS**

---

## 👩‍💻 Geliştirici
**Melisa Kabuk**
*UpSchool AI & Data Science Future Talent Program Adayı*

---
> *This project was completed during an intensive 4-hour development sprint using Cursor AI and Streamlit.*
