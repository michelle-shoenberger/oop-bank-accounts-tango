from account import Account


class CheckingAccount(Account):

    def __init__(self, id, date, balance=0, owner=None) -> None:
        super().__init__(id, date, balance, owner)
        self.number = 0

    def withdraw(self, amount):
        if amount + 1 > self._balance:
            raise Exception("Insufficient funds")
            return self._balance
        self._balance -= amount + 1
        return self._balance
    
    def withdraw_using_check(self, amount):
        if amount + 1 > self._balance + 10:
            raise Exception("Insufficient funds")
            return self._balance
        if self.number <= 3:
            self._balance -= amount 
            self.number += 1
        else:
            self._balance -= amount + 2
        return self._balance

    def reset_checks(self):
        self.number = 0
        