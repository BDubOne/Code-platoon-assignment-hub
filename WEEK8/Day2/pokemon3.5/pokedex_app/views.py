import json
from django.shortcuts import render
from .serializers import PokemonSerializer
from .models import Pokemon
from django.http import HttpResponse

from .models import Pokemon

def add_pokemon(poke_json):
    new_pokemon = json.loads(json_data)

    new_pokemon[9].get("name")


def get_pokemon(name):

    desired_pokemon = Pokemon.query(name=name)

    serialized_desired_pokemon = serialize("json", [desired_pokemon])
    return serialized_desired_pokemon

def pokemon_hello_world(request):
    a_pokemon=Pokemon.objects.first()
    return HttpResponse(f"a pokemon name is {a_pokemon.name}")
# Create your views here.
