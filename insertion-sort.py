from typing import List

def insertion_sort(array:List[int])->List[int]:
    for i in range(1, len(array)):
        _ = array[i]
        j = i - 1
        while j >= 0 and array[j] > _:
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = _
    
    return array

array = [5, 3, 8, 2]
print(insertion_sort(array))