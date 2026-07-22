

# 1. Book class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages")


# Create two books
book1 = Book("Atomic Habits", "James Clear", 320)
book2 = Book("The Alchemist", "Paulo Coelho", 208)

print("BOOKS:")
book1.describe()
book2.describe()



# 2. Product class

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, n):
        self.quantity += n

    def sell(self, n):
        self.quantity -= n


p = Product("Sugar", 80, 10)

print("\nPRODUCT (before):", p.quantity)
p.restock(5)
print("After restock:", p.quantity)
p.sell(3)
print("After sell:", p.quantity)



# 3. Make quantity private + getter

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity  # private

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n

    def sell(self, n):
        self.__quantity -= n


p2 = Product("Oil", 150, 20)

print("\nPRIVATE PRODUCT:")
print("Quantity:", p2.quantity)



# 4. Validate (prevent negative)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        if n > 0:
            self.__quantity += n

    def sell(self, n):
        if n > self.__quantity:
            print(f"Cannot sell {n}. Only {self.__quantity} available.")
        else:
            self.__quantity -= n


p3 = Product("Bread", 10, 5)

print("\nVALIDATION TEST:")
p3.sell(10)  # should refuse
print("Quantity after attempt:", p3.quantity)



# 5. Prove independence

pA = Product("Milk", 50, 10)
pB = Product("Eggs", 15, 30)
pC = Product("Rice", 70, 25)

print("\nBEFORE CHANGE:")
print("Milk:", pA.quantity)
print("Eggs:", pB.quantity)
print("Rice:", pC.quantity)

# Change only one product
pA.sell(5)

print("\nAFTER CHANGING MILK:")
print("Milk:", pA.quantity)
print("Eggs:", pB.quantity)  # unchanged
print("Rice:", pC.quantity)  # unchanged