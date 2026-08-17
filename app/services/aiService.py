import requests
from config import Config

class AIServiceError(Exception):
    # Yapay zeka servislerinde oluşabilecek hataları yakalamak için özel hata sınıfı.
    pass

class AIService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "openai/gpt-oss-20b"

    def yanitUret(self, mesaj, gecmisMesajlar=None):
        # API anahtarının tanımlı olup olmadığını kontrol et
        if not self.api_key or "groqAnahtari" in self.api_key:
            return "Demo Modu: Yapay zeka şu an aktif değil. Lütfen .env dosyanıza Groq anahtarınızı ekleyin."
        
        if gecmisMesajlar is None:
            gecmisMesajlar = []

        # Sistem talimatını mesaj dizisinin en başına ekle
        messages = [{"role": "system", "content": Config.BUSINESS_CONTEXT}]
        
        # Sohbet geçmişini mesaja dahil et
        for msg in gecmisMesajlar:
            messages.append(msg)
            
        # Kullanıcının son gönderdiği mesajı ekle
        messages.append({"role": "user", "content": mesaj})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": messages
        }
        try:     
            # Groq API'a istek at
            response = requests.post(self.api_url, headers=headers, json=payload)   
            # Eğer cevap başarılı değilse Groq'un hata mesajını ekrana yaz
            if response.status_code != 200:
                raise Exception(response.text)                
            data = response.json()
            return data["choices"][0]["message"]["content"]
            
        except Exception as e:
            raise AIServiceError(f"Groq Detayı: {str(e)}")
        
ai_service = AIService()
