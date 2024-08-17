# menu/urls.py
from django.urls import path
from .views import inicio_view
from . import views

urlpatterns = [

    path('', inicio_view, name='inicio'),
    
    path('login/', views.CustomLoginView.as_view(), name='login'),
        
    path('compras/<int:id>/', views.compra_detail, name='compra_detail'),

    path('compras/', views.compra_list, name='compra_list'),  # Lista de compras
    path('compras/new/', views.compra_create, name='compra_create'),  # Agregar compra
    # path('compras/<int:pk>/edit/', views.compra_update, name='compra_edit'),  # Editar compra
    # path('compras/<int:pk>/delete/', views.compra_delete, name='compra_delete'),  # Eliminar compra
    path('compras/<int:pk>/', views.compra_detail, name='compra_detail'),  # Ver detalles de la compra
    

    # Ruta temporal para ver compras
    path('compras/test/', lambda request: render(request, 'menu_templates/compra_list.html')),

    path('clientes/', views.cliente_list, name='cliente_list'),  # Lista de clientes
    path('clientes/new/', views.cliente_create, name='cliente_create'),  # Crear nuevo cliente
    path('clientes/<int:pk>/', views.cliente_detail, name='cliente_detail'),  # Detalle de cliente
    path('clientes/<int:pk>/edit/', views.cliente_update, name='cliente_update'),  # Editar cliente
    path('clientes/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),  # Eliminar cliente

    path('productos/', views.producto_list, name='producto_list'),  # Lista de productos
    path('productos/<int:pk>/detail/', views.producto_detail, name='producto_detail'),  # Detalle del producto
    path('productos/new/', views.producto_create, name='producto_create'),  # Crear producto
    path('productos/<int:pk>/edit/', views.producto_update, name='producto_update'),  # Editar producto
    path('productos/<int:pk>/delete/', views.producto_delete, name='producto_delete'),  # Eliminar producto
]


