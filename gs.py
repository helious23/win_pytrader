import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

gs = web.get_data_yahoo("078930.KS", start="2023-01-01", end="2024-03-15")

ma5 = gs["Adj Close"].rolling(window=5).mean()
ma20 = gs["Adj Close"].rolling(window=20).mean()
ma60 = gs["Adj Close"].rolling(window=60).mean()
ma120 = gs["Adj Close"].rolling(window=120).mean()

gs.insert(len(gs.columns), "MA5", ma5)
gs.insert(len(gs.columns), "MA20", ma20)
gs.insert(len(gs.columns), "MA60", ma60)
gs.insert(len(gs.columns), "MA120", ma120)

plt.plot(gs.index, gs["Adj Close"], label="Adj Close")
plt.plot(gs.index, gs["MA5"], label="MA5")
plt.plot(gs.index, gs["MA20"], label="MA20")
plt.plot(gs.index, gs["MA60"], label="MA60")
plt.plot(gs.index, gs["MA120"], label="MA120")

# 범례가 적절한 위치에 자동으로 출력 loc=best
plt.legend(loc="best")
# 격자 표시
plt.grid()
plt.show()
