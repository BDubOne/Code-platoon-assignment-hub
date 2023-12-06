from django.db import models
from user_app.models import User

# Create your models her


class List(models.Model):
    list_name=models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lists")
    completed =models.BooleanField(default=False)
