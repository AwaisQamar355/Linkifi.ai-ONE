from django.core.exceptions import ValidationError

def validate_svg(value):
    if not value.name.endswith('.svg'):
        raise ValidationError('Only .svg files are allowed.')