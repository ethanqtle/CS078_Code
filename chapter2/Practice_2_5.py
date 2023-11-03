print("\nSection 2.5.2")

class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

a = Account('Kirk')
print("a.balance\n #", a.balance)

print("a.holder\n # ", a.holder)

b = Account('Spock')
b.balance = 200
print("[acc.balance for acc in (a, b)]\n #", [acc.balance for acc in (a, b)])

print("a is a\n #", a is a)

print("a is not b\n #", a is not b)

c = a
print("c is a\n #", c is a)

class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

spock_account = Account('Spock')
print("spock_account.deposit(100)\n #", spock_account.deposit(100))
print("spock_account.withdraw(90)\n #", spock_account.withdraw(90))
print("spock_account.withdraw(90)\n #", spock_account.withdraw(90))
print("spock_account.holder\n #", spock_account.holder)

print("\nSection 2.5.3:")
print("getattr(spock_account, 'balance')\n # ", getattr(spock_account, 'balance'))
print("hasattr(spock_account, 'deposit')\n # ", hasattr(spock_account, 'deposit'))


print("type(Account.deposit)\n #", type(Account.deposit))
print("type(spock_account.deposit)\n #", type(spock_account.deposit))

print("Account.deposit(spock_account, 1001)\n #", Account.deposit(spock_account, 1001))
print("spock_account.deposit(1000)\n #", spock_account.deposit(1000))

print("\nSection 2.5.4:")
class Account:
    interest = 0.02 # A class attribute
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

spock_account = Account('Spock')
kirk_account = Account('Kirk')
print("spock_account.interest\n #", spock_account.interest)
print("kirk_account.interest\n #", kirk_account.interest)
Account.interest = 0.04
print("Account.interest = 0.04")
print("spock_account.interest\n #", spock_account.interest)
print("kirk_account.interest\n #", kirk_account.interest)

kirk_account.interest = 0.08
print("kirk_account.interest = 0.08")
print("spock_account.interest\n #", spock_account.interest)

Account.interest = 0.05
print("spock_account.interest\n #", spock_account.interest)
print("kirk_account.interest\n #", kirk_account.interest)

print("\nSection 2.5.5:")

print("\nSection 2.5.6:")
class Account:
    """A bank account that has a non-negative balance."""
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    
    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)

checking = CheckingAccount('Sam')
print("checking.deposit(10)\n #", checking.deposit(10))
print("checking.withdraw(5)\n #", checking.withdraw(5))
print("checking.interest\n #", checking.interest)

# working code for all accounts that inherit from Account
def deposit_all(winners, amount=5):
    for account in winners:
        account.deposit(amount)

# bad code that only works with Account objects
# def deposit_all(winners, amount=5):
#     for account in winners:
#         Account.deposit(account, amount)

print("\nSection 2.5.7:")
class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1           # A free dollar!

such_a_deal = AsSeenOnTVAccount("John")
print("such_a_deal.balance\n #", such_a_deal.balance)
print("such_a_deal.deposit(20)\n #", such_a_deal.deposit(20))
print("such_a_deal.withdraw(5)\n #", such_a_deal.withdraw(5))
print("such_a_deal.deposit_charge\n #", such_a_deal.deposit_charge)
print("such_a_deal.withdraw_charge\n #", such_a_deal.withdraw_charge)

print([c.__name__ for c in AsSeenOnTVAccount.mro()])
