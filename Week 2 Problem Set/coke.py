amount_due = 50
print("Amount Due:", amount_due)
while amount_due!=0:
    insert = int(input("Insert Coin:"))
    if insert in [25,10,5]:
        amount_due = amount_due-insert
    else:
        print("Amount Due:",amount_due)
        continue
    if amount_due>0:
        print("Amount Due:",amount_due)

    else:
        print("Change Owed:",abs(amount_due))
    if amount_due<0:
        break
