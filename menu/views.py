# menu/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Producto, Compra
from .forms import ClienteForm, ProductoForm, CompraForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Vistas para Cliente
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'menu_templates/cliente_list.html', {'clientes': clientes})

@login_required
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'menu_templates/cliente_detail.html', {'cliente': cliente})

@login_required
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'menu_templates/cliente_form.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = "menu_templates/login.html"
    
    def get_success_url(self):
        return reverse_lazy('compra_create')

@login_required
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'menu_templates/cliente_form.html', {'form': form})

@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'menu_templates/cliente_confirm_delete.html', {'cliente': cliente})

# Vistas para Producto
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'menu_templates/producto_list.html', {'productos': productos})

@login_required
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'menu_templates/producto_detail.html', {'producto': producto})

@login_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'menu_templates/producto_form.html', {'form': form})

@login_required
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'menu_templates/producto_form.html', {'form': form})

@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'menu_templates/producto_confirm_delete.html', {'producto': producto})



# Vistas para Compra
def compra_list(request): #vista de lista de compras 
    compras = Compra.objects.all()
    return render(request, 'menu_templates/compra_list.html', {'compras': compras})

@login_required
def compra_detail(request, pk):  #detalles de las compras 
    compra = get_object_or_404(Compra, pk=pk)
    return render(request, 'menu_templates/compra_detail.html', {'compra': compra})

@login_required
def compra_create(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            productos = form.cleaned_data['productos']
            total = sum(producto.precio for producto in productos)
            compra.total = total
            compra.save()
            compra.productos.set(productos)  # Guarda los productos relacionados
            return redirect('compra_list')
    else:
        form = CompraForm()
    return render(request, 'menu_templates/compra_form.html', {'form': form})


#def compra_update(request, pk):   #edit de compras 
    # compra = get_object_or_404(Compra, pk=pk)
    # if request.method == 'POST':
    #     form = CompraForm(request.POST, instance=compra)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('compra_list')
    # else:
    #     form = CompraForm(instance=compra)
    # return render(request, 'menu_templates/compra_form.html', {'form': form})

#def compra_delete(request, pk):
    # compra = get_object_or_404(Compra, pk=pk)
    # if request.method == 'POST':
    #     compra.delete()
    #     return redirect('compra_list')
    # return render(request, 'menu_templates/compra_confirm_delete.html', {'compra': compra})

# views.py

