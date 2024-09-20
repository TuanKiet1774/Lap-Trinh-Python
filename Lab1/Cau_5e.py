money = float(input('Nhập số tiền (VND): '))

while money <= 0:
  money = float(input('Số tiền không hợp lệ !!!\nMời bạn nhập lại: '))

day = int(input("Nhập số ngày gửi: "))

while day <= 0:
  day = int(input("Số ngày không hợp lệ !!!\nMời bạn nhập lại: "))

match money:
  case money if 0 < money < 10000000:
    LaiXuat = money * 0.05 * (day/365)
  case money if 10000000 < money < 20000000:
    LaiXuat = money * 0.07 * (day/365)
  case money if money > 20000000:
    LaiXuat = money * 0.1 * (day/365)
   
print(f"Lãi xuất sau {day} ngày gửi là: {round(LaiXuat,4)} VND")