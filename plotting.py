import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt


DOMAIN = "YAHOO"
DATE = "20-11-2020"

fileName = open("STOCK_CHART/{0} {1}.json".format(DOMAIN, DATE), )

DATA = json.load(fileName)

TIMES_STAMP = DATA["chart"]["result"][0]["timestamp"]
OPEN = DATA["chart"]["result"][0]["indicators"]["quote"][0]["open"]
CLOSE = DATA["chart"]["result"][0]["indicators"]["quote"][0]["close"]
VOLUME = DATA["chart"]["result"][0]["indicators"]["quote"][0]["volume"]
HGIH = DATA["chart"]["result"][0]["indicators"]["quote"][0]["low"]
LOW = DATA["chart"]["result"][0]["indicators"]["quote"][0]["low"]

#CONVERT TIME STAMP TO TIME
for i in range(0, len(TIMES_STAMP)):
  TIMES_STAMP[i] = dt.datetime.fromtimestamp(TIMES_STAMP[i]).strftime("%d/%m/%Y")

print(TIMES_STAMP)
