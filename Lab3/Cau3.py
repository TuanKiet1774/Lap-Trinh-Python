#Đếm số từ nguyên âm
'''
while True:
  s = input("Nhập chuỗi: ")
  if len(s) > 0:
    break
'''
s = ("Pham Tuan Kiet")
NguyeAm = ("ueoaiUEOAI")
count = 0

for i in range(len(s)):
  if s[i] in NguyeAm: 
    count += 1
    
#count = sum(s.count(vowel) for vowel in NguyeAm)

print("Số từ nguyên âm: ", count)