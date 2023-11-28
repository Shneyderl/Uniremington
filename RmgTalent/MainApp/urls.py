from django.urls import path
from . import views

urlpatterns = [
    path(' ', views.index, name='index'),
    path('index.html', views.index, name='index.html'),
    path('inicio', views.index, name='index.html'),
    path('job_listing.html', views.job_listing, name='job_listing.html'),
    path('job_listing', views.job_listing, name='job_listing.html'),
]