from django import forms
from .models import Ofertas, Empresas, Categorias

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Ofertas
        fields = ['idEmpOfer', 'titOfer', 'cargoOfer', 'descOfer', 'skillOfer', 'salOfer', 'contOfer', 'ubcOfer', 'catOfer']
