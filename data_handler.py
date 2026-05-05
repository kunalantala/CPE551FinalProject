"""
Names: Alexander Bonifacio, Kunal Antala
Emails: abonifac1@stevens.edu, kantala@stevens.edu
Date: 5/6/2026
Description: Handles all data operations for the portfolio tracker, including fetching live prices
from yfinance, saving and loading portfolio data as a CSV using Pandas, and a generator for streaming prices.
"""

import yfinance as yf
import pandas as pd
import time
from stock import Stock

def fetch_data(portfolio):
    """Fetches the latest market price for each stock in the portfolio and updates it."""
    symbols = list(portfolio.get_symbols()) # Converts the tuple to a list so it can be looped through
    prices = {} # Stores fetched prices before applying them to each Stock
    for symbol in symbols:
        try:
            ticker = yf.Ticker(symbol)
            prices[symbol] = ticker.fast_info.last_price # Pulls the most recent traded price
        except Exception as e:
            print(f"Error fetching {symbol}: {e}") # Catches invalid tickers so the program doesn't crash
            prices[symbol] = 0.0 # Falls back to 0.0 if the fetch didn't work
    for s in portfolio.get_stocks():
        s.set_current_price(prices.get(s.get_symbol(), 0.0)) # Applies the fetched price to each Stock
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S") # Records when the prices were pulled
    print(f"Prices updated at {timestamp}")

def save_portfolio(portfolio, filename="portfolio.csv"):
    """Saves the current holdings to a CSV file using Pandas."""
    data = {
        "symbol": [s.get_symbol() for s in portfolio.get_stocks()],
        "shares": [s.get_shares() for s in portfolio.get_stocks()],
        "purchase_price": [s.get_purchase_price() for s in portfolio.get_stocks()]
    }
    df = pd.DataFrame(data) # Converts the dict into a DataFrame
    df.to_csv(filename, index=False) # Writes to CSV, index=False stops pandas from adding a row number column
    print(f"Portfolio saved to {filename}")

def load_portfolio(portfolio, filename="portfolio.csv"):
    """Loads stock data from a CSV file and adds each row back into the portfolio."""
    try:
        df = pd.read_csv(filename) # Reads the saved CSV back into a DataFrame
        for _, row in df.iterrows(): # Goes row by row, _ means the row index isn't needed
            portfolio.add_stock(Stock(row["symbol"], row["shares"], row["purchase_price"])) # Reconstructs each Stock from the saved data
        print(f"Portfolio loaded from {filename}")
    except FileNotFoundError:
        print(f"Error: {filename} not found") # Handles the case where no saved file exists yet

def price_gen(portfolio):
    """Generator that provides each stock's symbol and current price one at a time."""
    for s in portfolio.get_stocks():
        yield s.get_symbol(), s.get_current_price() # Pauses and gives back one stock at a time