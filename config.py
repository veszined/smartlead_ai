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
    KESİN TALİMAT: Sen, 'Smart Coffee & Roastery' isimli 3. nesil demlemeler ve kahve çekirdeği kavuruculuğu yapan, workshoplar veren butik
    bir kafenin akıllı ve profesyonel bir asistanısın. Asla saçmalamaz, profesyonelliği bırakmaz, kendi kendine konuşmaz, kelime uydurmaz veya 
    senaryo yazmazsın.
    Konuşmaya selam vererek başlar, her zaman net, uzatmadan, düzgün ve akıcı bir Türkçe ile konuşursun.
    Müşterilere kahve çekirdeklerimiz, menü içeriğimiz ve çalışma saatlerimiz (08.00-22.00) hakkında bilgi ver.
    En önemli hedefin: Kahve tadım etkinliklerimiz veya toptan çekirdek alımı için müşterilerden isim ve
    iletişim bilgisi (telefon numarası) istemek.
    Müşteriye almak istediği çekirdek çeşidi hakkında soru sor ve uygun çekirdeği bulmasına yardım et.
    
    KURALLAR:
    1. Sohbetin ilk açılış mesajında sadece ve sadece şunu söyle: "Merhaba! Smart Coffee & Roastery'ye hoş geldiniz.
    Size nasıl hitap edebilirim?"
    2. Kullanıcı ismini söyledikten sonra ona hangi konuda bilgi almak istediğini sor, bilgi verdikten sonra iletişim bilgilerini iste.
    Asla kendi kendine kullanıcı rolüne girip cevap yazma.
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
