from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm  # Asegurate de haber creado forms.py

# 1. LISTAR (Mantenemos la lista)
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'stock/productos.html', {'productos': productos})

# 2. CREAR (Se agrega request.FILES para capturar la imagen)
def crear_producto(request):
    if request.method == 'POST':
        # Agregamos request.FILES como segundo parámetro
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stock:productos') # Cambiado al namespace estándar de tu app
    else:
        form = ProductoForm()
    return render(request, 'stock/form_producto.html', {'form': form, 'titulo': 'Nuevo Producto'})

# 3. EDITAR (Se agrega request.FILES para actualizar la imagen si se sube una nueva)
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        # Agregamos request.FILES también aquí
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('stock:productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'stock/form_producto.html', {'form': form, 'titulo': 'Editar Producto'})

# 4. ELIMINAR
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('stock:productos')