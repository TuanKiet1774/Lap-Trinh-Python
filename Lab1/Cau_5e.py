money = float(input('Nhập số tiền (VND): '))

while money <= 0:
  money = float(input('Số tiền không hợp lệ !!!\nMời bạn nhập lại: '))

month = int(input("Nhập số tháng: "))

while month <= 0:
  month = int(input("Số tháng không hợp lệ !!!\nMời bạn nhập lại: "))

match month:
  case month if 0 < month < 6:
    LaiSuat = money * 0.05
  case month if 6 <= month < 12:
    LaiSuat = month * 0.07
  case month if month >= 12:
    LaiSuat = month * 0.1
   
print(f"Lãi suất sau {month} tháng gửi là: {round(LaiSuat,4)} VND")