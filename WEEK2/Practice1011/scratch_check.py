from scratchpad import Student

student_one = Student("Joe", "joe@school.org")
print(student_one)

student_two = Student("Bryan", "bryan@student.org)")

student_three = Student("Adam", "adam@student.org")

for student in Student.all_students:
    student_instance = Student.all_students[student]
    print(f"{student_instance.name} | {student_instance.get_email}")