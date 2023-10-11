class Student:

    all_students = {}

    id = 1

    def __init__(self, name, email):
        Student.id += 1
        self.name = name
        self._id = Student.id
        self._email = email
        Student.all_students[self._id] = self

       
    def __str__(self):
        return f"{self.name} | {self.get_id} | {self.get_email}"
    
    @property
    def get_id(self):
        return self._id
    
    @get_id.setter
    def set_id(self, new_id):
        if new_id.isnumeric():
            self._id = new_id

    @property
    def get_email(self):
        return self._email
    
    @get_email.setter
    def set_email(self, new_email):
        valid = "@student.org"
        if valid in new_email[:-len(valid)]:
            self._email = new_email
    
    def go_to_school(self):
        return f"{self.name} is going to school"
    
    def start_studying(self):
        return f"{self.name} is studying right now"
 
    
