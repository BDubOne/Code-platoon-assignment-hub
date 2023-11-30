from rest_framework import serializers
from .models import Student
from subject_app.serializers import SubjectSerializer
from grade_app.models import Grade


class StudentSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()
    
    class Meta:
        model = Student
        fields = fields = [
            "id",
            "name",
            "student_email",
            "personal_email",
            "locker_number",
            "locker_combination",
            "good_student",
            "subjects"

        ]

    def get_subjects(self, instance):

        grades = Grade.objects.filter(student=instance)

        subjects = {}

        for grade in grades:
            subjects[grade.a_subject.subject_name] = grade.grade
            return subjects

class StudentAllSerializer(serializers.ModelSerializer):
    # subjects = SubjectSerializer(many=True)
    student_subjects = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "student_email",
            "personal_email",
            "locker_number",
            "locker_combination",
            "good_student",
            "subjects"

        ]
    def get_subjects(self, instance):
        grades = Grade.objects.filter(student=instance)

        subjects = {}

        for grade in grades:
            subjects[grade.a_subject.subject_name] = grade.grade
            return subjects
