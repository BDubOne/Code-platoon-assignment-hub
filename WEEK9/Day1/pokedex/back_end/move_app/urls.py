from django.urls import path
from .views import AllMoves, SingleMove

urlpatterns = [
    path('', AllMoves.as_view(), name="all_moves"),
    path("<str:name>/", SingleMove.as_view(), name="a_move"),
]