from typing import List

def bubble_sort(array:List[int])->List[int]:
    _ = 0
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = [3,-1,5,2,7,1]
print(bubble_sort(array))