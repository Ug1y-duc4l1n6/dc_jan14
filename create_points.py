import sqlite3

conn = sqlite3.connect('points.db')

cursor = conn.cursor()

query = """

CREATE TABLE IF NOT EXISTS points(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    X REAL,
    Y REAL
);

"""

cursor.execute(query)
conn.commit()
conn.close()