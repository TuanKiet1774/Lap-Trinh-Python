#Viết chương trình kiểm tra tính hợp lệ của mật khẩu
import re

def CheckPass(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

p = "phamtuankiet, Ptk@1774, TuanKiet1774, Kiet@1774"

# Tách các mật khẩu từ chuỗi nhập vào
pass_list = [x for x in p.split(',')]

RightPass = [x for x in pass_list if CheckPass(x)]

# In ra các mật khẩu hợp lệ
print("Mật khẩu hợp lệ:", ", ".join(RightPass))
