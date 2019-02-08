# bank account class
class Account:
    def __init__(self, *, number, firstname, lastname, balance=0.0):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.balance = balance
        assert type(number) == int, 'Number needs to be an integer'
        assert type(balance) == float, 'Balance needs to be a float'

    # def has_funds_for(self):

    def info(self):
        return f'Number {self.number}: {self.firstname} {self.lastname} - {self.balance} €'

    def has_funds_for(self, amount):
        return self.balance >= amount

    def add_to_balance(self, amount):
        assert amount > 0, 'Amount needs to be greater than 0'
        self.balance += amount

    def subtract_from_balance(self, amount):
            assert amount < self.balance, 'Account has not enough funds'
            self.balance -= amount

    def get__balance(self):
        """Check the balance"""
        return self.balance
