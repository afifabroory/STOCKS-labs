import json
import datetime as dt

priceSum = 0
mape = []
mapeSum = 0
movingAverage = []
source = input("Yahoo/IDX? ").upper()
n = int(input("SMA(n)? "))
stock = input("Kode Saham? ").upper()

# LOAD JSON FILE
DATA = json.load(open("STOCK_CHART/{}-{}-{}.json".format(stock,source, "20-11-2020")))

# GET DATA FROM JSON
DATE_STOCKS = DATA["chart"]["result"][0]["timestamp"]
CLOSE_STOCKS = DATA["chart"]["result"][0]["indicators"]["quote"][0]["close"]

# CONVERT TIMESTAMP TO FORMATTED TIME COMPLEXITY: O(N)
for i in range(0, len(DATE_STOCKS)):
    DATE_STOCKS[i] = dt.datetime.fromtimestamp(DATE_STOCKS[i]).strftime("%d/%m/%Y")

for t in range(0, len(CLOSE_STOCKS)):
  if (t < n):
    priceSum += float(CLOSE_STOCKS[t])

    if (t == (n-1)):
      Mt = float(priceSum/n)
    else:
      Mt = 0

  else:
    priceSum += float(CLOSE_STOCKS[t]) - float(CLOSE_STOCKS[t-n])
    Mt = float(priceSum/n)    

  movingAverage.append(float("{:.2f}".format(Mt)))

  mapeSum += abs(CLOSE_STOCKS[t] - movingAverage[t])/CLOSE_STOCKS[t]
  mape.append(float("{:.2f}".format(100 - (mapeSum/(t+1)) * 100)))


print('SMA(' + str(n) + ')')
print("DATE\t\tCLOSE\t\tFORECASTING BESOK")
for i in range(0, len(DATE_STOCKS)):
    actual = "NULL"
    forcasting = "NULL"

    if ((i%n) == 0):
      print('')  

    if (i >= (n-1)):
      if (movingAverage[i] - (CLOSE_STOCKS[i]) < 0):
        forcasting = "Forcasting Besok: ⬇️"
      elif (movingAverage[i] - (CLOSE_STOCKS[i]) > 0):
        forcasting = "Forcasting Besok: ⬆️"
      else:
        forcasting = "Forcasting Besok: -"

    if (CLOSE_STOCKS[i] > CLOSE_STOCKS[i-1]):
      actual = "[⬆️]"
    elif (CLOSE_STOCKS[i] < CLOSE_STOCKS[i-1]):
      actual = "[⬇️]"
    else:
      actual = "[-]"

    print(
          str(DATE_STOCKS[i]) + '\t{:.2f}\t{}'.format(CLOSE_STOCKS[i], actual) 
          + '\t' + str(movingAverage[i]) + "\t{}".format(forcasting) 
         ) 