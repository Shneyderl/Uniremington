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
# def postulacion(request):
#     return render(request, 'applies/Post_List.html',{'title': 'Postulaciones'
#     })

from django.shortcuts import render
from .models import Ofertas, Aplica, Alumnos

def postulacion(request):
    # Obtener todas las ofertas
    ofertas = Ofertas.objects.all()

    # Crear una lista para almacenar los datos de cada oferta
    data_ofertas = []

    # Iterar sobre las ofertas y obtener la información necesaria
    for oferta in ofertas:
        # Obtener la cantidad de postulaciones para la oferta actual
        cantidad_postulaciones = Aplica.objects.filter(idOferApp=oferta.idOfer).count()

        # Obtener la lista de alumnos que postularon a esta oferta
        alumnos_postulados = Aplica.objects.filter(idOferApp=oferta.idOfer).values_list('idAluApp__idAlu', 'idAluApp__nomAlu')

        # Crear un diccionario con la información de la oferta actual
        oferta_data = {
            'idOfer': oferta.idOfer,
            'titOfer': oferta.titOfer,
            'cantidad_postulaciones': cantidad_postulaciones,
            'alumnos_postulados': list(alumnos_postulados),
        }

        # Agregar el diccionario a la lista
        data_ofertas.append(oferta_data)

    return render(request, 'applies/Post_List.html', {'title': 'Postulaciones', 'data_ofertas': data_ofertas})


def applications(request, idOfer):
    oferta = Ofertas.objects.get(idOfer=idOfer)
    empresa = Empresas.objects.get(idEmp=oferta.idEmpOfer)
    current_time = datetime.now()
    return render(request, 'applies/applications.html',{'title': 'Aplicaciones', 'oferta': oferta, 'current_time': current_time, 'empresa' : empresa 
    })

def validar_numero_alu(request, idOfer, idAlu):
    if request.method == "POST":
        form = ValidarNumeroForm(request.POST)
        #print(form.is_valid())
        #if form.is_valid():  Se valida en el formulario
        #numero_alu = form.cleaned_data['numero_alu']
        existe_alu = Alumnos.objects.filter(idAlu=idAlu).exists()
        if existe_alu:
                # Crear un nuevo registro en el modelo Aplica
                Aplica.objects.create(
                    idOferApp_id=idOfer,
                    idAluApp_id=idAlu,
                    stsApp="aplicando",
                )
        # Devolver la respuesta JSON
                return JsonResponse({"existe": existe_alu})
        else:
                return JsonResponse({"existe": False})
    # Si hay un error o la solicitud no es POST, devolver una respuesta por defecto
    return JsonResponse({"existe": False})
