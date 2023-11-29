from django.shortcuts import render
from .models import Ofertas

# Create your views here.
def ver_ofertas(request):
    ofertas = Ofertas.objects.all()
    return render(request, 'mainapp/job_listing.html',{
        'title': 'Ofertas'
         },{
        'ofertas': ofertas
    })