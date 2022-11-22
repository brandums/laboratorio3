from django.core.exceptions import ValidationError

def validar_nombre_categoria(value):
    if len(value) < 4:
        raise ValidationError("Escriba un nombre de categoria de mas de 4 caracteres")

def validate_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("This field needs to have an email")