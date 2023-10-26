from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bryanbartell:Jellytime8@localhost/my_school'

db = SQLAlchemy(app)


class Subject(db.Model):
    __tablename__='subjects'
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(25))
    student_list = db.relationship("Student", backref="subject", lazy=True)
    teacher = db.relationship("Teacher", backref="subject", lazy=True,uselist=False)
                               

    def __str__(self):
        return f"{self.subject}"

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject_id= db.Column(db.Integer, db.ForeignKey('subjects.id'))
 




    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(db.Model):
    __tablename__= 'students'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    # subject_relation = db.relationship('Subject', foreign_keys=[subject])
    # teacher_relation = db.relationship('Teacher', seconday='subject_teacher_association', viewonly=True)

    @property
    def subject_name(self):
        if self.subject_relation:
            return self.subject_relation.subject
        else:
            return None
        
    @property 
    def teacher_name(self):
        if self.teacher_relation:
            return', '.join([f"{teacher.first_name} {teacher.last_name}" for teacher in self.teacher_relation])
        else:
            return None


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

subject_teacher_association = db.Table(
    'subject_teacher_association',
    db.Column('subject_id', db.Integer, db.ForeignKey('subjects.id')),
    db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id'))
)

        

@app.route('/students', methods=['GET'])
def get_all_students():

    students = Student.query.all()
    formatted_students = []

    for stud in students:
        student_subject = stud.subject_relation
        student_teacher = None
        for teacher in student_subject.teacher_relation:
            if teacher.subject_relation == student_subject:
                student_teacher = teacher
                break
        stud_data = {
            "id" : stud.id,
            "first_name": stud.first_name,
            "last_name": stud.last_name,
            "age": stud.age,
            "class": {
                "subject": student_subject.subject,
                "teacher" : f"{student_teacher.first_name} {student_teacher.last_name}"
            }
        }
        formatted_students.append(stud_data)
    return jsonify(formatted_students)

app.run(debug = True)
