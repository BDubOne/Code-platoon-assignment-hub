from django.shortcuts import render, get_object_or_404
from user_app.views import UserPermissions
from .serializers import List, ListSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

class AllLists(UserPermissions):
    def get(self, request):
        lists = ListSerializer(request.user.lists.all(), many = True)
        return Response(lists.data)
    
    def post(self, request):
        try:
            data = request.data.copy()
            data['user'] = request.user
            new_list = List.objects.create(**data)
            new_list.save()
            ser_list = ListSerializer(new_list)
            return Response(ser_list.data, status=HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response('wrong', status= HTTP_400_BAD_REQUEST)
        
class SingleList(UserPermissions):
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
