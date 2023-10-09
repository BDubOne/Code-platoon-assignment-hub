#primitive types

print("Hello world!!!")

a_small_number = 4.5

#how to check the type of a var

print(type(a_small_number))

#python number types

#int, float, complex

print(complex(4 / 3.5))
print(int(4 / 3.5))
print(float(4 / 3.5))

#modulo
print( 4.5 % 2)
print( 4 % 2)

# Python does not typecast like js.  == is bamalama

print("True" != True)
print("5" != 5)
print(5 == 5)

# string interpolation

name = "Sally"
print(f"Hello, my name is {name}")

# Data Types:

# Lists

berries = ['grape', 'tomato', 'cucumber', 
           'eggplant', 'banana', 'watermelon', 'pumpkin']
print(berries)

print(berries[0])
print(berries[-1])

# slice from list
print(berries[2:5]) #start is inclusive. End is exclusive
print(berries[:3]) #from beginning to index 3 exclusive
print(berries[2:]) # from index 2 inclusive to end

print(berries[::-1]) # reverse a list


#### Tuple ######

#tuple is kinda like a list, but it is immutable

days_of_the_week = ('sunday', 'monday', 
                    'tuesday', 'wednesday', 'thursday', 'friday',
                    'saturday', 'sunday')
print(days_of_the_week[5])


