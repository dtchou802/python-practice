import math

def numbPrimes():
    nump = input("How many primes do you want?")
    curNum=2
    pCount=0
    primes=[]

    #loop till you get required numbers of primes
    while pCount<nump:
        isPrime = True
        #check to see if curNum is prime
        for x in range(2,int(math.sqrt(curNum))+1):
            if(curNum % x ==0 and x !=curNum):
                isPrime = False
                break
        if(isPrime):
            primes.append(curNum)
            pCount+=1
        #check next number
        curNum+=1
    print(primes)

numbPrimes()

def primesUnder():
    nMax = input("All primes under?")
    curNum=2
    pCount=0
    primes=[]

    #loop under prime exceed certain number
    while curNum<nMax:
        isPrime = True
        #check to see if curNum is prime
        for x in range(2,int(math.sqrt(curNum))+1):
            if(curNum % x ==0 and x !=curNum):
                isPrime = False
                break
        if(isPrime):
            primes.append(curNum)
            pCount+=1
        #check next number
        curNum+=1
    print(primes)

primesUnder()


def primeFactors():
    fac=[]
    n = input("Number for prime factorization?")
    #get all 2 prime factors
    while n % 2 == 0:
        fac.append(2)
        n = n / 2
    #check if next numbers are prime, are
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            fac.append(i)
            n = n / i
    if n > 2:
        fac.append(n)
    print(fac)


    powC=1
    if(len(fac)==1):
        print (fac)
    else:
        for x in range(1,len(fac)):
            if(fac[x]==fac[x-1] and x==len(fac)-1):
                powC=powC+1
                print str(fac[x-1])+"^"+str(powC)
            elif(fac[x]!=fac[x-1] or x==len(fac)-1):
                print str(fac[x-1])+"^"+str(powC)
                powC=1
            elif(fac[x]==fac[x-1]):
                powC=powC+1


primeFactors()