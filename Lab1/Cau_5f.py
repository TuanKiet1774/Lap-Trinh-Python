while True:
  a = int(input("Nhập số a = "))
  if a > 0: 
    break

while True:
  b = int(input("Nhập số b = "))
  if b > 0:
    break

# Sử dụng hàm đệ quy
def  UCLN_DQ ( a, b):
  if b == 0:
    return a
  else:
    return UCLN_DQ(b, a % b)

# Sử dụng hàm
def UCLN (a, b):
  temp_a = a
  temp_b = b
  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a
  print(f"UCLN của {temp_a} và {temp_b} là: ", a)

# UCLN 
UCLN(a,b)

# BCNN
print(f"BCNN của {a} và {b} là: ", int((a*b)/(UCLN_DQ(a,b))))

