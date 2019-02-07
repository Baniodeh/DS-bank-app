from .account import Account
from .transaction import Transaction

class Bank:

    def __init__(self, name):
        self.name= name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account):
            assert type(account) == Account, 'Account should be an app.Account'
            assert account.number not in self.accounts, 'Account number 1 already taken!'
            self.accounts[account.number] = account
            return account

    def add_transaction(self, *, sender, recipient, subject, amount):
         assert sender.number in self.accounts, 'Sender has no account yet!'
         assert recipient.number in self.accounts, 'Recipient has no account yet!'
         assert amount > 0, 'Amount needs to be greater than 0'
         transaction = Transaction(sender=sender.number, recipient=recipient.number, subject=subject, amount=amount)
         self.transactions.append(transaction)
         return transaction
