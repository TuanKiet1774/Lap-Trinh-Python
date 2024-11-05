import advanced_math as a

n = int(input("Nhập số: "))

print(f"{n}! = {a.factorial(n)}")
print("Số Fibo thứ",n,"là", a.fibonacci(n))
print(n,"=",a.prime_factors(n))
if a.is_prime(n) == True:
  print(n,"là số nguyên tố")
else:
  print(n,"không phải số nguyên tố")