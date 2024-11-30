def mygcd(x,y):
    while y:
        x,y = y, x%y
    return x

num1 = int(input("Enter the Frst number:  "))
num2 = int(input("Enter the second number:  "))

result = mygcd(num1,num2)

print(f"GCD of {num1} and {num2} is = {result} ")