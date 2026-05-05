from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'cantidad', 'precio', 'categoria']
        # Esto genera automáticamente los inputs basados en tu modelo