from classes.school import School 

school = School('Ridgemont High') 

while True:
    mode = input('''
                 Ridgemont High Student Interface 
--------------------------------
Welcome, Richard. Your access level is Principal
    What would you like to do?
    Options:
    1 List All Students
    2 View Individual Student <student_id>
    3 Add a Student
    4 Remove a Student <student_id>
    5 Quit''')

    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:')
        student = school.find_student_by_id(student_id)
        if student:
            print(student)
    elif mode == '3':
        student_data = {'role': 'student'}
        student_data['name']     = input('Enter student name:\n')
        student_data['age']      = input('Enter student age: \n')
        student_data['school_id']= input('Enter student school id: \n')
        student_data['password'] = input('Enter student password: \n')

        school.add_student(student_data)
    
    elif mode == '4':
        student_id = input('Enter student id:\n')
        student = school.find_student_by_id(student_id)
        if student:
            school.students.remove(student)
            print('student was deleted!')
        
    
    elif mode == '5':
        print('Goodbye!')
        break
