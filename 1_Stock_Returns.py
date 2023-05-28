import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the list of stock symbols to compare
stock_symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']

# Fetch historical data for the stocks
data = yf.download(stock_symbols, start='2020-01-01', end='2023-05-27')['Adj Close']

# Calculate the daily returns for each stock
returns = data.pct_change()

# Plot the returns
plt.figure(figsize=(12, 6))

for symbol in stock_symbols:
    plt.plot(returns.index, returns[symbol], label=symbol)

plt.title('Stock Returns')
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.legend()
plt.show()
