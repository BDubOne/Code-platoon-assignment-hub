from .models import Subject
from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    grade_average = serializers.SerializerMethodField()
    student_grades = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ["subject_name", "professor", "students", "grade_average", "student_grades"]

    def get_students(self, obj):
        return obj.students.count()
    
    def get_student_grades(self, instance):
        grades = instance.grades.all()

        student_grades = {}

        for grade in grades:
            student_id = grade.student.id
            student_grades[student_id] = grade.grade
        return student_grades

    
    def get_grade_average(self, obj):
        grades = obj.grades.all()
        if grades:
            return round(sum([x.grade for x in grades])/len(grades),2)
        else:
            return 100

