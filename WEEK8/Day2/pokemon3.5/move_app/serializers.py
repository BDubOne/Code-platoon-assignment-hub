from rest_framework import serializers
from .models import Move

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'
    
    def create(self, validated_data):
        name = validated_data.get('name')
        accuracy = validated_data.get('accuracy', 20)
        pp = validated_data.get('pp', 20)
        power = validated_data.get('power', 80)

        move = Move.objects.create(
            name=name,
            accuracy=accuracy,
            pp=pp,
            power=power
        )
        return move


    
