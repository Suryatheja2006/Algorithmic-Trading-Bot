import yfinance as yf
import pandas as pd
import numpy as np

# Define the stock and date range
stock_symbol = 'AAPL'  # Replace with your chosen stock
start_date = '2020-01-01'
end_date = '2023-01-01'

# Fetch historical data
data = yf.download(stock_symbol, start=start_date, end=end_date)
data.dropna(inplace=True)  # Remove any missing values
print(data)  # Display the first few rows

def moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

# Calculate moving averages
data['MA50'] = moving_average(data, 50)
data['MA200'] = moving_average(data, 200)

# Signal Generation
data['Signal'] = 0
data['Signal'][50:] = np.where(data['MA50'][50:] > data['MA200'][50:], 1, 0)  # Buy signal
data['Position'] = data['Signal'].diff()

# print(data)

def backtest_strategy(data):
    initial_capital = 10000  # Initial investment
    shares = 0
    cash = initial_capital

    portfolio_values=[]
    for index, row in data.iterrows():
        # print(index)
        if row['Position'] == 1:  # Buy signal
            shares = cash // row['Close']  # Buy as many shares as possible
            cash -= shares * row['Close']
        elif row['Position'] == -1:  # Sell signal
            cash += shares * row['Close']  # Sell all shares
            shares = 0
        portfolio_values.append(cash+shares*row['Close'])
        
    data['Portfolio']=portfolio_values
    total_value = cash + shares * data.iloc[-1]['Close']  # Final portfolio value
    return total_value

# Calculate final value
final_value = backtest_strategy(data)
print(f"Final portfolio value: ${final_value:.2f}")
def calculate_performance(data, initial_capital):
    returns = data['Portfolio'].pct_change()
    # print(returns)
    sharpe_ratio = (returns.mean() / returns.std()) * np.sqrt(252)  # Annualize Sharpe ratio
    # profit = (initial_capital + data['Position'].cumsum() * data['Close']).iloc[-1] - initial_capital
    return sharpe_ratio

initial_capital=10000
sharpe_ratio = calculate_performance(data, initial_capital)
profit=final_value-initial_capital
print(f"Profit: ${profit:.2f}, Sharpe Ratio: {sharpe_ratio:.2f}")

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['MA50'], label='50-Day MA', alpha=0.75)
plt.plot(data['MA200'], label='200-Day MA', alpha=0.75)
plt.plot(data['Signal']*25,label='Signal',alpha=0.75)
plt.title(f"{stock_symbol} Price and Moving Averages")
plt.legend()
plt.show()