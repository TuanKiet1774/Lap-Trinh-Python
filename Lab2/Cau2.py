import math
#VD: 10 = 2 5
def Phan_tich(n):
  for i in range(2, int(math.sqrt(n)) + 1):  # Bao gồm cả căn bậc 2 của n
    while n % i == 0:
      print(i, end=" ")  # In ước số
      n //= i 
  if n > 1:  # Số còn lại lớn hơn 1
    print(n, end=" ")

while True:
  n = int(input("Nhập số nguyên dương n: "))
  if n > 0:
    break

print(n, "phân tích thành: ", end="")
Phan_tich(n) 
