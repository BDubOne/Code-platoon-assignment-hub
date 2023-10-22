import random
arr = [random.randint(1, 100) for _ in range(100)]
arr.sort()

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess >item:
            high = mid - 1
            print(high)
        elif guess < item:
            low = mid + 1
            print(low)
    return None

# print(binary_search(arr, 72))

def recursive_binary_search(list, item, low=None,high=None):
    if low is None or high is None:
        low, high = 0,len(list)-1

    if low > high:
        return None
    
    mid = (low + high) // 2
    guess = list[mid]

    if guess == item:
        return mid
    elif guess > item:
        return recursive_binary_search(list, item, low, mid-1)
    else: 
        return recursive_binary_search(list, item, mid+1, high)
    
result = recursive_binary_search(arr, 32)

# print(arr[result])
# print(recursive_binary_search(arr, 32))
# print(result)
    

    