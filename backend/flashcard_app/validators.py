from django.core.exceptions import ValidationError
import re


def validate_word(word):

    error_message = 'Invalid Word'

    regex = r'[^a-zA-Z]+'

    invalid_word = re.search(regex, word)

    print(invalid_word)

    if invalid_word:
        raise ValidationError(error_message, params={'word' : word})
    else:
        return word