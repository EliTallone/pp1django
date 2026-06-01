from django.db import models

# 1. Modelo Categoria (Se queda tal cual)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# 2. Unificamos el modelo Producto en uno solo
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField() 
    precio = models.FloatField()
    
    # Relación con Categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos', null=True, blank=True)
    
    # ¡Aquí sumamos el campo de imagen que te pide la consigna!
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre