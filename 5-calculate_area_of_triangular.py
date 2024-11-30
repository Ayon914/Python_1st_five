def triangle_d(a,b,c):
    s = (a+b+c)/2
    if a**2 == b**2 + c**2:
        return 0.5*b*c
    else:
        return s*(s-a)*(s-b)*(s-c)


a = int(input("enter larger side of T."))
b = int(input("enter secound side of T."))
c = int(input("enter 3rd side fof T."))
sum = triangle_d(a,b,c)
print(sum)