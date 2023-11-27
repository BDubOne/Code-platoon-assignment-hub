from django.db import models
from django.core import validators as v
from django.apps import apps

from subject_app.models import Subject
from student_app.models import Student

class Grade(models.Model):
    grade: models.DecimalField(null=False, blank=False, validators=[v.MaxValueValidator(100.00), v.MinValueValidator(0.00)])
    a_subject= models.ForeignKey(Subject, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"Grade for {self.student} in {self.a_subject} is {self.grade}"



# Create your models here.
