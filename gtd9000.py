#GHOST TX DESTROYER 9000

import csv

print( "==== WELCOME TO GHOST TX DESTROYER 9000 ====")
print( "============= DOOM AWAITS ==================")
print( "Please make sure to move the .csv file to the same location as the GTD9000.py file")
file = input("Then enter the name of the .csv file (i.e. bitcoin-txs-2017-11-20_17-44-48.csv) to be ghost-destroyified here -->:")
file = str.format(file)
#file = "bitcoin-txs-2017-11-20_17-44-48.csv"
file = file.strip()

deposits = []
withdrawals = []
fees = []

with open(file) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    for row in csvreader:
        if row[4]:
            f_amount = row[4].strip(" BTC")
            f_amount = f_amount.strip("-")
            f_amount = f_amount.strip()
            f_amount = float(f_amount)
            #print(f_amount)
            fees.append(f_amount)
        if "-" in row[3]:
            w_amount = row[3].strip(" BTC")
            w_amount = w_amount.strip("-")
            w_amount = float(w_amount)
            #print(w_amount)
            withdrawals.append(w_amount)
        else:
            d_amount = row[3].strip(" BTC")
            d_amount = float(d_amount)
            #print(d_amount)
            deposits.append(d_amount)

deposits_total = sum(deposits)
withdrawal_total = sum(withdrawals)
fees_total = sum(fees)

print ("Deposits: ", deposits_total)
print ("Withdrawals: ", withdrawal_total)
print ("Fees: ", fees_total)
print ("Total :" , deposits_total - (withdrawal_total + fees_total))
