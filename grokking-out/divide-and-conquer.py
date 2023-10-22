"""

----------
-        -
-        -
-        -
----------
-        -
-        -
-        -
----------
-        -
-        -
-        -
----------
-        -
-        -
-        -
----------
-   -   -- 
----------
1. Figure out base case
2. figure out how to reduce problem and get to base case"""

##ARRAY OF NUMBERS:
#Add numbers and return total

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

# print(sum([1,2,3,4]))

def recursive_sum(arr):
    if len(arr) == 0:
        return 0 
    
    result = arr.pop(0)
    return result + recursive_sum(arr)

# print(recursive_sum([1,2,3,4]))

###Check bin-search.py for recursive application of binary search####

###Quicksort####
import random
arr = [random.randint(1, 100) for _ in range(100)]

def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[len(list) // 2]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        print(f'Greater: {greater} Less: {less} Pivot: {pivot}')
        
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort(arr))
        
   
    


    
    
    