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

DATA = scraping.getData(stockCode, minute=False) # GET DATA
DATE_STOCKS = DATA["chart"]["result"][0]["timestamp"][-n_SMA:]
CLOSE_STOCKS = DATA["chart"]["result"][0]["indicators"]["quote"][0]["close"][-n_SMA:]

for i in range(len(CLOSE_STOCKS)):

  if ((CLOSE_STOCKS[i] == None) and (i != 0)):
    CLOSE_STOCKS[i] = CLOSE_STOCKS[i-1]

# Calculate Exponential Smoothing
forcastExp = CLOSE_STOCKS[0]
forcastSMA = sum(CLOSE_STOCKS)/len(CLOSE_STOCKS)

print("\nDATE\t\t\tCLOSE\t")
for i in range(len(CLOSE_STOCKS)):

  if ((CLOSE_STOCKS[i] == None) and (i != 0)):
    CLOSE_STOCKS[i] = CLOSE_STOCKS[i-1]

  #Expoonential Smoothing
  forcastExp = ALPHA * CLOSE_STOCKS[i] + (1 - ALPHA) * forcastExp

  # MSE, MAD & MAPE
  mseSum += abs(CLOSE_STOCKS[i] - forcastSMA)**2
  madSum += abs(CLOSE_STOCKS[i] - forcastSMA)
  mapeSum += abs(CLOSE_STOCKS[i] - forcastSMA) / CLOSE_STOCKS[i]

  print("{}\t{}".format(dt.datetime.fromtimestamp(
        DATE_STOCKS[i]).strftime("%d/%m/%Y - %H:%M"),CLOSE_STOCKS[i]))

MSE = mseSum/len(CLOSE_STOCKS)
MAD = madSum/len(CLOSE_STOCKS)
MAPE = 100 - (100 * mapeSum/len(CLOSE_STOCKS)) # IF MAPE RESULT > 90%, THEN THE FORCASTING IS BETTER.  

print("\nForcasting:\n{:.1f}\t(MA)\n{:.1f}\t(Exponential Smoothing)"
      "\n\nError Calculation:\nMAD\t{:.1f}\nMAPE\t{:.1f}%\nMSE\t{:.1f}"
      .format(forcastSMA, forcastExp, MAD, MAPE, MSE))
