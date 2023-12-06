from django.db import models
from list_app.models import List

class Task(models.Model):
    task_name = models.CharField()
    completed = models.BooleanField(default=False)
    task_description=models.TextField()
    parent_list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="tasks"
        )
    

# Create your models here.
