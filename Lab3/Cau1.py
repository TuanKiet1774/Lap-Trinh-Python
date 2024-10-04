#Đảo ngược chuỗi nhập vào
'''
while True:
  s = input("Nhập chuỗi: ")
  if len(s) > 0:
    break
'''
s = ("Phạm Tuấn Kiệt")  
temp = s.split()
s1 = ' '.join(reversed(temp)) 
print("Sau khi đổi ngược chuỗi",s,"ta được:",s1)