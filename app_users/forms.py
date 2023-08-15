from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class RecoverPasswordForm(forms.Form):
    email = forms.EmailField(required=True)
