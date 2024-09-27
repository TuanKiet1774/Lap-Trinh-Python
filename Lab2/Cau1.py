def So_pi (n):
  Pi = 0
  for i in range(n+1):
    Pi += (-1)**i / (2*i + 1)
  return Pi

while True:
  n = int(input("Nhập số nguyên dương n: "))
  if n >= 0:
    break
  
print("Kết quả:",round(4 * So_pi(n), 3)) 