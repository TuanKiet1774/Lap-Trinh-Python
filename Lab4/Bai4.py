def bin_dec(a):
    dec = 0
    for i in range(len(a)):
        if a[len(a) - 1 - i] == '1':
            dec += pow(2, i)
    return dec

#đúng điều kiện nhập nhị phân
while True:
  s = input("Nhập số nhị phân: ")
  if all(i in '01' for i in s): 
    break
  print("Số nhị phân chỉ chứa 1 và 0")
   
print(f'Giá trị thập phân của {s} là: {bin_dec(s)}')
