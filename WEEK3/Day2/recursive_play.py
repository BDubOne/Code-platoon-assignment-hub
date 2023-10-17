
import random

arr = [random.randint(1, 10) for _ in range(10)]
sorted_arr = sorted(arr)
print(arr)
print(sorted_arr)
solution = sorted_arr[-1]
print(solution)

def get_max(nums):
    current_max = float("-inf") #Basic Loop solution
    for num in nums:
        if num > current_max:
            current_max = num
    return current_max
print(get_max(arr))

def get_max_recursive(nums):
    if len(nums) == 1:
        return nums[0]
    else: 
        if nums[0] > nums[1]:
            nums.pop(1)
            return get_max_recursive(nums)
        else:
            return get_max_recursive(nums[1:])
        # if nums[0] > nums[1]: Dicey logic
        #     return nums[0]
        # else:
        #     return nums[1]
        
print(get_max_recursive(arr))