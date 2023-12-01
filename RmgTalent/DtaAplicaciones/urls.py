from django.urls import path
from . import views

urlpatterns = [
    #    Pagína/Aplicaciones    
    path('Post_List', views.applications),
    path('Post_List.html', views.applications),
]