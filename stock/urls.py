from django.urls import path
from . import views  # Importamos todas las views

urlpatterns = [
    # Ruta para listar (la que ya tenías, pero actualizada para usar views.algo)
    path('productos/', views.lista_productos, name='lista_productos'),
    
    # Ruta para el formulario de CREAR
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    
    # Ruta para EDITAR (necesita el ID del producto)
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    
    # Ruta para ELIMINAR (necesita el ID del producto)
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]