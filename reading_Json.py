import json

file = {
        'TRI': 'TRADING_INFO/2020-11-19-2020-08-25.json',
        'STC': 'STOCK_CHART/19-Nov-2020.json'
       }

f1 = open(file['STC'], )
data = json.load(f1)

fD = open('Time-Close.txt', 'w')

f2 = open(file['TRI'])
data = json.load(f2)

fI = open('Summary.txt', 'w')
for i in data['replies']:
  fI.write("ID: {}\nDate: {}\nPrevious: {}\nOpen Price: {}\nFirst Trade: {}\nHigh: {}\nLow: {}\nClose {}\nChange: {}\n\n".format(
  i['IDStockSummary'], i['Date'], i['Previous'], i['OpenPrice'], i['FirstTrade'], i['High'],i['Low'], i['Close'], i['Change']))  
