from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class SignUpForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email']

class LogInForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']