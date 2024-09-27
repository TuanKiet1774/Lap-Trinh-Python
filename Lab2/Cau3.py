def fibo_DQ (n):
  if n == 0: #điều kiện dừng
    return 0
  elif n == 1:
    return 1
  else:
    return fibo_DQ(n-1) + fibo_DQ(n-2)

while True:
  n = int(input("Nhập số nguyên n: "))
  if n >= 0:
    break

print("Số Fibonacci thứ",n ,"là (đệ quy) ", fibo_DQ(n))
