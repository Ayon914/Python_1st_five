def reverse(num):
    s = str(num)
    s = s[::-1]
    return int(s)

n = int(input("enter a number : "))
print(f"{n} in Reversed :{reverse(n)}")
