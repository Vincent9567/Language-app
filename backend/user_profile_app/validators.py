from django.core.exceptions import ValidationError
import re

def validate_name(name):

    error_message = "Improper name format"

    regex = r'(?=.*\d{2,})(?=.*[a-z])(?=.*[A-Z]).{8}'

    good_name = re.match(regex, name)

    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={'name' : name})
    

