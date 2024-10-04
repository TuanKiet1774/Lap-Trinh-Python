#Tìm từ có độ dài lớn hơn một số k cho trước
while True:
  k = int(input("Nhập chuỗi: "))
  if k > 0:
    break

s = ("Trường Đại Học Nha Trang")

print(list(filter(lambda x: len(x) > k, s.split())))
#print([x for x in s.split() if len(x) > k])
