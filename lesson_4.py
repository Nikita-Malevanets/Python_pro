class BankAccount:
    __balance = 0

    def __init__(self, initial_amount: float):
        if initial_amount < 0:
            raise ValueError("Initial amount cannot be negative")
        self.__balance = initial_amount

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.__balance += amount
        return self._balance

    def withdraw(self, amount: float):
        if amount > self._balance:
            raise ValueError("Amount cannot be greater than balance")
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self._balance -= amount
        return self._balance

    def get_balance(self) -> float:
        return self._balance


class InsufficientFundsError(Exception):
    def __init__(self, message = 'Not enough funds', balance = 0):
        super().__init__(message)
        self.balance = balance










