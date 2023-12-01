from django.shortcuts import render
from .models import Alumnos
from MainApp.models import Usuarios
# aqui se importan librerias de api de django
from django.http import Http404
from .form import AlumnoForm

# Create your views here.


def add_alumno (request):

    form = AlumnoForm()
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        #print(form)
        if form.is_valid():
            form = AlumnoForm(request.POST)
            form.save()
        
        # messages.success(request, 'Registrado correctamente')
        # return redirect('/')
        
    return render(request, 'alumnos/add_alumno.html',{'title': 'Crear Alumno','alumnos/add_alumno.html': form,
    })

def listar_alumno(request):
    alumnos = Alumnos.objects.all()
    print(alumnos)
    return render(request, 'alumnos/listar_alumno.html',{'title': 'Listado de alumnos', 'alumnos': alumnos
    })

def detail_alumno(request, idAlu):
    alumnos = Alumnos.objects.get(idAlu=idAlu)
    usuarios = Usuarios.objects.get(idUsr=idAlu)
    print(alumnos)
    print(usuarios)
    return render(request, 'alumnos/detail_alumno.html',{'title': 'Alumno', 'alumnos': alumnos, 'usuarios': usuarios
    })