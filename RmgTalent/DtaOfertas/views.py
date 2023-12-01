from django.shortcuts import render
from .models import Ofertas
# aqui se importan librerias de api de django
from django.http import Http404
from .form import OfertaForm

#from models import Ofertas

# Create your views here.

def add_offer (request):

    form = OfertaForm()
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        print(form)
        if form.is_valid():
            form = OfertaForm(request.POST)
            form.save()
        
        # messages.success(request, 'Registrado correctamente')
        # return redirect('/')
        
    return render(request, 'ofertas/add_offer.html',{'title': 'Crear Oferta','ofertas/add_offer.html': form,
    })

def job_details(request, idOfer):
    oferta = Ofertas.objects.get(idOfer=idOfer)
    print(oferta)
    return render(request, 'ofertas/job_details.html',{'title': 'Detalle Oferta', 'oferta': oferta
    })

def job_listing(request):
    ofertas = Ofertas.objects.all()
    return render(request, 'ofertas/job_listing.html',{'title': 'Listado de Ofertas', 'ofertas': ofertas
    })
