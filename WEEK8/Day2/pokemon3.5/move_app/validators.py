import re
from django.core.exceptions import ValidationError

def validate_move_name(name):
    regex = r"^[a-zA-Z]+ ?[a-zA-Z]+$"
    good_name = re.match(regex, name)
    if good_name:
        return name
    
    else:
        raise ValidationError("Improper Format")
