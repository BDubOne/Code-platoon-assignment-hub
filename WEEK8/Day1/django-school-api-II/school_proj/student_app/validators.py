import re 
from django.core.exceptions import ValidationError

def validate_name(name):
    error_message= 'Imporper name format'
    regex = r'^[A-Z][a-z]*$'
    good_name=re.match(regex,name)

    if good_name:
        return name
    else:
        raise ValidationError(error_message, params = { 'name': name })

def validate_student_email(student_email):
    error_message='Improper student_email format'
    regex=r'.+@school\.com$'
    good_student_email = re.match(regex, student_email)

    if good_student_emil:
        return student_email
    else:
        raise ValidationError(error_message, paramse = { 'student_email': student_email })

def validate_locker_combination(locker_combination):
    error_message = 'Improper locker_combination format'
    regex = r'^\d+-\d+$'
    good_locker_combination = re.match(regex, locker_combination)

    if good_locker_combination:
        return locker_combination
    else:
        raise ValidationError(error_message, params = { 'locker_combination': locker_combination })

