import sqlite3
from pathlib import Path

DB_PATH = Path("../database/airdrop.db")

def connect():
    return sqlite3.connect(DB_PATH)

def init():
    db = connect()
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            telegram_id INTEGER PRIMARY KEY,
            wallet TEXT
        );
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS claims (
            telegram_id INTEGER,
            timestamp INTEGER,
            tx_hash TEXT
        );
    """)
    db.commit()
    db.close()

def get_user(telegram_id):
    db = connect()
    cur = db.execute("SELECT wallet FROM users WHERE telegram_id=?", (telegram_id,))
    row = cur.fetchone()
    db.close()
    if row:
        return {"wallet": row[0]}
    return None

def save_user(telegram_id, wallet):
    db = connect()
    db.execute("INSERT INTO users (telegram_id, wallet) VALUES (?,?)", (telegram_id, wallet))
    db.commit()
    db.close()

def can_claim(telegram_id):
    # simple placeholder logic — real logic comes later
    return True

def record_claim(telegram_id, tx_hash):
    db = connect()
    db.execute(
        "INSERT INTO claims (telegram_id, timestamp, tx_hash) VALUES (?,?,?)",
        (telegram_id, 0, tx_hash)
    )
    db.commit()
    db.close()
