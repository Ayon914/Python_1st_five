def find_largest(n):
    unique_Num = list(set(n))
    if len(unique_Num) < 2:
        return "There is no largest Number"
    unique_Num.sort(reverse=True)
    return unique_Num[1]

Num = list(map(int,input("Enter numbers separated by spaces: ").split()))

Second_large = find_largest(Num)
print(f"The second largest number is : {Second_large}")