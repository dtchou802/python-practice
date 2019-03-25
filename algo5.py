import random

#max sub array brute force
def brute():
    maxSum=-1000
    maxArray=[]

    randArray = random.sample(range(-10, 20), 8)
    for x in range(0,len(randArray)):
        for i in range (x, len(randArray)+1):
            tempArray=randArray[x:i]
            if(sum(tempArray)>maxSum):
                maxSum=sum(tempArray)
                maxArray = tempArray

    print("Random values in the Array: \n", randArray)
    print("brute force max sub array : ",maxArray)
    print("brute force sum of max sub array : ",maxSum)



#max subarray div and conquer
def maxSubarray(A, low, high):
    #base case
    if low == high - 1:
        return low, high, A[low]

    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = maxSubarray(A, low, mid)
        right_low, right_high, right_sum = maxSubarray(A, mid, high)
        cross_low, cross_high, cross_sum = maxCrossingSubarray(A, low, mid, high)

        if (left_sum >= right_sum and left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >= left_sum and right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

def maxCrossingSubarray(A, low, mid, end):
    sum_low = -1000
    xtemp = 0
    x_low = mid
    for i in range(mid - 1, low - 1, -1):
        xtemp = xtemp + A[i]
        if xtemp >= sum_low:
            x_low = i
            sum_low = xtemp

    x_high = -1000
    xtemp = 0
    cross_high = mid + 1
    for i in range(mid, end):
        xtemp = xtemp + A[i]
        if xtemp >= x_high:
            cross_high = i + 1
            x_high = xtemp
    return x_low, cross_high, sum_low + x_high


A = random.sample(range(-10, 20), 8)
print("Random values in the Array: \n", A)
low, high, maximum = maxSubarray(A, 0, len(A))
print("Divide and Conquer Max sub array: ", A[low:high])
print("Divide and Conquer Max sum of array: ", sum(A[low:high]))
print("\n")


brute()






