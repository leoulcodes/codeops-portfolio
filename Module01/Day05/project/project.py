
# day06/practice.py

class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    # Read-only balance
    @property
    def balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount <= 0:
            print(" Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"Deposited {amount}")

    # Normal withdrawal
    def withdraw(self, amount):
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
            return

        if amount > self.__balance:
            print("❌ Insufficient funds.")
            return

        self.__balance -= amount
        print(f"Withdrew {amount}")

    def statement(self):
        return f"Account: {self.owner}, Balance: {self.balance}"


# SavingsAccount inherits from Account
class SavingsAccount(Account):
    def __init__(self, owner, account_number, balance=0, rate=0.05):
        super().__init__(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)   # reuse parent deposit method
        print(f"Interest added: {interest}")

    # Override statement()
    def statement(self):
        return f"Savings Account | Owner: {self.owner}, Balance: {self.balance}"


# CurrentAccount inherits from Account
class CurrentAccount(Account):
    def __init__(self, owner, account_number, balance=0, overdraft_limit=1000):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit

    # Override withdraw()
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return

        if amount > self.balance + self.overdraft_limit:
            print("❌ Overdraft limit exceeded.")
            return

        # Directly update private balance is not allowed,
        # so use parent withdrawal when possible
        if amount <= self.balance:
            super().withdraw(amount)
        else:
            overdraft_amount = self.balance - amount
            self._Account__balance = overdraft_amount
            print(f"Withdrew {amount} using overdraft")

    # Override statement()
    def statement(self):
        return f"Current Account | Owner: {self.owner}, Balance: {self.balance}"


# Polymorphic loop
if __name__ == "__main__":

    accounts = [
        Account("Abebe", "A001", 1000),
        SavingsAccount("Sara", "S001", 2000, 0.05),
        CurrentAccount("Miki", "C001", 500, 1000)
    ]

    # Add interest to savings account
    accounts[1].add_interest()

    # Transactions
    accounts[0].withdraw(200)
    accounts[1].withdraw(300)
    accounts[2].withdraw(1200)   # allowed because of overdraft

    print("\n--- Account Statements ---")

    # Polymorphism
    for account in accounts:
        print(account.statement())