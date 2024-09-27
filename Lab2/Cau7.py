def Nhi_Phan(n):
  if n == 0:
    print(0) #Dừng
    return 
  So_nhi_phan = "" #Tạo chuỗi rỗng
  while n > 0:
    temp = n % 2
    So_nhi_phan = str(temp)  + So_nhi_phan #Gán các giá trị dư vào đầu chuỗi
    n //= 2
  print(So_nhi_phan)

while True:
  n = int(input("Nhập số ở dạng thâp phân: "))
  if n >= 0:
    break
    
Nhi_Phan(n)
