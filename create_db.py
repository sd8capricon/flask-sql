import sqlite3

conn = sqlite3.connect('database.db')  # database location

try:
    # Create a table with cols id(pk, autoinc), name, review
    conn.execute(
        """create table reviews ();"""
    )
    conn.commit()
    print("Create Table reviews")
except Exception as e:
    print(e)
