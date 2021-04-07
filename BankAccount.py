class BankAccount:
    def __init__(self, account_balance=0, intrestRate=.01):
        # self.name = name
        self.account_balance = account_balance
        self.intrestRate = intrestRate

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.account_balance}")

    def yield_intrest(self):
        self.account_balance += self.intrestRate * self.account_balance
        return self


account1 = BankAccount()

account2 = BankAccount(500, .24)

account1.make_deposit(250).make_deposit(500).make_withdrawl(
    50).yield_intrest().display_account_info()

account2.make_deposit(1000).make_deposit(4000).make_withdrawl(250).make_withdrawl(
    750).make_withdrawl(1000).make_withdrawl(1000).yield_intrest().display_account_info()
