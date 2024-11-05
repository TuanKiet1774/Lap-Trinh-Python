def factorial(n):
  if n == 0 or n == 1: 
    return 1
  return n * factorial(n-1)

def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

def prime_factors(n):
  a = [] 
  for i in range(2, int(n**0.5) + 1):  # Bao gồm cả căn bậc 2 của n
    while n % i == 0:
      a.append(i)
      n //= i 
  if n > 1:  # Số còn lại lớn hơn 1
    a.append(n) 

  return " x ".join(map(str, a))
    
def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

#print("Hello")
if __name__ == "__main__":
  n = int(input("Nhập số: "))
  print(n,"! = ",factorial(n))
  print("Số Fibo thứ",n,"là", fibonacci(n))
  print(n,"=",prime_factors(n))
  if is_prime(n) == True:
    print(n,"là số nguyên tố")
  else:
    print(n,"không phải số nguyên tố")