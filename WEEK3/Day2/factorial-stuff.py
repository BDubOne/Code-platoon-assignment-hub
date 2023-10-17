def factorial(n):
    result = 1
    count = 1

    while count <=n:
        result *= count
        count += 1
    
    return result
# print(factorial(4))

def factorial_for(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result

# print(factorial_for(1558))
calls = 0
def factorial_recursion(n):
    print(f'n is {n}')
    if n <= 1:
        print('dun')
        return 1
    print('recursing')
    return f'Solution : {n * factorial(n-1)}'

print(factorial_recursion(6))

    
    

        
        





