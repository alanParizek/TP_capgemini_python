from django.forms import ModelForm
from .models import ChangoXproducto, Producto

class AgregarProductoForm(ModelForm):     
    # valor inicial para el ModelChoiceField (buscar la respuesta que habla de eso):
    # https://stackoverflow.com/questions/657607/setting-the-selected-value-on-a-django-forms-choicefield

    def __init__(self, *args, **kwargs):
        self.fields['producto'].queryset = Producto.objects.all()

    @classmethod
    def formularioConValoresIniciales(cls, valoresIniciales: tuple[Producto, int] ):
        form = AgregarProductoForm()
        producto, cantidad = valoresIniciales
        form.fields['producto'].initial = producto #si no anda fijarse con form.initial['producto'] = producto
        form.fields['cantidad'].initial = cantidad
        return form

    class Meta:
        model = ChangoXproducto
        fields = ['producto', 'cantidad']