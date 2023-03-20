import sqlite3

conn = sqlite3.connect('database.db')

# Create a table
conn.execute(
    """CREATE TABLE IF NOT EXISTS REVIEWS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        restaurant VARCHAR(50) NOT NULL,
        review TEXT NOT NULL
        );"""
)
conn.commit()
