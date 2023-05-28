import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the list of stock symbols to compare
stock_symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']

# Fetch historical data for the stocks
stock_data = yf.download(stock_symbols, start='2020-01-01', end='2023-05-27')['Adj Close']

# Calculate the cumulative returns for each stock
stock_cumulative_returns = stock_data.apply(lambda x: x / x[0])

# Calculate the total returns for each stock
stock_total_returns = stock_cumulative_returns.iloc[-1] - 1

# Find the stock with the highest total return
best_stock = stock_total_returns.idxmax()

# Plot the cumulative returns for stocks
plt.figure(figsize=(12, 6))
for symbol in stock_symbols:
    plt.plot(stock_cumulative_returns.index, stock_cumulative_returns[symbol], label=symbol)

plt.title('Stock Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.show()

# Print the best stock and its total return
print(f"The best stock to invest in is {best_stock} with a total return of {stock_total_returns[best_stock]:.2%}")

# Define the list of cryptocurrency tickers to compare
crypto_tickers = ['BTC-USD', 'ETH-USD', 'USDT-USD', 'BNB-USD', 'ADA-USD']

# Fetch historical data for the cryptocurrencies
crypto_data = yf.download(crypto_tickers, start='2020-01-01', end='2023-05-27')['Adj Close']

# Calculate the cumulative returns for each cryptocurrency
crypto_cumulative_returns = crypto_data.apply(lambda x: x / x[0])

# Calculate the total returns for each cryptocurrency
crypto_total_returns = crypto_cumulative_returns.iloc[-1] - 1

# Find the cryptocurrency with the highest total return
best_cryptocurrency = crypto_total_returns.idxmax()

# Plot the cumulative returns for cryptocurrencies
plt.figure(figsize=(12, 6))
for ticker in crypto_tickers:
    plt.plot(crypto_cumulative_returns.index, crypto_cumulative_returns[ticker], label=ticker)

plt.title('Cryptocurrency Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.show()

# Print the best cryptocurrency and its total return
print(f"The best cryptocurrency to invest in is {best_cryptocurrency} with a total return of {crypto_total_returns[best_cryptocurrency]:.2%}")
