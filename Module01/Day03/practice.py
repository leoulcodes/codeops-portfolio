
# unique cities
cities = ["Addis Ababa", "Mekelle", "Dukem", "Bahirdar", "Addis Ababa", "Dukem"]
print(set(cities))
print(len(set(cities)))

# Price report
Grocery = {"soap":50,
           "Shampoo":60,
           "detergent":150,
           "vegetables":1000,
           "Fruits":2000}
for item,price in Grocery.items():
    print(f"{item} is {price} in ETB")



# Tax Comprehesion
prices = [100, 250, 400, 80]
list = [p*1.15 for p in prices ]
print(list)

# cheap items
cheap =[p for p in prices if p>200]
print(cheap)


#write & read
with open("names.txt") as f:
    for line in f:
        text = f.read()
        print(text)

#safe division
try:
    number= int(input("Enter a number: "))
    solution= 1000/number
except ValueError:
    print("Enter a number")
except ZeroDivisionError:
    print("Cannot divide by 0")
else:
    print(solution)
finally:
    print("Done")