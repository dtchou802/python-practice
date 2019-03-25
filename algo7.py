import heapq
import random
from math import floor
#import numpy
from queue import PriorityQueue



def heapSortA(array):
    n = len(array)

    for rt in range(n,-1,-1):
        heapify(array, rt, n)

    for rt in range(n-1,0,-1):
        array[rt], array[0] = array[0], array[rt]
        heapify(array, 0, rt)
    print(array)


def heapSort():
    #num = int(input("how many elements in random array? "))
    #randArray = random.sample(range(1, 20), num)
    randArray = [4,4,3,1]
    print ("original: ",randArray)
    n = len(randArray)

    #build max heap
    for rt in range(floor(n/2),-1,-1):
        heapify(randArray, rt, n)
    print("max heap: ",randArray)

    for rt in range(n-1,0,-1):
        print("rt swap " +  str(rt) + " and " + str(0))
        randArray[rt], randArray[0] = randArray[0], randArray[rt]
        print(randArray)
        heapify(randArray, 0, rt)
    print("sorted: ",randArray)

def heapify(array, rt, n):
    max = rt
    left = 2 * rt + 1
    right = 2 * rt + 2

    if left < n and array[left] > array[rt]:
        max = left

    if right < n and array[right] > array[max]:
        max = right

    if max != rt:
        print("swap " +  str(max) + " and " + str(rt))
        array[rt], array[max] = array[max], array[rt]
        print(array)
        heapify(array, max, n)



def randomK():
    k=int(input("How many lists: "))
    l=int(input("How many elements in each list: "))
    combArray = [[0 for x in range(l)] for y in range(k)]
    for x in range (0,k):
        randArray = random.sample(range(1, 20), l)
        randArray.sort()
        print("original: ",randArray[x])
        combArray[x] = randArray

    print(combArray)



#randomK()
heapSort()