import csv

class Student:
    def __init__(self, name, age, role, school_id, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        students = []
        with open('./data/students.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_student = cls(**row)
                students.append(new_student)
        # print(students)
        return students