# Algorithmic-Trading-Bot

## Overview
This is a simple algorithmic trading bot that trades based on a moving average crossover strategy. It buys or sells a stock when the 50-day moving average crosses the 200-day moving average, simulating a basic trend-following trading strategy.

The bot uses historical stock data from Yahoo Finance and performs backtesting on this data to analyze the strategy's performance.

## Features
- Fetches historical stock price data using Yahoo Finance API (`yfinance` library).
- Implements a moving average crossover strategy (50-day vs. 200-day).
- Backtests the strategy over a chosen period.
- Provides analysis metrics such as total returns and Sharpe ratio.
- Visualizes the trading signals on stock price data.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/trading-bot.git
   cd trading-bot
2. **Install Dependencies:**This project requires Python 3.7+ and the following dependencies:
     yfinance,
     matplotlib,
     numpy. Install them via:
   ```bash
   pip install yfinance
   pip install matplotlib
   pip install numpy
3. **Obtain Stock Data:** The bot uses Yahoo Finance to fetch stock data. No API key is required, but ensure you internet connection is active
## Usage 

1. **Run the Scrpt:** You can run the trading_bot.py to execute the algorithm
   ```bash
   python3 tradin_bot.py
2. **Parameters:** You can specify different stock symbols and date ranges within the script. By default, it fetches Apple stock (AAPL) data from 2020-01-01 to 2023-01-01. Modify the stock_symbol, start_date, and end_date variables in the script as per your needs.
3. **Output:** Trading signals: Buy and sell signals are plotted against the stock's closing price.
   Performance Metrics: Displays total returns and the Sharpe ratio in the console

## Project Structure
```bash
Algorithmic_Trading_Bot/
│
├── README.md             # Project description and instructions
├── trading_bot.py        # Main script with trading logic
└── images/               # Folder to store visualizations
    └── trading_signals.png  # Sample image of buy/sell signals

