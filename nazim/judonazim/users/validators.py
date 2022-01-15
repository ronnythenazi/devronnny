from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class CustomPasswordValidator():

    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('סיסמה חייבת להכיל לפחות  %(min_length)d ספרות.') % {'min_length': self.min_length})
        if not any(char.isalpha() for char in password):
            raise ValidationError(_('סיסמה חייבת להכיל לפחות %(min_length)d אותיות.') % {'min_length': self.min_length})
        if not any(char in special_characters for char in password):
            raise ValidationError(_('סיסמה חייבת להכיל לפחות %(min_length)d תווים מיוחדים.') % {'min_length': self.min_length})

    def get_help_text(self):
        return ""
