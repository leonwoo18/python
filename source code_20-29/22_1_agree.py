from cs50 import get_string
import re
s = get_string("do you agree?\n")


if re.search("y(es)?", s): #查找s中是否包含有y、yes字眼
    print("Agreed.")
elif re.search("n(o)?", s): #查找s中是否包含有n、no字眼
    print("Not agreed.")
