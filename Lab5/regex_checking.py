import re

def count_words(s):
  a = re.findall(r'\b\w+\b', s)
  return len(a)

def find_emails(s):
    # Sử dụng biểu thức chính quy để tìm các địa chỉ email trong văn bản
    e = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', s)
    return e
  
def find_dates(s):
    d = re.findall(r'\b\d{2}/\d{2}/\d{4}\b|\b\d{2}-\d{2}-\d{4}\b', s)
    return d

def censor_bad_words(s, bad_words):
  for word in bad_words:
    s = re.sub(r'\b'+ re.escape(word) + r'\b','*' * len(word), s, flags = re. IGNORECASE)  
  return s


if __name__ == "__main__":
  s = "Nha Trang University abc@gmail.com"
  
  s1 = """Hôm đó là ngày 01/11/2023. Liên hệ với tôi qua email john.doe@example.com.
Một ngày đẹp trời khác là 10-12-2022. Một số lời nói xấu như idiot, badword
cần được kiểm duyệt.
Nha Trang University, today is 4/11/2024.
"""
  print("Số lượng từ:", count_words(s))  
  print("Email: ", find_emails(s))
  print("Date: ", find_dates(s1))
  
  bad_words = ["idiot", "badword"]
  print("\nVăn bản sau khi kiểm duyệt từ xấu:")
  print(censor_bad_words(s1, bad_words))
