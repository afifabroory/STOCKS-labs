import scraping
import datetime as dt

source = "YAHOO"
smaSum = 0
mapeSum = 0
madSum = 0
mseSum = 0
exp_smth = 0
ALPHA = 0.1

# GET INPUT
n_SMA = int(input("Enter Input of n, SMA(n): "))
stockCode = str(input("Enter Stock Code: ")).upper()

# CREATE INSTANCE OBJECT
scraping = scraping.Scraping("STOCK_CHART", "YAHOO", stockCode)

DATA = scraping.getData() # GET DATA
DATE_STOCKS = DATA["chart"]["result"][0]["timestamp"][-n_SMA:]
CLOSE_STOCKS = DATA["chart"]["result"][0]["indicators"]["quote"][0]["close"][-n_SMA:]

# Calculate Exponential Smoothing
forcastExp = CLOSE_STOCKS[0]

for i in range(len(CLOSE_STOCKS)):

  # Simple Moving Average
  smaSum += CLOSE_STOCKS[i]

  #Expoonential Smoothing
  forcastExp = ALPHA * CLOSE_STOCKS[i] + (1 - ALPHA) * forcastExp

  # MSE, MAD & MAPE
  mseSum += abs(CLOSE_STOCKS[i] - forcastSMA)**2
  madSum += abs(CLOSE_STOCKS[i] - forcastSMA)
  mapeSum += abs(CLOSE_STOCKS[i] - forcastSMA) / CLOSE_STOCKS[i]

forcastSMA = smaSum/n_SMA
MSE = mseSum/n_SMA
MAD = madSum/n_SMA
MAPE = 100 - (100 * mapeSum/n_SMA) # IF MAPE RESULT > 90%, THEN THE FORCASTING IS BETTER.

print("\nDATE\t\tCLOSE")
for i in range(0, len(CLOSE_STOCKS)):
  print("{}\t{}".format(dt.datetime.fromtimestamp(
        DATE_STOCKS[i]).strftime("%d/%m/%Y"),CLOSE_STOCKS[i]))

print("\nForcasting:\n{:.1f}\t(MA)\n{:.1f}\t(Exponential Smoothing)"
      "\n\nError Calculation:\nMAD\t{:.1f}\nMAPE\t{:.1f}%\nMSE\t{:.1f}"
      .format(forcastSMA, forcastExp, MAD, MAPE, MSE))
