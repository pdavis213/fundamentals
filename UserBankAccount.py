class User:

    def __init__(self, name, email_address, account):
        self.name = name
        self.email = email_address
        self.account = BankAccount(intrestRate=0.02, account_balance=0)

#     def addToUserList():


# class UserCatalog:

#     def __init__(self):
#         self.userList = {}


class BankAccount:

    def __init__(self, intrestRate=0.02, account_balance=0, ):
        # self.name = name
        self.account_balance = account_balance
        self.intrestRate = intrestRate

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def tranfer_money(self, name, amount):
        self.account_balance -= amount
        name.account_balance += amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.account_balance}")
        return self

    def yield_intrest(self):
        self.account_balance += self.intrestRate * self.account_balance
        return self


micha = User("Micha", "m@internet.com", BankAccount())
austin = User

micha.account.make_deposit(500).make_withdrawl(
    50).yield_intrest().display_account_info()
