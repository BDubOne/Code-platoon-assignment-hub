from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Move
from .serializers import MoveSerializer

@api_view(['GET'])
def get_moves(request):
    moves = Move.objects.all()
    serializers = MoveSerializer(moves, many=True)
    return Response(serializer.data)

# Create your views here.
