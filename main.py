# Bubble Sort Algo
def bubblesort(array):
    for element in range(len(array)):
        for elements in range(len(array)-1):
            if array[elements] > array[elements+1]:
                array[elements], array[elements+1] = array[elements+1], array[elements]
    return array
