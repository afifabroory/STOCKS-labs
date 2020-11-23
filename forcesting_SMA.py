import json
import datetime as dt
import write_html as html
import load_stocks as files

# DECLARING VARIABLE
nSMA = [5,10,20,25,30]

source = input("Enter Input [YAHOO/IDX]: ").upper() # GET INPUT

# LOAD DATA JSON OF LQ45
STOCKS = json.load(open("data/stock_index/LQ45.json"))

# GET CURRENT DAY/MONTH/YEAR
currentTime = dt.datetime.now()

# TRAVARSE TO ALL STOCKS ELEMENT OF INDEX TIME COMPLEXITY: O(N)
for k in range(0, len(STOCKS)):

  # CREATE object Write_html
  output = html.WriteHTML(STOCKS[k])

  DATA = files.LoadStocks(STOCKS[k], source, "22-11-2020") # LOAD JSON FILE
  CLOSE_STOCKS, DATE_STOCKS = DATA.getData() # GET DATA STOCKS FROM JSON

  # TRAVARSE TO ALL SMA
  for j in range(0, len(nSMA)):

    # DECLARING VARIABLE FRASH VARIBLE EVREY ITERATION
    priceSum = 0
    mape = []
    mapeSum = 0
    movingAverage = []
    n = nSMA[j]

    output.writeHead(n) # WRITE HEADER TO HTML

    # TRAVARSE TO ALL LIST CLOSE_STOCKS[]. TIME COMPLEXITY: O(N)
    for t in range(0, len(CLOSE_STOCKS)):

      # CHECK DATA IF CLOSE_STOCKS[ITERATION-t] is NONE AND CHANGE TO 0
      if (CLOSE_STOCKS[t] == None):
        CLOSE_STOCKS[t] = 0

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
      # FORMULA: MAPE = 1/n SUM(At - Ft/At)
      # n             : Number of times the summuation iteration happen
      # At            : Actual Value
      # Ft            : Forcast Value

      #if (CLOSE_STOCKS[t] != 0):
      #  mapeSum += (abs(CLOSE_STOCKS[t] - movingAverage[t])/CLOSE_STOCKS[t])
      #else: 
      #  mapeSum += abs(CLOSE_STOCKS[t] - movingAverage[t])

      if (CLOSE_STOCKS[t] != 0):
        mape.append(float("{:.2f}".format(
                   (100 - (abs(CLOSE_STOCKS[t] - movingAverage[t])/CLOSE_STOCKS[t]) / n) 
                    * 100)))
      else:
          mape.append(float("{:.2f}".format(
                      (100 - (abs(CLOSE_STOCKS[t] - movingAverage[t]) / n) * 100))
                      ))

    for l in range(0, len(DATE_STOCKS)):

        # DEFAULT VALUE FOR ACTUAL AND FORCASTING
        actual = "NULL"
        forcasting = "NULL"
        forcastingInfo = '-'
        actualInfo = ''

        # CHECK UP/DOWN/SIDE OF SUBARRAY 
        # CLOSE_STOCKS[n-1 ... DATE_STOCKS.length - 1]
        # AND movingAverage[movingAverage[n-1 ... DATE_STOCKS.length - 1]]
        if (l >= (n-1)):
          if (movingAverage[l] - (CLOSE_STOCKS[l]) < 0):
            forcasting = "#ff0000"
            forcastingInfo = "DOWN 📉"
          elif (movingAverage[l] - (CLOSE_STOCKS[l]) > 0):
            forcasting = "#008000"
            forcastingInfo = "UP 📈"
          else:
            forcasting = "#333333"
            forcastingInfo = "FLAT 😐"

        # CHECK UP/DOWN/SIDE OF CLOSE_STOCKS[i] AND CLOSE_STOCKS[i-1] 
        if (l > 0):
          if (CLOSE_STOCKS[l] > CLOSE_STOCKS[l-1]):
            actual = "#008000"
            actualInfo = "📈"
          elif (CLOSE_STOCKS[l] < CLOSE_STOCKS[l-1]):
            actual = "#ff0000"
            actualInfo = "📉"
          else:
            actual = "#333333"
            actualInfo = "😐"

        # WRITE BOYD OF CONTENT TO HTML
        output.writeBody(
                         DATE_STOCKS[l], actual, CLOSE_STOCKS[l], actualInfo, 
                         forcasting, movingAverage[l], mape[l], forcastingInfo
                        )

    output.writeBottom(mape[-1]) # WRITE TO HTML
