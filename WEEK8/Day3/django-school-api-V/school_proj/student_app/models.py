from django.db import models
from django.core import validators as v
from django.core.exceptions import ValidationError as e
from django.apps import apps
from .validators import (
    validate_combination_format,
    validate_name_format,
    validate_school_email,
)





# Create your models here.
class Student(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_name_format]
    )
    student_email = models.EmailField(
        null=False, blank=False, unique=True, validators=[validate_school_email]
    )
    personal_email = models.EmailField(null=False, blank=False, unique=True)
    locker_number = models.IntegerField(
        default=110,
        null=False,
        blank=False,
        unique=True,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(200)],
    )
    locker_combination = models.CharField(
        default="12-12-12",
        null=False,
        blank=False,
        max_length=255,
        validators=[validate_combination_format],
    )
    good_student = models.BooleanField(default=True)
    subjects = models.ManyToManyField('subject_app.Subject', related_name='students', validators=[v.MinLengthValidator(0), v.MaxLengthValidator(8)])

    def subjects(self):
        return self.subjects.all()
    
    def __str__(self):
        return self.name

    def add_subject(self, subject_id):
        try:
            self.subjects.add(subject_id)
        except:
            raise e("This students class schedule is full!")

    def remove_subject(self, subject_id):
        try:
            self.subjects.pop(subject_id)
        except:
            raise e("This students class schedule is empty!")
