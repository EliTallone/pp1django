from django.urls import path
from . import views  # Importamos todas las views

# Agregamos esta línea para registrar el namespace 'stock' que pide el proyecto
app_name = 'stock'

urlpatterns = [
    # Cambiamos el name a 'productos' para que machee con tus otras pantallas
    path('productos/', views.lista_productos, name='productos'),
    
    # Ruta para el formulario de CREAR
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    
    # Ruta para EDITAR (necesita el ID del producto)
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    
    # Ruta para ELIMINAR (necesita el ID del producto)
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]