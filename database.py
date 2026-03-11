import sqlite3

conn = sqlite3.connect("users.db",check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
user_id INTEGER PRIMARY KEY,
bots_today INTEGER DEFAULT 0,
images_today INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS files(
name TEXT,
file_id TEXT,
description TEXT
)
""")

conn.commit()

def add_user(user_id):

    cursor.execute("SELECT * FROM users WHERE user_id=?",(user_id,))
    data = cursor.fetchone()

    if not data:
        cursor.execute(
        "INSERT INTO users(user_id) VALUES(?)",
        (user_id,)
        )
        conn.commit()