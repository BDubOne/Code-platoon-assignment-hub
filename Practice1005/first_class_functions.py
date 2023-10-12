##Firstclass 

def say_hello(name):
    print(f"hello {name}")

def say_hello_extra(name, other_hello_function):
    print(f"hi {name}")
    other_hello_function(name)

say_hello_extra("Alice", say_hello)


dict = {"foo": "bar"}

say_hello(dict)   ## Python's job is not to judge the data

'''
def add_one(x):
    return x + 1

    this kind of function would be better as a lambda
    '''

add_two = lambda x : x + 2

print(add_two(5))

say_hi = lambda name : f"hello {name}"

say_hello_extra("Bob", say_hi)

### Map Functions ###

my_list = [1,2,3,4,5,6,7,8,9]

new_list = map(lambda item : item + 2, my_list)
print(list(new_list))

new_list = map(add_two, my_list)
print(list(new_list))

## print(my_list) my_list has not changed

### Filter ###

''' filter, rather than manipulating data, returns 
qualifying data
'''
new_list_by_three = filter(lambda item : item % 3 == 0, my_list)
print(list(new_list_by_three))

print(type(new_list))



##reduce ##
a_list = [1,2,3,4,5,6,7,8,9,10]
add_two_things = lambda agg, item : agg + item
print(add_two_things(1,4))

import functools

words = ['hello', 'world', 'its', 'sunny']
sentence = functools.reduce(lambda agg, item : f"{agg} {item}", words)
sum = functools.reduce(lambda agg, item : agg + item, a_list)
print(sentence)
print(sum)
my_var = 7 ##this is to practice modules on modules.py


### PASS ####

'''
Pass is a placeholder for when you know you will need a function,
but you don't know what to write yet.
'''

def hello():
    # fill in the code here

    pass

