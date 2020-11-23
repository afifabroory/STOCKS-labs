"""class WriteHTML()
		
		CONSTRUCTOR
			the constructor need to pass is stockCode

		METHOD
			writeHEAD() is to write a HTML file HEADER of content
		 	wirteBODY() is to write a HTML file BODY/TABLE of content.
		 	writeBOTTOM() is to write a HTML file BOTTOM of content
"""

class WriteHTML:

  def __init__(WriteHTML, stockCode):
    WriteHTML.stockCode = stockCode.upper()
    WriteHTML.f = open("data/html/tmp/SMA-{}.html".format(stockCode), 'w')
    WriteHTML.f.write(
              "<a href=#5>SMA(5)</a> - "
              "<a href=#10>SMA(10)</a> - "
              "<a href=#20>SMA(20)</a> - "
              "<a href=#25>SMA(25)</a> - "
              "<a href=#30>SMA(30)</a>"
            )

    # 0 : N
    # 1 : STOCK CODE
  def writeHead(WriteHTML, n):
    WriteHTML.f.write(
              "<h2 style=\"text-align: center;\">"
              "&nbsp;<a name=\"{0}\"><strong>SMA({0}) {1}</strong></h2>"
              .format(n, WriteHTML.stockCode)
            )
    WriteHTML.f.write(
             "<p style=\"text-align: center; margin-top=0px;\">"
             "<a href=#>BACK TO TOP</a></p>"
    			 )
    WriteHTML.f.write(
    				  "<table style=\"height: 66px; width: 680,2833px;" 
    				  "margin-left: auto; margin-right: auto;\" border=\"BLACK\">"
    				  "<tbody><tr style=\"height: 9px;\">"
    				  "<td style=\"width: 91px; height: 9px; text-align: center;\">"
    			 	  "&nbsp;<strong>DATE</strong></td>"
    				  "<td style=\"width: 149px; height: 9px; text-align: center;\">"
    				  "&nbsp;<strong>CLOSE</strong></td>"
    				  "<td style=\"width: 149px; height: 9px; text-align: center;\">"
    				  "&nbsp;<strong>FORCASTING</strong></td>"
    				  "<td style=\"width: 88.2833px; height: 9px; text-align: center;\">"
    			  	"<strong>&nbsp;ACCURACY</strong></td>"
						  "<td style=\"width: 155px; height: 9px; text-align: center;\">"
						  "<strong>&nbsp;TOMORROW</strong></td>"
					 )

      # DATE : DATE
	    # ACTUAL : ACTUAL (RAISE/DOWN COLOR)
	    # CLOSING : CLOSING PRICE
	    # ACT_INF : ACTUAL INFORMATION [EMOJI]
	    # FORCASTING : FORCASTING (RAISE/DOWN COLOR)
	    # SMA : SMA PRICE
	    # MAPE : MAPE
	    # FCT_INF : FORCASTING INFORMATION
  def writeBody(WriteHTML, DATE, ACTUAL, CLOSING, ACT_INF, FORCASTING, 
                SMA, MAPE, FCT_INF
               ):
	  WriteHTML.f.write(
	   				  "<tr style=\"height: 14px;\">"
	   				  "<td style=\"width: 95px; height: 14px; text-align: center;\">"
	    				"&nbsp;{}</td>"
	   					"<td style=\"width: 149px; height: 14px; text-align: center;\">"
	   					"<span style=\"color:{};\">"
	   					"&nbsp;{:.2f} {}</span></td>"
	    				"<td style=\"width: 149px; height: 14px; text-align: center;\">"
	   					"<span style=\"color: {};\">" 
	    				"&nbsp;{:.2f}&nbsp;</span></td>"
	  					"<td style=\"width: 88.2833px; height: 14px; text-align: center;\">"
	   					"{:.2f}%</td>"
	   					"<td style=\"width: 155px; height: 14px; text-align: center;\">"
	   					"{}</td></tr></tr>"
	   					.format(DATE, ACTUAL, CLOSING, ACT_INF, 
	   						      FORCASTING, SMA, MAPE, FCT_INF
	   						     )
	   			 )

  def writeBottom(WriteHTML, MAPE):
	  WriteHTML.f.write(
	  	        "</tbody></table><h3 style=\"text-align: center;\">&nbsp;<strong>"
	            "Tingkat Akurasi Forcasting untuk Besok: {}".format(MAPE) +
	            "%</strong></h3>"
	         )