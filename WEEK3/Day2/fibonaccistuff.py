calls = 0
def fib_naive(n):
    global calls
    calls += 1

    if n == 0 or n == 1:
        return 1
    else:
        result = fib_naive(n-1) + fib_naive(n-2)
        return result
    
def fib_smart(n):
    global calls

    fibs = [1, 1]

    while len(fibs) - 1 < n:
        calls += 1
        fibs.append(fibs[-1] + fibs[-2])
    
    return fibs[-1]


input = 10
result = fib_naive(input)
print(f'computed fib_naive({input}) = {result} in {calls} calls')
calls = 0
result = fib_smart(input)
print(f'computed fib_smart({input}) = {result} in {calls} calls')