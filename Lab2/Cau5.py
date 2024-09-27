import string

s = input("Nhập chuỗi: ")
count_num = 0
count_lower = 0
count_upper = 0

for i in range(len(s)):
  if s[i] in string.digits:
    count_num += 1
  elif s[i] in string.ascii_lowercase:
    count_lower += 1
  elif s[i] in string.ascii_uppercase:
    count_upper += 1

print(f'"{s}" có {count_num} ký số, {count_lower} ký tự thường, {count_upper} ký tự in')