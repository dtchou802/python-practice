import random


def selectionSort():
	randArray = random.sample(range(1, 100), 8)
	print("Random values in the Array: \n", randArray)

	for x in range(len(randArray)):
		min=x
		for i in range(x+1,len(randArray)):
			if(randArray[min]>randArray[i]):
				min = i
		randArray[x], randArray[min] = randArray[min], randArray[x]

	print("After selection sort: \n",randArray)

selectionSort()

def insertionSort():
	randArray = random.sample(range(1, 100), 8)
	print("Random values in the Array: \n", randArray)

	for x in range(len(randArray)):
		key = randArray[x]
		i=x-1
		while(i>=0) and (randArray[i]<key):
			randArray[i+1] = randArray[i]
			i = i -1
		randArray[i+1]=key
	print("After insertion sort: \n",randArray)

insertionSort()
