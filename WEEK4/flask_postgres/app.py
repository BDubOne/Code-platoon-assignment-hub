from flask import Flask, jsonify

""" # flask is a module. Flask is a class, enabling me to run a python browser. jsonify is a class enabling me to format information from python into JSON Objects so that they can be utilized by JS-based webpages."""

from flask_sqlalchemy import SQLAlchemy
"""#SQLAlchemy is a class that allows me to translate information from SQL databases into Python format so that it can be manipulated from a py file"""

app = Flask(__name__)#This identifies my app as a flask server with a name to be defined

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bryanbartell:Jellytime8@localhost/students'

#This configures my flask server to retrieve information from my SQL database using my postgresql credentials on my local server


db = SQLAlchemy(app)
"""Here, I am defining my application, which will provide a flask-based server with information from my SQL database.
"""

class Student(db.Model):
    """this identifies the format my SQL data will take when it runs through the SQLAlchemy Python interpreter"""
    id = db.Column(db.Integer, primary_key = True) #primary_key is the same as PRIMARY KEY in sql format
    first_name = db.Column(db.String(20)) #Python does not require me to designate variable string-lengths
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer) # I need to find out whether I can use Int and Str for String and Integer when using this module
    grade = db.Column(db.String(1))

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
        # return jsonify({
        #     'id': self.id,
        #     'first_name': self.first_name,
        #     'last_name': self.last_name,
        #     'age': self.age,
        #     'grade': self.grade})
    
@app.route('/students', methods=['GET']) # I route my  app to be able to retrieve information from the database, but not to be able to post, delete, or place information. This may need to change if I want to be able to add to the JSON through the server.
#The particular route is <ip-address>/students
def get_all_students():
    """This is a method to retrieve all student data from SQL in JSON format"""
    students = Student.query.all()
    formatted_students = []
    for stud in students:
        formatted_students.append(
            {
            "id": stud.id,
            "first_name": stud.first_name,
            "last_name": stud.last_name,
            "age": stud.age,
            "grade": stud.grade,
            }
        )
    return jsonify(formatted_students)

@app.route('/old_students', methods = ['GET'])
def get_old_students():
    """This is a method to retrieve all student data for students over the age of 20 from SQL in JSON format"""
    students = Student.query.filter(Student.age > 20) #get used to this method
    old_students = [] #may be able to tweak repr dunder to skip this step
    for stud in students:
        old_students.append(
            {
            "id": stud.id,
            "first_name": stud.first_name,
            "last_name": stud.last_name,
            "age": stud.age,
            "grade": stud.grade,
            }
        )
    return jsonify(old_students)
   

@app.route('/young_students', methods = ['GET'])
def get_young_students():
    """This is a method to retrieve all student data for students under the age of 21 from SQL in JSON format and put it on the server as "<ip>/young_students"""
    students= Student.query.filter(Student.age < 21) #get used to this method
    young_students = [] #may be able to tweak repr dunder to skip this step
    for stud in students:
        young_students.append(
            {
            "id": stud.id,
            "first_name": stud.first_name,
            "last_name": stud.last_name,
            "age": stud.age,
            "grade": stud.grade,
            }
        )
    return jsonify(young_students)

@app.route('/advanced_students', methods = ['GET'])
def get_advanced_students():
    """This is a method to retrieve all student data for students under the age of 21 from SQL in JSON format and put it on the server as "<ip>/young_students"""
    students= Student.query.filter(Student.age < 21, Student.grade == 'A') #get used to this method
    advanced_students = [] #may be able to tweak repr dunder to skip this step
    for stud in students:
        advanced_students.append(
            {
            "id": stud.id,
            "first_name": stud.first_name,
            "last_name": stud.last_name,
            "age": stud.age,
            "grade": stud.grade,
            }
        )
    return jsonify(advanced_students)

@app.route('/student_names', methods=['GET'])
def get_student_names():
    """This is a method to retrieve only the first_name and last_name inJSON format"""
    students = Student.query.all()
    student_names = []
    for stud in students:
        student_names.append(
            {
            
            "first_name": stud.first_name,
            "last_name": stud.last_name,
          
            }
        )
    return jsonify(student_names)

@app.route('/student_ages', methods=['GET'])
def get_student_ages():
    """
    his function creates a new variable combining the first_name and last_name into student_name and returns the name and age for each student in the database
    """
    students = Student.query.all()
    student_ages = []
    for stud in students:
        student_name = f"{stud.first_name} {stud.last_name}" #declaring student_name variable
        student_ages.append(
            {
            'student_name': student_name, #Formatting return
            'age': stud.age,

            }
        )
    return jsonify(student_ages)

app.run(debug = True)#Debug allows the server to be interrupted and refresh if I change this file instead of crashing.





