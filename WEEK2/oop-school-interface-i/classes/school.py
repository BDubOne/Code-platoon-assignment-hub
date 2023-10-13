from classes.staff import Staff
from classes.student import Student


class School:
    def __init__(self, name):
        self.name = name   
        self.students = Student.all_students() 
        self.staff = Staff.all_staff() #List of student instances

    
    def list_students(self):
        for idx, stud in enumerate(self.students):
            print(f"{idx + 1} {stud.name} {stud.school_id}")

    def find_student_by_id(self, student_id):
        for stud in self.students:
            if student_id == stud.school_id:
                return stud
        
        return f"{student_id} does not match any students"
            

    def add_student(self, student_data):
        #create student through kwargs
        new_student = Student(**student_data)
        self.students.append(new_student)

    # def remove_student(self, student_data):

            
  


