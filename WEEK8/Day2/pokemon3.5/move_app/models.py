from django.db import models
from django.core import validators as v


from .validators import validate_move_name

class Move(models.Model):



    name= models.CharField(blank=False, null=False,validators = [validate_move_name])

    accuracy = models.PositiveIntegerField( default=20, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])

    pp = models.PositiveIntegerField(
        default=20,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(30)])

    power = models.PositiveIntegerField(default=80, validators=[v.MaxValueValidator(100)])

    def __str__(self):
        return f"|{self.name} | {self.accuracy} | {self.pp} | {self.power}|"
    



