# Base work
class Convertor:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        self.amount = amount
        return self.balance - self.amount
    def deposit(self, amount):
        self.amount = amount
        return self.balance - self.amount
v = Convertor(100)
v.balance(200)
print(v.withdraw(2))
