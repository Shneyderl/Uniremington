from django import forms

class ValidarNumeroForm(forms.Form):
    numero_alu = forms.CharField(max_length=12)