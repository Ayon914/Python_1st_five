

Num2 = list(map(int,input("Enter numbers separated by spaces: ").split()))
Num1 = list(map(int,input("Enter numbers separated by spaces: ").split()))
common_Num = list(set(Num1) & set(Num2))

print(f"The Common Number of {Num1} & {Num2} is = {common_Num}")