from django.contrib import admin
from .models import Producto, Categoria

# Usamos el decorador @admin.register como pide la consigna
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que se ven en el listado
    list_display = ('nombre', 'cantidad', 'precio', 'categoria')
    
    # El filtro lateral (Requisito: al menos un filtro)
    list_filter = ('categoria',)
    
    # El buscador (Requisito: al menos una búsqueda)
    search_fields = ('nombre',)

# Registramos la Categoria de forma simple para poder crear categorías nuevas
admin.site.register(Categoria)