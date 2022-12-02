from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chango, ChangoXproducto
from .forms import AgregarProductoForm, FormFoto


# vamos a tener fomulario foto y formulario carrito
# formulario foto tiene un submit que con lo valores del VDI pone por default los valores del form carrito
# formulario carrito tiene un submit que crea un ChangoXproducto que se muestra luego la lista de compras

# en todas las funciones hay que mandarle en el context los dos forms

# info de valor: form.fields['manager'].initial = manager_employee_id

# Create your views here.
class ChangoController():
    @staticmethod
    @login_required()
    def verCarrito(request):
        formAgregarProducto = AgregarProductoForm.formularioConValoresIniciales(request.session['valoresIniciales'])
        formFoto = FormFoto() # hacer FormFoto
        # agregar al context los productos en el carrito del usuario logueado para que los muestre (obtenemos el usuario de la session)
        context = {'formSubirFoto': formFoto, 'formAgregarProducto':formAgregarProducto}
        return render(request, "carrito.html") #, context)

    @staticmethod
    @login_required()
    def chequearFoto(request):
        # agarra la foto, llama al VDI y mete en la session los valores de producto y cantidad
        request.session['valoresIniciales'] = # agregarle la tupla
        return render(request, "carrito.html")

    @staticmethod
    @login_required()
    def agregarProducto(request):
        chango = Chango.carritoDelUsuario(request.user)
        form = AgregarProductoForm(request.POST, request.session['productoAagregar'])
        if form.is_valid():
            chango.agregarProducto(request.POST['producto'], request.POST['cantidad'])
        
        # agregar el producto al carrito de ese usuario (obtenemos el usuario de la session)
        # redireccionar a la pagina de ver carrito
        return render(request, "carrito.html")

    @staticmethod
    @login_required()
    def sacarProducto(request):
        chango = Chango.carritoDelUsuario(request.user)
        chango.sacarTodosDeUnProducto(request.POST['producto'])
        # redireccionar a la pagina de ver carrito
        return render(request, "carrito.html")

    @staticmethod
    @login_required()
    def cerrarCompra(request):
        chango = Chango.carritoDelUsuario(request.user)
        chango.cerrarCompra()
        nuevoChango = Chango(usuario=request.user)
        chango.save()
        nuevoChango.save()
        # vaciar el carrito de ese usuario (obtenemos el usuario de la session)
        # crearle un carrito nuevo
        # hacer otras cosas?
        # redireccionar a la pagina de ver carrito
        return render(request, "carrito.html")

    
    