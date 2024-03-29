from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):

    # Adding a mandatory email field to the UserCreationForm
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']