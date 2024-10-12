
def Danh_Sach (a, b):
  Giao = [x for x in a if x in b] # phần tử chung
  Hop = list(set(a+b)) #lấy hết
  a_tru = list(set(a) - set(b)) # có trong a nhưng ko có trong b
  b_tru = list(set(b) - set(a)) # có trong b nhưng ko có trong a
  return Giao, Hop, a_tru, b_tru

a = [1, 2, 3, 4, 5, 6]
b = [2, 4, 6, 8, 0]
#for ds in Danh_Sach(a,b):
#  print(ds)
  
print(f"a giao b: {Danh_Sach(a,b)[0]} \na hơp b: {Danh_Sach(a,b)[1]} \na - b: {Danh_Sach(a,b)[2]} \nb - a: {Danh_Sach(a,b)[3]}")