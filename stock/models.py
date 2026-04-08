from django.db import models

class Producto(models.Model):
    nombre= models.CharField(max_length=100)
    cantidad= models.ImageField()
    precio = models.FloatField()


    def __str__(self):
        return self.nombre