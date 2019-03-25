
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr,low,high):
    count=0
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
    print("pivot is: ",pivot)

    for j in range(low , high):
        # If current element is smaller than or
        # equal to pivot
        count+=1
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            print("swap: "+ str(i) +" and " + str(j))
            arr[i],arr[j] = arr[j],arr[i]
            print(arr[low:high+1])

    print("L swap: " + str(high) +" and " + str(i+1))
    arr[i+1],arr[high] = arr[high],arr[i+1]
    print("count is: ", count)
    print(arr)
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
        # Separately sort elements before
        # partition and after partition
        #quickSort(arr, low, pi-1)
        #quickSort(arr, pi+1, high)

#arr = [1, 2, 3, 4, 5, 6, 7]
#arr = [7, 6, 5, 4, 3, 2, 1]
#arr = [2, 2, 2, 2, 2, 2, 2]
#arr = [2,2,2]
arr= [1,4,7,2,8,6]
print("original arr: ",arr)
n = len(arr)
quickSort(arr,0,n-1)

print ("Sorted array is: ", arr)
