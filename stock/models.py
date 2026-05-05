from django.db import models

# 1. Agregamos el segundo modelo (Categoria)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    # Corregimos ImageField por IntegerField para que sea un número
    cantidad = models.IntegerField() 
    precio = models.FloatField()
    
    # 2. Creamos la relación (Foreign Key)
    # on_delete=models.CASCADE significa que si borras la categoría, se borran sus productos
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos', null=True, blank=True)

    def __str__(self):
        return self.nombre