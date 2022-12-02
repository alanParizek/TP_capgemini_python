from django.forms import ModelForm
from .models import Usuario

class SignUpForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class LogInForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']