import scraping
import numpy as np
import pandas as pd
import mplfinance as mpf
import datetime as dt

stock = input("Enter Stock Code: ")
n = int(input("How many days want to showed? "))

data = scraping.getData(stock, minute=False)

dateStock = data["chart"]["result"][0]["timestamp"][-n:]
closeStock = np.array(data["chart"]["result"][0]["indicators"]["quote"][0]["close"][-n:])
openStock = np.array(data["chart"]["result"][0]["indicators"]["quote"][0]["open"][-n:])
highStock = np.array(data["chart"]["result"][0]["indicators"]["quote"][0]["high"][-n:])
lowStock = np.array(data["chart"]["result"][0]["indicators"]["quote"][0]["low"][-n:])

haOpen = None
haClose = None
haHigh = None
haLow = None

for i in range(0, len(dateStock)):
    dateStock[i] = dt.datetime.fromtimestamp(dateStock[i]).strftime("%d/%m/%y")
    if (i == 0):
        haOpen = np.array(((openStock[i] + closeStock[i])/2))
        haClose = (openStock + closeStock + lowStock + highStock)/4

        max = max([highStock[i], haOpen, haClose[i]])
        min = min([lowStock[i], haOpen, haClose[i]])
        haHigh = np.array(max)
        haLow = np.array(min)
    else:
        if (i == 1):
            open = (haOpen + haClose[i])/2
        else:
            open = (haOpen[i-1] + haClose[i-1])/2

        high = np.amax([highStock[i], open, haClose[i]])
        low = np.amin([lowStock[i], open, haClose[i]])

        haHigh = np.append(haHigh, high)
        haLow = np.append(haLow, low)
        haOpen = np.append(haOpen, open)

d ={'Date': dateStock, 'Open': haOpen, 'Close': haClose,'High': haHigh, 'Low': haLow}
#d ={'Date': dateStock, 'Open': openStock, 'Close': closeStock,'High': highStock, 'Low': lowStock}
df = pd.DataFrame.from_dict(d)
df = df.set_index(['Date'])
df.index = pd.to_datetime(df.index, format='%d/%m/%y')
print(df)
mpf.plot(df,type='candle', style='yahoo', figratio=(18,10), mav=15)
