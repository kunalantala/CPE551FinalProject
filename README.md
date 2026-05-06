# Stock Portfolio Tracker

## Team Members
* Kunal Antala | kantala@stevens.edu | 20023640
* Alexander Bonifacio | abonifac1@stevens.edu | 20023912

## Project Description

### Overview
Managing a stock portfolio is overwhelming without a structured system. Spreadsheets are error-prone, professional tools are expensive, and manually tracking prices is tedious. This project is a Python-based portfolio tracker that lets users add and remove stocks, fetch real-time price data from Yahoo Finance, calculate gain/loss, visualize holdings with bar charts, and save everything to CSV for future sessions.

### Dependencies and Libraries
Install all required libraries before running:
`pip install yfinance pandas matplotlib pytest`

* yfinance: Fetches live stock prices from Yahoo Finance
* pandas: Reads and writes portfolio data as CSV files
* matplotlib: Plots bar charts of current stock values
* pytest: Runs test cases to validate program logic

### File and Module Structure

* **`main.ipynb`** - Main Jupyter Notebook that runs the full portfolio workflow
* **`stock.py`** - Defines the `Stock` class
* **`portfolio.py`** - Defines the `Portfolio` class (composition with `Stock`)
* **`data_handler.py`** - Handles yfinance fetching, CSV save/load, and the price generator
* **`report.py`** - Prints the portfolio summary and plots the bar chart
* **`test_project.py`** - Pytest test cases for `total_value` and `gain_loss`
* **`README.md`** - Project documentation

---

## How to Run

### Requirements
* Python 3.12, 3.13, or 3.14
* Jupyter Notebook or VS Code with the Jupyter extension

### Steps
1. Clone the repository:
   git clone https://github.com/kunalantala/CPE551FinalProject.git
   cd CPE551FinalProject

2. Install dependencies:
   pip install yfinance pandas matplotlib pytest

3. Open `main.ipynb` in VS Code or Jupyter and run all cells top to bottom.

4. To run the Pytest test cases:
   pytest test_project.py

### Notes
* An internet connection is required for `fetch_data()` to pull live prices from Yahoo Finance
* The notebook saves a `portfolio.csv` file and a `portfolio_chart.png` to the project folder when run

---

## Main Contributions

**Alexander Bonifacio**
* Implemented the `Stock` class with private attributes, getters, and operator overloads (`__str__`, `__eq__`)
* Implemented the `Portfolio` class with composition structure, list comprehension, and total value tracking (`__str__`, `__len__`)
* Implemented `data_handler.py` with live price fetching via yfinance, CSV save/load using Pandas, and price generator
* Implemented `report.py` with portfolio summary printing and Matplotlib bar chart visualization
* Wrote Pytest test cases for `total_value()` and `gain_loss()` using NVDA and AMD

**Kunal Antala**
* Set up and managed the GitHub repository
* Implemented `main.ipynb` connecting all modules with the full portfolio workflow
* Wrote project documentation and README
