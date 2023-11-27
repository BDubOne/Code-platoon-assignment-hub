from django.db import models
from django.utils import timezone

from django.core import validators as v
from .validators import validate_name

from move_app.models import Move

class Pokemon(models.Model):

    name = models.CharField(max_length=200, blank=False, null=False, validators=[validate_name])

    level = models.IntegerField(default=1, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])

    date_encountered=models.DateField(default='2008-01-01')

    date_captured = models.DateTimeField(default=timezone.now)

    description = models.TextField(default="Unknown", validators=[v.MinLengthValidator(7), v.MaxLengthValidator(150)])

    captured = models.BooleanField(default = False)
    moves = models.ManyToManyField(Move, related_name='pokemon')

    def __str__(self):
        return f"{self.name} {'has been captured' if self.captured else 'is yet to be caught'}"
    
    def level_up(self):
        self.level += 1
        self.save()

    def change_caught_status(self):
        self.captured = not self.captured
        self.save()

# Create your models here.
