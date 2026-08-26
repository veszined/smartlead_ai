# Smart Coffee & Roastery - AI Lead Generator

Bu proje, 'Smart Coffee & Roastery' adlı 3. nesil butik bir kafe için geliştirilmiş, doğal dil işleme (NLP) yeteneğine sahip bir yapay zeka asistanıdır. 

Sistem, müşterilerle doğal bir Türkçe ile sohbet eder, menü ve çalışma saatleri hakkında bilgi verir. 
En temel amacı; tadım etkinlikleri veya toptan satışlar için müşterilerden isim ve telefon numarası (Lead) toplayarak işletmenin veritabanına kaydetmektir.

## Kullanılan Teknolojiler
* **Frontend:** Wix Velo (JavaScript)
* **Backend:** Python, Flask, Flask-CORS
* **Veritabanı:** SQLite
* **Yapay Zeka:** Groq API (Model: openai/gpt-oss-120b)
* **Sunucu:** Render

## Canlı Önizleme
* **Wix Web Sitesi:** https://sevvalldeniz.wixsite.com/smartcoffeeroastery
* **API Endpoint:** https://smartlead-ves.onrender.com

## Kurulum ve Çalıştırma
Projeyi kendi bilgisayarınızda çalıştırmak için:

1. Repoyu klonlayın: 
git clone https://github.com/veszined/smartlead_ai.git

2. Gerekli kütüphaneleri yükleyin: 
pip install -r requirements.txt

3. Ana dizinde bir .env dosyası oluşturun ve gizli API anahtarlarınızı ekleyin:
GROQ_API_KEY=sizinGroqApiAnahtariniz
SECRET_KEY=gizliAnahtariniz

4. Uygulamayı başlatın: 
python run.py

5. Sistem http://localhost:5000 adresinde çalışmaya başlayacaktır.
