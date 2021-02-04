class BankAccount():
    def __init__(self, balance, name, number):
        self.balance = balance
        self.name =name
        self.number = number

    def withdraw(self, amout):

        self.balance = self.balance - amout

        return self.balance
    
    def deposit(self, amout):
        self.balance = self.balance + amout
        return self.balance

    def getBalance(self):
        print("잔고는 {0}원 입니다.".format(self.balance))
    
class SavingsAccount(BankAccount):
    def __init__(self, balance, name, number, interest_rate):
        super().__init__(balance,name,number)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        return self.balance

class CheckingAccount(BankAccount):
    def __init__(self, balance, name, number, withdraw_charge):
        super().__init__(balance, name, number)
        self.withdraw_charge = int(withdraw_charge)

    def withdraw(self):
        return self.balance - 1000


a = SavingsAccount(100000, "김원준", 12345, 0.05)
a.add_interest()
print("현재 잔액 : {0}".format(a.balance))