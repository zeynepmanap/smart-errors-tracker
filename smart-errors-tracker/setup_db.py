# setup_db.py
import sqlite3

conn = sqlite3.connect('errors.db')
cursor = conn.cursor()

# Eski tablo varsa sil
cursor.execute('DROP TABLE IF EXISTS errors')

# Yeni tabloyu oluştur
cursor.execute('''
CREATE TABLE errors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    error_message TEXT,
    source TEXT,
    stack_trace TEXT,
    user_id TEXT,
    possible_cause TEXT
)
''')

conn.commit()
conn.close()

print("Veritabanı ve tablo hazır!")
