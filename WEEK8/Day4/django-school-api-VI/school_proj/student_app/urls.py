from django.urls import path, register_converter
from .views import AllStudents, SingleStudent
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, 'int_or_str')

urlpatterns = [
    path("", AllStudents.as_view(), name='all_students'),

    path('<int_or_str:id>/', SingleStudent.as_view(), name='single_student')
]