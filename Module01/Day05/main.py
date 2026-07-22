
class Account:
    def __init__(self, owner: str, account_number: str, initial_balance: float = 0.0):
        self.owner = owner
        self.account_number = account_number
        
        if initial_balance < 0:
            print(f" Warning: Initial balance cannot be negative. Setting to 0.0.")
            self._balance = 0.0  # Using protected attribute so subclasses can access it
        else:
            self._balance = float(initial_balance)

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print(" Deposit must be positive.")
            return
        self._balance += amount
        print(f" Deposited {amount:,.2f}. New Balance: {self._balance:,.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print(" Withdrawal must be positive.")
            return
        if amount > self._balance:
            print(" Rejection: Insufficient funds.")
            return
        self._balance -= amount
        print(f" Withdrew {amount:,.2f}. New Balance: {self._balance:,.2f}")

    def statement(self) -> str:
        """Standard account type label."""
        return f"[Standard Account] Owner: {self.owner} | No: {self.account_number} | Balance: {self._balance:,.2f}"


# --- Step 2: Add SavingsAccount ---
class SavingsAccount(Account):
    def __init__(self, owner: str, account_number: str, initial_balance: float, interest_rate: float):
        super().__init__(owner, account_number, initial_balance)
        self.interest_rate = interest_rate  # e.g., 0.05 for 5%

    def add_interest(self) -> None:
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f" Interest added: +{interest:,.2f} (Rate: {self.interest_rate * 100}%). New Balance: {self._balance:,.2f}")

    # --- Step 4: Override statement() ---
    def statement(self) -> str:
        return f"[Savings Account]  Owner: {self.owner} | No: {self.account_number} | Balance: {self._balance:,.2f} | Rate: {self.interest_rate * 100}%"


# --- Step 3: Add CurrentAccount with Overdraft Allowance ---
class CurrentAccount(Account):
    def __init__(self, owner: str, account_number: str, initial_balance: float, overdraft_limit: float):
        super().__init__(owner, account_number, initial_balance)
        self.overdraft_limit = overdraft_limit  # Positive value representing allowable negative buffer

    # --- Step 3: Override withdraw() ---
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print(" Withdrawal must be positive.")
            return
        
        # Validation checks the available balance PLUS the overdraft limit
        if amount > (self._balance + self.overdraft_limit):
            print(f" Rejection: Overdraft limit exceeded. Requested: {amount} | Maximum allowed: {self._balance + self.overdraft_limit}")
            return
        
        self._balance -= amount
        print(f" Withdrew {amount:,.2f}. New Balance: {self._balance:,.2f}")

    # --- Step 4: Override statement() ---
    def statement(self) -> str:
        return f"[Current Account]  Owner: {self.owner} | No: {self.account_number} | Balance: {self._balance:,.2f} | Overdraft Limit: {self.overdraft_limit:,.2f}"


# --- Step 5: Polymorphic Loop Implementation ---
if __name__ == "__main__":
    print("--- Creating the Account Family ---")
    
    # Mixed list of different account objects
    accounts = [
        Account(owner="Abebe Kebede", account_number="AB-1001", initial_balance=1000.0),
        SavingsAccount(owner="Aster Chala", account_number="SV-2002", initial_balance=5000.0, interest_rate=0.07),
        CurrentAccount(owner="Dawit Alamu", account_number="CR-3003", initial_balance=500.0, overdraft_limit=1000.0)
    ]

    print("\n--- Running Target Actions ---")
    # Demonstrating unique operations safely before the loop
    # aster's savings account earns interest
    accounts[1].add_interest() 
    # dawit's current account uses overdraft safely
    accounts[2].withdraw(1200.0) 

    print("\n--- Step 5: Polymorphic Statement Loop ---")
    # This loop demonstrates polymorphism. It calls statement() on each object 
    # without knowing or caring about its specific subclass.
    for account in accounts:
        print(account.statement())