# Encapsulation is the practice of hiding implementation details and
# restricting direct access to object attributes. In Python, it's implemented using:
# Public attributes (name)
# Protected attributes (_name)
# Private attributes (__name)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (using __ to indicate private)

    def deposit(self, amount):
        self.__balance += amount  # Modify the private balance attribute

    def get_balance(self):
        return self.__balance  # Access the private balance attribute

# Creating an object of BankAccount class
account = BankAccount(100)

# Depositing money into the account
account.deposit(50)

# Getting the updated balance
print(account.get_balance())  # Output: 150
