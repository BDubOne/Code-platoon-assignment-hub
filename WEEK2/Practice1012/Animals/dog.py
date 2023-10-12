from pet import Pet

class Dog(Pet):
    def __init__ (self, name, breed, color, age):
        super().__init__(name, breed, color, age)


    def speak(self):
        print(f'{self.name} goes woof!')
        
    def sleep(self):
        print(f"{self.name} is sleeping")

    def play(self):
        print(f'{self.name} is playing with their bone!')