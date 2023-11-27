from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MoveSerializer
from .models import Move

class AllMoves(APIView):

    def get(self, request):
        moves = MoveSerializer(Move.objects.all(), many=True)
        return Response(moves.data)
    
class SingleMove(APIView):
    def get(self, request, name):
        move = Move.objects.get(name=name.title())
        return Response(MoveSerializer(move).data)

# Create your views here.
