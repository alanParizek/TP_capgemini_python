from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Chango, ChangoXproducto
from .forms import AgregarProductoForm


# vamos a tener fomulario foto y formulario carrito
# formulario foto tiene un submit que con lo valores del VDI pone por default los valores del form carrito
# formulario carrito tiene un submit que crea un ChangoXproducto que se muestra luego la lista de compras

# en todas las funciones hay que mandarle en el context los dos forms

# info de valor: form.fields['manager'].initial = manager_employee_id

# Create your views here.
def carrito(request):
    # formCarrito = CarritoForm()
    # context = {'form':formCarrito}
    return render(request, "carrito.html") 
#, context)
class ChangoController():
    @staticmethod
    @login_required()
    def verCarrito(request):
        try:
            formAgregarProducto = AgregarProductoForm.formularioConValoresIniciales(request.session['valoresIniciales'])
        except:
            formAgregarProducto = AgregarProductoForm()
        chango = Chango.carritoDelUsuario(request.user)
        itemsCarrito = ChangoXproducto.objects.filter(chango=chango)
        # agregar al context los productos en el carrito del usuario logueado para que los muestre (obtenemos el usuario de la session)
        context = {'formAgregarProducto':formAgregarProducto, 'itemsCarrito':itemsCarrito}
        return render(request, "carrito.html", context)

    @staticmethod
    @login_required()
    def chequearFoto(request):
        # agarra la foto, llama al VDI y mete en la session los valores de producto y cantidad
        request.session['valoresIniciales'] = (producto, cantidad)# agregarle la tupla con el VDI
        ChangoController.verCarrito(request)

    @staticmethod
    @login_required()
    def agregarProducto(request):
        chango = Chango.carritoDelUsuario(request.user)
        form = AgregarProductoForm(request.POST)
        if form.is_valid():
            chango.agregarProducto(request.POST['producto'], request.POST['cantidad'])
        ChangoController.eliminarDefaultsSession()
        # agregar el producto al carrito de ese usuario (obtenemos el usuario de la session)
        # redireccionar a la pagina de ver carrito
        ChangoController.verCarrito(request)

    @staticmethod
    @login_required()
    def sacarProducto(request):
        chango = Chango.carritoDelUsuario(request.user)
        chango.sacarTodosDeUnProducto(request.POST['producto'])
        ChangoController.eliminarDefaultsSession()
        # redireccionar a la pagina de ver carrito
        ChangoController.verCarrito(request)
        
    @staticmethod
    def eliminarDefaultsSession(request):
        try:
            request.session.pop('valoresIniciales')
        except:
            pass
        # borra la key del dict de la session

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
        return HttpResponse('Gracias por su compra, sera atendido por nuestros cajeros en un instante!')

    
    