from django.core import validators as v
from django.db import models

from .validators import validate_name, validate_student_email, validate_locker_combination

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False, validators = [validate_name])
    student_email = models.EmailField(null=False, blank=False, unique=True, validators =[validate_student_email]) 
    personal_email = models.EmailField(null=False, unique=True)
    locker_number = models.IntegerField(default=1, unique=True, validators = [v.MinLengthValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(default='12-12-12', validators=[validate_locker_combination])
    good_student = models.BooleanField(default=True)

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


    
