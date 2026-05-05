"""
Names: Alexander Bonifacio, Kunal Antala
Emails: abonifac1@stevens.edu, kantala@stevens.edu
Date: 5/6/2026
Description: Provides two functions for reporting stock portfolio data. report_gen prints a text summary
of all holdings, and portfolio_plot plots a bar chart of current stock values using Matplotlib.
"""

import matplotlib.pyplot as plt

def report_gen(portfolio):
    """Prints a full summary of the portfolio including each stock's details and overall totals."""
    if len(portfolio) == 0: # Checks if the portfolio is empty before trying to print anything
        print("Portfolio is empty.")
        return
    print(f"\n{portfolio.get_name()} Report")
    for s in portfolio.get_stocks(): # Goes through each Stock and prints it using its defined __str__
        print(s)
        print()
    print(f"Total Value: ${portfolio.total_value():.2f}")
    print(f"Total Gain/Loss: ${portfolio.total_gain_loss():.2f}")

def portfolio_plot(portfolio):
    """Plots a bar chart showing the current value of each stock in the portfolio."""
    symbols = list(portfolio.get_symbols())
    values = [s.get_current_price() * s.get_shares() for s in portfolio.get_stocks()] # Calculates current value for each stock
    paired = list(zip(symbols, values)) # Pairs each ticker with its total value
    labels = [p[0] for p in paired] # Pulls just the symbol from each pair
    amounts = [p[1] for p in paired] # Pulls just the value from each pair
    plt.figure(figsize=(10, 5))
    plt.bar(labels, amounts, color="steelblue")
    plt.title(f"{portfolio.get_name()} Stock Values")
    plt.xlabel("Symbol")
    plt.ylabel("Value ($)")
    plt.tight_layout()
    plt.savefig("portfolio_chart.png") # Saves the chart as a png file
    plt.show()