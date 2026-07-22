
# bank.py


# Singleton Pattern: BankConfig


class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Shared bank settings
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000

        return cls._instance



# Observer Pattern


class SMSAlert:
    def update(self, account, message):
        print(f"SMS Alert ({account.owner}): {message}")


class AuditLog:
    def update(self, account, message):
        print(f"Audit Log: {account.account_number} - {message}")



# Base Account Class
# SRP: Only handles balance operations


class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

        # Observers list
        self.observers = []


    @property
    def balance(self):
        return self.__balance


    def subscribe(self, observer):
        self.observers.append(observer)


    def _notify(self, message):
        for observer in self.observers:
            observer.update(self, message)


    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount")
            return

        self.__balance += amount

        self._notify(
            f"Deposited {amount}. Balance: {self.balance}"
        )


    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount")
            return

        if amount > self.__balance:
            print("Insufficient balance")
            return

        self.__balance -= amount

        self._notify(
            f"Withdrew {amount}. Balance: {self.balance}"
        )


    def statement(self):
        return f"Account {self.account_number}: {self.balance}"


# =====================================================
# Savings Account
# =====================================================

class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)

        self.config = BankConfig()


    def add_interest(self):

        interest = self.balance * self.config.interest_rate

        self.deposit(interest)

        self._notify(
            f"Interest added: {interest}"
        )


    def statement(self):
        return (
            f"Savings Account | "
            f"Owner: {self.owner}, "
            f"Balance: {self.balance}"
        )



# Current Account


class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)

        self.config = BankConfig()


    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal")
            return


        allowed = self.balance + self.config.overdraft_limit


        if amount > allowed:
            print("Overdraft limit exceeded")
            return


        self._Account__balance -= amount


        self._notify(
            f"Withdrew {amount}. Balance: {self.balance}"
        )


    def statement(self):
        return (
            f"Current Account | "
            f"Owner: {self.owner}, "
            f"Balance: {self.balance}"
        )



# Factory Pattern


class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind.lower() == "savings":
            return SavingsAccount(
                owner,
                number,
                balance
            )


        elif kind.lower() == "current":
            return CurrentAccount(
                owner,
                number,
                balance
            )


        else:
            raise ValueError("Unknown account type")



# Testing


if __name__ == "__main__":


    # Create accounts using Factory

    accounts = [
        AccountFactory.create(
            "savings",
            "Abebe",
            "S001",
            5000
        ),

        AccountFactory.create(
            "current",
            "Sara",
            "C001",
            1000
        )
    ]


    # Create observers

    sms = SMSAlert()
    audit = AuditLog()


    # Subscribe observers

    for account in accounts:
        account.subscribe(sms)
        account.subscribe(audit)


    print("\n--- Transactions ---")


    # Savings transactions

    savings = accounts[0]

    savings.deposit(1000)
    savings.add_interest()


    # Current transactions

    current = accounts[1]

    current.withdraw(1500)


    print("\n--- Statements ---")


    # Polymorphic loop

    for account in accounts:
        print(account.statement())


    print("\n--- Singleton Test ---")

    config1 = BankConfig()
    config2 = BankConfig()

    print(config1.interest_rate)
    print(config1 is config2)