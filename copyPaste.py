import requests
import urllib.request
import time
from bs4 import BeautifulSoup

hasil = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

namaStok = input('Masukkan KodeSaham : ');
nilaiNString = input('Masukkan NilaiN : ');

nilaiN = int(nilaiNString)

url='https://finance.yahoo.com/quote/'+namaStok+'.JK/history?p='+namaStok+'.JK'

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

for tbody in soup.select('tbody'):
    i = 0
    for tr in tbody.select('tr'):
        j = 0
        for td in tr.select('td'):
            data = td.text
            if (j==0):
                dataTgl = data
            if (j==5):
                dataHarga = data.replace(',','').replace('-','0')
            j = j+1

        if (dataHarga != '0') :
            hasil[0].append(dataTgl)
            hasil[1].append(dataHarga)
        i = i + 1

hasil[0].reverse()
hasil[1].reverse()

nilaiSum = 0
nilaiSumMAPE = 0
jmlSumMAPE = 0
nF = 0
nA = 0
hasil[3].append(0);
jmlMaks = (len(hasil[1]))

for k in range(0, jmlMaks):
    if (k < nilaiN) :
        nilaiSum += float(hasil[1][k])
        hasil[2].append(nilaiSum)

        if (k == (nilaiN-1)):
            nF = float(nilaiSum/nilaiN)
        else :
            nF = 0
    else:
        print(k-nilaiN)
        nilaiSum += float(hasil[1][k]) - float(hasil[1][k-nilaiN])
        hasil[2].append(nilaiSum)
        nF = float(nilaiSum/nilaiN)

    hasil[3].append(nF)

# FORCESTING ACCURACY
    if (k < nilaiN) :
        hasil[4].append(0)
        hasil[5].append(0)
    else :
        nF = float(hasil[3][k])
        nA = float(hasil[1][k])
        
        nilaiGap = abs(nF-nA)
        
        hasil[4].append(nilaiGap)
        hasil[5].append((nilaiGap/nA)*100)
        nilaiSumMAPE += (nilaiGap/nA)*100
        jmlSumMAPE += 1



################### MA(5)##########333

## hasil[1]
#   [
#    '600.00', '605.00', '595.00', '605.00', '600.00', '610.00', '600.00', 
#    '640.00', '650.00', '660.00', '650.00', '645.00', '675.00', '660.00', 
#    '655.00', '650.00', '660.00', '650.00', '685.00', '685.00', '690.00', 
#    '685.00', '725.00', '720.00', '730.00', '730.00', '700.00', '705.00', 
#    '750.00', '835.00', '840.00', '825.00', '800.00', '770.00', '770.00', 
#    '785.00', '805.00', '795.00', '780.00', '790.00', '785.00', '795.00', 
#    '820.00', '820.00', '840.00', '850.00', '830.00', '825.00', '825.00', 
#    '825.00', '795.00', '740.00', '775.00', '800.00', '805.00', '795.00', 
#    '775.00', '790.00', '765.00', '735.00', '750.00', '720.00', '730.00', 
#    '725.00', '715.00', '705.00', '735.00', '725.00', '720.00', '720.00', 
#    '715.00', '720.00', '765.00', '780.00', '765.00', '955.00', '935.00', 
#    '940.00', '1055.00', '1035.00', '1100.00', '1085.00', '1085.00', '1060.00', 
#    '1055.00', '1100.00', '1110.00', '1105.00', '1125.00', '1125.00', '1240.00', 
#    '1200.00', '1195.00', '1170.00', '1170.00', '1185.00', '1190.00', '1240.00', 
#    '1235.00', '1210.00'
#   ]
#print(hasil[1])

MA = []
N = 5
Yt = 0
t = 0

#print(len(hasil[1]))
#for i in range(0, len(hasil[1])):
    #if (i == 0):
        #for t in range(0, 5):
           # MA.append(0)
            #Yt += float(hasil[1][t])

   # else:
        #for k in range(,((N+i)-1)):
 #           Yt += float(hasil[1][0])

#    MA.append(Yt/N)
    #Yt = 0

#print(MA)


## hasil[3]
#   [
#    0, 0, 0, 0, 0, 601.0, 603.0, 602.0, 611.0, 620.0, 632.0, 640.0, 649.0, 656.0, 
#    658.0, 657.0, 657.0, 660.0, 655.0, 660.0, 666.0, 674.0, 679.0, 694.0, 701.0, 
#    710.0, 718.0, 721.0, 717.0, 723.0, 744.0, 766.0, 791.0, 810.0, 814.0, 801.0, 
#    790.0, 786.0, 785.0, 787.0, 791.0, 791.0, 789.0, 794.0, 802.0, 812.0, 825.0, 
#    832.0, 833.0, 834.0, 831.0, 820.0, 802.0, 792.0, 787.0, 783.0, 783.0, 790.0, 
#    793.0, 786.0, 772.0, 763.0, 752.0, 740.0, 732.0, 728.0, 719.0, 722.0, 721.0, 
#    720.0, 721.0, 723.0, 720.0, 728.0, 740.0, 749.0, 797.0, 840.0, 875.0, 930.0, 
#    984.0, 1013.0, 1043.0, 1072.0, 1073.0, 1077.0, 1077.0, 1082.0, 1086.0, 1099.0, 
#    1113.0, 1141.0, 1159.0, 1177.0, 1186.0, 1195.0, 1184.0, 1182.0, 1191.0, 1204.0, 
#    1212.0
#   ]
#


print(hasil[0]) # DATE
print(hasil[1]) # CLOSING PRICE
print(hasil[2]) # SUM(CLOSING PRICE)
print(hasil[3]) # M_(t+1)
print(hasil[4]) # GAP VALUE
print(hasil[5]) # MAPE

print('-----------------------------------')
print('Forecasting Simple Moving Average,dengan N = '+str(nilaiN))
print('Prediksi Untuk Besok :'+str(hasil[3][jmlMaks])+', tingkat akurasi :%3.2f%%'%(100-(nilaiSumMAPE/jmlSumMAPE)) )
