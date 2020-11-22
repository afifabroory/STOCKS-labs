import target_web as data
import datetime as time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

SOURCE = "YAHOO"
LQ45 = [
				"AALI","ACES","ADHI","ADRO","AKRA","ANTM","APLN","ASII","ASSA","BBCA",
				"BBKP","BBNI","BBRI","BBTN","BDMN","BEST","BJBR","BJTM","BMRI","BMTR",
				"BNLI","BRIS","BRPT","BSDE","BTPS","BULL","CLEO","CPIN","CTRA","DMAS",
				"ELSA","ERAA","EXCL","GGRM","GIAA","HKMU","HMSP","HOKI","ICBP","INAF",
				"INCO","INDF","INDY","INKP","INTP","ISAT","ITMG","JPFA","JRPT","JSMR",
				"KAEF","KBLI","KINO","KLBF","LINK","LPKR","LPPF","LSIP","MAIN","MAPI",
				"MDKA","MEDC","MIKA","MNCN","MTDL","MYOR","PGAS","PNBN","PNLF","PSAB",
				"PTBA","PTPP","PWON","RALS","SCMA","SIDO","SILO","SIMP","SMBR","SMGR",
				"SMRA","SMSM","SPTO","SRIL","SSIA","SSMS","TBIG","TINS","TKIM","TLKM",
				"TOWR","TPIA","UNTR","UNVR","WEGE","WIKA","WOOD","WSBP","WSKT","WTON"
			 ]

for i in range(1, len(LQ45)):
		driver = webdriver.Firefox('/usr/local/bin')

		currentTime = time.datetime.now()
		DATE = str(currentTime.day) + '-' + str(currentTime.month) + '-' + str(currentTime.year)

		DATA = data.TargetWeb("YAHOO", "STOCK_CHART", LQ45[i])

		# ACCESS WEB USING PROXY
		##driver.get("https://www.proxysite.com/")
		##element = driver.find_element_by_name('d')
		##element.send_keys(DATA.getURL())
		##element.send_keys(Keys.ENTER)

		# ACESS WEB !(USING PROXY)
		driver.get("view-source:"+ DATA.getURL())

		# CHANGE WEBSITE VIEW TO VIEW-SOURCE (IF USING PROXY)
		##url = driver.current_url
		##driver.get("view-source:" + url)

		# GET PAGE TEXT
		dataPage = driver.find_element_by_xpath("/html/body/pre").text

		file = open("STOCK_CHART/{}-YAHOO-{}.json".format(LQ45[i] ,DATE), 'w')
		file.write(dataPage)

		sleep(120)
		driver.quit()
