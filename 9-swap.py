def mySwap(x,y):
    x,y = y,x
    return x,y



a = int(input("Enter the first number, A = "))
b = int(input("Enter the second number, B = "))
print(f"Before Swap A = {a} & B = {b}")

Result = mySwap(a,b)

print(f"After Swap = {Result}")
