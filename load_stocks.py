import json
import datetime as time


"""class LoadStocks()
	This purpose for provide a clean data so and doesn't make main code too long.

	CONSTURCTOR
		LoadStocks class only need to pass parameter stocksCode and date for
		intialization. Default date is now date (System).
		Format DATE must be dd-mm-yyyy

	METHOD
		getClose() this method aim to process CLOSE & DATE, this class
		returning two lists first is CLOSE and second is DATE.
		This class process the data if CLOSE is NULL so iteration of getClose()
		method skip to next iteration and DATE is also skipped."""
class LoadStocks:

  global currentTime
  global STOCK_PATH
  global current
  global CLOSE_STOCKS
  global DATE_STOCKS

  currentTime = time.datetime.now()
  STOCK_PATH = "STOCK_CHART/{0}/{1}-{0}-{2}.json"
  current = (str(currentTime.day) + "-" +  str(currentTime.month) 
  						+ "-" + str(currentTime.year)
  					)
  CLOSE_STOCKS = []
  DATE_STOCKS = []

  def __init__(LoadStocks, stocksCode, source, date=current):
    LoadStocks.stocksCode = str(stocksCode)
    LoadStocks.source = str(source)
    LoadStocks.date = str(date)


  def getData(LoadStocks):

  	# LOAD STOCKS DATA FROM JSON
    STOCK = json.load(open(STOCK_PATH.format(LoadStocks.source, 
                     LoadStocks.stocksCode, LoadStocks.date)))

    # GET CLOSE AND DATE DATA
    tmpDATE_STOCKS = STOCK["chart"]["result"][0]["timestamp"]
    tmpCLOSE_STOCKS = STOCK["chart"]["result"][0]["indicators"]["quote"][0]["close"]

    # CLEANING DATA AND CONVERT DATE TO dd-mm-yyyy FORMAT
    for i in range(0, len(tmpCLOSE_STOCKS)):
      if (tmpCLOSE_STOCKS[i] == None):
        continue
        
      CLOSE_STOCKS.append(tmpCLOSE_STOCKS[i])
      DATE_STOCKS.append(tmpDATE_STOCKS[i])

    return CLOSE_STOCKS, DATE_STOCKS
