from django.urls import path
from .views import AllSubjects

urlpatterns = [
    path("", AllSubjects.as_view(), name='all_subjects'),
]