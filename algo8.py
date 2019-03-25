import random

def countingSort(A,B,n,k):
    C=[0] * (k+1)
    print ("C is: ",C)
    for i in range(0,n):
        C[A[i]]= C[A[i]]+1
    print(C)
    for j in range (1,k+1):
        C[j] = C[j] + C[j-1]
        print("C is: ", C)
    print("b is ",B)
    for x in range (n-1,-1,-1):
        B[C[A[x]]-1] = A[x]
        C[A[x]] = C[A[x]]-1
        print("C is: ", C)
        print("B is: ",B)

    print("end")



def Rand( end, num):
    result = []
    for j in range(num):
        result.append(random.randint(0, end))
    return result

#n=int(input("n elements in lists: "))
#k=int(input("K range: "))
#B=[0] * n

#randArr=Rand(k, n)
#print("rand array: ",randArr)
countingSort([1,8,8,4,6,7,3,3,9,2],[0,0,0,0,0,0,0,0,0,0],10,9)



def countingSortR(A,d,n,k):
    C=[0] * (k+1)
    B=[0] * n
    print("C array: " + C)
    for i in range(0,n):
        value = int(A[i]/10**(d-1))
        print("value: ",value)
        C[value%10 ] +=1
    print(C)
    for j in range (1,k+1):
        C[j] = C[j] + C[j-1]
        print("C is: ",C)
    for x in range (n-1,-1,-1):
        value = int(A[x]/10**(d-1))
        B[C[(value)%10]-1] = A[x]
        C[(value)%10] -= 1
    print("B is: ",B)
    print("end")
    for i in range(0,len(A)):
        A[i]=B[i]

def radix(A,d):
    for i in range(1,d+1):
        print(A)
        k=9
        countingSortR(A,i,n,k)


# d=int(input("enter number of digits "))
# n=int(input("number of integer elements "))
# min = 10**(d-1)
# max = (10**(d)) - 1
# rArray=random.sample(range(min, max), n)
# print(rArray)
#
# radix(rArray,d)
