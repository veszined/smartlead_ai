import sqlite3
from flask import g
from config import Config

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(Config.DATABASE_NAME)
        g.db.row_factory = sqlite3.Row 
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                iletisim TEXT NOT NULL,
                mesaj TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()
    app.teardown_appcontext(close_db)

def leadEkle(isim, iletisim, mesaj=""):
    db = get_db()
    db.execute(
        'INSERT INTO leads (isim, iletisim, mesaj) VALUES (?, ?, ?)',
        (isim, iletisim, mesaj)
    )
    db.commit()

def tumLeadler():
    db = get_db()
    leadler = db.execute(
        'SELECT * FROM leads ORDER BY tarih DESC'
    ).fetchall()
    return [dict(row) for row in leadler]