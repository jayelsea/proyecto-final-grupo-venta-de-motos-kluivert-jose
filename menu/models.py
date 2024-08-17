# menu/models.py

from django.db import models
from django.db.models import Sum

class Moto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=100, default='Sin descripción')
    categoria = models.CharField(max_length=1)    # Campo de categoría

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha = models.DateField()
    detalle = models.TextField(blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Campo para el total

    def save(self, *args, **kwargs):
        # Primero guarda el objeto para que tenga un ID
        super().save(*args, **kwargs)

        # Luego calcula el total usando el ID del objeto guardado
        # Primero asegura que los productos estén asociados
        if self.pk:
            total = self.productos.aggregate(Sum('precio'))['precio__sum'] or 0.00
            Compra.objects.filter(pk=self.pk).update(total=total)  # Actualiza solo el campo total

    def __str__(self):
        return f"Compra {self.id} - {self.cliente.nombre}"