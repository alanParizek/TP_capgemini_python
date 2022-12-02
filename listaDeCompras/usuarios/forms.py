from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class LogInForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']