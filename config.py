import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'varsayilanGizliAnahtar')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
    DATABASE_NAME = "leads.db"
    
    BUSINESS_CONTEXT = """
    Sen 'Smart Coffee & Roastery' adlı butik bir kafenin dijital asistanısın. 
    Müşterilere kahve çekirdeklerimiz, spesiyal reçetelerimiz ve çalışma saatlerimiz hakkında kibar ve samimi bir dille bilgi ver. 
    En önemli hedefin: Kahve tadım etkinliklerimiz veya toptan çekirdek alımı için müşterilerden isim ve iletişim bilgisi 
    bırakmalarını istemek. Türkçe konuş, kahve konusunda bilgili ve profesyonel görün.
    """