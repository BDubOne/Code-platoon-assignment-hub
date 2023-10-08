def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1

main()
""""
if (a == True) and (b == False) and \
    (c == True):
    print("Continuation of statements")

 
    Python Keywords
    False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise

import keyword

print(keyword.kwlist)
"""

import keyword

print(keyword.kwlist)

message = 'Hello, World!'
print(message)

message = 'Good Bye!'
print(message)

''' 
variable_name = value
'''

message = '"Beautiful is better than ugly," said Tim Peters'

print(message)

message = 'It\'s also a valid string' # \ escapes quotes

print(message)

message = r'C:\python\bin' #using r before the string generates a raw string
print(message)

multi_string_message = '''
The way to make 
a string
span multiple
lines
is with 
three quotes
'''
print(multi_string_message)

# f-strings

name = "John"
message = f"Hi {name}"

print(message)

# Concatenate in Python

greeting = 'Good ' 'Morning!'

print(greeting)
greeting = "Good "
time = "Afternoon"

greeting = greeting + time + '!' 
# reassigning variable  can call the previous designation

print(greeting)

str = "Python String" #Printing indexes
print(str[0])
print(str[1])

#To count from the end of a string, use [-1], etc

print(str[-1]) #while it begins at 0 from beginning, the final line is [-1]
print(str[-2])

#Getting string length

str = "Python String"
str_len = len(str)
print(str_len)

#Slicing Strings

str = "Python String"
print(str[0:2])



