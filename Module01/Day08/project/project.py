
# day08/bank_registry.py



# Account Class (unchanged + history)


class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance
        self.history = []   # stack


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




# Account Registry


class AccountRegistry:

    def __init__(self):
        self.accounts = {}        # O(1)
        self.account_list = []    # insertion order


    def add(self, account):
        self.accounts[account.account_number] = account
        self.account_list.append(account)


    
    # 1. Leaderboard
    
    def top_by_balance(self, n):

        return sorted(
            self.account_list,
            key=lambda a: a.balance,
            reverse=True
        )[:n]


    
    # Binary Search (no "in", no loops for search)
    
    def _binary_search(self, numbers, target, left, right):

        if left > right:
            return -1

        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            return self._binary_search(
                numbers,
                target,
                mid + 1,
                right
            )

        else:
            return self._binary_search(
                numbers,
                target,
                left,
                mid - 1
            )


    # -------------------------------------------------
    # 2. Find using Binary Search
    # -------------------------------------------------
    def find_by_number(self, number):

        # Step 1: sort account numbers
        numbers = sorted(self.accounts.keys())

        # Step 2: binary search
        index = self._binary_search(
            numbers,
            number,
            0,
            len(numbers) - 1
        )

        if index == -1:
            return None

        return self.accounts[numbers[index]]


    # -------------------------------------------------
    # Recursive transaction sum
    # -------------------------------------------------
    def _sum_history(self, history):

        if not history:
            return 0

        first = history[0]["amount"]

        return first + self._sum_history(history[1:])


    # -------------------------------------------------
    # 3. Recursive total transactions
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
    acc1 = Account("Abebe", "A003", 1000)
    acc2 = Account("Sara", "A001", 3000)
    acc3 = Account("Miki", "A002", 2000)

    # Add accounts
    registry.add(acc1)
    registry.add(acc2)
    registry.add(acc3)


    # Transactions
    acc1.deposit(500)
    acc1.withdraw(200)

    acc2.deposit(1000)

    acc3.withdraw(300)


    print("\n--- Top by Balance ---")

    for acc in registry.top_by_balance(2):
        print(acc)


    print("\n--- Binary Search Find ---")

    print(registry.find_by_number("A002"))
    print(registry.find_by_number("A999"))


    print("\n--- Total Transactions (Recursive) ---")

    print("A003 total:", registry.total_transactions("A003"))
    print("A001 total:", registry.total_transactions("A001"))