def fibo (n):
  if n == 0: #Số fibo đầu tiên 
    return 0
  elif n == 1: #Số Fibo thứ 2
    return 1
  else:  
    f0 = 0
    f1 = 1
    for i in range(2,n+1):
      fn = f0 + f1
      f0 = f1
      f1 = fn
    return fn

while True:
  n = int(input("Nhập số nguyên n: "))
  if n >= 0:
    break
  
print("Số Fibonacci thứ",n ,"là ", fibo(n))