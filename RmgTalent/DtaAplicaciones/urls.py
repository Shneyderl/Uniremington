from django.urls import path
from . import views
from .views import validar_numero_alu
from .views import postulacion
from DtaAlumnos.views import detail_alumno

urlpatterns = [
    #    Pagína/Aplicaciones    
    path('Post_List', views.postulacion, name='postulacion'),
    path('Post_List.html', views.postulacion, name='postulacion'),
    path('applications/<int:idOfer>/', views.applications, name='applications'),
    path('applications.html/<int:idOfer>/', views.applications, name='applications'),
    path('validar_numero_alu/<int:idOfer>/<int:idAlu>/', views.validar_numero_alu, name='validar_numero_alu'),
    #path('validar_numero_alu/<int:idOfer>/', views.validar_numero_alu, name='validar_numero_alu'),
]