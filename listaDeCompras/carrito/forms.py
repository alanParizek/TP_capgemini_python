from django.forms import ModelForm, Form
from django import forms
from .models import ChangoXproducto
from productos.models import Producto, ProductoContable, ProductoEnGramos

class AgregarProductoForm(ModelForm):     
    # valor inicial para el ModelChoiceField (buscar la respuesta que habla de eso):
    # https://stackoverflow.com/questions/657607/setting-the-selected-value-on-a-django-forms-choicefield
    class Meta:
        model = ChangoXproducto
        fields = ['producto', 'cantidad']

    def __init__(self, *args, **kwargs):
        super(AgregarProductoForm, self).__init__(*args, **kwargs)
        self.fields['producto'].queryset = Producto.objects.all().select_subclasses()

    @classmethod
    def formularioConValoresIniciales(cls, valoresIniciales: tuple[int, int] ):
        form = AgregarProductoForm()
        idProducto, cantidad = valoresIniciales
        form.fields['producto'].initial = Producto.objects.get(pk=idProducto) #si no anda fijarse con form.initial['producto'] = ...
        form.fields['cantidad'].initial = cantidad
        return form
    
class ImageForm(Form):
    img = forms.ImageField()
            
