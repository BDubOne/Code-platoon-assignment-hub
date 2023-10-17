result = 0
def recursive_i(num):
    
    

    if result == num:
        print(result)
        return result
    
    return  recursive_i(result + 1)

recursive_i(10)
    