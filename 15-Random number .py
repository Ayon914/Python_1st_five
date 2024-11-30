import random
def randfloat(x,y):
    return random.uniform(x,y)   ##int->randint


a = float(input("Enter the lower bound: "))
b = float(input("Enter the upper bound: "))

myRandom = randfloat(a,b)


print(f"The random float number between {a} and {b} is = {myRandom}")