from django.http import Http404
from django.shortcuts import render
from models import Ofertas

# Create your views here.
def job_listing(request):
    print(request)
    try:
        o = Ofertas.objects.get()
    except Ofertas.DoesNotExist:
        raise Http404("No hay ofertas")        
    return render(request, 'mainapp/job_listing.html', {"ofertas": o})
    