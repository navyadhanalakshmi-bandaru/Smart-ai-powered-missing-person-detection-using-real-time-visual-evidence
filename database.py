import sqlite3

def init_database():
    conn = sqlite3.connect('missing_persons.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS missing_persons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        last_seen_location TEXT,
        contact_number TEXT,
        description TEXT,
        image_path TEXT,
        face_encoding BLOB,
        status TEXT DEFAULT 'Missing'
    )''')

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

def get_connection():
    return sqlite3.connect('missing_persons.db')

if __name__ == "__main__":
    init_database()
