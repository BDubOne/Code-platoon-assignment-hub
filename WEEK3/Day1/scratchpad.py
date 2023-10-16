# class Node:

#     def __init__(self, value):
#         self._value = value
#         self._next = None

#     @property
#     def get_value(self):
#         return self._value
#     @get_value.setter
#     def set_value(self, new_value):
#         self._value = new_value
    
#     @property 
#     def get_next(self):
#         return self._next
#     @get_next.setter
#     def set_next(self, new_next):
#         self._next = new_next
    

# def idk():
#     head = Node(3)

#     some_node = Node(5)

#     head._next = some_node

#     no_next_node = False
#     current_node = head

#     while(no_next_node):
#         print(current_node._value)

#         if current_node._next is not None:
#             current_node = current_node._next
#             print(current_node)
        
#         else:
#             no_next_node = True
#             print(no_next_node)

# idk()




# nums_0 = Node(1)
# nums_1 = Node(2)
# nums_2 = Node(3)
# nums_3 = Node(3)
# nums_4 = Node(4)
# nums_5 = Node(5)
# nums_6 = Node(6)
# nums_7 = Node(7)

def double_elements_new_array():
    arr = [1, 4, 6, 8, 9]
    new_arr = []
    for i in arr:
        new_arr.append(i * 2)
    print(new_arr)
    return new_arr


def double_elements_in_place():
    arr = [1, 4, 6, 8, 9]
    for i in range(len(arr)):
        arr[i] = arr[i] * 2
    print(arr)
    return arr
double_elements_new_array()
double_elements_in_place()

from collections import Counter
import random

arr = [random.randint(1, 100) for _ in range(100)]
counter = Counter(arr)
duplicates = {item: count for item, count in counter.items() if count > 1}

result_list = [[(item * count, (count, item)) for item, count in duplicates.items()]]
print(duplicates)
print(result_list)
# for item, count in duplicates.items():
#     print(f'{item} is duplicated {count} times')


def contains_duplicates_sort(arr):


    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            print(arr[i])
            
    
# print(contains_duplicates_sort(arr))








