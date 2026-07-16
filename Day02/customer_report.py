
customers = [ ["ruth", 5500], ["Eyerusalem", 3000] ,["tsion",300], ["bekele",7000]   ]

def tier(balance):
    if balance>3000:
        return "premium"
    elif balance>1000:
        return "standard"
    else :
        return "basic"

premium_count = 0
standard_count = 0
basic_count = 0


        
for name,balance in customers:
    print(f"{name} is {tier(balance)} with {balance}ETB")

for name,balance in customers:
    customer_tier = tier(balance)
    if customer_tier == "premium":
            premium_count +=1
    elif customer_tier == "standard":
            standard_count +=1
    else:
            basic_count +=1

print(f"There are {premium_count}premium customers {standard_count} standard customers and {basic_count} basic customers")


