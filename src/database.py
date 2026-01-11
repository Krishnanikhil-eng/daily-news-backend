import sqlite3
import os

DB_PATH = "data/news.db"

def init_db():
    pass
    
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/news.db")

    """
    Create database and table if not exists.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        link TEXT,
        summary TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_news(title, link, summary):
    """
    Save one news record into database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO news (title, link, summary) VALUES (?, ?, ?)",
        (title, link, summary)
    )

    conn.commit()
    conn.close()


def get_all_news():
    """
    Read all news from database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT title, link, summary FROM news")
    rows = cursor.fetchall()

    conn.close()
    return rows
