from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm  # Asegurate de haber creado forms.py

# 1. LISTAR (La que ya tenías, la mantenemos)
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'stock/productos.html', {'productos': productos})

# 2. CREAR (Usa el formulario para agregar productos nuevos)
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos') # Nos manda a la lista al terminar
    else:
        form = ProductoForm()
    return render(request, 'stock/form_producto.html', {'form': form, 'titulo': 'Nuevo Producto'})

# 3. EDITAR (Busca un producto por su ID y permite modificarlo)
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'stock/form_producto.html', {'form': form, 'titulo': 'Editar Producto'})

# 4. ELIMINAR
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')