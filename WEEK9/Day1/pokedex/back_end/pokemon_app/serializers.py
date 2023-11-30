from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    moves = serializers.SerializerMethodField()

    class Meta:
        model = Pokemon
        fields = '__all__'

    def get_moves(self, instance):
        moves = instance.moves.all()
        move_names = [move.name for move in moves]
        return move_names