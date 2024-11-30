def check_p(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
            return True


mynum = int(input("enter a num : "))
check = check_p(mynum)

if check_p(mynum):
    print(f"{mynum} is a prime num ")
else:
    print(f"{mynum} is not a prime num ")