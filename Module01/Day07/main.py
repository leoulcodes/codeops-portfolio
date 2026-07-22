
# day07/bank.py


# Account Class


class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

        # Transaction history stack
        self.history = []


    @property
    def balance(self):
        return self.__balance


    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit")
            return

        self.__balance += amount

        # Push transaction to stack
        self.history.append({
            "type": "deposit",
            "amount": amount
        })

        print(f"Deposited {amount}")


    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal")
            return

        if amount > self.__balance:
            print("Insufficient balance")
            return

        self.__balance -= amount

        # Push transaction to stack
        self.history.append({
            "type": "withdraw",
            "amount": amount
        })

        print(f"Withdrew {amount}")


    def undo_last(self):

        if not self.history:
            print("No transaction history")
            return


        # Remove latest transaction
        transaction = self.history.pop()


        if transaction["type"] == "deposit":

            self.__balance -= transaction["amount"]

            print(
                f"Undo deposit: {transaction['amount']}"
            )


        elif transaction["type"] == "withdraw":

            self.__balance += transaction["amount"]

            print(
                f"Undo withdrawal: {transaction['amount']}"
            )


    def __str__(self):

        return (
            f"{self.account_number} | "
            f"{self.owner} | "
            f"Balance: {self.balance}"
        )




# Account Registry


class AccountRegistry:

    def __init__(self):

        # Dictionary for O(1) lookup
        self.accounts = {}

        # List keeps insertion order
        self.account_list = []


    def add(self, account):

        self.accounts[
            account.account_number
        ] = account

        self.account_list.append(account)



    def find(self, number):

        # O(1) average lookup
        return self.accounts.get(number)



    def list_all(self):

        return self.account_list



# =====================================================
# Testing
# =====================================================

if __name__ == "__main__":


    registry = AccountRegistry()


    # Create accounts

    acc1 = Account(
        "Abebe",
        "ACC001",
        1000
    )


    acc2 = Account(
        "Sara",
        "ACC002",
        2000
    )


    # Add accounts to registry

    registry.add(acc1)
    registry.add(acc2)



    print("\n--- Find Account ---")

    print(
        registry.find("ACC001")
    )



    print("\n--- All Accounts ---")

    for account in registry.list_all():
        print(account)



    print("\n--- Transactions ---")

    acc1.deposit(500)

    acc1.withdraw(200)

    acc1.deposit(300)


    print(
        "Balance:",
        acc1.balance
    )



    print("\n--- Undo Last Transaction ---")

    acc1.undo_last()

    print(
        "Balance:",
        acc1.balance
    )



    print("\n--- Undo Again ---")

    acc1.undo_last()

    print(
        "Balance:",
        acc1.balance
    )