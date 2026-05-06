from django.urls import path
from . import views

urlpatterns = [
    # 0. HOME
    path('', views.home, name='home'),

    # 1. INVENTARIO (Panel completo)
    path('productos/', views.lista_productos, name='lista_productos'),
    
    # 2. PANTALLA DE VENTAS (Solo ventas)
    path('ventas/', views.pantalla_ventas, name='pantalla_ventas'),
    
    # 3. CREAR
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    
    # 4. EDITAR
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    
    # 5. ELIMINAR
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    # 6. ACCIÓN DE VENTA
    path('productos/venta/<int:id>/', views.registrar_venta, name='registrar_venta'),
]