"""
Names: Alexander Bonifacio, Kunal Antala
Emails: abonifac1@stevens.edu, kantala@stevens.edu
Date: 5/6/2026
Description: Defines a Portfolio class that holds a collection of Stock objects and tracks
total value and gain/loss across all positions. Demonstrates composition (Portfolio has-a Stock).
"""

from stock import Stock

class Portfolio:
    """
    Represents a named collection of Stock instances. Manages adding, removing,
    and summarizing all holdings. Composition: Portfolio has-a list of Stocks.
    """
    def __init__(self, name):
        self.__name = name  # Private, stores the portfolio name
        self.__stocks = []  # Private list that holds each Stock instance

    def get_name(self):
        """Returns the name of this portfolio."""
        return self.__name # __name is private so this is the only way to read it

    def get_stocks(self):
        """Returns the list of Stock instances in the portfolio."""
        return self.__stocks # __stocks is private so this is the only way to read it

    def add_stock(self, stock):
        """Adds a Stock instance to the portfolio."""
        self.__stocks.append(stock) # Appends to the end of the list

    def remove_stock(self, symbol):
        """Removes a stock by ticker symbol if it exists."""
        self.__stocks = [s for s in self.__stocks if s.get_symbol() != symbol.upper()] # Rebuilds the list without the matching symbol, .upper() keeps it case-insensitive

    def total_value(self):
        """Calculates the total current market value of all holdings."""
        total = 0
        for s in self.__stocks: # Goes through each Stock one by one
            total += s.get_current_price() * s.get_shares() # Multiplies price by shares to get its current value
        return total

    def total_gain_loss(self):
        """Sums the gain or loss across every stock in the portfolio."""
        total = 0
        for s in self.__stocks:
            total += s.gain_loss() # gain_loss() is defined in Stock, so this delegates the calculation there
        return total

    def get_symbols(self):
        """Returns a tuple of all ticker symbols currently in the portfolio."""
        return tuple(s.get_symbol() for s in self.__stocks) # Tuple keeps the result immutable

    def __len__(self):
        return len(self.__stocks) # Returns how many stocks are currently in the portfolio

    def __str__(self):
        return (f"portfolio: {self.__name}\n"
                f"stocks: {len(self.__stocks)}\n"
                f"total_value: {self.total_value():.2f}\n"
                f"total_gain_loss: {self.total_gain_loss():.2f}")


if __name__ == "__main__":
    p = Portfolio("Alex & Kunal Portfolio")
    s1 = Stock("NVDA", 5, 800.0)
    s1.set_current_price(900.0)
    p.add_stock(s1)
    print(p) 