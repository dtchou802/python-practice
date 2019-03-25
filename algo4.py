
# a^n div and conquer
def divNconq(a, n):
    if n==0:
        return 1

    elif (int(n % 2) == 0):
        return(divNconq(a,int(n/2))*divNconq(a, int(n/2)))

    else:
        return (a*divNconq( a,int(n/2))*divNconq(a, int(n/2)))


a = int(input("In a^n what is a?"))
n = int(input("In a^n what is n?"))
print(divNconq(a,n))