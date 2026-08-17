from flask import Blueprint, request, jsonify
from app.services.aiService import ai_service, AIServiceError
from app.database import leadEkle, tumLeadler

pages_bp = Blueprint('pages', __name__)
api_bp = Blueprint('api', __name__)

@pages_bp.route('/')
def index():
    return "Karşılama Sayfası API'ı çalışıyor"

@pages_bp.route('/dashboard')
def dashboard():
    return "Yönetim Paneli API'ı çalışıyor"

@api_bp.route('/sohbet', methods=['POST'])
def sohbet():
    veri = request.get_json()
    if not veri or 'mesaj' not in veri:
        return jsonify({"basari": False, "hata": "Eksik veri"}), 400
    
    try:
        cevap = ai_service.yanitUret(veri['mesaj'], veri.get('gecmisMesajlar', []))
        return jsonify({"basari": True, "cevap": cevap}), 200
    except Exception as e:
        print(f"GERÇEK HATA: {str(e)}")
        return jsonify({"basari": False, "hata": f"Gerçek Hata: {str(e)}"}), 503

@api_bp.route('/leads', methods=['POST'])
def yeniLead():
    veri = request.get_json()
    if not veri or 'isim' not in veri or 'iletisim' not in veri:
        return jsonify({"basari": False, "hata": "Eksik veri"}), 400
    
    try:
        leadEkle(veri['isim'], veri['iletisim'], veri.get('mesaj', ''))
        return jsonify({"basari": True, "mesaj": "Kaydedildi"}), 201
    except Exception:
        return jsonify({"basari": False, "hata": "Veritabanı hatası"}), 500

@api_bp.route('/leads', methods=['GET'])
def leadsListele():
    try:
        leadler = tumLeadler()
        return jsonify({"basari": True, "data": leadler}), 200
    except Exception:
        return jsonify({"basari": False, "hata": "Veritabanı hatası"}), 500
