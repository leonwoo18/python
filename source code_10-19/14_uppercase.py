#string类型自带了upper()函数
from cs50 import  get_string

s = get_string("Before: ")
print("After: ", end="")
print(s.upper())
