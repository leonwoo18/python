from cs50 import get_string
s = get_string("do you agree?\n")

#if s in ["Y", "y", "yes", "Yes"]:
if s.lower() in ["y", "yes"]:
    print("Agreed.")
#elif s in ["N", "n", "Nope"]:
elif s.lower in ["n", "no"]:
    print("Not agreed.")
