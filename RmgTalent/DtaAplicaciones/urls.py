from django.urls import path
from . import views

urlpatterns = [
    #    Pagína/Aplicaciones    
    path('applications', views.applications),
    path('applications.html', views.applications),
]