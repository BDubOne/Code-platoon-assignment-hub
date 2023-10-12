class Parent:
    def __init__(self, job, name) -> None:
        self.job = job
        self.name = name

class Father(Parent):
    def __init__(self, job, name):
        super().__init__(job, name)

class Mother(Parent):
    def __init__(self, job, name):
        super().__init__(job, name)


class Child:
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother

john = Father("SE", "john")
mary = Mother("SE", "mary")

billy = Child("Billy", john, mary)

print(billy.name)
print(billy.father.name)