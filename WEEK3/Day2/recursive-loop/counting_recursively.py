
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

def count(n):  #Weird Hack from Claireese and Josh
    if n == 0:
        print(0)
        return
    else:
        print(n)
        count(n-1)
        print(n)
count(6)
    
    