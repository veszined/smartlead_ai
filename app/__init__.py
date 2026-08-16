from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from app.database import init_db

def create_app():
    app = Flask(__name__)
    app.json.ensure_ascii = False
    app.config.from_object(Config)
    
    CORS(app)
    
    init_db(app)
    
    from app.routes import pages_bp, api_bp
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    @app.route('/health')
    def health():
        return jsonify({"durum": "aktif", "mesaj": "Sistem çalışıyor!"}), 200
        
    return app