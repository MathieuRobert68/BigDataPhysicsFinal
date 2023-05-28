import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the list of cryptocurrency tickers to compare
tickers = ['BTC-USD', 'ETH-USD', 'USDT-USD', 'BNB-USD', 'ADA-USD']

# Fetch historical data for the cryptocurrencies
data = yf.download(tickers, start='2020-01-01', end='2023-05-27')['Adj Close']

# Calculate the daily returns for each cryptocurrency
returns = data.pct_change()

# Plot the returns
plt.figure(figsize=(12, 6))

for ticker in tickers:
    plt.plot(returns.index, returns[ticker], label=ticker)

plt.title('Cryptocurrency Returns')
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.legend()
plt.show()
