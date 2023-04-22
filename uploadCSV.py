import sqlite3

conn = sqlite3.connect("historicData.db")
cur = conn.cursor()

sql="""
CREATE TABLE IF NOT EXISTS historical_data (
  slNo INTEGER PRIMARY KEY,
  date DATETIME NOT NULL,
  price REAL NOT NULL,
  instrument_name TEXT NOT NULL
)
"""


cur.execute(sql)
print("Database has been created")

conn.commit()
conn.close()