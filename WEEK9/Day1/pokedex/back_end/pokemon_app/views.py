from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from .models import Pokemon
from .serializers import PokemonSerializer

class AllPokemon(APIView):

    def get(self, request):
        pokemon = PokemonSerializer(Pokemon.objects.order_by('name'), many=True)
        return Response(pokemon.data)
    
    def post(self, request):
        new_pokemon = PokemonSerializer(data = request.data)
        if new_pokemon.is_valid():
            new_pokemon.save()
            return Response(new_pokemon.data, status=HTTP_201_CREATED)
        else:
            return Response(new_pokemon.errors, status=HTTP_400_BAD_REQUEST)

class SinglePokemon(APIView):

    


    

    def get(self, request, id):
        pokemon = None
        
        if type(id) == int:
            pokemon = Pokemon.objects.get(id = id)

        else: 
            pokemon = Pokemon.objects.get(name=id.title())
        
        return Response(PokemonSerializer(pokemon).data)
    
    def put(self, request, id):
        request_body = request.data
        print(f"{SinglePokemon} id {id}: {request_body}")
        if type(id) ==int:
            pokemon=Pokemon.objects.get(id = id)
        else:
            pokemon = Pokemon.objects.get(name = id.title())
        
        
        if 'level_up' in request_body and request_body['level_up']:
            pokemon.level_up
        if 'captured' in request_body and type(request_body['captured']) == bool:
            pokemon.change_caught_status(request_body.get('captured'))
        if 'moves' in request_body:
            pokemon.moves.add(request_body.get('moves'))
        if 'description' in request_body and request_body.get('description'):
            pokemon.description = request_body.get('description')
        if 'type' in request_body and request_body.get('type'):
            pokemon.type = request_body.get('type')

        serialized_pokemon = PokemonSerializer(pokemon, data = request_body, partial = True)
        if serialized_pokemon.is_valid():
            serialized_pokemon.save()
            return Response(status=HTTP_204_NO_CONTENT)
        
        else:
            print(serialized_pokemon.errors)
            return Response(status=HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        pokemon= self.get(self, id)
        pokemon.delete()

        return Response(status=HTTP_204_NO_CONTENT)
        


# Create your views here.
