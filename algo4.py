def divNconq():
    a = float(input("In a^n what is a?"))
    n = float(input("In a^n what is n?"))

    if n % a == 0:
        for x in range(int(n/2)):
            ans=a*a;

        print("a^n computes to",ans*ans)
    else:
        for x in range(int(n/2)-1):
            ans=a*a;
        print("a^n computes to",ans*ans*a)

divNconq()