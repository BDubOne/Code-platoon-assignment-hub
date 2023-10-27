from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bryanbartell:Jellytime8@localhost/my_school'

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__= 'students'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject_id= db.Column(db.Integer, db.ForeignKey('subjects.id'))


class Subject(db.Model):
    __tablename__='subjects'
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(25))  
    teacher = db.relationship("Teacher", backref="subject", lazy=True,uselist=False)
    student_list = db.relationship("Student", backref="subject", lazy=True)
                                  

@app.route('/students', methods=['GET'])
def get_all_students():

    students = Student.query.all()
    student_list = [
        {
            "id" : student.id,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "age": student.age,
            "class": {
                "subject": student.subject.subject,
                "teacher" : f"{student.subject.teacher.first_name} {student.subject.teacher.last_name}",
            },
        }
        for student in students
    ]
    return jsonify(student_list)

@app.route("/subjects", methods=["GET"])
def get_subjects():
    subjects = Subject.query.all()
    subject_list = [
        {
            "subject": subject.subject,
            "teacher": f"{subject.teacher.first_name} {subject.teacher.last_name}",
            "students": [
                f"{student.first_name} {student.last_name}"
                for student in subject.student_list
            ],
        }
        for subject in subjects
    ]
    return jsonify(subject_list)

@app.route("/teachers", methods=["GET"])
def get_teachers():
    teachers = Teacher.query.all()
    teacher_list = [
        {
            "first_name": teacher.first_name,
            "last_name": teacher.last_name,
            "age": teacher.age,
            "subject": {
                "subject": teacher.subject.subject,
                "students": [
                    f"{student.first_name} {student.last_name}"
                    for student in teacher.subject.student_list
                ],
            },
        }
        for teacher in teachers
    ]
    return jsonify(teacher_list)

@app.route("/", methods=["GET"])
def home():
    return jsonify("Home Page")
    



app.run(debug = True)
