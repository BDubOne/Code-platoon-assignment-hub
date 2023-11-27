from django.urls import path
from .views import geometry_hello_world, circle_area

urlpatterns = [
    path("", geometry_hello_world),
    path("circle/", circle_area),
]