from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm  # <- Aquí ya va a encontrar tu archivo nuevo

def home(request):
    return render(request, 'sistema/home.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():  # <- Corregido aquí
            user = form.save()
            login(request, user)  # Loguea automáticamente al usuario recién registrado
            return redirect('home')
    else:
        form = RegistroForm()
        
    return render(request, 'sistema/registro.html', {'form': form})