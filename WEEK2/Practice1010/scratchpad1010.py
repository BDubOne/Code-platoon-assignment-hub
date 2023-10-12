## Dog Class

class Dog:
    '''Init is an example of a dunder method.
        Another one is the __str__ method. 
        Spend some time practicing dunder methods'''
    def __init__(self, name, breed="Unknown", color="brown"): #Init is short for initialize
        '''Self is in reference to a particular class instance
            Name is the first attribute each instance will have.
            
            Providing default values can prevent errors'''
        self.name = name #This particular(self) dog(class) has a name.
        self._legs = 4 # Attribute does not have to be an argument if it is a constant
        self. breed = breed
        self.color = color

    @property
    def legs(self):
        return self._legs
    
    @legs.setter
    def set_legs(self, new_leg_number):
        if new_leg_number % 2 == 0 and new_leg_number < 5:
            self._legs = new_leg_number
    
    def __str__(self):
        return f"{self.name} is a {self.color} {self.breed} with {self.legs} legs"

        '''Now, Let's add some methods.'''
    def speak(self):
        print(f"{self.name} is barking like crazy!")

# apollo = Dog("Apollo", "GSD", "Black and White") 

'''if I want to account for different orders, I can say what goes where with an "=". To do this, I can also Pass a default
'''
apollo = Dog(name="Apollo", breed="GSD", color="Black and White")    
#apollo.set._legs()
print(apollo) 

apollo.speak() # use instance of class method



'''
### Practicing Decorators ###
def a_decorator(func):
    def nested_func():
        print("Decorator was triggered")
        func()
        print("Decorator is completed")
    return nested_func

@a_decorator
def greeting():
    print("Good afternoon!")

# @a_decorator 
def goodbye(): # Decorator only applies to function immediately following @
    print("Have a good evening!")

greeting()
'''