from django.core.exceptions import ValidationError as e
from django.utils import timezone

def validate_relay(relay):
    error_message = f"'{relay}' value must be either True or False."
    if type(relay) != bool:
        raise e(error_message, params={ 'relay', relay })
    
def validate_stroke(stroke):
    error_message= f"{stroke}is not a valid stroke"
    valid_strokes= ['front crawl', 'butterfly', 'breast', 'back','freestyle']

    if stroke not in valid_strokes:
        raise e(error_message, params={ 'stroke', stroke })
    else:
        return stroke
    
def validate_record_date(record_date):
    error_message ="Can't set record in the future."

    if record_date > timezone.now():
        raise e(error_message, params={ 'record_date', record_date })
    