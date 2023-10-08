# string methods

name = 'jonathan'
print(name.capitalize()) #cap first letter

print("greg young".replace('g', '12345'))

# is a key in a dictionary?

another_dict = {
    "green beans": "gross",
    "donuts": "yummy",
}
if 'donuts' in another_dict.keys():
    print('we have donuts')
else:
    print('no donuts')

# is value in dictionary

if 'yummy' in another_dict.values():
    print('people like it')
else:
    print('no one likes it')


    # Switch cases
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "Java":
        print("You can become a mobile app developer")
    
    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")    
    
    case _:
        print("The language doesn't matter, what matters is solving problems.")
#Underscore is used as default

## Lambda Functions ##



