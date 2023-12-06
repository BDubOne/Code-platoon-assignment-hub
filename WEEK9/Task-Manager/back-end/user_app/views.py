from django.shortcuts import render

# Create your views here.
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

class SignUp(APIView):
    def post(self, request):
        try:
            data = request.data.copy()
            data['username'] = request.data['email']
            user = User.objects.create_user(**data)
            token = Token.objects.create(user=user)
            return Response(
                {'user': user.email, 'token': token.key},
                status=HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response("something wrong",status=HTTP_400_BAD_REQUEST)
        

class LogIn(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            user = authenticate(username = email, password = password)
            if user:
                token, created = Token.objects.get_or_create(user = user)
                return Response({'user':user.email, 'token': token.key})
            return Response(status=HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)
            return Response("something wrong", status=HTTP_400_BAD_REQUEST)

class UserPermissions(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email": request.user.email})

class LogOut(UserPermissions):

    def post(self, request):
        user = UserSerializer(request.user)
        request.user.auth_token.delete()
        return Response(user.data)
    
class Info(UserPermissions):
    def get(self, request):
        user = UserSerializer
        return Response(user.data)
    
    def put(self, request):
        user = UserSerializer(request.user, data=request.data, partial = True)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(user.errors, status=HTTP_400_BAD_REQUEST)
    

    

            
