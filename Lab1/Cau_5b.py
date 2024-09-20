# sử dụng hàm
def Khoi_luong (kg):
  return kg * 2.2

# không có hàm
n = float(input("Nhập vào khối lượng: "))
print(n,"kg = ", round(n * 2.2, 2), "pound")

print(n,"kg = ", round(Khoi_luong(n), 2), "pound (Sử dụng hàm)")