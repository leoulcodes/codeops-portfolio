
# day07/bank_registry.py



# Account Class


class Account:

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

        # Stack for transaction history
        self.history = []


    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit")
            return

        self.balance += amount

        # Push transaction record
        self.history.append({
            "type": "deposit",
            "amount": amount
        })

        print(f"Deposited {amount}")


    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal")
            return

        if amount > self.balance:
            print("Insufficient balance")
            return

        self.balance -= amount

        # Push transaction record
        self.history.append({
            "type": "withdraw",
            "amount": amount
        })

        print(f"Withdrew {amount}")


    def undo_last(self):

        if not self.history:
            print("No transactions to undo")
            return


        # Remove latest transaction
        transaction = self.history.pop()


        if transaction["type"] == "deposit":

            # Reverse deposit
            self.balance -= transaction["amount"]

            print(
                f"Undid deposit of {transaction['amount']}"
            )


        elif transaction["type"] == "withdraw":

            # Reverse withdrawal
            self.balance += transaction["amount"]

            print(
                f"Undid withdrawal of {transaction['amount']}"
            )



    def __str__(self):
        return (
            f"{self.account_number} - "
            f"{self.owner} - "
            f"Balance: {self.balance}"
        )



# =====================================================
# Account Registry
# =====================================================

class AccountRegistry:

    def __init__(self):

        # Dictionary for O(1) lookup
        self.accounts = {}

        # List for insertion order
        self.account_order = []



    def add(self, account):

        self.accounts[
            account.account_number
        ] = account

        self.account_order.append(account)



    def find(self, number):

        # O(1) dictionary lookup
        return self.accounts.get(number)



    def list_all(self):

        # Returns insertion order
        return self.account_order



# =====================================================
# Testing
# =====================================================

if __name__ == "__main__":


    registry = AccountRegistry()


    # Create accounts

    acc1 = Account(
        "Abebe",
        "A001",
        1000
    )


    acc2 = Account(
        "Sara",
        "A002",
        2000
    )


    acc3 = Account(
        "Miki",
        "A003",
        500
    )


    # Add accounts

    registry.add(acc1)
    registry.add(acc2)
    registry.add(acc3)



    print("\n--- Find Account ---")

    account = registry.find("A002")

    print(account)



    print("\n--- All Accounts ---")

    for acc in registry.list_all():
        print(acc)



    print("\n--- Transactions ---")

    acc1.deposit(500)
    acc1.withdraw(200)
    acc1.deposit(300)


    print(
        "Current balance:",
        acc1.balance
    )


    print("\n--- Undo Last ---")

    acc1.undo_last()

    print(
        "Balance after undo:",
        acc1.balance
    )


    print("\n--- Undo Again ---")

    acc1.undo_last()

    print(
        "Balance after undo:",
        acc1.balance
    )