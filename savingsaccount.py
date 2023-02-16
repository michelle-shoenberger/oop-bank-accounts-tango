from account import Account

class ArgumentError(Exception):
    def __init__(self, msg) -> None:
        print(msg)

class SavingsAccount(Account):

    def __init__(self, id, date, balance=0, owner=None) -> None:
        super().__init__(id, date, balance, owner)
        if int(balance) < 10:
            raise ArgumentError('Below minimum amount')
        
    def withdraw(self, amount):
        if amount + 2 > self._balance - 10:
            raise Exception("Insufficient funds")
            return self._balance
        self._balance -= amount + 2
        return self._balance

    def add_interest(self, rate):
        interest = self._balance * rate /100
        self._balance += interest
        return interest