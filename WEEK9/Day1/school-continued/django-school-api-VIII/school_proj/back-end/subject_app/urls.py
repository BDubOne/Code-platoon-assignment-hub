from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import All_subjects, A_subject, SubjectViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('',All_subjects.as_view(), name='all_subjects'),
    path('<str:subject>/', A_subject.as_view(), name='a_subject'),
    
]
