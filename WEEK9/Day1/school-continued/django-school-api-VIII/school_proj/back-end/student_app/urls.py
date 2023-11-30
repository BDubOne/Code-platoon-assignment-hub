from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import All_students, A_student, StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("", All_students.as_view(), name='all_students'),
    path("<int:id>/", A_student.as_view(), name="a_student"),
]
