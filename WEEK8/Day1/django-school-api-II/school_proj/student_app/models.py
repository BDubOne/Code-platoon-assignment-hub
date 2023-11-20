from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False)
    student_email = models.EmailField(null = False, blank = False)
    personal_email = models.EmailField(null = False, blank = False)
    locker_number = models.IntegerField(default=1, null = False, blank = False)
    locker_combination = models.CharField(max_length=255, null = False, blank = False)
    good_student = models.BooleanField()

    def __str__(self):
        return f'{self.name} - {self.student_email} - {self.locker_number}'
    
    @property
    def get_combination(self):
        return self.locker_combination
    @get_combination.setter
    def set_combination(self, new_combination):
        self.locker_combination=new_combination

    @property 
    def get_good_student(self):
        return self.good_student
    @get_good_student.setter
    def set_good_student(self, new_good_student):
        if isinstance(new_good_student, bool):
            self.good_student = new_good_student


    
