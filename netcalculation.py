# Copyright (c) 2021 Muhammad Afif Abroory <afif.abroory@gmail.com>

import math

print("\nFee Calculation for BNI Securities\n")

price = int(input("Masukkan harga saham\t: "))
share = int(input("Masukkan jumlah lot\t: "))

option = input("Membeli atau Menjual? [B/S] >> ").upper()
while (option != 'B' and option != 'S'):
	print("\n[WARNING] Masukkan 'B' atau 'S' bukan '{}'!".format(option))
	option = input("Membeli atau Menjual? [B/S] >> ").upper()
	
BUY_FEE = 0.3 # Constant number for Tax + Broker fee in BNI Securities
SELL_FEE = 0.4 # Constatn number for Tax + Broker fee in BNI Securities

# Calculate total without tax and fee a.k.a gross (maybe the terms is wrong). 
grossTotal = price * share * 100 # 100 is magic number for 1 lot. which is 1 lot equal to 100 (RIP English wkwk)

if option == 'B':
	netTotal = math.floor(grossTotal + (grossTotal * (BUY_FEE/100)))
	
	print("\n\tTotal = {:,d} x {} x 100".format(price,share))
	print("\t      = {:,d} (Tanpa fee)".format(grossTotal))
	print("\n\tTotal = {0} + ({0} x {1}%)".format(grossTotal,BUY_FEE))
	print("\t      = {:,d} (Dengan fee)".format(netTotal))
	print("\nMaka total yang harus dibayar adalah Rp. {:,d}".format(netTotal))
	
elif option == 'S':
	buyPrice = int(input("\n[OPTIONAL] Masukkan harga beli (Masukkan angka 0 untuk mengkosongkan harga beli): "))
	
	netTotal = math.floor(grossTotal - (grossTotal * (SELL_FEE/100)))
	
	print("\n\tGross Profit = {:,d} x {} x 100".format(price,share))
	print("\tGross Profit = {:,d} (Tanpa fee dan belum dikurangi dengan harga beli)".format(grossTotal))
	print("\n\tProfit = {0} - ({0} x {1}%)".format(grossTotal,SELL_FEE))
	print("\t       = {:,d} (Belum dikurangi harga beli, hanya dikurangi dengan fee)".format(netTotal))
	if (buyPrice != 0):
		netProfit = netTotal - (buyPrice * 100 * share)
		print("\nMaka Profit yang anda terima adalah Rp. {:,d} (Belum dikurangi harga beli)".format(netTotal))
		print("Maka Net Profit yang anda terima adalah Rp. {:,d} (Telah dikurangi harga beli)".format(netProfit))
	else:
		print("\nMaka Profit yang anda terima adalah Rp. {:,d} (Belum dikurangi harga beli)".format(netTotal))
