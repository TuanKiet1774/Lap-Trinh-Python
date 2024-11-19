from bank import Bank
from transaction import Transaction

# Tạo ngân hàng và tài khoản
bank = Bank()
account1 = bank.create_account("Alice")
account2 = bank.create_account("Bob")
account3 = bank.create_account("Kelvin")

# Thực hiện các giao dịch
transaction1 = Transaction(1, account1, "deposit", 1000)
transaction2 = Transaction(2, account1, "withdraw", 200)
transaction3 = Transaction(3, account2, "deposit", 500)

# Xử lý các giao dịch
bank.process_transaction(transaction1)
bank.process_transaction(transaction2)
bank.process_transaction(transaction3)

# In thông tin tài khoản và giao dịch
bank.list_accounts()
bank.list_transactions()

print(account1)
