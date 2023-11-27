from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class AllStudents(APIView):
    """Students APIView"""

    def get(self, request):
        students = StudentSerializer(Student.objects.all(), many=True)
        return Response(students.data)
    
class SingleStudent(APIView):
    def get(self, request, id):

        student = None

        if type(id) == int:
            student = Student.objects.get(id = id)
        
        else: 
            student = Student.objects.get(name=id.title())
        
        return Response(StudentSerializer(student).data)
    



# Create your views here.
