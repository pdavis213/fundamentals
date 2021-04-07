class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

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


michah = User("Michah", "michah@internet.com")
harleigh = User("Harleigh", "Sherbert@internet.com")
austin = User("Austin", "3ustin@internet.com")

michah.make_deposit(1000).make_deposit(
    45).make_deposit(4569).make_withdrawl(3000)
print(michah.account_balance)

harleigh.make_deposit(90000000).make_deposit(
    42).make_withdrawl(36784).make_withdrawl(999)
print(harleigh.account_balance)

austin.make_deposit(15000).make_withdrawl(
    875).make_withdrawl(800).make_withdrawl(850)
print(austin.account_balance)

michah.make_deposit(1000).tranfer_money(harleigh, 50)
print(michah.account_balance)
print(harleigh.account_balance)
