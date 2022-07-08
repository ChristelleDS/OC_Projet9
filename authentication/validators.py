from django.core.exceptions import ValidationError


class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir un chiffre', code='password_no_number')

    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins un chiffre.'
