from django.core.exceptions import ValidationError
import re


def validate_name(name):
    error_message = "Improper name format"

    regex = r'^[A-Z][a-z]*$'

    good_name = re.match(regex, name)

    if good_name:
        return name
    
    else:
        raise ValidationError(error_message, params = { 'name' : name })
    

def validate_type(value):
    allowed_types = ['rock', 'normal', 'bug', 'ghost', 'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy', 'unknown', 'shadow']
    
    if value.lower() not in allowed_types:
        raise ValidationError(f"Invalid type: {value}. Please choose from {', '.join(allowed_types)}.")