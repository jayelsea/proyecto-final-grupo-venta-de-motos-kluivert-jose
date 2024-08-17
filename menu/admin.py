
# Register your models here.
from django.contrib import admin
from .models import Moto



class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'categoria')
    search_fields = ('nombre', 'descripcion')


class CompraAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'total')
    search_fields = ('cliente__nombre',)
