from django.shortcuts import render, get_object_or_404
from user_app.views import UserPermissions
from .serializers import Task, TaskSerializer
from list_app.serializers import List, ListSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

class AllTasks(UserPermissions):
    def get(self, request, list_id):
        all_tasks = request.user.lists.get(id = list_id).tasks.all()
        return Response(TaskSerializer(all_tasks, many=True).data)
    
    def post(self, request):
        try:
            data = request.data.copy()
            data['user'] = request.user
            new_task = Task.objects.create(**data)
            new_task.save()
            ser_task = TaskSerializer(new_task)
            return Response(ser_task.data, status=HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response('wrong', status= HTTP_400_BAD_REQUEST)
        
class SingleTask(UserPermissions):
    def get_a_list(self, user, list_id):
        try:
            list = user.lists.get(id = list_id)
            return list
        except Exception as e:
            print(e)
            return Response("OBJECT DOES NOT EXIST", status=HTTP_404_NOT_FOUND)
        
    def get(self, request, list_id):
        list = self.get_a_list(request.user,list_id)
        if list:
            return Response(ListSerializer(list).data)
        return Response("Object does not exist", status=HTTP_404_NOT_FOUND)
    
    def put(self, request, list_id):
        list = self.get_a_list(request.user, list_id)
        if list:
            ser_list = ListSerializer(list, data=request.data, partial=True)
            if ser_list.is_valid():
                ser_list.save()
            return Response(ser_list.data)
        return Response("Object does not exist", status=HTTP_404_NOT_FOUND)
    
    def delete(self, request, list_id):
        list = self.get_a_list(request.user, list_id)
        if list:
            list.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response("Object does not exist", status=HTTP_404_NOT_FOUND)

# Create your views here.
