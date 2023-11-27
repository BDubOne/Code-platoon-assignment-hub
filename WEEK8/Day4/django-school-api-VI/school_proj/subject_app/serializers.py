from rest_framework import serializers
from .models import Subject
from grade_app.models import Grade


class SubjectSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    grade_average = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ["subject_name", "professor", "students", "grade_average"]

    def get_students(self, instance):
        students = instance.students.all()
        student_names= [student.name for student in students]
        return len(student_names)
    
    def get_grade_average(self,grades):
        grades = Grade.a_subject.filter("subject_name")
        grade_average = sum(grades.grade)/len(grades)
        return grade_average