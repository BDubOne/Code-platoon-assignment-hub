from django.shortcuts import render
from django.http import HttpResponse
import math

# Create your views here.

def geometry_hello_world(request):
    return HttpResponse("Geometry Hello World")

def circle_area(response):
    circle_area = math.pi * (2 ** 2)
    return HttpResponse(f"Circle Area is {circle_area}")


