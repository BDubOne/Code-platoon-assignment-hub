from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject_name', 'professor')

class SubjectAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'