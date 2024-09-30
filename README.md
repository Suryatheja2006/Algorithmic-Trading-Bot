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
     yfinance
     matplotlib
     numpy
   
