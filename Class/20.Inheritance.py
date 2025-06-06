class Account:
    #Class attribute
    interest = 0.02
    def __init__(self,account_holder):
        #Instance attribute
        self.balance = 0
        self.holder = account_holder
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance   #return None 
    
    def withdraw(self,amount):
        if amount>self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
    
class Bank:
    """A bank *has* accounts
    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    """
    def __init__(self):
        self.accounts = []
    def open_account(self, holder, amount, kind = Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account 
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

class SavingsAccount(Account):
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self,amount - self.deposit_fee)

#Multiple Inheritance
class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1