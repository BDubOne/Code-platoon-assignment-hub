from django.core import validators as v
from django.db import models
from django.utils import timezone


#imports from my code
from .validators import validate_name


class Pokemon(models.Model):
    '''pokemon'''
    name = models.CharField(max_length=255, blank=False, null=True, validators=[validate_name])
    level = models.IntegerField(default=1, validators=[ v.MinValueValidator(1), v.MaxValueValidator(100)])
    date_encountered=models.DateField(default='2008-01-01')
    date_captured=models.DateTimeField(default=timezone.now)
    description = models.TextField(default='Unknown', validators=[v.MinLengthValidator(7), v.MaxLengthValidator(500)])
    captured= models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='pokemon'

    def __str__(self):
        return f"{self.name} {'has been captured' if self.captured else 'is yet to be captured'}"
    
    def change_caught_status(self):
        self.captured=not self.captured
        self.save()

    def set_level(self, new_level):
        self.level=new_level
        self.full_clean_save()
        self.save()

    def full_clean_save(self):
        self.full_clean()
        self.save()

    @property 
    def get_description(self):
        return self.description
    
    @get_description.setter
    def set_description(self, new_description):
        self.description=new_description
        self.full_clean_save()



