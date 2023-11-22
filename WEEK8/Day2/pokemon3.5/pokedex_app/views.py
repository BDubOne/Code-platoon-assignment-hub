import json
from django.shortcuts import render
from django.core.serializers import serialize

from .models import Pokemon

def add_pokemon(poke_json):
    new_pokemon = json.loads(json_data)

    new_pokemon[9].get("name")


def get_pokemon(name):

    desired_pokemon = Pokemon.query(name=name)

    serialized_desired_pokemon = serialize("json", [desired_pokemon])
    return serialized_desired_pokemon

# Create your views here.
