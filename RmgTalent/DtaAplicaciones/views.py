from django.shortcuts import render
from .models import Aplica
from .models import Ofertas
from .models import Alumnos
from DtaEmpresas.models import Empresas
# aqui se importan librerias de api de django
from django.http import Http404
from datetime import datetime
from django.http import JsonResponse
from .forms import ValidarNumeroForm


# Create your views here.

# CRUD de django modelo por metodos tradicional
def postulacion(request):
    return render(request, 'applies/Post_List.html',{
        'title': 'Postulaciones'
    })
def applications(request, idOfer):
    oferta = Ofertas.objects.get(idOfer=idOfer)
    empresa = Empresas.objects.get(idEmp=oferta.idEmpOfer)
    current_time = datetime.now()
    return render(request, 'applies/applications.html',{'title': 'Aplicaciones', 'oferta': oferta, 'current_time': current_time, 'empresa' : empresa 
    })

def validar_numero_alu(request):
    if request.method == "POST":
        form = ValidarNumeroForm(request.POST)
        print('ingresa')
        if form.is_valid():
            numero_alu = form.cleaned_data['numero_alu']
            existe_alu = Alumnos.objects.filter(idAlu=numero_alu).exists()

            # Devolver la respuesta JSON
            return JsonResponse({"existe": existe_alu})

    # Si hay un error o la solicitud no es POST, devolver una respuesta por defecto
    return JsonResponse({"existe": False})
