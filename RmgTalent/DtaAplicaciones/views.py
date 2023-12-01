from django.shortcuts import render
from .models import Aplica
# aqui se importan librerias de api de django
from django.http import Http404


# Create your views here.

# CRUD de django modelo por metodos tradicional
def applications(request):
    return render(request, 'applies/Post_List.html',{
        'title': 'Postulaciones'
    })