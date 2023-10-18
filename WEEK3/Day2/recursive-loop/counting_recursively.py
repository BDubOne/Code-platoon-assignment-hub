
def recursive_i(num):
    if num == 0:
        print(num)
        return 0
    recursive_i(num-1)
    print(num)
    return num

print(recursive_i(6))

def recursive_d(n):
    if n < 0:
        
        return 
    print(n)
    recursive_d(n-1)
    
    
    
print(recursive_d(6))
    