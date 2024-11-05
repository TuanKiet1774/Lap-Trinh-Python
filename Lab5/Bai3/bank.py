from account import Account

#Lớp Bank để quản lý các tài khoản và giao dịch
class Bank:
  def __init__(self):
    self.accounts = []
    self.transactions = []
  #Tạo tài khoản
  def create_account(self, owner):
    account_id = len(self.accounts) + 1
    account = Account(account_id, owner)
    self.accounts.append(account)
    return account
  
  def get_account(self, account_id):
    for account in self.accounts:
      if account.account_id == account_id:
        return account
    return None
  
  def process_transaction(self, transaction):
    if transaction.execute():
      self.transactions.append(transaction)
      return True
    return False
  
  def list_accounts(self):
    for account in self.accounts:
      print(account)
  
  def list_transactions(self):
    for transaction in self.transactions:
      print(transaction)