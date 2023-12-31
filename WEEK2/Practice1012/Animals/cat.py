from pet import Pet

class Cat(Pet):
    def __init__(self, name, breed, color, age, claws=True, favorite_toy="string ball"):
        super().__init__(name, breed, color, age)
        self._claws = claws
        self._favorite_toy = favorite_toy

    
    @property
    def get_claws(self):
        return self._claws
    @get_claws.setter
    def set_claws(self, has_claws):
        if isinstance(has_claws, bool):
            self._claws = has_claws

    def speak(self):
        print(f'{self.name} goes meow meow!')

    
    def play(self):
        print(f'{self.name} is playing with their ball of string!')