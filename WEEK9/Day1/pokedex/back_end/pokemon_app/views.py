from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pokemon
from .serializers import PokemonSerializer

class AllPokemon(APIView):

    def get(self, request):
        pokemon = PokemonSerializer(Pokemon.objects.order_by('name'), many=True)
        return Response(pokemon.data)

class SinglePokemon(APIView):

    def get(self, request, id):
        pokemon = None
        
        if type(id) == int:
            pokemon = Pokemon.objects.get(id = id)

        else: 
            pokemon = Pokemon.objects.get(name=id.title())
        
        return Response(PokemonSerializer(pokemon).data)

# Create your views here.
