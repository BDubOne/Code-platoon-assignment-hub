def fibonacci(n):
    fib_list = [0, 1]
    if n < 1:
        return None
    index = 1
    while index < n:
        fib_list.append(fib_list[index] + fib_list[index - 1])
        index += 1


    return fib_list[n - 1]

print(fibonacci(11))
        


