import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the list of cryptocurrency tickers to compare
tickers = ['BTC-USD', 'ETH-USD', 'USDT-USD', 'BNB-USD', 'ADA-USD']

# Fetch historical data for the cryptocurrencies
data = yf.download(tickers, start='2020-01-01', end='2023-05-27')['Adj Close']

# Calculate the cumulative returns for each cryptocurrency
cumulative_returns = data.apply(lambda x: x / x[0])

# Calculate the total returns for each cryptocurrency
total_returns = cumulative_returns.iloc[-1] - 1

# Find the cryptocurrency with the highest total return
best_cryptocurrency = total_returns.idxmax()

# Plot the cumulative returns for all cryptocurrencies
plt.figure(figsize=(12, 6))

for ticker in tickers:
    plt.plot(cumulative_returns.index, cumulative_returns[ticker], label=ticker)

plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.show()

# Print the best cryptocurrency and its total return
print(f"The best cryptocurrency to invest in is {best_cryptocurrency} with a total return of {total_returns[best_cryptocurrency]:.2%}")
