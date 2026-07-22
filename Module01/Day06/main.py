
from abc import ABC, abstractmethod
from typing import List


# OBSERVER PATTERN (Steps 2 & 4: SRP Alert Service / Observer Interface)


class AlertObserver(ABC):
    """Abstract Observer class for handling account activity notifications."""
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class SMSAlertService(AlertObserver):
    """Concrete Observer providing SMS notifications (SRP: Handles ONLY alerts)."""
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def update(self, message: str) -> None:
        print(f"📱 [SMS to {self.phone_number}]: {message}")


# =====================================================================
# CORE ACCOUNT FAMILY (Day 5 foundation with Observer integration)


class Account:
    def __init__(self, owner: str, account_number: str, initial_balance: float = 0.0):
        self.owner = owner
        self.account_number = account_number
        self._balance = float(initial_balance) if initial_balance >= 0 else 0.0
        self._observers: List[AlertObserver] = []  # Step 4: Storage for observers

    @property
    def balance(self) -> float:
        return self._balance

    # Step 4: Observer management methods
    def subscribe(self, observer: AlertObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def _notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print(" Deposit must be positive.")
            return
        self._balance += amount
        # Alert trigger
        self._notify(f"Deposit of {amount:,.2f} ETB successful. Current balance: {self._balance:,.2f} ETB.")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print(" Withdrawal must be positive.")
            return
        if amount > self._balance:
            print(" Rejection: Insufficient funds.")
            return
        self._balance -= amount
        # Alert trigger
        self._notify(f"Withdrawal of {amount:,.2f} ETB successful. Current balance: {self._balance:,.2f} ETB.")

    def statement(self) -> str:
        return f"[Standard Account] Owner: {self.owner} | No: {self.account_number} | Balance: {self._balance:,.2f}"


class SavingsAccount(Account):
    def __init__(self, owner: str, account_number: str, initial_balance: float, interest_rate: float):
        super().__init__(owner, account_number, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self) -> None:
        interest = self._balance * self.interest_rate
        self._balance += interest
        self._notify(f"Interest of {interest:,.2f} ETB applied. Current balance: {self._balance:,.2f} ETB.")

    def statement(self) -> str:
        return f"[Savings Account]  Owner: {self.owner} | No: {self.account_number} | Balance: {self._balance:,.2f} | Rate: {self.interest_rate * 100}%"


class CurrentAccount(Account):
    def __init__(self, owner: str, account_number: str, initial_balance: float, overdraft_limit: float):
        super().__init__(owner, account_number, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print(" Withdrawal must be positive.")
            return
        if amount > (self._balance + self.overdraft_limit):
            print(f" Rejection: Overdraft limit exceeded.")
            return
        self._balance -= amount
        self._notify(f"Withdrawal of {amount:,.2f} ETB successful (Overdraft used if balance negative). Current balance: {self._balance:,.2f} ETB.")

    def statement(self) -> str:
        return f"[Current Account]  Owner: {self.owner} | No: {self.account_number} | Balance: {self._balance:,.2f} | Overdraft Limit: {self.overdraft_limit:,.2f}"



# FACTORY PATTERN (Step 3: AccountFactory)


class AccountFactory:
    """Factory class handles object creation logic dynamically based on input."""
    @staticmethod
    def create(kind: str, owner: str, account_number: str, initial_balance: float, **kwargs) -> Account:
        kind = kind.lower().strip()
        
        if kind == "savings":
            # Safely fetch savings-specific arguments with defaults
            interest_rate = kwargs.get("interest_rate", 0.05)
            return SavingsAccount(owner, account_number, initial_balance, interest_rate)
            
        elif kind == "current":
            # Safely fetch current-specific arguments with defaults
            overdraft_limit = kwargs.get("overdraft_limit", 1000.0)
            return CurrentAccount(owner, account_number, initial_balance, overdraft_limit)
            
        else:
            raise ValueError(f"Unknown account type requested: '{kind}'. Choose 'savings' or 'current'.")


# =====================================================================
# SIMULATION WORKFLOW (Step 5: Factory, Attach Alert, Run Workflow)
# =====================================================================

if __name__ == "__main__":
    print("--- Step 3 & 5: Instantiating via AccountFactory ---")
    
    # 1. Open accounts via the factory interface
    sav_acc = AccountFactory.create(
        kind="savings", 
        owner="Aster Chala", 
        account_number="SV-2002", 
        initial_balance=5000.0, 
        interest_rate=0.07
    )
    
    curr_acc = AccountFactory.create(
        kind="current", 
        owner="Dawit Alamu", 
        account_number="CR-3003", 
        initial_balance=500.0, 
        overdraft_limit=1500.0
    )

    print(sav_acc.statement())
    print(curr_acc.statement())

    print("\n--- Step 4 & 5: Attaching Observers ---")
    # 2. Wire up the independent SMS alert observers to the accounts
    aster_sms = SMSAlertService(phone_number="+251-911-111111")
    dawit_sms = SMSAlertService(phone_number="+251-922-222222")
    
    sav_acc.subscribe(aster_sms)
    curr_acc.subscribe(dawit_sms)

    print("\n--- Triggering Operations & Firing Automated Alerts ---")
    # 3. Perform actions to see the alert mechanics dispatch automatically
    sav_acc.deposit(2500.0)
    sav_acc.add_interest()
    
    print()
    curr_acc.withdraw(1200.0)  # Utilizes authorized overdraft buffer safely