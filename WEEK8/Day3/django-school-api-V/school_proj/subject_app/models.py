from django.db import models
from django.apps import apps
from django.core import validators as v
from django.core.exceptions import ValidationError as e
from student_app.models import Student




# Create your models here.
class Subject(models.Model):
    subject_name: models.CharField(max_length=250,null=False, blank=False, unique=True)
    professor: models.CharField(max_length=100,null=False, blank=False)
    students: models.ManyToManyField('student_app.Student', related_name='subjects', validators=[v.MinLengthValidator(0), v.MaxLengthValidator(31)])

    def students(self):
        return self.students.all()
    
    def __str__(self):
        return f"{self.subject_name} taught by {self.professor}"
    
    def add_a_student(self, student_id):
        try:
            student = Student.objects.get(pk=student_id)
            self.students.add(student)
        except models.ExistingRelatedObject:
            raise e("This subject is full!")
        
    def drop_a_student(self, student_id):
        try:
            student=Student.objects.get(pk=student_id) 
            self.students.remove(student)
        except Student.DoesNotExist:
            raise e("This subject is empty!")