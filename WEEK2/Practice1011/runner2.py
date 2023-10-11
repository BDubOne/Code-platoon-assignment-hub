from scratchpad import Student

def create_a_student():
    name = input("Student's name?   ")
    email = name+"@student.org"
    new_student = Student(name, email) #
    print(Student.all_students)

create_a_student()