

# Register your models here.
from django.contrib import admin



class MotoAdmin(admin.ModelAdmin):
    # Puedes personalizar la vista del modelo aquí si es necesario
    list_display = ('marca', 'modelo', 'año', 'precio')
    search_fields = ('marca', 'modelo')


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