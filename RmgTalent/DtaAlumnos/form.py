from django import forms
from .models import Alumnos

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['idAlu', 'nomAlu', 'apeAlu', 'carAlu', 'semAlu']