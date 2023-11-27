from django.urls import path, register_converter

from .views import AllPokemon, SinglePokemon
from .converters import IntoOrStrConverter


register_converter(IntoOrStrConverter, 'int_or_str')

urlpatterns = [
    path('', AllPokemon.as_view(), name='all_pokemon'),
    path('<int_or_str:id>/', SinglePokemon.as_view(), name='a_pokemon')
]