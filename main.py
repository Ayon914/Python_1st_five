def fibo(n):
    fst = 0;
    snd = 1;
    print(f"{fst} {snd}",end=" ")
    for i in range(3,n+1):
        fibo = fst + snd
        fst = snd
        snd = fibo
        print(fibo,end=" ")



mynum = int(input("Enter a number = "))


