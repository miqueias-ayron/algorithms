from typing import List

def selection_sort(array:List[int])->List[int]:
    
    for j in range(len(array)):
        min_index = j
        for i in range(len(array)):
            if array[i] < array[min_index]:
                min_index = i
      
        if array[j] > array[min_index]:
            array[j], array[min_index] = array[min_index], array[j]