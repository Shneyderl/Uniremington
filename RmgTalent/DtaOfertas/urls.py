from django.urls import path
from . import views

urlpatterns = [       
    #    Ofertas
    #path('Ofertas/', include('DtaOfertas.urls')),
    path('job_listing', views.job_listing),
    path('job_listing.html', views.job_listing),
    
    #    Ofertas/Detalles
    path('job_details/<int:idOfer>/', views.job_details, name='job_details'),
    path('job_details.html/<int:idOfer>/', views.job_details, name='job_details'),
    
    #    Ofertas/Administración
    path('add_offer',views.add_offer, name='add_offer'),
    path('add_offer.html',views.add_offer, name='add_offer'),
    #path('ofertas',views.ver_ofertas, name='ver_ofertas'),
    # path('ver/<int:pk>',views.editar, name='ver_recolector'),
    # path('eliminar/<int:pk>',views.eliminar, name='eliminar_recolector'),
    # path('v1/api',views.Recolector_APIView_List.as_view()),
    # path('v1/api/<int:pk>',views.Recolector_APIView_Detail.as_view())    
]