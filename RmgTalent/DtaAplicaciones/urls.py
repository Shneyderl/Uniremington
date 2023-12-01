from django.urls import path
from . import views
from .views import validar_numero_alu

urlpatterns = [
    #    Pagína/Aplicaciones    
    path('applications/<int:idOfer>/', views.applications, name='applications'),
    path('applications.html/<int:idOfer>/', views.applications, name='applications'),
    path('applications.html/<int:idAlu>/', validar_numero_alu, name='validar_numero_alu'),
]