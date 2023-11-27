from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ["name", "student_email", "locker_number", "subjects"]

    def get_subjects(self, instance):
        subjects = instance.subjects.all()
        subject_names = [subject.subject_name for subject in subjects]
        return subject_names
    


            