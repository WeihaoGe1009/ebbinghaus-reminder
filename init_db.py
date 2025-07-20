import sqlite3

conn = sqlite3.connect("review_items.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS memory_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    created_at DATE NOT NULL,
    category TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS review_schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id INTEGER NOT NULL,
    review_date DATE NOT NULL,
    FOREIGN KEY (item_id) REFERENCES memory_items(id)
)
""")

conn.commit()
conn.close()
print("database initialized")

