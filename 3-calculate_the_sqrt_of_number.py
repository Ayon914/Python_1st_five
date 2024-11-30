def sqr_root(n):
    if n<0:
        print("This number's root is not real")
    else:
        return n**0.5


mynum = int(input("Enter a number = "))
root_num = sqr_root(mynum)
print(f"The root of{mynum} is = {root_num}")
