#交互_键盘输入
words = input("say something!\n").lower()

if "hello" in words:
    print("hello to you too!")
elif "how are you" in words:
    print("I am well, thanks!")
elif "goodbye" in words:
    print("goodbye to you too!")
else:
    print("huh?")