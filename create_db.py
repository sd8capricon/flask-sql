import sqlite3

conn = sqlite3.connect('database.db')

# Create a table

try:
    conn.execute(
        """create table reviews (
            id integer primary key autoincrement,
            name varchar(50) not null,
            review varchar(200) not null
            );"""
    )
    conn.commit()

    print("Created Table reviews")

except Exception as e:
    print(e)
