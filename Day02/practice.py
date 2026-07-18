
# Exercises
#  Temperature label
temp = int(input("Enter temperature in your area: "))
if temp > 28:
    print("It's hot ")
elif temp >15:
    print ("It's warm ")
else:
    print( "It's cold ")

# # Receipt loop
for i in range (1,10):
    print(f"Receipt {i}")


# Even Numbers
for i in range (1,20):
    if i % 2 == 0:
        print(f"{i}")


#Discount function
def apply_discount(price, percent=10):
    # price = int(input("Enter Price for discount: "))
    print(f"{price - price / percent}")

apply_discount(2000)


# countdown
i=5
while i >=1:
    print(f"{i}")
    i -=1
print("Liftoff")