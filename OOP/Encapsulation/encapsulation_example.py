#create a class Student with:
#__grades (Private list)
#add_grade(grade) — adds a grade if it's between 0 and 100
#average property — returns the average grade
#@average.setter — forbidden (Read-only)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private
    
    # Getter
    @property
    def balance(self):
        return self.__balance
    
    # Setter with validation
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("the balance cannot be negative")
        self.__balance = amount
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit successful. Your balance is: {self.__balance}"
        return "The amount must be positive"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawal successful. Your balance is: {self.__balance}"
        return "Insufficient funds or invalid amount"


# Test
acc = BankAccount("Ahmed", 1000)
print(acc.balance)        # 1000 (getter)
acc.deposit(500)          # 1500
acc.withdraw(200)         # 1300
print(acc.balance)        # 1300 (getter)
acc.__balance -= 200
print(acc.balance)        # 1300 (still unchanged, encapsulation works)

