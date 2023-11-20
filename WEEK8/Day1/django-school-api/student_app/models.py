from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    student_email = models.EmailField(max_length=250,default=None, null=False, blank=False, unique=True)
    personal_email= models.EmailField(max_length=250, unique=True)
    locker_number = models.IntegerField(default=1, unique=True)
    locker_combination=models.CharField(max_length=100)
    good_student=models.BooleanField(default=True)



