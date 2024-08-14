# menu/forms.py

from django import forms
from .models import Cliente, Producto, Compra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio','categoria']

class CompraForm(forms.ModelForm):
    productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )    
    class Meta:
        model = Compra
        fields = ['cliente', 'productos', 'fecha','detalle']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})  # Para usar el selector de fecha HTML5
        }
