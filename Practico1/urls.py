"""
URL configuration for Practico1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sistema.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('stock/', include('stock.urls')),
    
    # 1. Rutas de autenticación por defecto de Django (Login / Logout)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # 2. Incluimos las URLs de la app sistema para el registro más adelante
    path('sistema/', include('sistema.urls')),
    
]

# 3. Esto le permite a Django servir los archivos multimedia (imágenes) en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)