from django.core.exceptions import ValidationError


def min_lenght_validator(value):
    if len(value) < 16:
        raise ValidationError('lenght must be at least 16 characters')
