import csv
import sqlite3

conn = sqlite3.connect("historicData.db")
cursor = conn.cursor()

with open("historical_prices.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
        cursor.execute("INSERT INTO historical_data (slNo, date, price, instrument_name) VALUES (?, ?, ?, ?)", row)
        conn.commit()

conn.close()
