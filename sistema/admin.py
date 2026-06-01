from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

# Registramos el usuario personalizado utilizando la configuración nativa de Django
admin.site.register(UsuarioPersonalizado, UserAdmin)