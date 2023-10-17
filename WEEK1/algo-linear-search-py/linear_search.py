def linear_search(value_to_find, array_to_search_through):
    index = 0
    for element in array_to_search_through:
        if element == value_to_find:
            return index
        index += 1
    return None
        

print(linear_search("a", ['b','a','n','a','n','a'])) 

  

def linear_search_global(value_to_find, array_to_search_through):
    index_list = []
    index = 0
    
    for element in array_to_search_through:
        if element == value_to_find:
            index_list.append(index)
        index += 1

    if len(index_list) >=1:
        return index_list
    
    return None

print(linear_search_global("a", ['b','a','n','a','n','a'])) 

   