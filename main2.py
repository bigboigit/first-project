# List of sorting algos

def bubblesort(ar):
	for i in range(len(ar)):
		for j in range(i, len(ar) - 1):
			if ar[j] > ar[j+1]:
				ar[j], ar[j+1] = ar[j+1], ar[j]
	return ar
print(bubblesort([1000, 10, 20]))