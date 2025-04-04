class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful! New balance: {self.balance}"
        return "Deposit amount must be greater than zero."
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        if amount > 0:
            self.balance -= amount
            return f"Withdrawal successful! New balance: {self.balance}"
        return "Withdrawal amount must be greater than zero."
    def get_balance(self):
        return f"Account Balance: {self.balance}"
# Creating an object of BankAccount class
account = BankAccount("123456789", "John Doe", 1000)
# Using the banking application
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
