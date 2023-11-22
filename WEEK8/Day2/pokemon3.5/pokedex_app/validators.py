
import re
from django.core.exceptions import ValidationError


def validate_name(name):
    """validate name is just letter and starts with capital letter"""
    error_message="Improper name format"
    
    regex = r'^[A-Z][a-z]*$'

    good_name = re.match(regex, name)

    if good_name:
        return name
    else: 
        raise ValidationError(error_message, params={'name': name})