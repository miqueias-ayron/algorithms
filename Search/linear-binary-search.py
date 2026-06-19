from typing import List
import math

def linear_search(array:List[int], target:int)->int:
    for i in range(len(array)):
        count += 1
        if array[i] == target:
            return i, count
    return -1, count

def binary_search(array:List[int], target:int)->int:
    low = 0
    high = len(array)

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