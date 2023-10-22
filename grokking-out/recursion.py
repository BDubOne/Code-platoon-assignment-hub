
###Box of Boxes, looking for a key###


#while Loop
"""def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box()
            pile.append(item)
        elif item.is_a_key():
print "found the key"""


#Recursion
"""def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print( "found the key!")"""

#CountDown

def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)

# print(countdown(5))

###Call Stack Name Visual####
def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you, " + name + "?")
def bye():
    print("Ok bye!")

# greet("Bryan")


###Factorial ###
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

# print(fact(6))
