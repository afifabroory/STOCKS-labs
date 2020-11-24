import calendar
import time

"""class TargetWeb
  This class to provide a complete URL of TargetWeb in given parameter
  stockCode, keyDomain, keyPath, keyParameter.
  This class have one method getURL()

  CONSTRUCTOR
     Constructor is used for initialization parameter 
    keyDomain, keyPath, & keyParameter.
    
    __init__(stockCode, keyDomain, keyPath, keyParameter)
      stockCode   : for changing URL parameter.
                     stockCode format index is 0.
                     default value for stockCode is '' (EMPTY STRING).
      keyDomain    : is a key for accessing dictionary domainDict.
      keyPath      : is a key for accessing dictionary pathDict. Where it's is from keyDomain + keyParameter.
      keyParameter : is a key for accesing dictionary parameterDict. Where it's is from keyDomain + keyParameter

  METHOD
    getURL()
     Method getURL() aims to process a complete URL from a dictionary
    domain, path and parameter.

    This method doesn't need any input anymore.

    This method accessing Dictionary domainDict, pathDict and paramterDict
    Values using Key keyDomain, keyPath and keyParameter.
    Values and concatenate each Values of Dictionary and
    change the string format of stockCode position to given input.

    Method getURL() return a variable string URL."""
class TargetWeb():

    global  domainDict
    global pathDict
    global parameterDict
    
    domainDict = {
                  "IDX": "https://www.idx.co.id/umbraco/Surface",
                  "YAHOO": "https://query2.finance.yahoo.com"
                 }
    pathDict = {
                "IDX_TRADING_INFO": "/ListedCompany/GetTradingInfoSS?",
                "IDX_STOCK_CHART": "/Helper/GetStockChart?",
                "YAHOO_STOCK_CHART": "/v8/finance/chart/{0}.JK"
               }
    parameterDict = {
                     "IDX_TRADING_INFO": "code={0}&language=id-id&draw=2&columns[0][data]=No&columns[0][name]=&"
                 			         "columns[0][searchable]=true&columns[0][orderable]=false&"
                 				     "columns[0][search][value]=&columns[0][search][regex]=false&"
                 				     "columns[1][data]=Date&columns[1][name]=&columns[1][searchable]=true&"
                 				     "columns[1][orderable]=false&columns[1][search][value]=&"
                 				     "columns[1][search][regex]=false&columns[2][data]=OpenPrice&"
                 				     "columns[2][name]=&columns[2][searchable]=true&"
                 				     "columns[2][orderable]=false&columns[2][search][value]=&"
                 				     "columns[2][search][regex]=false&columns[3][data]=High&"
                 				     "columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=false&"
                 				     "columns[3][search][value]=&columns[3][search][regex]=false&"
                 				     "columns[4][data]=Low&columns[4][name]=&columns[4][searchable]=true&"
                 				     "columns[4][orderable]=false&columns[4][search][value]=&"
                 				     "columns[4][search][regex]=false&columns[5][data]=Close&"
                 				     "columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=false&"
                 				     "columns[5][search][value]=&columns[5][search][regex]=false&"
                 				     "columns[6][data]=Volume&columns[6][name]=&columns[6][searchable]=true&"
                 				     "columns[6][orderable]=false&columns[6][search][value]=&"
                 				     "columns[6][search][regex]=false&columns[7][data]=Value&"
                 				     "columns[7][name]=&columns[7][searchable]=true&columns[7][orderable]=false&"
                 				     "columns[7][search][value]=&columns[7][search][regex]=false&"
                 				     "columns[8][data]=Frequency&columns[8][name]=&columns[8][searchable]=true&"
                 				     "columns[8][orderable]=false&columns[8][search][value]=&"
                 				     "columns[8][search][regex]=false&start=0&length=60&search[value]=&"
                 				     "search[regex]=false&_=1605794489395",
                     "IDX_STOCK_CHART": "indexCode={0}&period=1d",
                     "YAHOO_STOCK_CHART":"?&symbol={0}.JK&period1=-122198400&period2={1}&interval=1d"
                    }

#"YAHOO_STOCK_CHART":"?&symbol={0}.JK&period1=-122198400&period2=1605875079&interval=1d&includePrePost=true&events=div|split|earn&lang=en-US&region=US&crumb=BLiN6wzK37F&corsDomain=finance.yahoo.com"

    def __init__(TargetWeb, keyDomain, keyParameter, stockCode = ''):
        TargetWeb.stockCode = stockCode.upper()
        TargetWeb.keyDomain = keyDomain.upper()
        TargetWeb.keyPath = (keyDomain + '_' + keyParameter).upper()
        TargetWeb.keyParameter = (keyDomain + '_' + keyParameter).upper()
        TargetWeb.ts = calendar.timegm(time.gmtime())

    def getURL(TargetWeb):
        domain = domainDict[TargetWeb.keyDomain]
        path = pathDict[TargetWeb.keyPath]
        parameter = parameterDict[TargetWeb.keyParameter]

        URL = (domain + path + parameter).format(TargetWeb.stockCode, TargetWeb.ts)
        print(URL)

        return URL
