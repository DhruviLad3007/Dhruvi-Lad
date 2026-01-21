class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):
    def account_type(self):
        print("Savings Account Balance:", self.balance)

class CurrentAccount(BankAccount):
    def account_type(self):
        print("Current Account Balance:", self.balance)

s = SavingsAccount(5000)
c = CurrentAccount(10000)

s.account_type()
c.account_type()
