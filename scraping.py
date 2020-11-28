import requests
import calendar
import time
import urllib.request
import json
import pandas as pd
from bs4 import BeautifulSoup

def getData(stockCode, minute=False):
  timestamp = calendar.timegm(time.gmtime())

  if (minute == True):
    YAHOO = ("https://query1.finance.yahoo.com/v8/finance/chart/{0}.JK?"
            "region=US&lang=en-US&includePrePost=false&interval=5m&range=1d"
            "&corsDomain=finance.yahoo.com&.tsrc=finance")
  else:
    YAHOO = ("https://query1.finance.yahoo.com/v8/finance/chart/{0}.JK"
        "?&symbol={0}.JK&period1=1&period2={1}&interval=1d")

  page = requests.get(YAHOO.format(stockCode, timestamp))
  scraping = BeautifulSoup(page.text, "html.parser")

  data = json.loads(scraping.get_text())

  return data
