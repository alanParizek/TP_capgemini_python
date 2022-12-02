from django.forms import ModelForm
from .models import Chango

class CarritoForm(ModelForm):
    class Meta:
        model = Chango
        fields = []#'username', 'first_name', 'last_name', 'email', 'password'
