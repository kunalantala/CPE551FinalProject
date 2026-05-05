# Stock Portfolio Tracker

## Team Members
| Name                | Email                 | Stevens ID |
|---------------------|-----------------------|------------|
| Alexander Bonifacio | abonifac1@stevens.edu | 20023912   |
| Kunal Antala        | kantala@stevens.edu   | 20023640   |

---

## Project Description

### Overview
Managing a stock portfolio is overwhelming without a structured system. Spreadsheets are error-prone, professional tools are expensive, and manually tracking prices is tedious. This project is a Python-based portfolio tracker that lets users add and remove stocks, fetch real-time price data from Yahoo Finance, calculate gain/loss, visualize holdings with bar charts, and save everything to CSV for future sessions.

### Dependencies and Libraries
Install all required libraries before running:
```
pip install yfinance pandas matplotlib pytest
```

| Library | Purpose |
|---------|---------|
| yfinance | Fetches live stock prices from Yahoo Finance |
| pandas | Reads and writes portfolio data as CSV files |
| matplotlib | Plots bar charts of current stock values |
| pytest | Runs test cases to validate program logic |

### File and Module Structure
```
CPE551FinalProject/
├── main.ipynb          # Main Jupyter Notebook — runs the full portfolio workflow
├── stock.py            # Defines the Stock class
├── portfolio.py        # Defines the Portfolio class (composition with Stock)
├── data_handler.py     # Handles yfinance fetching, CSV save/load, and price generator
├── report.py           # Prints portfolio summary and plots bar chart
├── test_project.py     # Pytest test cases for total_value and gain_loss
└── README.md           # Project documentation
```

---

- Wrote Pytest test cases for `total_value()` and `gain_loss()` using NVDA and AMD

**Kunal Antala**
- Set up and managed the GitHub repository
- Implemented `main.ipynb` connecting all modules with the full portfolio workflow
- Wrote project documentation and README
