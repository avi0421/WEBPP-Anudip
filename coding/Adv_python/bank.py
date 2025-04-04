class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account balance is ${self.balance}.")

# Creating a bank account
account = BankAccount("123456789", "John Doe", 500)

# Performing transactions
account.check_balance()  # Check initial balance
account.deposit(200)     # Deposit $200
account.withdraw(100)    # Withdraw $100
account.check_balance()  # Check final balance
