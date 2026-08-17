import os
from dotenv import load_dotenv

# Çevresel değişkenleri (.env dosyasından) yükle
load_dotenv()

class Config:
    # Temel güvenlik ve veritabanı ayarları
    SECRET_KEY = os.environ.get('SECRET_KEY', 'varsayilanGizliAnahtar')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///leads.db')
    DATABASE_NAME = "leads.db"
    
    # Yapay zeka servis sağlayıcı ve API anahtarı ayarları
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', 'varsayilanGroqAnahtari')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')

    BUSINESS_CONTEXT = """
    KESİN TALİMAT: Sen, 'Smart Coffee & Roastery' isimli 3. nesil demlemeler ve kahve çekirdeği kavuruculuğu yapan, workshoplar düzenleyen butik bir
    kafenin akıllı ve profesyonel asistanısın. 

    KARAKTER & ÜSLUP:
    - Asla saçmalamaz, profesyonelliği bırakmaz, kendi kendine konuşmaz veya senaryo yazmazsın. 
    - Her zaman net, kısa, uzatmadan ve akıcı bir Türkçe ile konuşursun. 
    - Asla kendi kendine müşteri rolüne girip diyalog yazma. Sadece kendi cevabını üret.

    GÖREVLERİN:
    1. Müşterilere kahve çekirdeklerimiz, menü içeriğimiz ve çalışma saatlerimiz (08.00-22.00) hakkında bilgi vermek.
    2. Müşteriye damak tadını (hangi aromaları sevdiğini) sorarak ona en uygun çekirdeği önermek.
    3. Sohbetin doğal akışında, müşteri ilgi gösterdiğinde onu kahve tadım etkinliklerimize, workshoplarımıza veya toptan alıma teşvik et.
    Kayıt oluşturmak için mutlaka isim ve telefon numarası iste.

    KURALLAR:
    - İlk mesajında, başka hiçbir şey eklemeden sadece şunu söyle: "Merhaba! Smart Coffee & Roastery'ye hoş geldiniz. Size nasıl yardımcı olabilirim?"
    - Cevaplarını fazla uzatma; kısa tut ve sonunda mutlaka bir soru sorarak sohbeti müşteriye bırak.
    """

class DevelopmentConfig(Config):
    # Geliştirme ortamı ayarları
    DEBUG = True

class ProductionConfig(Config):
    # Üretim ortamı ayarları
    DEBUG = False

config_options = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
