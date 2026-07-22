
# day08/registry.py


# =====================================================
# Account (with transaction history stack)
# =====================================================

class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance
        self.history = []   # stack (list)


    @property
    def balance(self):
        return self.__balance


    def deposit(self, amount):
        if amount <= 0:
            return

        self.__balance += amount

        self.history.append({
            "type": "deposit",
            "amount": amount
        })


    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            return

        self.__balance -= amount

        self.history.append({
            "type": "withdraw",
            "amount": amount
        })


    def __str__(self):
        return f"{self.account_number} | {self.owner} | {self.balance}"


# =====================================================
# AccountRegistry
# =====================================================

class AccountRegistry:

    def __init__(self):
        self.accounts = {}        # O(1) lookup
        self.account_list = []    # insertion order


    def add(self, account):
        self.accounts[account.account_number] = account
        self.account_list.append(account)


    # -------------------------------------------------
    # 1. Leaderboard (Top N balances)
    # -------------------------------------------------
    def top_by_balance(self, n):
        return sorted(
            self.account_list,
            key=lambda acc: acc.balance,
            reverse=True
        )[:n]


    # -------------------------------------------------
    # Binary Search (recursive)
    # -------------------------------------------------
    def _binary_search(self, arr, target, left, right):

        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            return self._binary_search(arr, target, mid + 1, right)

        else:
            return self._binary_search(arr, target, left, mid - 1)


    # -------------------------------------------------
    # 2. Find by account number using binary search
    # -------------------------------------------------
    def find_by_number(self, number):

        sorted_numbers = sorted(self.accounts.keys())

        index = self._binary_search(
            sorted_numbers,
            number,
            0,
            len(sorted_numbers) - 1
        )

        if index == -1:
            return None

        return self.accounts[sorted_numbers[index]]


    # -------------------------------------------------
    # Recursive sum helper
    # -------------------------------------------------
    def _sum_history(self, history):

        if not history:
            return 0

        return (
            history[0]["amount"] +
            self._sum_history(history[1:])
        )


    # -------------------------------------------------
    # 3. Total transactions (recursive)
    # -------------------------------------------------
    def total_transactions(self, number):

        account = self.accounts.get(number)

        if not account:
            return 0

        return self._sum_history(account.history)


# =====================================================
# Testing
# =====================================================

if __name__ == "__main__":

    registry = AccountRegistry()

    # Create accounts
    a1 = Account("Abebe", "A003", 1000)
    a2 = Account("Sara", "A001", 3000)
    a3 = Account("Miki", "A002", 2000)

    # Add them
    registry.add(a1)
    registry.add(a2)
    registry.add(a3)

    # Transactions
    a1.deposit(500)
    a1.withdraw(200)

    a2.deposit(1000)

    a3.withdraw(300)


    # -------------------------------
    print("\n--- Leaderboard ---")
    for acc in registry.top_by_balance(2):
        print(acc)


    # -------------------------------
    print("\n--- Binary Search ---")
    print(registry.find_by_number("A002"))
    print(registry.find_by_number("A999"))


    # -------------------------------
    print("\n--- Recursive Totals ---")
    print("A003 total:", registry.total_transactions("A003"))
    print("A001 total:", registry.total_transactions("A001"))