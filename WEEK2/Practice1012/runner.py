from Animals.dog import Dog
from Animals.cat import Cat

apollo = Dog("Apollo", "GSD", "Gold", 3)

socks = Cat("socks", "tabi", "orange", 3)

print(socks.get_age)
socks.set_age=5
print(socks.get_age)
socks.play()
socks.speak()
apollo.speak()