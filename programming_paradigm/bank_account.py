class BankAccount:
    def __init__(self, account_balance=0):
        # Initialize the account balance
        self.account_balance = account_balance

    def deposit(self, amount):
        # Add the deposit amount to the account balance
        self.account_balance += amount

    def withdraw(self, amount):
        # Check if there's enough balance for the withdrawal
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Return the current balance
        return f"Current Balance: {self.account_balance}"