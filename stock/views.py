from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm

# 0. HOME - Panel principal
def home(request):
    return render(request, 'stock/home.html')

# 1. LISTAR - Gestión de Inventario (CRUD completo)
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'stock/productos.html', {'productos': productos})

# 2. PANTALLA DE VENTAS - Registro administrativo de ventas efectuadas
def pantalla_ventas(request):
    productos = Producto.objects.all()
    return render(request, 'stock/ventas.html', {'productos': productos})

# 3. CREAR - Alta de nuevo producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado correctamente en el inventario.")
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'stock/form_producto.html', {'form': form, 'titulo': 'Nuevo Producto'})

# 4. EDITAR - Modificación de datos existentes
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f"Datos de '{producto.nombre}' actualizados.")
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'stock/form_producto.html', {'form': form, 'titulo': 'Editar Producto'})

# 5. ELIMINAR - Baja definitiva de producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    nombre = producto.nombre
    producto.delete()
    messages.warning(request, f"Se ha eliminado '{nombre}' del sistema.")
    return redirect('lista_productos')

# 6. REGISTRAR VENTA - Asentar salida de stock físico
def registrar_venta(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    # Detectamos el origen para que la experiencia de usuario sea fluida
    referer = request.META.get('HTTP_REFERER', '')
    
    if producto.cantidad > 0:
        producto.cantidad -= 1
        producto.save()
        # Mensaje enfocado a control de stock
        messages.success(request, f"Salida registrada: 1 unidad de '{producto.nombre}' descontada del stock.")
    else:
        messages.error(request, f"Error de inventario: '{producto.nombre}' no tiene existencias para descontar.")
    
    # Redirección inteligente: vuelve a la pantalla desde donde se apretó el botón
    if 'ventas' in referer:
        return redirect('pantalla_ventas')
    return redirect('lista_productos')