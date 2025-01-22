# Bank Account Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient balance")

# Create a bank account object
account = BankAccount(1000)

# Perform operations
account.deposit(500)   # Output: Deposited 500, New Balance: 1500
account.withdraw(200)  # Output: Withdrew 200, New Balance: 1300
account.withdraw(1500) # Output: Insufficient balance
