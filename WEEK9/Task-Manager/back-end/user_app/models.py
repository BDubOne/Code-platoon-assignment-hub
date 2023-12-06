from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    age= models.PositiveIntegerField(default=18)
    display_name= models.CharField(null=True, blank=True)
    address = models.TextField()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = []


# Create your models here.
