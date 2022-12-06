from django.contrib import admin
from .models import ProductoContable, ProductoEnGramos

# Register your models here.
admin.site.register(ProductoContable)
admin.site.register(ProductoEnGramos)