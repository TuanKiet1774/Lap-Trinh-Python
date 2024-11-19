import re

def count_words(s):
  a = re.findall(r'\b\w+\b', s)
  return len(a)
#\b là ranh giới (" ", "-", "@", ".", ",") == \W

def find_emails(s):
    e = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', s)
    return e
# + ít nhất 1 
# số lượng từ 2 -> vô cùng

def find_dates(s):
    d = re.findall(r'\b\d{2}/\d{2}/\d{4}\b|\b\d{2}-\d{2}-\d{4}\b', s)
    return d

def censor_bad_words(s):
  bad_words = ["idiot", "badword"]
  for word in bad_words:
    s = re.sub(r'\b'+word+r'\b','*' * len(word), s, flags = re. IGNORECASE)  
  return s
#re. IGNORECASE không phân biệt hoa thường

if __name__ == "__main__":
  s = "Nha Trang University abc@gmail.com"
  
  s1 = """Hôm đó là ngày 01/11/2023. Liên hệ với tôi qua email john.doe@example.com.
Một ngày đẹp trời khác là 10-12-2022. Một số lời nói xấu như idiot, badword
cần được kiểm duyệt.
Nha Trang University, today is 4/11/2024.
"""
  print("Số lượng từ:", count_words(s))  
  print("Email: ", find_emails(s))
  print("Date: ",find_dates(s1))
  
  
  print("\nVăn bản sau khi kiểm duyệt từ xấu:")
  print(censor_bad_words(s1))


