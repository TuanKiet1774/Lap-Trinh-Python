#Lớp Transaction là các giao dịch 
from account import *
class Transaction:
  def __init__(self, transaction_id, account, type, amount):
    self.transaction_id = transaction_id
    self.account = account
    self.type = type
    self.amount = amount
    
  def execute(self):
    if self.type == "deposit":
      return self.account.deposit(self.amount)
    elif self.type == "withdraw":
      return self.account.withdraw(self.amount)
    return False
  
  def __str__(self):
    return f"Transaction[Tra_ID: {self.transaction_id}, Owner: {self.account.owner}, Type: {self.type}, Amount: {self.amount}]"


