from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': '18', 'grade': 'A'},
    {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': '19', 'grade': 'B'},
    {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': '20', 'grade': 'C'},
    {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': '18', 'grade': 'A'},
    {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': '19', 'grade': 'B'}
]
"https://127.0.0.1:5000/students"
@app.route('/students', methods=['GET']) # GET PUT POST DELETE
def get_students():
    return jsonify(students)

@app.route('/old_students', methods=['GET'])
def get_old_students():
    old_students =[]
    for index in range(len(students)):
        if students[index]['age'] > 20:
            old_students.append(students[index])
    return jsonify(old_students)

@app.route('/young_students', methods=['GET'])
def get_young_students():
    young_students =[]
    for index in range(len(students)):
        if students[index]['age'] < 21:
            young_students.append(students[index])
    return jsonify(young_students)

@app.route('/advance_students', methods=['GET'])
def get_advance_students():
    advance_students =[]
    for index in range(len(students)):
        if students[index]['age'] < 21 and students[index]['grade'] == 'A':
            advance_students.append(students[index])
    return jsonify(advance_students)

@app.route('/student_names', methods=['GET'])
def get_student_names():
    student_names =[]
    for index in range(len(students)):
        student_names.append(f"first_name: {students[index]['first_name']}, last_name: {students[index]['last_name']}")
    return jsonify(student_names)

@app.route('/student_ages', methods=['GET'])
def get_student_ages():
    student_ages =[]
    for index in range(len(students)):
        student_name = f"{students[index]['first_name']} {students[index]['last_name']}"
        student_ages.append({student_name: students[index]['age']})
    return jsonify(student_ages)



app.run(debug=True)
   
