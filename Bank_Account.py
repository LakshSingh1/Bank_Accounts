class BankAccount:
    def __init__(self, interest_rate, initial_balance=0):
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount

    def display_account_info(self):
        print("Balance: $" + str(self.balance))

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate

