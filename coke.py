deposit = 0
coke = 50
due= 50

while deposit < coke:
    print ("Amount Due: " + str (due))
    coin = int(input("Insert Coin: "))
    if coin == 25:
        deposit += 25
    elif coin == 10:
        deposit += 10
    elif coin == 5:
        deposit += 5
    due = coke - deposit
    
changedue = coke - deposit
finaldue = str(abs(changedue))
print ("Change Owed: " + finaldue)
