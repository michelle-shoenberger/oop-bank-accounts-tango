from owner import Owner
import os, csv

class Account:

    def __init__(self, id, date, balance=0, owner=None) -> None:
        self._id = id
        if int(balance) < 0:
            raise Exception("Invalid balance")
        else:
            self._balance = int(balance)
        self.owner = owner
        self.opendate = date

    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return self
        else:
            raise ValueError("Insufficient funds")
    
    def deposit(self, amount):
        self._balance += amount
        return self
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        check = input(f"Confirm reset balance to {amount}: [y/n] ")
        if check =='y':
            self._balance = amount
        
    def __str__(self) -> str:
        return f"Account # {self._id}: ${self._balance}."

    def update_owner(self, owner):
        self.owner = owner

    @classmethod
    def all_accounts(cls):
        # get owners
        owners = Owner.all_owners()
        # Owner - accounts
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "./support/account_owners.csv")
        acc_dict = {}
        with open(path) as ownerfile:
            reader = csv.reader(ownerfile)
            for row in reader:
                acc_dict[row[0]] = row[1]

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "./support/accounts.csv")
        lst = []
        with open(path) as csvfile:
            header = ['id', 'balance', 'date']
            reader = csv.DictReader(csvfile, fieldnames=header)
            for row in reader:
                if row['id'] in acc_dict:
                    row['owner'] = acc_dict[row['id']]
                lst.append(Account(**row))
        return lst

    @classmethod
    def find(cls, id):
        for account in Account.all_accounts():
            if account._id == id:
                return account