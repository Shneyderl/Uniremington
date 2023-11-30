from django.urls import path
from . import views

urlpatterns = [       
    #    Alumnos
    path('listar_alumno', views.listar_alumno, name='listar_alumno'),
    path('listar_alumno.html', views.listar_alumno, name='listar_alumno'), 

    path('add_alumno',views.add_alumno, name='add_alumno'),
    path('add_alumno.html',views.add_alumno, name='add_alumno'),
]