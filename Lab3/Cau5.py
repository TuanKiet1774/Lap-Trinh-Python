#In ra tất cả các kết hợp có 3 chữ số
from itertools import permutations

temp = permutations([1,2,3],3)
#in ra 1 list có các phần tử là các tuple
print(list(temp))