from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html',{
        'title': 'Inicio'
    })

# def job_listing(request):
#     #ofertas = Ofertas.objects.all()
#     return render(request, 'mainapp/job_listing.html',{
#         'title': 'Ofertas'
#         # },{
#         #'ofertas': ofertas
#     })

def contact(request):
    return render(request, 'mainapp/contact.html',{
        'title': 'Contactanos'
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        'title': 'Acerca de Nosotros'
    })

def register(request):
    return render(request, 'registration/register.html',{
        'title': 'Registrarse'
    })

def login(request):
    return render(request, 'registration/login.html',{
        'title': 'Inicio de sesión'
    })



