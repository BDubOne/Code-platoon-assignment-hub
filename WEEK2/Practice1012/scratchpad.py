class Dog:
    def __init__(self,name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self._age = age

    def bark(self):
        print(f'{self.name} goes woof!')
    
    def sleep(self):
        print(f"{self.name} is sleeping")

    def play(self):
        print(f'{self.name} is playing with their bone!')

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age

class Cats:
    def __init__(self, name, breed, color, age, claws=True):
        self.name = name
        self.breed = breed
        self.color = color
        self._age = age
        self._claws = claws
    
    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age

    @property
    def get_claws(self):
        return self._claws
    @get_claws.setter
    def set_claws(self, has_claws):
        if isinstance(has_claws, bool):
            self._claws = has_claws

    def bark(self):
        print(f'{self.name} goes woof!')
    
    def sleep(self):
        print(f"{self.name} is sleeping")

    def play(self):
        print(f'{self.name} is playing with their bone!')

   