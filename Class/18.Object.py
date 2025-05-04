#Class
class Account:
    def __init__(self,account_holder):
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
    
a= Account('Carl')
b= Account('Leo')
a.backup=b
"""
>>> getattr(a,'balance')  
0
>>> hasattr(a,'balance')
True
"""
