from cs50 import get_string
#不是python自带的print函数，导入进来的get_string还是需要换行符\n
s = get_string("what's your name?\n")
print("hello, " + s)
print("hello,", s)    #删除了+号，和hello后面的一个空格
print(f"hello, {s}")  #用{}代入s，记得在前面加f