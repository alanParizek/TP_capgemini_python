from PIL import Image
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Chango, ChangoXproducto, NoPuedeCerrarseLaCompraException
from .forms import AgregarProductoForm, ImageForm
from productos.models import Producto
from obtenedorDeProductos.models import ObtenedorDeProductos


# vamos a tener fomulario foto y formulario carrito
# formulario foto tiene un submit que con lo valores del VDI pone por default los valores del form carrito
# formulario carrito tiene un submit que crea un ChangoXproducto que se muestra luego la lista de compras

# en todas las funciones hay que mandarle en el context los dos forms

# info de valor: form.fields['manager'].initial = manager_employee_id

class ChangoController():
    @staticmethod
    @login_required()
    def verCarrito(request):
        # agrega el formulario para agregar el producto. Si los tiene cargados, muestra los valores iniciales

        try:
            print(request.session['valoresIniciales'])
            formAgregarProducto = AgregarProductoForm.formularioConValoresIniciales(request.session['valoresIniciales'])
        except:
            print('tiroerror')
            formAgregarProducto = AgregarProductoForm()
        errorVDI = False
        if request.session.has_key('valoresIniciales'):
            errorVDI = request.session['valoresIniciales'] == [None, None]
        print(errorVDI)
        # agrega los items del carrito para mostrar
        chango = ChangoController.getChangoUser(request)
        itemsCarrito = map(
            lambda changoProd: {"changoXprod": changoProd,
                                "unidad": (Producto.objects.get_subclass(pk=changoProd.producto_id)).unidad},
            ChangoXproducto.objects.filter(chango=chango)
            )
        context = {'itemsCarrito': itemsCarrito, 'formAgregarProducto': formAgregarProducto,
                   'formSubirImagen': ImageForm(), 'listaDePrecios': Producto.listaDePrecios(),
                   'errorNoReconocioElProducto': errorVDI, 'total': chango.total()}
        return render(request, "carrito.html", context)

    @staticmethod
    def getUser(request):
        if not hasattr(request, '_cached_user'):
            request._cached_user = auth.get_user(request)
        return request._cached_user
    
    @staticmethod
    def getChangoUser(request):
        user = ChangoController.getUser(request)
        return Chango.carritoDelUsuario(user)

    @staticmethod
    @login_required()
    def chequearFoto(request):
        # agarra la foto, llama al VDI y mete en la session los valores de producto y cantidad
        formImagen = ImageForm(request.POST, request.FILES)
        producto: Producto
        cantidad: int
        if not formImagen.is_valid():
            return redirect('carrito')
        image_field = formImagen.cleaned_data['img']
        imagen = Image.open(image_field)
        (producto, cantidad) = ObtenedorDeProductos().obtenerProducto(imagen)
        if producto == None: # si no se encontro el producto, setea en None los valores iniciales y asi django no los carga en el form
            request.session['valoresIniciales'] = (None, None)
        else:
            request.session['valoresIniciales'] = (producto.pk, cantidad)
        return redirect('carrito')

    @staticmethod
    @login_required()
    def agregarProducto(request):
        chango = ChangoController.getChangoUser(request)
        form = AgregarProductoForm(request.POST)
        if form.is_valid():
            producto = Producto.objects.get(pk=request.POST['producto'])
            chango.agregarProducto(producto, int(request.POST['cantidad']))
        ChangoController.eliminarDefaultsSession(request)
        # agregar el producto al carrito de ese usuario (obtenemos el usuario de la session)
        # redireccionar a la pagina de ver carrito
        return redirect('carrito')
        
    @staticmethod
    @login_required()
    def sacarProducto(request, idProd):
        chango = ChangoController.getChangoUser(request)
        producto = Producto.objects.get(pk=int(idProd))
        chango.sacarTodosDeUnProducto(producto)
        ChangoController.eliminarDefaultsSession(request)
        # redireccionar a la pagina de ver carrito
        return redirect('carrito')
        
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
        ChangoController.eliminarDefaultsSession(request)
        chango = ChangoController.getChangoUser(request)
        try:
            chango.cerrarCompra()
        except NoPuedeCerrarseLaCompraException as e:
            return HttpResponse(e.__str__())

        usuario = ChangoController.getUser(request)
        nuevoChango = Chango(usuario=usuario)
        nuevoChango.save()
        return render(request, 'compraCerrada.html')
    