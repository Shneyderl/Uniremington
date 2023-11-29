from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('index', views.index, name='index'),

    #path('job_listing.html', views.job_listing, name='job_listing.html'),
    #path('job_listing', views.job_listing, name='job_listing.html'),

    #    Contactenos
    path('contact', views.contact),
    path('contact.html', views.contact),
    
    #    Acerca
    path('about', views.about),
    path('about.html', views.about),
    
    #    Ingreso
    path('login', views.login),
    path('login.html', views.login),
    
    #    Registro
    path('register', views.register),
    path('register.html', views.register),    
]