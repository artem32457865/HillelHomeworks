
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            return "Некоректна сума"
        if amount > self.balance:
            return "Недостатньо коштів"
        
        self.balance -= amount
        return "Гроші знято"



account = BankAccount(1000)


assert account.withdraw(300) == "Гроші знято"
assert account.balance == 700


assert account.withdraw(1000) == "Недостатньо коштів"
assert account.balance == 700


assert account.withdraw(-100) == "Некоректна сума"
assert account.balance == 700

print("Усі тести пройдено!")

