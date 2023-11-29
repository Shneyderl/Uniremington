from django.http import Http404
from django.shortcuts import render
from .models import Ofertas
# aqui se importan librerias de api de django
from django.http import Http404

#from models import Ofertas

# Create your views here.

# CRUD de django modelo por metodos tradicional
def add_offer (request):
    
    if request.method == 'POST':
        
        idEmpOfer=request.POST.get('idEmpOfer')
        titOfer=request.POST.get('titOfer')
        cargoOfer=request.POST.get('cargoOfer')
        descOfer=request.POST.get('descOfer')
        skillOfer=request.POST.get('skillOfer')
        salOfer=request.POST.get('salOfer')
        contOfer=request.POST.get('contOfer')
        ubcOfer=request.POST.get('ubcOfer')
        catOfer=request.POST.get('catOfer')        
        
        addOferta=Ofertas.objects.create(
            idEmpOfer=idEmpOfer,
            titOfer=titOfer,
            cargoOfer=cargoOfer,
            descOfer=descOfer,
            skillOfer=skillOfer,
            salOfer=salOfer,
            contOfer=contOfer,
            ubcOfer=ubcOfer,
            catOfer=catOfer 
        )
        
        # messages.success(request, 'Registrado correctamente')
        # return redirect('/')
        
    return render(request, 'ofertas/add_offer.html',{
        'title': 'Crear Oferta',
    })

def job_details(request):
    return render(request, 'ofertas/job_details.html',{
        'title': 'Detalle Oferta'
    })

def job_listing(request):
    ofertas = Ofertas.objects.all()
    print(request)
    return render(request, 'ofertas/job_listing.html',{'title': 'Listado de Ofertas', 'ofertas': ofertas
    })
