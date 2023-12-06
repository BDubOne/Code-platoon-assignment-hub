from rest_framework.serializers import ModelSerializer
from .models import List
from task_app.serializers import TaskSerializer


class ListSerializer(ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = List
        fields = ['list_name', 'completed', 'tasks']
