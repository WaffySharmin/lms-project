from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=[
        (User.Role.STUDENT, 'Student'),
        (User.Role.TEACHER, 'Teacher'),
    ])

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')
