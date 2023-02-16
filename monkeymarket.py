from account import Account
from savingsaccount import ArgumentError


class MoneyMarketAccount(Account):

    def __init__(self, id, date, balance=0, owner=None) -> None:
        super().__init__(id, date, balance, owner)
        self.counter = 0
        if int(balance) < 10000:
            raise ArgumentError("Minimum balance is $10,000")
        self.freeze = False
    
    def withdraw(self, amount):
        if self.freeze == False and self.counter <= 6:
            self.counter += 1
            if self._balance - amount < 10000:
                self._balance -= amount + 100
                self.freeze = True
            else:
                self._balance -= amount
        return self._balance

    def deposit(self, amount):
        if self.freeze == True:
            self._balance += amount
            if self._balance >= 10000:
                self.freeze = False
            return self._balance
        if self.counter <= 6:
            self.counter += 1
            self._balance += amount
        return self._balance

    def add_interest(self,rate):
        interest = self._balance * rate /100
        self._balance += interest
        return interest

    def reset_transactions(self):
        self.counter = 0
    
