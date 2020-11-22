import json
import datetime as dt

priceSum = 0
mape = []
mapeSum = 0
movingAverage = []

source = intput("YAHOO/IDX? ").upper()
n = int(input("SMA(n)? "))
STOCKS = input("KODE SAHAM? ").upper()

# WRITE FILE
f = file("{}.html".format(STOCKS), 'w')


# LOAD JSON FILE
DATA = json.load(open("STOCK_CHART/{}-{}-{}.json"
                .format(STOCKS, source, "22-11-2020")))

# GET DATA FROM JSON
DATE_STOCKS = DATA["chart"]["result"][0]["timestamp"]
CLOSE_STOCKS = DATA["chart"]["result"][0]["indicators"]["quote"][0]["close"]

# CONVERT TIMESTAMP TO FORMATTED TIME COMPLEXITY: O(N)
for i in range(0, len(DATE_STOCKS)):
    DATE_STOCKS[i] = dt.datetime.fromtimestamp(DATE_STOCKS[i])
                     .strftime("%d/%m/%Y")

for t in range(0, len(CLOSE_STOCKS)):
  if (CLOSE_STOCKS[t] == None):
    CLOSE_STOCKS[t] = 0.0

  if (t < n):
    priceSum += float(CLOSE_STOCKS[t])

    if (t == (n-1)):
      Mt = float(priceSum/n)
    else:
      Mt = 0.0

  else:
    priceSum += CLOSE_STOCKS[t] - CLOSE_STOCKS[t-n]
    Mt = float(priceSum/n)    

  movingAverage.append(float("{:.2f}".format(Mt)))

  if (CLOSE_STOCKS[t] != 0.0):
    mapeSum += abs(CLOSE_STOCKS[t] - movingAverage[t])/CLOSE_STOCKS[t]
    mape.append(float("{:.2f}".format(100 - (mapeSum/(t+1)) * 100)))

f.write("""
<pre>
SMA({}) - {}\nDATE\t\tCLOSE\t\t\tFORECASTING BESOK
</pre>
""".format(n, STOCKS))
for i in range(0, len(DATE_STOCKS)):
    actual = "NULL"
    forcasting = "NULL"

    if ((i%n) == 0):
      f.write('\n')  

    if (i >= (n-1)):
      if (movingAverage[i] - (CLOSE_STOCKS[i]) < 0):
        forcasting = "Forcasting Besok: [TURUN]"
      elif (movingAverage[i] - (CLOSE_STOCKS[i]) > 0):
        forcasting = "Forcasting Besok: [NAIK]"
      else:
        forcasting = "Forcasting Besok: [DATAR]"

    if (CLOSE_STOCKS[i] > CLOSE_STOCKS[i-1]):
      actual = "[NAIK]"
    elif (CLOSE_STOCKS[i] < CLOSE_STOCKS[i-1]):
      actual = "[TURUN]"
    else:
      actual = "[DATAR]"

    f.write(
          str(DATE_STOCKS[i]) + '\t{:.2f}\t{}'.format(CLOSE_STOCKS[i], actual) 
          + '\t\t' + str(movingAverage[i]) + "\t{}\n".format(forcasting) 
         ) 
f.write("""Tingkat Akurasi Forcasting untuk besok: {}%""".format(mape[-1]))
