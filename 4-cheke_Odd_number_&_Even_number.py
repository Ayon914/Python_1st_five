def check_odd_even(n):
    if n%2==0:
        return "is an even number "
    else :
        return "is an odd number"
mynum = int(input("enter a num : "))
check = check_odd_even(mynum)
print(f"answare : {check}")