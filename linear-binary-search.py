from typing import List
import math

def linear_search(array:List[int], target:int)->int:
    count = 0 #contagem do numero de etapas
    for i in range(len(array)):
        count += 1
        if array[i] == target:
            return i, count
    return -1, count

def binary_search(array:List[int], target:int)->int:
    low = 0
    high = len(array)

    count = 0 #contagem do numero de etapas
    while low < high:
        count += 1
        mid = math.floor((low + high)/2)
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid
        else:
            return mid, count
    return -1, count

array = [-7, -5, -1, 3, 5, 7, 11, 17, 28, 76, 85]

print(linear_search(array=array, target=11))
print(binary_search(array=array, target=11))
