"""
Names: Alexander Bonifacio, Kunal Antala
Emails: abonifac1@stevens.edu, kantala@stevens.edu
Date: 5/6/2026
Description: Defines a Stock class that stores a ticker symbol, number of shares, and purchase price,
and calculates gain or loss based on the current market price.
"""

class Stock:
    """
    Represents a single stock holding with a symbol, shares owned, and purchase price.
    Tracks the current price and computes gain or loss against what was originally paid.
    """
    def __init__(self, symbol, shares, purchase_price):
        self.__symbol = symbol.upper() # Stored uppercase so comparisons are consistent
        self.__shares = shares
        self.__purchase_price = purchase_price
        self.__current_price = 0.0 # Starts at 0 until live data is fetched

    def get_symbol(self):
        """Returns the ticker symbol for this stock."""
        return self.__symbol

    def get_shares(self):
        """Returns the number of shares held."""
        return self.__shares

    def get_purchase_price(self):
        """Returns the original purchase price per share."""
        return self.__purchase_price

    def get_current_price(self):
        """Returns the most recently fetched market price."""
        return self.__current_price

    def set_current_price(self, price):
        """Updates the current market price after a live data fetch."""
        self.__current_price = price

    def gain_loss(self):
        """Calculates total gain or loss based on current price vs what was paid."""
        return (self.__current_price - self.__purchase_price) * self.__shares # Difference in price multiplied by shares owned

    def __str__(self):
        return (f"symbol: {self.__symbol}\n"
                f"shares: {self.__shares}\n"
                f"purchase_price: {self.__purchase_price}\n"
                f"current_price: {self.__current_price}\n"
                f"gain/loss: {self.gain_loss():.2f}")

    def __eq__(self, other):
        return self.__symbol == other.get_symbol() # Two stocks are equal if they share the same ticker


if __name__ == "__main__":
    s = Stock("NVDA", 5, 800.0)
    s.set_current_price(900.0)
    print(s) 