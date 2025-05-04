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

tom_account = Account('Tom')
# Instance attribute assignment:
tom_account.interest = 0.08
# Class attribute assignment:
Account.interest = 0.05
jim_account = Account('Jim')
"""
>>> tom_account.interest
0.08  
>>> jim_account.interest
0.05
"""
m = map(jim_account.deposit,range(10,20))
#Bound method = Object + Function
"""
>>> type(Account.deposit)
<class 'function'>
>>> type(jim_account.deposit)  
<class 'method'>
>>> Account.deposit(jim_account,1003)
1003
>>> jim_account.deposit(1022)
2025
"""