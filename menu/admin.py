
# Register your models here.
from django.contrib import admin
from .models import Moto



class ClienteAdmin(admin.ModelAdmin):
    # Personaliza la vista del modelo Cliente si es necesario
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')


class CategoriaAdmin(admin.ModelAdmin):
    # Personaliza la vista del modelo Categoria si es necesario
    list_display = ('nombre',)
    search_fields = ('nombre',)


class ProductoAdmin(admin.ModelAdmin):
    # Personaliza la vista del modelo Producto si es necesario
    list_display = ('nombre', 'precio', 'descripcion', 'categoria')
    search_fields = ('nombre', 'descripcion')


class CompraAdmin(admin.ModelAdmin):
    # Personaliza la vista del modelo Compra si es necesario
    list_display = ('cliente', 'fecha', 'total')
    search_fields = ('cliente__nombre',)