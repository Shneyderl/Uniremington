from django.urls import path
from . import views

urlpatterns = [       
    path('add_offer',views.add_offer, name='add_offer'),
    #path('ofertas',views.ver_ofertas, name='ver_ofertas'),
    # path('ver/<int:pk>',views.editar, name='ver_recolector'),
    # path('eliminar/<int:pk>',views.eliminar, name='eliminar_recolector'),
    # path('v1/api',views.Recolector_APIView_List.as_view()),
    # path('v1/api/<int:pk>',views.Recolector_APIView_Detail.as_view())    
]