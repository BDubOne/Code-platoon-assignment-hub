import csv
from classes.person import Person

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    
    def __repr__(self):
        return f'''{self.name}
----------
age: {self.age}
id: {self.school_id}'''
    
    @classmethod
    def all_members(cls):
        students = []
        with open('./data/students.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_student = cls(**row)
                students.append(new_student)

        return students