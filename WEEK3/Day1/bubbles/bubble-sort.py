sequence = [4, 3, 5, 0, 1]
swaps = 0

import random

arr = [random.randint(1, 10) for _ in range(10)]

def bubble_swap(arr):
    print(f'Initial array: {arr}')
    swaps = 0

    for i in range(len(arr)):
        if arr[i] < arr[i - 1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            swaps += 1
    print(f'{swaps} swaps')
    print(f'result: {arr}')
# bubble_swap(arr)
        
    

def big_bubble_swap(arr):
    print(f'Initial array: {arr}')
    swaps = 0
   
    

    for _ in range(len(arr)):
        made_swap = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swaps += 1
                made_swap = True
        if not made_swap:
            break
      
   

   
    print(f"Sorted array: {arr}")
    print(f"Swaps: {swaps}")

big_bubble_swap(arr)

def sorting(arr):
    print(f"Initial array: {arr}")
    
    sorted_arr = sorted(arr)
    print(f"Sorted array using 'sorted()': {sorted_arr}")
    print(f"original array remains unchanged: {arr}")

# sorting(arr)