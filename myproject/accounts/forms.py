from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']
class LoginForm(AuthenticationForm):
    pass