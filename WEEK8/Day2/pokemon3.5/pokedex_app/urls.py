from django.urls import path
from .views import pokemon_hello_world

urlpatterns = [
   
    path("", pokemon_hello_world),
]