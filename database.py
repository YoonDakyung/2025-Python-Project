import sqlite3
import os
from datetime import datetime

DB_NAME = "worries.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    if not os.path.exists(DB_NAME):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE worries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                emotion TEXT,
                content TEXT,
                empathy INTEGER DEFAULT 0,
                created_at TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                worry_id INTEGER,
                content TEXT,
                created_at TEXT,
                FOREIGN KEY(worry_id) REFERENCES worries(id)
            )
        ''')
        conn.commit()
        conn.close()