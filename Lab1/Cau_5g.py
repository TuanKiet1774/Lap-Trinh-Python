while True:
  n = int(input("Nhập số nguyên n: "))
  if n >= 0:
    break

count = 0
if n == 0:
  count = 1
else:
  while n > 0:
    count += 1
    #n = int (n / 10)
    n //= 10

print("Số lượng: ", count)

