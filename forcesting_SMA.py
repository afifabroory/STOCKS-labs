import json
import datetime as dt

# DECLARING VARIABLE
priceSum = 0
mape = []
mapeSum = 0
movingAverage = []

# GET CURRENT DAY/MONTH/YEAR
currentTime = dt.datetime.now()

# GET INPUT
n = int(input("Enter Input of n, SMA(n): "))
source = input("Enter Input [YAHOO/IDX]: ").upper()

# LOAD DATA JSON OF LQ45
STOCKS = json.load(open("data/stock_index/LQ45.json"))

# TRAVARSE TO ALL STOCKS ELEMENT TIME COMPLEXITY: O(N)
for k in range(0, len(STOCKS)):
  # LOAD JSON FILE
  DATA = json.load(open("STOCK_CHART/{}-{}-{}.json"
                    .format(STOCKS[k], source,
                    (str(currentTime.day)+ "-" + str(currentTime.month) + "-"
                    + str(currentTime.year))
                    )))

  # GET DATA STOCKS FROM JSON
  DATE_STOCKS = DATA["chart"]["result"][0]["timestamp"]
  CLOSE_STOCKS = DATA["chart"]["result"][0]["indicators"]["quote"][0]["close"]


  # CONVERT TIMESTAMP TO FORMATTED TIME COMPLEXITY: O(N)
  for i in range(0, len(DATE_STOCKS)):
      DATE_STOCKS[i] = dt.datetime.fromtimestamp(
        DATE_STOCKS[i]).strftime("%d/%m/%Y")


  # TRAVARSE TO ALL LIST CLOSE_STOCKS[]. TIME COMPLEXITY: O(N)
  for t in range(0, len(CLOSE_STOCKS)):

    # CHECK DATA IF CLOSE_STOCKS[ITERATION-t] is NONE AND CHANGE TO 0
    if (CLOSE_STOCKS[t] == None or CLOSE_STOCKS[t] == 0.0):
      CLOSE_STOCKS[t] = 1

    # CHECK IF ITERATION-t IN SUBARRAY [0 ... n-1]
    if (t < n):

      # SUM ALL ELEMENT OF CLOSE_STOCKS[] TO priceSum
      priceSum += float(CLOSE_STOCKS[t])

      # CHECK IF ITERATION-t INEDX IS n-1 INDEX AND THEM CALCULATE MA_t+1. 
      # ELSE MA_t
      if (t == (n-1)):
        Mt = float(priceSum/n)
      else:
        Mt = 0.0

    else:

      # SUM ELEMENT OF (CLOSE_STOCKS[ITERATION-t] - CLOSE_STOCKS[ITERATION-n]
      priceSum += CLOSE_STOCKS[t] - CLOSE_STOCKS[t-n]
      Mt = float(priceSum/n) # CALCULATE MA_t+1

    # ADD MA_t+1 RESULT TO LIST movingAverage[]
    movingAverage.append(float("{:.2f}".format(Mt)))

    # CALCULATE MAPE AND ADD CALCULATION TO MAPE[] TO PERCENTAGE FORMAT.
    # FORMULA: MAPE = 1/n SUM(At - Ft/At) * 100
    # n             : Number of times the summuation iteration happen
    # At            : Actual Value
    # Ft            : Forcast Value
    mapeSum += (abs(CLOSE_STOCKS[t] - movingAverage[t])/CLOSE_STOCKS[t])
    mape.append(float("{:.2f}".format(100 - ((mapeSum/(t+1) * 100)))))


  # LOAD FILE/CREATE FILE
  f = open("data/html/SMA({})-{}.html".format(n, STOCKS[k]), 'w')

  # WRITE TO HTML
  f.write("""
  <pre>
  SMA({}) - {}\n\nDATE\t\tCLOSE\t\t\tFORECASTING BESOK""".format(n, STOCKS[k]))
  for i in range(0, len(DATE_STOCKS)):

      # DEFAULT VALUE FOR ACTUAL AND FORCASTING
      actual = "NULL"
      forcasting = "NULL"

      # MULTIPLE OF N WRITE NEW LINE
      if ((i%n) == 0):
        f.write('\n')  

      # CHECK UP/DOWN/SIDE OF SUBARRAY 
      # CLOSE_STOCKS[n-1 ... DATE_STOCKS.length - 1]
      # AND movingAverage[movingAverage[n-1 ... DATE_STOCKS.length - 1]]
      if (i >= (n-1)):
        if (movingAverage[i] - (CLOSE_STOCKS[i]) < 0):
          forcasting = "Forcasting Besok: [TURUN]"
        elif (movingAverage[i] - (CLOSE_STOCKS[i]) > 0):
          forcasting = "Forcasting Besok: [NAIK]"
        else:
          forcasting = "Forcasting Besok: [DATAR]"

      # CHECK UP/DOWN/SIDE OF CLOSE_STOCKS[i] AND CLOSE_STOCKS[i-1] 
      if (CLOSE_STOCKS[i] > CLOSE_STOCKS[i-1]):
        actual = "[NAIK]"
      elif (CLOSE_STOCKS[i] < CLOSE_STOCKS[i-1]):
        actual = "[TURUN]"
      else:
        actual = "[DATAR]"

      # WRITE TO HTML
      f.write(
            str(DATE_STOCKS[i]) + '\t{:.2f}\t{}'.format(CLOSE_STOCKS[i], actual) 
            + '\t\t' + str(movingAverage[i]) + "\t{}\n".format(forcasting) 
           ) 

  # WRITE TO HTML
  f.write("""
  Tingkat Akurasi Forcasting untuk besok: {}%</pre>""".format(mape[-1]))
