import time
import datetime


class Transaction:
   def __init__(self, *, sender, recipient, subject, amount, transaction_id, category):
       assert isinstance(sender, int), 'Sender needs to be an integer'
       assert isinstance(recipient, int), 'Recipient needs to be an integer'
       assert isinstance(amount, float), 'Amount needs to be a float'
       assert amount > 0.0, 'Amount needs to be greater than 0'
       assert isinstance(transaction_id, int), 'Transaction_id needs to be an integer'
       self.sender = sender
       self.recipient = recipient
       self.subject = subject
       self.amount = amount
       self.transaction_id = transaction_id
       self.category = category
       self.created_at = time.time()


   def info(self):
       #'From 1 to 2: Test transaction - 10.0 €'
       date = datetime.datetime.fromtimestamp(self.created_at).strftime('%Y-%m-%d %H:%M:%S')
       return f'{date}: From {self.sender} to {self.recipient}: {self.subject} {self.category} {self.transaction_id} - {self.amount} €'
