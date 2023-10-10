class Student:
    
    def __init__(self, name, grade, email, legs, id):
        self.name = name
        self.grade = grade
        self._email = email
        self._legs = legs
        self._id = id
    
    @property
    def email(self):
        return self._email

    @email.setter
    def set_email(self, new_email):
        if type(new_email) == string and "@school.org" in new_email:
            self._email = new_email
    
    @property
    def legs(self):
        return self._legs

    @property
    def id(self):
        return self._id
    
    @id.setter
    def set_id(self, new_id):
        if len(new_id) == 8 and not new_id[0].isnumeric():
            self._id = new_id
    
    def __str__(self):
        return f"{self.name} | {self.grade} | {self.id}"
    
    def go_to_class(self):
        print(f"{self.name} is in class")

student_one = Student("Bryan", "Code Platoon", "shibbidy@school.org", 2, "b3204734")

print(student_one)

student_one.set_id = "m34b5678"
print(student_one.id)