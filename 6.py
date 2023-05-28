import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the cryptocurrency ticker to compare
crypto_ticker = 'BNB-USD'

# Fetch historical data for the cryptocurrency
crypto_data = yf.download(crypto_ticker, start='2020-01-01', end='2023-05-27')['Adj Close']

# Calculate the cumulative returns for the cryptocurrency
crypto_cumulative_returns = crypto_data / crypto_data.iloc[0]

# Plot the cumulative returns for the cryptocurrency
plt.figure(figsize=(12, 6))
plt.plot(crypto_cumulative_returns.index, crypto_cumulative_returns, label=crypto_ticker)

plt.title('Cryptocurrency Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.show()

# Calculate the total return for the cryptocurrency
crypto_total_return = crypto_cumulative_returns.iloc[-1] - 1

# Print the total return for the cryptocurrency
print(f"The total return for {crypto_ticker} is {crypto_total_return:.2%}")
