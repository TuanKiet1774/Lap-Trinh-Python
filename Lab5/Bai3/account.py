#Lớp Account dùng để lưu thông tin tài khoản, bao gồm các phương thức để nạp tiền và rút tiền.
class Account:
  def __init__(self, account_id, owner):
    self.account_id = account_id
    self.owner = owner
    self.balance = 0
  
  #Nạp tiền
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      return True
    return False
  
  #Rút tiền
  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      return True
    return False

  def __str__(self):
    return f"Account[Acc_ID: {self.account_id}, Owner: {self.owner}, Balance: {self.balance}]"