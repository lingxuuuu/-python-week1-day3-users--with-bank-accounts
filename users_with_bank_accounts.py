class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = 0.01
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print('Insufficient funds: Charging a $5 fee')
        self.balance -= 5
        return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1+self.int_rate)
        return self

class User:
    def __init__(self, name_parameter, email_parameter):
        self.name = name_parameter
        self.email = email_parameter
        self.account = BankAccount(int_rate=0.02, balance=0)   

    def make_deposit(self, amount):
        self.account.deposit += amount

    def make_withdrawal(self, amount):
        self.account.withdraw -= amount

    def display_user_balance(self):
        print(f" User: {self.name}, Balance: ${self.account.display_account_info}")

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account_balance += amount
    
checking = BankAccount(0.01, 500)
saving = BankAccount(0.05, 10000)

