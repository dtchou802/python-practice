import time
from random import *
import itertools
import math


def randomize(n):
    randArray=list(range(1, n+1))
    shuffle(randArray)
    #print("Random values in the Array: \n", randArray)
    return randArray

def checkHires(array):
    totalHires=1;
    key = array[0];
    for x in range (1,len(array)):
        if (array[x] == 1):
            totalHires+=1
            break
        if(array[x]<key):
            totalHires+=1
            key = array[x]
    return totalHires


def sum(n):
    start_time = time.time()
    total=0;
    for x in range (1,n+1):
        total = 1/x +total
    print("Summation:",total)
    print("Summation takes: %s seconds " % (time.time() - start_time))

def gen10000(n):
    start_time = time.time()
    sum=0
    for x in range(0,10000):
        array=randomize(n)
        sum = sum + checkHires(array)
    avg = sum/10000
    print ("10,000 arrays average: ",avg)
    print("10,000 random takes: %s seconds " % (time.time() - start_time))

def enumerate(n):
    start_time = time.time()
    totalh=0;
    exacth=0;
    enumerlist = list(itertools.permutations(randomize(n)))
    print(len(enumerlist))
    #print(math.factorial(n))
    for l in enumerlist:
        totalh = totalh + checkHires(l)
        if checkHires(l) == 2:
            exacth = exacth +1;
            print(l)

    print(enumerlist)
    print("exact hires: ", exacth)
    print ("Enumeration average: ",totalh/len(enumerlist))
    print("Enumerate takes: %s seconds " % (time.time() - start_time))

def lgN(n):
    start_time = time.time()
    print("LgN :", math.log(n))
    print("LnN takes: %s seconds " % (time.time() - start_time))


#sum(10)
#gen10000(10)
enumerate(4)
#lgN(10)