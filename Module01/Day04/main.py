
class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance   # private attribute

    # Read-only property
    @property
    def balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount <= 0:
            print(" Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f" Deposited {amount}. New balance: {self.__balance}")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print(" Insufficient funds.")
            return
        self.__balance -= amount
        print(f" Withdrew {amount}. New balance: {self.__balance}")



#Testing with two accounts
# Create accounts
acc1 = Account("Abebe Birhanu", "AB123")
acc2 = Account("Sara Mekonnen", "SM456", 500)

# Transactions
acc1.deposit(1000)
acc1.withdraw(200)
acc1.withdraw(2000)   # overdraft test

acc2.deposit(-50)     # invalid deposit
acc2.withdraw(100)

# Check balances
print(f"{acc1.owner} Balance:", acc1.balance)
print(f"{acc2.owner} Balance:", acc2.balance)