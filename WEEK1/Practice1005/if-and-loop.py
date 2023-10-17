#Conditional Logic
def can_drink_beer(age, country):
    if age >= 21 or age >= 18 and country == "Canada" :
        return True
    elif country == 'Antarctica':
        return True
    else:
        return False
    

print(can_drink_beer(21, 'USA'))

#Looping

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for x in my_list:
    print(x)

#python range
one_to_ten = range(11)
# print(one_to_ten)

# loop through range

#for x in one_to_ten:
 #   print(x)

for x in range(10):
    print(x)

#loop through list and get index

for index, el in enumerate(my_list): # el is element. enumerate adds an index
    print(index, el)

my_dict = {
    "donuts": "yummy",
    "green beans": "gross",
}

for key in my_dict:
    print(my_dict[key])

for value in my_dict.values():
    print(value)


    # while loops

    x = 9
    while x > 0:
        print(x)
        x = x - 1



    