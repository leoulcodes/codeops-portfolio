
class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance  # private attribute

    # Read-only property
    @property
    def balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"{amount} ETB deposited successfully.")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient funds.")
            return
        self.__balance -= amount
        print(f"{amount} ETB withdrawn successfully.")

    # Account statement
    def statement(self):
        print("\nACCOUNT STATEMENT")
        print("-" * 30)
        print(f"Owner          : {self.owner}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : {self.__balance:.2f} ETB")