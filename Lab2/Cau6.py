from difflib import SequenceMatcher

s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")

Check = SequenceMatcher(None,s1,s2)

print("Mức độ tương tự", int(Check.ratio() * 100),"%")
#Tính toán và trả về mức độ tương đồng: ratio()