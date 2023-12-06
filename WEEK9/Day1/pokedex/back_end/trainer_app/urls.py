from django.urls import path
from .views import SignUp, LogIn, LogOut, Info, MasterSignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('master/', MasterSignUp.as_view(), name='master'),
    path("login/", LogIn.as_view(), name="login"),
    path("logout/", LogOut.as_view(), name="logout"),
    path("info/", Info.as_view(), name="info"),
]