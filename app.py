from flask import Flask
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database_praktikum.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS mahasiswa (id INTEGER PRIMARY KEY, nama TEXT, nim TEXT)')
    cursor.execute('INSERT OR IGNORE INTO mahasiswa (id, nama, nim) VALUES (1, "Dwiky Rahman", "102062400146")')
    conn.commit()
    conn.close()

@app.route('/')
def hello():
    conn = sqlite3.connect('database_praktikum.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM mahasiswa')
    data = cursor.fetchone()
    conn.close()
    
    return f"Halo dari Flask + Docker + Jenkins! Data Database: {data}"

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)