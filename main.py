from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/historical-data')
def get_historical_data(symbol: str = None, from_date: str = None, to_date: str = None):
    data = []
    with sqlite3.connect('./historicData.db') as conn:
        c = conn.cursor()
        if symbol and from_date and to_date:
            c.execute("SELECT date, price FROM historical_data WHERE instrument_name=? AND date BETWEEN ? AND ?", (symbol, from_date, to_date))
        else:
            c.execute("SELECT date, price FROM historical_data")
        rows = c.fetchall()
        for row in rows:
            data.append({'date': row[0], 'price': row[1]})
    return data