#1. Create a class BankAccount
class BankAccount:
    bank_name ="RDB bank ltd"
    def __init__(self,name,type,balance):
        self.name =name
        self.type = type
        self.balance = balance

    def deposit (self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount

a1=BankAccount("shalini",'savings',2000)

a2=BankAccount("agarwal",'current',100)

a1.withdraw(200)
a2.deposit(700)

print(a1.balance,a2.balance)
print(a1.bank_name)

"""/h different account holder, account type, and balance.
9. Withdraw and deposit the 1000, 2000 in the first and second accounts respectively and check whether the balance is updated accordingly."""