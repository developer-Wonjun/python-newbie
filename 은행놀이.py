class bank:
    def __init__(self, balance = 0):
        self.balance = balance
    
    def money(self):
        return self.balance
    
    def withdraw(self, plus):
        self.balance +=plus
        return self.balance
    
    def deposit(self, minus):
        self.balance -= minus
        return self.balance

a = bank(2000)

print("현재 금액은 {0}입니다.".format(a.money()))
print("5000원 입금하셔서 현재 잔액은 {0}입니다.".format(a.withdraw(5000)))
print("3000원 출금하셔서 현재 잔액은 {0}입니다.".format(a.deposit(3000)))
