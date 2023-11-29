from django.shortcuts import render
from .models import Ofertas
# aqui se importan librerias de api de django
from django.http import Http404


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
        
    return render(request, 'ofertas/add.html',{
        'title': 'Crear Oferta',
    })


def ver_ofertas(request):
    ofertas = Ofertas.objects.all()
    return render(request, 'mainapp/job_listing.html',{
        'title': 'Ofertas'
         },{
        'ofertas': ofertas
    })