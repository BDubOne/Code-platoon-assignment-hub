from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age, password, role):
        self.name = name
        self.age = age
        self.password = password
        self.role = role

    @abstractmethod
    def all_members(self):
        pass