stock = {}
try:
    with open("stock.txt") as f:
        for line in f:
            item,qty = line.strip().split(",")
            stock[item] = int(qty)
except FileNotFoundError:
    print("No stock file yet - starting empty")

def adjust(item, amount):
    stock[item]= stock.get(item, 0) + amount

low = [item for item, qty in stock.items() if qty<10]
print("Low stock:", low)