from django.urls import path, include
from .views import AllLists, SingleList


urlpatterns = [
    path('lists/', AllLists.as_view(), name='lists'),
    path('<int:list_id>/', SingleList.as_view(), name='single_list'),
    path('<int:list_id/tasks')
    # path('master/', MasterSignUp.as_view(), name='master'),
    # path("single-list/", LogIn.as_view(), name="login"),
    # path("logout/", LogOut.as_view(), name="logout"),
    # path("info/", Info.as_view(), name="info"),
]