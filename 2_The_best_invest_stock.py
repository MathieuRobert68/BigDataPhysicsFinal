import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the list of stock symbols to compare
stock_symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']

# Fetch historical data for the stocks
data = yf.download(stock_symbols, start='2020-01-01', end='2023-05-27')['Adj Close']

# Calculate the cumulative returns for each stock
cumulative_returns = data.apply(lambda x: x / x[0])

# Calculate the total returns for each stock
total_returns = cumulative_returns.iloc[-1] - 1

# Find the stock with the highest total return
best_stock = total_returns.idxmax()

# Plot the cumulative returns for all stocks
plt.figure(figsize=(12, 6))

for symbol in stock_symbols:
    plt.plot(cumulative_returns.index, cumulative_returns[symbol], label=symbol)

plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.show()

# Print the best stock and its total return
print(f"The best stock to invest in is {best_stock} with a total return of {total_returns[best_stock]:.2%}")
