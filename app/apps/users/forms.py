from django.forms import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'username',)

    def clean_email(self):
        cd = super().clean()
        email = cd.get('email')
        if email and self.Meta.model.objects.filter(email=email).exists():
            raise ValidationError(f'User with email {email} already exists.')
        return email


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'username', 'image',)
