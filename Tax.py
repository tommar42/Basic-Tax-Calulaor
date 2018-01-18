import time
print ("I am python")

money = input("\nHow much is the thing? " )

check = money.isdigit()

while check == False:
    print ("that not a number")
    money = input("What percentage of tax is chagred on this good? " )
    check = money.isdigit()

int(money)
print ("The cost is set to " + money)

tax = input("\nWhat percentage of tax is chagred on this good? " )

check2 = tax.isdigit()

while check == False:
    print ("that not a number")
    money = input("What percentage of tax is chagred on this good? " )
    check2 = tax.isdigit()

int(tax)

taxmoney = float(money) / 100 * float(tax)
totalcost = float(taxmoney) + float(money)
print("You will have to pay £" + str(money) + " with £" + str(taxmoney) + " of that being tax!" )
