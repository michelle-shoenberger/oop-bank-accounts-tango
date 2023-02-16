from account import Account

class Bank:
    def __init__(self):
        self.tracker = 0
        self.accounts = []

    def add_account(self, id, balance):
        try:
            new_account = Account(id, balance)
        except:
            raise Exception("Invalid account")
        self.accounts.append(new_account)
        return new_account

    def interactions(self, id, action, value):
        for account in self.accounts:
            if account._id == id:
                if action == "withdraw":
                    return account.withdraw(value)
                elif action == "deposit":
                    return account.deposit(value)
                else:
                    return "invalid action"


bank = Bank()
print(Account.all_accounts())
