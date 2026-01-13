import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


print("Downloading S&P 500 (^GSPC) data...")
sp500 = yf.download("^GSPC", start="2000-01-01", end="2025-01-01")
print(sp500.head(), "\n")


tickers = ["SPY", "VOO", "IVV"]
print("Downloading ETF data...")
etf_data = yf.download(tickers, period="5y")
print(etf_data.tail(), "\n")


print("Downloading list of S&P 500 companies...")
sp500_tickers = yf.Tickers(" ".join(tickers)).symbols 

sp500_list = yf.download("SPY", period="1d")  
sp500_table = yf.get_sp500_components()
sp500_df = pd.DataFrame(sp500_table)

print("First 10 companies:")
print(sp500_df.head(10), "\n")

plt.figure(figsize=(12,6))
plt.plot(sp500["Close"])
plt.title("S&P 500 (^GSPC) Close Price")
plt.xlabel("Year")
plt.ylabel("Price")
plt.grid(True)
plt.show()

sp500["Daily_Return"] = sp500["Close"].pct_change()
print("Daily returns:")
print(sp500["Daily_Return"].head())

